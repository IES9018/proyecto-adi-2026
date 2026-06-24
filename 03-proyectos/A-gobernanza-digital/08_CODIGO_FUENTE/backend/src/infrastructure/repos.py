"""Implementaciones concretas de los repositorios usando SQLModel.

Traducen entre las entidades de dominio (dataclasses) y los modelos ORM
(SQLModel), implementando los puertos definidos en domain/ports.py.
"""

from typing import Optional

from sqlmodel import Session, select

from src.domain.models import (
    Solicitud,
    Usuario,
    EvaluacionTecnica,
    EvaluacionInstitucional,
    Resolucion,
    Auditoria,
    EstadoSolicitud,
    Rol,
)
from src.domain.ports import SolicitudRepository, UsuarioRepository
from src.infrastructure.db import (
    SolicitudORM,
    UsuarioORM,
    EvaluacionTecnicaORM,
    EvaluacionInstitucionalORM,
    ResolucionORM,
    AuditoriaORM,
)


class SolicitudRepositorySQL(SolicitudRepository):
    """Implementación SQL de SolicitudRepository usando SQLModel.

    Convierte entre SolicitudORM (tabla) y Solicitud (dataclass de dominio)
    en cada operación para mantener la pureza de la capa de dominio.
    """

    def __init__(self, session: Session) -> None:
        """Inyecta la sesión de SQLModel.

        Args:
            session: Sesión activa de base de datos.
        """
        self.session = session

    def guardar(self, solicitud: Solicitud) -> Solicitud:
        orm = SolicitudORM.from_domain(solicitud)
        # merge inserta o actualiza según exista la PK
        orm = self.session.merge(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def buscar_por_id(self, id: str) -> Optional[Solicitud]:
        orm = self.session.get(SolicitudORM, id)
        return orm.to_domain() if orm else None

    def listar_por_solicitante(self, email: str) -> list[Solicitud]:
        statement = select(SolicitudORM).where(
            SolicitudORM.solicitante_email == email
        )
        results = self.session.exec(statement).all()
        return [r.to_domain() for r in results]

    def listar_todas(self) -> list[Solicitud]:
        statement = select(SolicitudORM)
        results = self.session.exec(statement).all()
        return [r.to_domain() for r in results]

    def listar_aprobadas(self) -> list[Solicitud]:
        statement = select(SolicitudORM).where(
            SolicitudORM.estado == EstadoSolicitud.APROBADA.value
        )
        results = self.session.exec(statement).all()
        return [r.to_domain() for r in results]

    def actualizar_estado(
        self, id: str, estado: EstadoSolicitud
    ) -> Optional[Solicitud]:
        orm = self.session.get(SolicitudORM, id)
        if not orm:
            return None
        orm.estado = estado.value
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def guardar_evaluacion_tecnica(
        self, evaluacion: EvaluacionTecnica
    ) -> EvaluacionTecnica:
        orm = EvaluacionTecnicaORM.from_domain(evaluacion)
        orm = self.session.merge(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def guardar_resolucion(self, resolucion: Resolucion) -> Resolucion:
        orm = ResolucionORM.from_domain(resolucion)
        orm = self.session.merge(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def obtener_evaluacion_tecnica(
        self, solicitud_id: str
    ) -> Optional[EvaluacionTecnica]:
        statement = select(EvaluacionTecnicaORM).where(
            EvaluacionTecnicaORM.solicitud_id == solicitud_id
        )
        orm = self.session.exec(statement).first()
        return orm.to_domain() if orm else None

    def obtener_resolucion(self, solicitud_id: str) -> Optional[Resolucion]:
        statement = select(ResolucionORM).where(
            ResolucionORM.solicitud_id == solicitud_id
        )
        orm = self.session.exec(statement).first()
        return orm.to_domain() if orm else None

    def guardar_auditoria(self, auditoria: Auditoria) -> Auditoria:
        orm = AuditoriaORM.from_domain(auditoria)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def guardar_evaluacion_institucional(
        self, evaluacion: EvaluacionInstitucional
    ) -> EvaluacionInstitucional:
        orm = EvaluacionInstitucionalORM.from_domain(evaluacion)
        orm = self.session.merge(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def buscar_evaluacion_institucional(
        self, solicitud_id: str
    ) -> Optional[EvaluacionInstitucional]:
        statement = select(EvaluacionInstitucionalORM).where(
            EvaluacionInstitucionalORM.solicitud_id == solicitud_id
        )
        orm = self.session.exec(statement).first()
        return orm.to_domain() if orm else None


class UsuarioRepositorySQL(UsuarioRepository):
    """Implementación SQL de UsuarioRepository usando SQLModel."""

    def __init__(self, session: Session) -> None:
        """Inyecta la sesión de SQLModel.

        Args:
            session: Sesión activa de base de datos.
        """
        self.session = session

    def guardar(self, usuario: Usuario) -> Usuario:
        orm = UsuarioORM(
            email=usuario.email,
            nombre=usuario.nombre,
            password_hash=usuario.password_hash,
            rol=usuario.rol.value,
            creado_en=usuario.creado_en,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return Usuario(
            email=orm.email,
            nombre=orm.nombre,
            password_hash=orm.password_hash,
            rol=Rol(orm.rol),
            creado_en=orm.creado_en,
        )

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        orm = self.session.get(UsuarioORM, email)
        if not orm:
            return None
        return Usuario(
            email=orm.email,
            nombre=orm.nombre,
            password_hash=orm.password_hash,
            rol=Rol(orm.rol),
            creado_en=orm.creado_en,
        )
