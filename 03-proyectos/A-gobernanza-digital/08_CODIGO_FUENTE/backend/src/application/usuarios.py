"""Casos de uso de gestión de usuarios.

Implementa la lógica de negocio para crear usuarios en el sistema.
Solo el admin_tecnico tiene permisos para esta operación.
"""

from src.application.auth import hash_password
from src.domain.models import Usuario, Rol
from src.domain.ports import UsuarioRepository


class CrearUsuario:
    """Caso de uso: Crear un nuevo usuario en el sistema.

    Solo puede ser ejecutado por un administrador técnico.
    Hashea la contraseña y persiste el usuario.
    """

    def __init__(self, repo: UsuarioRepository) -> None:
        self.repo = repo

    def ejecutar(
        self,
        email: str,
        nombre: str,
        password: str,
        rol: str,
    ) -> Usuario:
        """Crea un nuevo usuario con sus credenciales.

        Args:
            email: Correo electrónico del nuevo usuario.
            nombre: Nombre completo del usuario.
            password: Contraseña en texto plano (se hashea internamente).
            rol: Rol del usuario ("solicitante", "admin_tecnico" o "directivo").

        Returns:
            El usuario creado.

        Raises:
            ValueError: Si el email ya existe o el rol es inválido.
        """
        # Validar que el email no esté en uso
        existente = self.repo.buscar_por_email(email)
        if existente:
            raise ValueError(f"Ya existe un usuario con el email '{email}'.")

        # Validar rol
        roles_validos = [r.value for r in Rol]
        if rol not in roles_validos:
            raise ValueError(
                f"Rol inválido '{rol}'. Debe ser uno de: {', '.join(roles_validos)}."
            )

        password_hash = hash_password(password)
        usuario = Usuario(
            email=email,
            nombre=nombre,
            password_hash=password_hash,
            rol=Rol(rol),
        )

        return self.repo.guardar(usuario)
