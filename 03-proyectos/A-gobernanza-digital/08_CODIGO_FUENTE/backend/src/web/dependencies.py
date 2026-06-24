"""Dependencias inyectables para FastAPI.

Proveen la sesión de base de datos, el usuario autenticado desde el token JWT
y los verificadores de rol (admin, directivo) usando el sistema de dependencias
de FastAPI (Depends).
"""

import os
from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlmodel import Session

from src.application.auth import decodificar_token
from src.domain.models import Usuario, Rol
from src.infrastructure.db import obtener_session
from src.infrastructure.repos import UsuarioRepositorySQL


# ─── Configuración JWT ────────────────────────────────────────────────────────

SECRET_KEY: str = os.getenv("SECRET_KEY", "clave-secreta-desarrollo-cambiar-en-prod")
ALGORITHM: str = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ─── Dependencias ─────────────────────────────────────────────────────────────

def get_db() -> Generator[Session, None, None]:
    """Provee una sesión de base de datos por cada request.

    La sesión se cierra automáticamente al finalizar el request.
    """
    session = obtener_session()
    try:
        yield session
    finally:
        session.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    """Obtiene el usuario autenticado desde el token JWT del header Authorization.

    Decodifica el token, extrae el email (claim 'sub') y busca al usuario
    en la base de datos. Si el token es inválido, expiró o el usuario
    no existe, retorna HTTP 401.

    Args:
        token: Token Bearer del header Authorization.
        db: Sesión de base de datos inyectada.

    Returns:
        Entidad Usuario con los datos del usuario autenticado.

    Raises:
        HTTPException 401: Si el token es inválido o el usuario no existe.
    """
    credenciales_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decodificar_token(token)
        email: str | None = payload.get("sub")
        if email is None:
            raise credenciales_exception
    except JWTError:
        raise credenciales_exception

    repo = UsuarioRepositorySQL(db)
    usuario = repo.buscar_por_email(email)
    if usuario is None:
        raise credenciales_exception

    return usuario


def get_admin(
    usuario: Usuario = Depends(get_current_user),
) -> Usuario:
    """Restringe el acceso a usuarios con rol admin_tecnico.

    Args:
        usuario: Usuario autenticado inyectado por get_current_user.

    Returns:
        El mismo usuario si tiene rol admin_tecnico.

    Raises:
        HTTPException 403: Si el usuario no tiene el rol requerido.
    """
    if usuario.rol != Rol.ADMIN_TECNICO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de administrador técnico.",
        )
    return usuario


def get_directivo(
    usuario: Usuario = Depends(get_current_user),
) -> Usuario:
    """Restringe el acceso a usuarios con rol directivo.

    Args:
        usuario: Usuario autenticado inyectado por get_current_user.

    Returns:
        El mismo usuario si tiene rol directivo.

    Raises:
        HTTPException 403: Si el usuario no tiene el rol requerido.
    """
    if usuario.rol != Rol.DIRECTIVO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de directivo.",
        )
    return usuario
