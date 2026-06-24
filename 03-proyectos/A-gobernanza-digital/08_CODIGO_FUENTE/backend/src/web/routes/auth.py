"""Rutas de autenticación — login JWT y perfil del usuario."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session

from src.application.auth import LoginUsuario
from src.domain.models import Usuario
from src.infrastructure.repos import UsuarioRepositorySQL
from src.web.dependencies import get_current_user, get_db

router = APIRouter()


# ─── Schemas ─────────────────────────────────────────────────────────────────

class LoginRequest(BaseModel):
    """Cuerpo de la petición de inicio de sesión."""
    email: str
    password: str


class LoginResponse(BaseModel):
    """Respuesta con el token JWT de acceso."""
    access_token: str
    token_type: str


class UsuarioResponse(BaseModel):
    """Datos públicos del usuario autenticado."""
    email: str
    nombre: str
    rol: str


# ─── Endpoints ───────────────────────────────────────────────────────────────

@router.post("/login", response_model=LoginResponse)
def login(datos: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    """Inicia sesión con email y contraseña.

    Devuelve un access token JWT con 30 minutos de validez
    que debe enviarse como Bearer token en las peticiones autenticadas.
    """
    repo = UsuarioRepositorySQL(db)
    caso_uso = LoginUsuario(repo)
    try:
        resultado = caso_uso.ejecutar(datos.email, datos.password)
        return LoginResponse(**resultado)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )


@router.get("/me", response_model=UsuarioResponse)
def obtener_usuario_actual(
    usuario: Usuario = Depends(get_current_user),
) -> UsuarioResponse:
    """Devuelve los datos del usuario autenticado (requiere token válido)."""
    return UsuarioResponse(
        email=usuario.email,
        nombre=usuario.nombre,
        rol=usuario.rol.value,
    )
