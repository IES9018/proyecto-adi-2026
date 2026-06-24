"""Rutas de evaluación técnica y resolución.

Endpoints para que el admin técnico evalúe solicitudes y el directivo
emita resoluciones finales.
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session

from src.application.solicitudes import EvaluarTecnicamente, EmitirResolucion
from src.domain.models import Usuario, EvaluacionTecnica, Resolucion
from src.infrastructure.repos import SolicitudRepositorySQL
from src.web.dependencies import get_db, get_admin, get_directivo, get_current_user

router = APIRouter(prefix="/solicitudes")


# ─── Schemas ─────────────────────────────────────────────────────────────────

class EvaluacionTecnicaRequest(BaseModel):
    """Checklist de evaluación técnica (10 ítems)."""
    repo_publico: bool = False
    licencia_compatible: bool = False
    https_configurado: bool = False
    hash_contrasenas: bool = False
    vars_entorno: bool = False
    puerto_localhost: bool = False
    headers_seguridad: bool = False
    dockerizado: bool = False
    logs_configurados: bool = False
    backup_definido: bool = False
    observaciones: Optional[str] = None


class EvaluacionTecnicaResponse(BaseModel):
    """Respuesta con el resultado de la evaluación técnica."""
    id: str
    solicitud_id: str
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
    fecha: datetime


class ResolucionRequest(BaseModel):
    """Datos para emitir una resolución."""
    decision: str  # "aprobada" o "rechazada"
    fundamentos: str
    condiciones: Optional[str] = None


class ResolucionResponse(BaseModel):
    """Respuesta con los datos de la resolución emitida."""
    id: str
    solicitud_id: str
    numero: str
    decision: str
    fundamentos: str
    condiciones: Optional[str] = None
    fecha: datetime


def _evaluacion_a_response(e: EvaluacionTecnica) -> EvaluacionTecnicaResponse:
    """Convierte entidad EvaluacionTecnica a DTO de respuesta."""
    return EvaluacionTecnicaResponse(
        id=e.id,
        solicitud_id=e.solicitud_id,
        evaluador_email=e.evaluador_email,
        repo_publico=e.repo_publico,
        licencia_compatible=e.licencia_compatible,
        https_configurado=e.https_configurado,
        hash_contrasenas=e.hash_contrasenas,
        vars_entorno=e.vars_entorno,
        puerto_localhost=e.puerto_localhost,
        headers_seguridad=e.headers_seguridad,
        dockerizado=e.dockerizado,
        logs_configurados=e.logs_configurados,
        backup_definido=e.backup_definido,
        dictamen=e.dictamen.value if e.dictamen else None,
        observaciones=e.observaciones,
        fecha=e.fecha,
    )


def _resolucion_a_response(r: Resolucion) -> ResolucionResponse:
    """Convierte entidad Resolucion a DTO de respuesta."""
    return ResolucionResponse(
        id=r.id,
        solicitud_id=r.solicitud_id,
        numero=r.numero,
        decision=r.decision.value,
        fundamentos=r.fundamentos,
        condiciones=r.condiciones,
        fecha=r.fecha,
    )


# ─── Endpoints ───────────────────────────────────────────────────────────────

@router.post(
    "/{solicitud_id}/evaluar-tecnica",
    response_model=EvaluacionTecnicaResponse,
)
def evaluar_tecnicamente(
    solicitud_id: str,
    datos: EvaluacionTecnicaRequest,
    admin: Usuario = Depends(get_admin),
    db: Session = Depends(get_db),
) -> EvaluacionTecnicaResponse:
    """Evalúa técnicamente una solicitud (solo admin técnico).

    Calcula el dictamen automáticamente:
    - 10/10 → apto
    - 7-9/10 → condicional
    - 0-6/10 → no apto

    Si es no apto, la solicitud pasa a RECHAZADA.
    Si es apto o condicional, pasa a PENDIENTE_INSTITUCIONAL.
    """
    repo = SolicitudRepositorySQL(db)
    caso_uso = EvaluarTecnicamente(repo)
    try:
        checklist = datos.model_dump(exclude={"observaciones"})
        evaluacion = caso_uso.ejecutar(
            solicitud_id=solicitud_id,
            checklist=checklist,
            observaciones=datos.observaciones,
            evaluador_email=admin.email,
        )
        return _evaluacion_a_response(evaluacion)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post(
    "/{solicitud_id}/resolver",
    response_model=ResolucionResponse,
)
def emitir_resolucion(
    solicitud_id: str,
    datos: ResolucionRequest,
    directivo: Usuario = Depends(get_directivo),
    db: Session = Depends(get_db),
) -> ResolucionResponse:
    """Emite una resolución final sobre una solicitud (solo directivo).

    La solicitud debe estar en estado PENDIENTE_INSTITUCIONAL.
    La resolución puede aprobar o rechazar definitivamente.
    """
    repo = SolicitudRepositorySQL(db)
    caso_uso = EmitirResolucion(repo)
    try:
        resolucion = caso_uso.ejecutar(
            solicitud_id=solicitud_id,
            decision=datos.decision,
            fundamentos=datos.fundamentos,
            condiciones=datos.condiciones,
            evaluador_email=directivo.email,
        )
        return _resolucion_a_response(resolucion)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get(
    "/{solicitud_id}/resolver",
    response_model=ResolucionResponse,
)
def ver_resolucion(
    solicitud_id: str,
    usuario: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ResolucionResponse:
    """Consulta la resolución emitida para una solicitud.

    Requiere autenticación. Devuelve 404 si no hay resolución aún.
    """
    repo = SolicitudRepositorySQL(db)
    resolucion = repo.obtener_resolucion(solicitud_id)
    if not resolucion:
        raise HTTPException(
            status_code=404,
            detail="No se encontró resolución para esta solicitud.",
        )
    return _resolucion_a_response(resolucion)
