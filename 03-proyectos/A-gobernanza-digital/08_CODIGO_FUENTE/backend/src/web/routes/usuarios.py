"""Rutas de administración de usuarios.

Endpoints para que el admin técnico gestione usuarios del sistema.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session

from src.application.usuarios import CrearUsuario
from src.domain.models import Usuario
from src.infrastructure.repos import UsuarioRepositorySQL
from src.web.dependencies import get_db, get_admin

router = APIRouter(prefix="/admin")


# ─── Schemas ─────────────────────────────────────────────────────────────────

class UsuarioCreate(BaseModel):
    """Datos para crear un nuevo usuario."""
    email: str
    nombre: str
    password: str
    rol: str  # "solicitante", "admin_tecnico" o "directivo"


class UsuarioResponse(BaseModel):
    """Respuesta con los datos del usuario creado (sin password)."""
    email: str
    nombre: str
    rol: str


# ─── Endpoints ───────────────────────────────────────────────────────────────

@router.post(
    "/usuarios",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_usuario(
    datos: UsuarioCreate,
    admin: Usuario = Depends(get_admin),
    db: Session = Depends(get_db),
) -> UsuarioResponse:
    """Crea un nuevo usuario en el sistema (solo admin técnico).

    Requiere autenticación con rol admin_tecnico.
    La contraseña se hashea con bcrypt antes de almacenar.
    """
    repo = UsuarioRepositorySQL(db)
    caso_uso = CrearUsuario(repo)
    try:
        usuario = caso_uso.ejecutar(
            email=datos.email,
            nombre=datos.nombre,
            password=datos.password,
            rol=datos.rol,
        )
        return UsuarioResponse(
            email=usuario.email,
            nombre=usuario.nombre,
            rol=usuario.rol.value,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
