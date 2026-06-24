"""Configuración de base de datos con SQLModel.

Define los modelos ORM (tablas) y provee el motor y las sesiones.
Usa DATABASE_URL de variable de entorno, con SQLite como valor por defecto
(ADR-004: SQLite en dev, PostgreSQL en prod).
"""

import os
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


# ─── Configuración del motor ──────────────────────────────────────────────────

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "sqlite:///gobernanza.db",
)

# SQLite requiere check_same_thread=False para funcionar con FastAPI
_connect_args: dict = (
    {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

engine = create_engine(DATABASE_URL, echo=False, connect_args=_connect_args)


def crear_tablas() -> None:
    """Crea todas las tablas definidas como modelos SQLModel.

    Es idempotente: si las tablas ya existen, no las recrea.
    Se llama al iniciar la aplicación (evento startup).
    """
    SQLModel.metadata.create_all(engine)


def obtener_session() -> Session:
    """Devuelve una nueva sesión de base de datos.

    Returns:
        Sesión de SQLModel lista para usar.
    """
    return Session(engine)


# ─── Modelos ORM ──────────────────────────────────────────────────────────────

class UsuarioORM(SQLModel, table=True):
    """Tabla de usuarios del sistema."""
    __tablename__ = "usuario"

    email: str = Field(primary_key=True)
    nombre: str
    password_hash: str
    rol: str
    creado_en: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SolicitudORM(SQLModel, table=True):
    """Tabla de solicitudes de alojamiento."""
    __tablename__ = "solicitud"

    id: str = Field(primary_key=True)
    proyecto: str
    nivel: int
    subdominio: str
    descripcion: str
    objetivo_educativo: str
    arquitectura: str
    justificacion_arquitectura: Optional[str] = None
    patron_diseno: Optional[str] = None
    url_repositorio: str
    licencia: str
    lenguajes: str
    frameworks: Optional[str] = None
    base_datos: str
    puertos: Optional[str] = None
    acceso_publico: bool = False
    autenticacion: Optional[str] = None
    roles_usuario: Optional[str] = None
    datos_personales: bool = False
    contenido_usuarios: bool = False
    estado: str = "borrador"
    solicitante_email: str
    creada_en: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    actualizada_en: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # ── Conversión a/desde dominio ──────────────────────────────────────

    def to_domain(self) -> "Solicitud":
        """Convierte el registro ORM a la entidad de dominio Solicitud."""
        from src.domain.models import Solicitud as SolicitudDominio, EstadoSolicitud
        return SolicitudDominio(
            id=self.id,
            proyecto=self.proyecto,
            nivel=self.nivel,
            subdominio=self.subdominio,
            descripcion=self.descripcion,
            objetivo_educativo=self.objetivo_educativo,
            arquitectura=self.arquitectura,
            justificacion_arquitectura=self.justificacion_arquitectura,
            patron_diseno=self.patron_diseno,
            url_repositorio=self.url_repositorio,
            licencia=self.licencia,
            lenguajes=self.lenguajes,
            frameworks=self.frameworks,
            base_datos=self.base_datos,
            puertos=self.puertos,
            acceso_publico=self.acceso_publico,
            autenticacion=self.autenticacion,
            roles_usuario=self.roles_usuario,
            datos_personales=self.datos_personales,
            contenido_usuarios=self.contenido_usuarios,
            estado=EstadoSolicitud(self.estado),
            solicitante_email=self.solicitante_email,
            creada_en=self.creada_en,
            actualizada_en=self.actualizada_en,
        )

    @classmethod
    def from_domain(cls, solicitud: "Solicitud") -> "SolicitudORM":
        """Crea un registro ORM a partir de la entidad de dominio."""
        return cls(
            id=solicitud.id,
            proyecto=solicitud.proyecto,
            nivel=solicitud.nivel,
            subdominio=solicitud.subdominio,
            descripcion=solicitud.descripcion,
            objetivo_educativo=solicitud.objetivo_educativo,
            arquitectura=solicitud.arquitectura,
            justificacion_arquitectura=solicitud.justificacion_arquitectura,
            patron_diseno=solicitud.patron_diseno,
            url_repositorio=solicitud.url_repositorio,
            licencia=solicitud.licencia,
            lenguajes=solicitud.lenguajes,
            frameworks=solicitud.frameworks,
            base_datos=solicitud.base_datos,
            puertos=solicitud.puertos,
            acceso_publico=solicitud.acceso_publico,
            autenticacion=solicitud.autenticacion,
            roles_usuario=solicitud.roles_usuario,
            datos_personales=solicitud.datos_personales,
            contenido_usuarios=solicitud.contenido_usuarios,
            estado=solicitud.estado.value,
            solicitante_email=solicitud.solicitante_email,
            creada_en=solicitud.creada_en,
            actualizada_en=solicitud.actualizada_en,
        )


class EvaluacionTecnicaORM(SQLModel, table=True):
    """Tabla de evaluaciones técnicas."""
    __tablename__ = "evaluacion_tecnica"

    id: str = Field(primary_key=True)
    solicitud_id: str = Field(foreign_key="solicitud.id", unique=True)
    evaluador_email: str
    repo_publico: Optional[bool] = None
    licencia_compatible: Optional[bool] = None
    https_configurado: Optional[bool] = None
    hash_contrasenas: Optional[bool] = None
    vars_entorno: Optional[bool] = None
    puerto_localhost: Optional[bool] = None
    headers_seguridad: Optional[bool] = None
    dockerizado: Optional[bool] = None
    logs_configurados: Optional[bool] = None
    backup_definido: Optional[bool] = None
    dictamen: Optional[str] = None
    observaciones: Optional[str] = None
    fecha: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_domain(self) -> "EvaluacionTecnica":
        """Convierte a entidad de dominio."""
        from src.domain.models import EvaluacionTecnica as ETDominio, DictamenTecnico
        return ETDominio(
            id=self.id,
            solicitud_id=self.solicitud_id,
            evaluador_email=self.evaluador_email,
            repo_publico=self.repo_publico,
            licencia_compatible=self.licencia_compatible,
            https_configurado=self.https_configurado,
            hash_contrasenas=self.hash_contrasenas,
            vars_entorno=self.vars_entorno,
            puerto_localhost=self.puerto_localhost,
            headers_seguridad=self.headers_seguridad,
            dockerizado=self.dockerizado,
            logs_configurados=self.logs_configurados,
            backup_definido=self.backup_definido,
            dictamen=DictamenTecnico(self.dictamen) if self.dictamen else None,
            observaciones=self.observaciones,
            fecha=self.fecha,
        )

    @classmethod
    def from_domain(cls, evaluacion: "EvaluacionTecnica") -> "EvaluacionTecnicaORM":
        """Crea desde entidad de dominio."""
        return cls(
            id=evaluacion.id,
            solicitud_id=evaluacion.solicitud_id,
            evaluador_email=evaluacion.evaluador_email,
            repo_publico=evaluacion.repo_publico,
            licencia_compatible=evaluacion.licencia_compatible,
            https_configurado=evaluacion.https_configurado,
            hash_contrasenas=evaluacion.hash_contrasenas,
            vars_entorno=evaluacion.vars_entorno,
            puerto_localhost=evaluacion.puerto_localhost,
            headers_seguridad=evaluacion.headers_seguridad,
            dockerizado=evaluacion.dockerizado,
            logs_configurados=evaluacion.logs_configurados,
            backup_definido=evaluacion.backup_definido,
            dictamen=evaluacion.dictamen.value if evaluacion.dictamen else None,
            observaciones=evaluacion.observaciones,
            fecha=evaluacion.fecha,
        )


class EvaluacionInstitucionalORM(SQLModel, table=True):
    """Tabla de evaluaciones institucionales."""
    __tablename__ = "evaluacion_institucional"

    id: str = Field(primary_key=True)
    solicitud_id: str = Field(foreign_key="solicitud.id", unique=True)
    evaluador_email: str
    alineacion_educativa: Optional[bool] = None
    contribucion_perfil: Optional[bool] = None
    riesgo_institucional: Optional[bool] = None
    dictamen: Optional[str] = None
    observaciones: Optional[str] = None
    fecha: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ResolucionORM(SQLModel, table=True):
    """Tabla de resoluciones finales."""
    __tablename__ = "resolucion"

    id: str = Field(primary_key=True)
    solicitud_id: str = Field(foreign_key="solicitud.id", unique=True)
    numero: str = Field(unique=True)
    decision: str
    fundamentos: str
    condiciones: Optional[str] = None
    fecha: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_domain(self) -> "Resolucion":
        """Convierte a entidad de dominio."""
        from src.domain.models import Resolucion as ResDominio, DecisionResolucion
        return ResDominio(
            id=self.id,
            solicitud_id=self.solicitud_id,
            numero=self.numero,
            decision=DecisionResolucion(self.decision),
            fundamentos=self.fundamentos,
            condiciones=self.condiciones,
            fecha=self.fecha,
        )

    @classmethod
    def from_domain(cls, resolucion: "Resolucion") -> "ResolucionORM":
        """Crea desde entidad de dominio."""
        return cls(
            id=resolucion.id,
            solicitud_id=resolucion.solicitud_id,
            numero=resolucion.numero,
            decision=resolucion.decision.value,
            fundamentos=resolucion.fundamentos,
            condiciones=resolucion.condiciones,
            fecha=resolucion.fecha,
        )
