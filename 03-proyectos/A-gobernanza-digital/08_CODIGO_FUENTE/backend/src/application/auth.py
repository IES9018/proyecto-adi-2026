"""Caso de uso de autenticación de usuarios.

Gestiona el inicio de sesión con email/contraseña y la generación
de tokens JWT siguiendo el ADR-003.
"""

import os
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from src.domain.ports import UsuarioRepository


# ─── Configuración de seguridad ───────────────────────────────────────────────

SECRET_KEY: str = os.getenv("SECRET_KEY", "clave-secreta-desarrollo-cambiar-en-prod")
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ─── Funciones helper ─────────────────────────────────────────────────────────

def verificar_password(password_plano: str, password_hash: str) -> bool:
    """Verifica que una contraseña en texto plano coincida con su hash bcrypt.

    Args:
        password_plano: Contraseña ingresada por el usuario.
        password_hash: Hash almacenado en la base de datos.

    Returns:
        True si la contraseña es correcta, False en caso contrario.
    """
    return pwd_context.verify(password_plano, password_hash)


def hash_password(password: str) -> str:
    """Genera el hash bcrypt de una contraseña.

    Args:
        password: Contraseña en texto plano.

    Returns:
        Hash bcrypt listo para almacenar.
    """
    return pwd_context.hash(password)


def crear_access_token(data: dict) -> str:
    """Crea un token JWT de acceso con tiempo de expiración.

    Args:
        data: Diccionario con los claims del token (debe incluir 'sub').

    Returns:
        Token JWT codificado como string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decodificar_token(token: str) -> dict:
    """Decodifica y valida un token JWT.

    Args:
        token: Token JWT a decodificar.

    Returns:
        Diccionario con los claims del token.

    Raises:
        jose.JWTError: Si el token es inválido o expiró.
    """
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


# ─── Caso de uso ──────────────────────────────────────────────────────────────

class LoginUsuario:
    """Caso de uso: Iniciar sesión y obtener token JWT.

    Verifica las credenciales del usuario y genera un access token
    con claims: sub (email), rol (rol del usuario).
    """

    def __init__(self, repo: UsuarioRepository) -> None:
        """Inyecta el repositorio de usuarios.

        Args:
            repo: Implementación concreta de UsuarioRepository.
        """
        self.repo = repo

    def ejecutar(self, email: str, password: str) -> dict:
        """Autentica un usuario y devuelve un token JWT.

        Args:
            email: Correo electrónico del usuario.
            password: Contraseña en texto plano.

        Returns:
            Diccionario con 'access_token' y 'token_type'.

        Raises:
            ValueError: Si las credenciales son inválidas.
        """
        usuario = self.repo.buscar_por_email(email)
        if not usuario:
            raise ValueError("Credenciales inválidas.")

        if not verificar_password(password, usuario.password_hash):
            raise ValueError("Credenciales inválidas.")

        access_token = crear_access_token(
            data={"sub": usuario.email, "rol": usuario.rol.value}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
