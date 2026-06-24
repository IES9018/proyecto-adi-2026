"""Tests unitarios del caso de uso CrearSolicitud.

Usa un repositorio en memoria (dict) en vez de mocks,
demostrando que el dominio no depende de infraestructura.
"""

from typing import Optional

from src.domain.models import (
    Solicitud,
    EstadoSolicitud,
    EvaluacionTecnica,
    EvaluacionInstitucional,
    Resolucion,
    Auditoria,
)
from src.domain.ports import SolicitudRepository
from src.application.solicitudes import CrearSolicitud


# ─── Repositorio en memoria para tests ────────────────────────────────────────

class InMemorySolicitudRepo(SolicitudRepository):
    """Implementación de SolicitudRepository que almacena en un dict.

    Perfecta para tests unitarios: sin base de datos, sin mocks,
    sin frameworks. Demuestra el valor de la arquitectura hexagonal.
    """

    def __init__(self) -> None:
        self.solicitudes: dict[str, Solicitud] = {}
        self.evaluaciones: dict[str, EvaluacionTecnica] = {}
        self.resoluciones: dict[str, Resolucion] = {}
        self.evaluaciones_institucionales: dict[str, EvaluacionInstitucional] = {}
        self.auditorias: list[Auditoria] = []

    def guardar(self, solicitud: Solicitud) -> Solicitud:
        self.solicitudes[solicitud.id] = solicitud
        return solicitud

    def buscar_por_id(self, id: str) -> Optional[Solicitud]:
        return self.solicitudes.get(id)

    def listar_por_solicitante(self, email: str) -> list[Solicitud]:
        return [s for s in self.solicitudes.values() if s.solicitante_email == email]

    def listar_todas(self) -> list[Solicitud]:
        return list(self.solicitudes.values())

    def listar_aprobadas(self) -> list[Solicitud]:
        return [
            s for s in self.solicitudes.values()
            if s.estado == EstadoSolicitud.APROBADA
        ]

    def actualizar_estado(
        self, id: str, estado: EstadoSolicitud
    ) -> Optional[Solicitud]:
        s = self.solicitudes.get(id)
        if s:
            s.estado = estado
        return s

    def guardar_evaluacion_tecnica(
        self, evaluacion: EvaluacionTecnica
    ) -> EvaluacionTecnica:
        self.evaluaciones[evaluacion.id] = evaluacion
        return evaluacion

    def guardar_resolucion(self, resolucion: Resolucion) -> Resolucion:
        self.resoluciones[resolucion.id] = resolucion
        return resolucion

    def obtener_evaluacion_tecnica(
        self, solicitud_id: str
    ) -> Optional[EvaluacionTecnica]:
        for e in self.evaluaciones.values():
            if e.solicitud_id == solicitud_id:
                return e
        return None

    def obtener_resolucion(self, solicitud_id: str) -> Optional[Resolucion]:
        for r in self.resoluciones.values():
            if r.solicitud_id == solicitud_id:
                return r
        return None

    def guardar_auditoria(self, auditoria: Auditoria) -> Auditoria:
        self.auditorias.append(auditoria)
        return auditoria

    def guardar_evaluacion_institucional(
        self, evaluacion: EvaluacionInstitucional
    ) -> EvaluacionInstitucional:
        self.evaluaciones_institucionales[evaluacion.id] = evaluacion
        return evaluacion

    def buscar_evaluacion_institucional(
        self, solicitud_id: str
    ) -> Optional[EvaluacionInstitucional]:
        for e in self.evaluaciones_institucionales.values():
            if e.solicitud_id == solicitud_id:
                return e
        return None


# ─── Tests ────────────────────────────────────────────────────────────────────

class TestCrearSolicitud:
    """Tests unitarios para el caso de uso CrearSolicitud."""

    def test_crear_solicitud_valida(self) -> None:
        """Crear una solicitud con datos válidos debe persistirla en PENDIENTE_TECNICA."""
        repo = InMemorySolicitudRepo()
        caso_uso = CrearSolicitud(repo)

        datos = {
            "proyecto": "Portal Educativo",
            "nivel": 2,
            "subdominio": "portal",
            "descripcion": "Portal de recursos educativos",
            "objetivo_educativo": "Centralizar materiales",
            "arquitectura": "Monolito MVC",
            "url_repositorio": "https://github.com/ies/portal",
            "licencia": "MIT",
            "lenguajes": "Python, JavaScript",
            "base_datos": "PostgreSQL",
        }

        solicitud = caso_uso.ejecutar(datos, solicitante_email="alumno@ies9018.edu.ar")

        # Verificar que se generó un ID
        assert solicitud.id
        assert len(solicitud.id) == 36  # UUID v4

        # Verificar estado inicial
        assert solicitud.estado == EstadoSolicitud.PENDIENTE_TECNICA

        # Verificar que los datos se guardaron
        assert solicitud.proyecto == "Portal Educativo"
        assert solicitud.nivel == 2
        assert solicitud.subdominio == "portal"
        assert solicitud.solicitante_email == "alumno@ies9018.edu.ar"

        # Verificar que se persistió en el repo
        assert repo.buscar_por_id(solicitud.id) is not None
        assert len(repo.listar_todas()) == 1

    def test_campos_obligatorios_faltantes(self) -> None:
        """Falta un campo obligatorio debe lanzar ValueError."""
        repo = InMemorySolicitudRepo()
        caso_uso = CrearSolicitud(repo)

        datos = {
            "proyecto": "Proyecto X",
            # Falta 'nivel', 'subdominio', etc.
        }

        try:
            caso_uso.ejecutar(datos, solicitante_email="test@test.com")
            assert False, "Debería haber lanzado ValueError"
        except ValueError as e:
            assert "obligatorio" in str(e).lower()

        # El repo debe seguir vacío
        assert len(repo.listar_todas()) == 0

    def test_nivel_invalido(self) -> None:
        """Nivel fuera de rango 1-3 debe lanzar ValueError."""
        repo = InMemorySolicitudRepo()
        caso_uso = CrearSolicitud(repo)

        datos = {
            "proyecto": "Proyecto X",
            "nivel": 5,  # inválido
            "subdominio": "test",
            "descripcion": "Test",
            "objetivo_educativo": "Test",
            "arquitectura": "Test",
            "url_repositorio": "https://test.com",
            "licencia": "MIT",
            "lenguajes": "Python",
            "base_datos": "SQLite",
        }

        try:
            caso_uso.ejecutar(datos, solicitante_email="test@test.com")
            assert False, "Debería haber lanzado ValueError"
        except ValueError as e:
            assert "nivel" in str(e).lower()

    def test_listar_por_solicitante(self) -> None:
        """Crear varias solicitudes y verificar que se filtran por email."""
        repo = InMemorySolicitudRepo()
        caso_uso = CrearSolicitud(repo)

        datos_base = {
            "proyecto": "P",
            "nivel": 1,
            "subdominio": "s",
            "descripcion": "d",
            "objetivo_educativo": "o",
            "arquitectura": "a",
            "url_repositorio": "https://u.com",
            "licencia": "MIT",
            "lenguajes": "Python",
            "base_datos": "SQLite",
        }

        caso_uso.ejecutar(datos_base, solicitante_email="a@ies.edu.ar")
        caso_uso.ejecutar(datos_base, solicitante_email="b@ies.edu.ar")
        caso_uso.ejecutar(datos_base, solicitante_email="a@ies.edu.ar")

        de_a = repo.listar_por_solicitante("a@ies.edu.ar")
        de_b = repo.listar_por_solicitante("b@ies.edu.ar")

        assert len(de_a) == 2
        assert len(de_b) == 1
