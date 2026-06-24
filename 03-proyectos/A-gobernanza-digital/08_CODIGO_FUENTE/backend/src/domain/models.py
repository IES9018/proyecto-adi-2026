"""Entidades del dominio de Gobernanza Digital.

Define las entidades puras como dataclasses, sin dependencias
de infraestructura ni frameworks externos (regla hexagonal).
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import uuid


# ─── Enums ────────────────────────────────────────────────────────────────────

class Rol(str, Enum):
    """Roles de usuario del sistema."""
    SOLICITANTE = "solicitante"
    ADMIN_TECNICO = "admin_tecnico"
    DIRECTIVO = "directivo"


class EstadoSolicitud(str, Enum):
    """Estados posibles de una solicitud de alojamiento."""
    BORRADOR = "borrador"
    PENDIENTE_TECNICA = "pendiente_tecnica"
    PENDIENTE_INSTITUCIONAL = "pendiente_institucional"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"
    SUSPENDIDA = "suspendida"


class DictamenTecnico(str, Enum):
    """Dictamen que emite el admin técnico tras evaluar."""
    APTO = "apto"
    CONDICIONAL = "condicional"
    NO_APTO = "no_apto"


class DictamenInstitucional(str, Enum):
    """Dictamen que emite el directivo tras la evaluación institucional."""
    FAVORABLE = "favorable"
    DESFAVORABLE = "desfavorable"
    CONDICIONAL = "condicional"


class DecisionResolucion(str, Enum):
    """Decisión final de una resolución."""
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"


# ─── Funciones helper ─────────────────────────────────────────────────────────

def _ahora() -> datetime:
    """Devuelve la fecha/hora actual en UTC."""
    return datetime.now(timezone.utc)


def _nuevo_id() -> str:
    """Genera un identificador único."""
    return str(uuid.uuid4())


# ─── Entidades ────────────────────────────────────────────────────────────────

@dataclass
class Usuario:
    """Usuario del sistema con sus credenciales y rol.

    Attributes:
        email: Correo electrónico (identificador único).
        nombre: Nombre completo del usuario.
        password_hash: Hash bcrypt de la contraseña.
        rol: Rol dentro del sistema.
        creado_en: Fecha de creación del registro.
    """
    email: str
    nombre: str
    password_hash: str
    rol: Rol
    creado_en: datetime = field(default_factory=_ahora)


@dataclass
class Solicitud:
    """Solicitud de alojamiento de un proyecto digital educativo.

    Representa el formulario completo que un solicitante envía para pedir
    alojamiento en la infraestructura del instituto.
    """
    proyecto: str
    nivel: int
    subdominio: str
    descripcion: str
    objetivo_educativo: str
    arquitectura: str
    url_repositorio: str
    licencia: str
    lenguajes: str
    base_datos: str
    solicitante_email: str
    id: str = field(default_factory=_nuevo_id)
    justificacion_arquitectura: Optional[str] = None
    patron_diseno: Optional[str] = None
    frameworks: Optional[str] = None
    puertos: Optional[str] = None
    acceso_publico: bool = False
    autenticacion: Optional[str] = None
    roles_usuario: Optional[str] = None
    datos_personales: bool = False
    contenido_usuarios: bool = False
    estado: EstadoSolicitud = EstadoSolicitud.BORRADOR
    creada_en: datetime = field(default_factory=_ahora)
    actualizada_en: datetime = field(default_factory=_ahora)


@dataclass
class EvaluacionTecnica:
    """Evaluación técnica de una solicitud realizada por un admin técnico.

    Contiene el checklist de 10 ítems que verifican aspectos de seguridad,
    despliegue y buenas prácticas del proyecto.
    """
    solicitud_id: str
    evaluador_email: str
    id: str = field(default_factory=_nuevo_id)
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
    dictamen: Optional[DictamenTecnico] = None
    observaciones: Optional[str] = None
    fecha: datetime = field(default_factory=_ahora)


@dataclass
class EvaluacionInstitucional:
    """Evaluación institucional realizada por un directivo."""
    solicitud_id: str
    evaluador_email: str
    id: str = field(default_factory=_nuevo_id)
    alineacion_educativa: Optional[bool] = None
    contribucion_perfil: Optional[bool] = None
    riesgo_institucional: Optional[bool] = None
    dictamen: Optional[DictamenInstitucional] = None
    observaciones: Optional[str] = None
    fecha: datetime = field(default_factory=_ahora)


@dataclass
class Resolucion:
    """Resolución final emitida por el directivo sobre una solicitud."""
    solicitud_id: str
    numero: str
    decision: DecisionResolucion
    fundamentos: str
    id: str = field(default_factory=_nuevo_id)
    condiciones: Optional[str] = None
    fecha: datetime = field(default_factory=_ahora)


@dataclass
class Auditoria:
    """Registro de auditoría de cambios en solicitudes."""
    solicitud_id: str
    usuario_email: str
    rol: str
    campo_modificado: str
    id: str = field(default_factory=_nuevo_id)
    valor_anterior: Optional[str] = None
    valor_nuevo: Optional[str] = None
    timestamp: datetime = field(default_factory=_ahora)
