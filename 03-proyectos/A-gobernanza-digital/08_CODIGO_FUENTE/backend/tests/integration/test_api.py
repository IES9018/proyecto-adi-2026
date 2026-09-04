"""Tests de integración con TestClient de FastAPI + SQLite en archivo temporal.

Prueba el flujo completo: login → crear solicitud → listar.
Usa un archivo temporal de SQLite que se limpia al finalizar.
"""

import os
import tempfile
from pathlib import Path

# ⚠️  Debe ejecutarse antes de importar src.*
# Usar un archivo temporal asegura que todas las conexiones ven la misma base
_temp_db = Path(tempfile.gettempdir()) / "gobernanza_test_integracion.db"
_temp_db_str = f"sqlite:///{_temp_db}"
os.environ["DATABASE_URL"] = _temp_db_str

from sqlmodel import Session, SQLModel

# Importar la app — el motor global usará el archivo temporal
from src.web.main import app
from src.application.auth import hash_password
from src.infrastructure.db import engine, UsuarioORM
from fastapi.testclient import TestClient


# ─── Configuración de la base de datos de prueba ─────────────────────────────

# Crear tablas frescas (drop_all + create_all por si hay restos)
SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

# Insertar usuarios de prueba
with Session(engine) as session:
    session.add(UsuarioORM(
        email="solicitante@ies9018.edu.ar",
        nombre="Estudiante Solicitante",
        password_hash=hash_password("secreto123"),
        rol="solicitante",
    ))
    session.add(UsuarioORM(
        email="admin@ies9018.edu.ar",
        nombre="Admin Técnico",
        password_hash=hash_password("admin123"),
        rol="admin_tecnico",
    ))
    session.add(UsuarioORM(
        email="directivo@ies9018.edu.ar",
        nombre="Directivo",
        password_hash=hash_password("directivo123"),
        rol="directivo",
    ))
    session.commit()


# Cliente de prueba
client = TestClient(app)


# ─── Limpieza al finalizar el módulo ─────────────────────────────────────────

def _limpiar() -> None:
    """Elimina la base de datos temporal (ignora errores de archivo en uso)."""
    try:
        if _temp_db.exists():
            _temp_db.unlink()
    except PermissionError:
        pass  # Archivo en uso, se limpiará en la próxima ejecución

import atexit
atexit.register(_limpiar)


# ─── Tests ────────────────────────────────────────────────────────────────────

class TestAuthAPI:
    """Tests de integración de los endpoints de autenticación."""

    def test_login_exitoso(self) -> None:
        """Login con credenciales correctas devuelve token JWT."""
        response = client.post("/auth/login", json={
            "email": "solicitante@ies9018.edu.ar",
            "password": "secreto123",
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert len(data["access_token"]) > 20

    def test_login_credenciales_invalidas(self) -> None:
        """Login con contraseña incorrecta devuelve 401."""
        response = client.post("/auth/login", json={
            "email": "solicitante@ies9018.edu.ar",
            "password": "contraseña-equivocada",
        })
        assert response.status_code == 401

    def test_login_usuario_inexistente(self) -> None:
        """Login con email no registrado devuelve 401."""
        response = client.post("/auth/login", json={
            "email": "noexiste@ies9018.edu.ar",
            "password": "cualquiera",
        })
        assert response.status_code == 401

    def test_me_con_token_valido(self) -> None:
        """GET /auth/me con token válido devuelve datos del usuario."""
        login_resp = client.post("/auth/login", json={
            "email": "solicitante@ies9018.edu.ar",
            "password": "secreto123",
        })
        token = login_resp.json()["access_token"]

        response = client.get(
            "/auth/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "solicitante@ies9018.edu.ar"
        assert data["nombre"] == "Estudiante Solicitante"
        assert data["rol"] == "solicitante"

    def test_me_sin_token(self) -> None:
        """GET /auth/me sin token devuelve 401."""
        response = client.get("/auth/me")
        assert response.status_code == 401


class TestSolicitudesAPI:
    """Tests de integración del CRUD de solicitudes."""

    def _obtener_token(self, email: str = "solicitante@ies9018.edu.ar") -> str:
        """Helper: obtiene un token JWT para un usuario de prueba."""
        passwords = {
            "solicitante@ies9018.edu.ar": "secreto123",
            "admin@ies9018.edu.ar": "admin123",
            "directivo@ies9018.edu.ar": "directivo123",
        }
        resp = client.post("/auth/login", json={
            "email": email,
            "password": passwords[email],
        })
        assert resp.status_code == 200, f"Login falló ({email}): {resp.text}"
        return resp.json()["access_token"]

    def test_crear_solicitud(self) -> None:
        """POST /solicitudes crea una solicitud y devuelve 201."""
        token = self._obtener_token()

        response = client.post(
            "/solicitudes",
            json={
                "proyecto": "Portal Educativo",
                "nivel": 2,
                "subdominio": "portal",
                "descripcion": "Portal de recursos educativos digitales",
                "objetivo_educativo": "Centralizar el acceso a materiales",
                "arquitectura": "Monolito MVC con Flask",
                "url_repositorio": "https://github.com/ies9018/portal",
                "licencia": "MIT",
                "lenguajes": "Python, JavaScript",
                "base_datos": "PostgreSQL",
            },
            headers={"Authorization": f"Bearer {token}"},
        )

        assert response.status_code == 201, response.text
        data = response.json()
        assert data["proyecto"] == "Portal Educativo"
        assert data["estado"] == "pendiente_tecnica"
        assert data["solicitante_email"] == "solicitante@ies9018.edu.ar"
        assert "id" in data

    def test_crear_solicitud_sin_auth(self) -> None:
        """POST /solicitudes sin token devuelve 401."""
        response = client.post("/solicitudes", json={
            "proyecto": "Test",
            "nivel": 1,
            "subdominio": "test",
            "descripcion": "test",
            "objetivo_educativo": "test",
            "arquitectura": "test",
            "url_repositorio": "https://test.com",
            "licencia": "MIT",
            "lenguajes": "Python",
            "base_datos": "SQLite",
        })
        assert response.status_code == 401

    def test_crear_solicitud_faltan_campos(self) -> None:
        """POST /solicitudes con campos faltantes devuelve 422."""
        token = self._obtener_token()

        response = client.post(
            "/solicitudes",
            json={"proyecto": "Incompleto"},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 422

    def test_listar_mis_solicitudes(self) -> None:
        """GET /solicitudes lista solo las del usuario autenticado."""
        token = self._obtener_token()

        client.post(
            "/solicitudes",
            json={
                "proyecto": "Mi Proyecto",
                "nivel": 1,
                "subdominio": "mip",
                "descripcion": "Desc",
                "objetivo_educativo": "Obj",
                "arquitectura": "Arq",
                "url_repositorio": "https://repo.com",
                "licencia": "MIT",
                "lenguajes": "Python",
                "base_datos": "SQLite",
            },
            headers={"Authorization": f"Bearer {token}"},
        )

        response = client.get(
            "/solicitudes",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        # Verificar que "Mi Proyecto" está en la lista (puede haber otros de tests anteriores)
        proyectos = [s["proyecto"] for s in data]
        assert "Mi Proyecto" in proyectos

    def test_obtener_solicitud_propia(self) -> None:
        """GET /solicitudes/{id} permite al dueño ver su solicitud."""
        token = self._obtener_token()

        create_resp = client.post(
            "/solicitudes",
            json={
                "proyecto": "Para Ver",
                "nivel": 3,
                "subdominio": "ver",
                "descripcion": "Desc",
                "objetivo_educativo": "Obj",
                "arquitectura": "Arq",
                "url_repositorio": "https://repo.com",
                "licencia": "MIT",
                "lenguajes": "Python",
                "base_datos": "SQLite",
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        solicitud_id = create_resp.json()["id"]

        response = client.get(
            f"/solicitudes/{solicitud_id}",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200
        assert response.json()["id"] == solicitud_id

    def test_admin_lista_todas(self) -> None:
        """GET /admin/solicitudes permite al admin ver todas las solicitudes."""
        admin_token = self._obtener_token("admin@ies9018.edu.ar")

        response = client.get(
            "/admin/solicitudes",
            headers={"Authorization": f"Bearer {admin_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_solicitante_no_accede_admin(self) -> None:
        """Un solicitante no puede acceder a /admin/solicitudes."""
        token = self._obtener_token("solicitante@ies9018.edu.ar")

        response = client.get(
            "/admin/solicitudes",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 403


class TestCatalogoAPI:
    """Tests de integración del catálogo público."""

    def test_catalogo_sin_auth(self) -> None:
        """GET /catalogo funciona sin autenticación."""
        response = client.get("/catalogo")
        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)

    def test_catalogo_solo_aprobadas(self) -> None:
        """El catálogo solo muestra solicitudes aprobadas."""
        login_resp = client.post("/auth/login", json={
            "email": "solicitante@ies9018.edu.ar",
            "password": "secreto123",
        })
        token = login_resp.json()["access_token"]

        client.post(
            "/solicitudes",
            json={
                "proyecto": "No Aprobado Aún",
                "nivel": 1,
                "subdominio": "noap",
                "descripcion": "Desc",
                "objetivo_educativo": "Obj",
                "arquitectura": "Arq",
                "url_repositorio": "https://repo.com",
                "licencia": "MIT",
                "lenguajes": "Python",
                "base_datos": "SQLite",
            },
            headers={"Authorization": f"Bearer {token}"},
        )

        response = client.get("/catalogo")
        proyectos = [item["proyecto"] for item in response.json()]
        assert "No Aprobado Aún" not in proyectos
