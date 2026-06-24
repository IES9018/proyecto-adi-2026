"""Puertos (interfaces abstractas) del dominio de Gobernanza Digital.

Define los contratos que la capa de infraestructura debe implementar.
La capa de aplicación depende de estas interfaces, no de implementaciones
concretas (principio de inversión de dependencias).
"""

from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models import (
    Solicitud,
    Usuario,
    EvaluacionTecnica,
    EvaluacionInstitucional,
    Resolucion,
    Auditoria,
    EstadoSolicitud,
)


class SolicitudRepository(ABC):
    """Puerto para la persistencia de solicitudes y sus evaluaciones."""

    @abstractmethod
    def guardar(self, solicitud: Solicitud) -> Solicitud:
        """Persiste una solicitud nueva o actualiza una existente.

        Args:
            solicitud: Entidad Solicitud a persistir.

        Returns:
            La solicitud persistida (con posibles campos generados).
        """
        ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Optional[Solicitud]:
        """Busca una solicitud por su identificador único.

        Args:
            id: Identificador UUID de la solicitud.

        Returns:
            La solicitud encontrada o None si no existe.
        """
        ...

    @abstractmethod
    def listar_por_solicitante(self, email: str) -> list[Solicitud]:
        """Lista las solicitudes creadas por un solicitante.

        Args:
            email: Correo del solicitante.

        Returns:
            Lista de solicitudes del solicitante.
        """
        ...

    @abstractmethod
    def listar_todas(self) -> list[Solicitud]:
        """Lista todas las solicitudes del sistema (uso administrativo).

        Returns:
            Lista completa de solicitudes.
        """
        ...

    @abstractmethod
    def listar_aprobadas(self) -> list[Solicitud]:
        """Lista las solicitudes aprobadas para el catálogo público.

        Returns:
            Lista de solicitudes con estado APROBADA.
        """
        ...

    @abstractmethod
    def actualizar_estado(
        self, id: str, estado: EstadoSolicitud
    ) -> Optional[Solicitud]:
        """Actualiza el estado de una solicitud.

        Args:
            id: Identificador de la solicitud.
            estado: Nuevo estado a asignar.

        Returns:
            La solicitud actualizada o None si no existe.
        """
        ...

    @abstractmethod
    def guardar_evaluacion_tecnica(
        self, evaluacion: EvaluacionTecnica
    ) -> EvaluacionTecnica:
        """Persiste una evaluación técnica.

        Args:
            evaluacion: Entidad EvaluacionTecnica a persistir.

        Returns:
            La evaluación persistida.
        """
        ...

    @abstractmethod
    def guardar_resolucion(self, resolucion: Resolucion) -> Resolucion:
        """Persiste una resolución.

        Args:
            resolucion: Entidad Resolucion a persistir.

        Returns:
            La resolución persistida.
        """
        ...

    @abstractmethod
    def obtener_evaluacion_tecnica(
        self, solicitud_id: str
    ) -> Optional[EvaluacionTecnica]:
        """Obtiene la evaluación técnica asociada a una solicitud.

        Args:
            solicitud_id: ID de la solicitud.

        Returns:
            La evaluación técnica o None si no existe.
        """
        ...

    @abstractmethod
    def obtener_resolucion(self, solicitud_id: str) -> Optional[Resolucion]:
        """Obtiene la resolución asociada a una solicitud.

        Args:
            solicitud_id: ID de la solicitud.

        Returns:
            La resolución o None si no existe.
        """
        ...

    @abstractmethod
    def guardar_auditoria(self, auditoria: Auditoria) -> Auditoria:
        """Persiste un registro de auditoría.

        Args:
            auditoria: Entidad Auditoria a persistir.

        Returns:
            El registro de auditoría persistido.
        """
        ...

    @abstractmethod
    def guardar_evaluacion_institucional(
        self, evaluacion: EvaluacionInstitucional
    ) -> EvaluacionInstitucional:
        """Persiste una evaluación institucional.

        Args:
            evaluacion: Entidad EvaluacionInstitucional a persistir.

        Returns:
            La evaluación institucional persistida.
        """
        ...

    @abstractmethod
    def buscar_evaluacion_institucional(
        self, solicitud_id: str
    ) -> Optional[EvaluacionInstitucional]:
        """Busca la evaluación institucional de una solicitud.

        Args:
            solicitud_id: ID de la solicitud.

        Returns:
            La evaluación institucional o None si no existe.
        """
        ...


class UsuarioRepository(ABC):
    """Puerto para la persistencia de usuarios."""

    @abstractmethod
    def guardar(self, usuario: Usuario) -> Usuario:
        """Persiste un usuario nuevo.

        Args:
            usuario: Entidad Usuario a persistir.

        Returns:
            El usuario persistido.
        """
        ...

    @abstractmethod
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca un usuario por su correo electrónico.

        Args:
            email: Correo del usuario.

        Returns:
            El usuario encontrado o None si no existe.
        """
        ...


class EmailService(ABC):
    """Puerto para el servicio de envío de correos electrónicos."""

    @abstractmethod
    def enviar_notificacion(
        self, destinatario: str, asunto: str, cuerpo: str
    ) -> None:
        """Envía un correo de notificación.

        Args:
            destinatario: Dirección de correo destino.
            asunto: Asunto del mensaje.
            cuerpo: Cuerpo del mensaje en texto plano.
        """
        ...
