"""Rutas de solicitudes de alojamiento.

Endpoints para crear, listar y consultar solicitudes, tanto para
el solicitante como para administradores.
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session

from src.application.solicitudes import CrearSolicitud
from src.domain.models import Solicitud, Usuario
from src.infrastructure.repos import SolicitudRepositorySQL
from src.web.dependencies import get_current_user, get_db, get_admin

# ─── Routers ─────────────────────────────────────────────────────────────────

router = APIRouter(prefix="/solicitudes")
admin_router = APIRouter(prefix="/admin")


# ─── Schemas ─────────────────────────────────────────────────────────────────

class SolicitudCreate(BaseModel):
    """Campos requeridos para crear una solicitud nueva."""
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


class SolicitudResponse(BaseModel):
    """Respuesta con todos los campos de una solicitud."""
    id: str
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
    acceso_publico: bool
    autenticacion: Optional[str] = None
    roles_usuario: Optional[str] = None
    datos_personales: bool
    contenido_usuarios: bool
    estado: str
    solicitante_email: str
    creada_en: datetime
    actualizada_en: datetime


def _a_response(s: Solicitud) -> SolicitudResponse:
    """Convierte una entidad Solicitud de dominio a DTO de respuesta."""
    return SolicitudResponse(
        id=s.id,
        proyecto=s.proyecto,
        nivel=s.nivel,
        subdominio=s.subdominio,
        descripcion=s.descripcion,
        objetivo_educativo=s.objetivo_educativo,
        arquitectura=s.arquitectura,
        justificacion_arquitectura=s.justificacion_arquitectura,
        patron_diseno=s.patron_diseno,
        url_repositorio=s.url_repositorio,
        licencia=s.licencia,
        lenguajes=s.lenguajes,
        frameworks=s.frameworks,
        base_datos=s.base_datos,
        puertos=s.puertos,
        acceso_publico=s.acceso_publico,
        autenticacion=s.autenticacion,
        roles_usuario=s.roles_usuario,
        datos_personales=s.datos_personales,
        contenido_usuarios=s.contenido_usuarios,
        estado=s.estado.value,
        solicitante_email=s.solicitante_email,
        creada_en=s.creada_en,
        actualizada_en=s.actualizada_en,
    )


# ─── Endpoints ───────────────────────────────────────────────────────────────

@router.post("", response_model=SolicitudResponse, status_code=status.HTTP_201_CREATED)
def crear_solicitud(
    datos: SolicitudCreate,
    usuario: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SolicitudResponse:
    """Crea una nueva solicitud de alojamiento.

    La solicitud se crea en estado PENDIENTE_TECNICA automáticamente.
    Requiere autenticación (cualquier rol).
    """
    repo = SolicitudRepositorySQL(db)
    caso_uso = CrearSolicitud(repo)
    try:
        solicitud = caso_uso.ejecutar(datos.model_dump(), solicitante_email=usuario.email)
        return _a_response(solicitud)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("", response_model=list[SolicitudResponse])
def listar_mis_solicitudes(
    usuario: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[SolicitudResponse]:
    """Lista las solicitudes creadas por el usuario autenticado."""
    repo = SolicitudRepositorySQL(db)
    solicitudes = repo.listar_por_solicitante(usuario.email)
    return [_a_response(s) for s in solicitudes]


@router.get("/{solicitud_id}", response_model=SolicitudResponse)
def obtener_solicitud(
    solicitud_id: str,
    usuario: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SolicitudResponse:
    """Obtiene una solicitud por su ID.

    El solicitante solo puede ver sus propias solicitudes.
    Los roles admin_tecnico y directivo pueden ver cualquier solicitud.
    """
    repo = SolicitudRepositorySQL(db)
    solicitud = repo.buscar_por_id(solicitud_id)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada.")

    # Control de acceso: dueño o staff
    es_dueno = solicitud.solicitante_email == usuario.email
    es_staff = usuario.rol.value in ("admin_tecnico", "directivo")
    if not es_dueno and not es_staff:
        raise HTTPException(
            status_code=403,
            detail="No tenés permiso para ver esta solicitud.",
        )

    return _a_response(solicitud)


# ─── Endpoints de administrador ──────────────────────────────────────────────

@admin_router.get("/solicitudes", response_model=list[SolicitudResponse])
def listar_todas_solicitudes(
    admin: Usuario = Depends(get_admin),
    db: Session = Depends(get_db),
) -> list[SolicitudResponse]:
    """Lista todas las solicitudes del sistema (solo admin técnico)."""
    repo = SolicitudRepositorySQL(db)
    solicitudes = repo.listar_todas()
    return [_a_response(s) for s in solicitudes]
