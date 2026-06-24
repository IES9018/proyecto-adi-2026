"""Ruta del catálogo público de proyectos aprobados.

Endpoint sin autenticación que lista las solicitudes que fueron
aprobadas y están disponibles para consulta pública.
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session

from src.infrastructure.repos import SolicitudRepositorySQL
from src.web.dependencies import get_db

router = APIRouter()


# ─── Schema ──────────────────────────────────────────────────────────────────

class CatalogoItem(BaseModel):
    """Datos públicos de un proyecto aprobado en el catálogo."""
    id: str
    proyecto: str
    nivel: int
    subdominio: str
    descripcion: str
    objetivo_educativo: str
    arquitectura: str
    url_repositorio: str
    licencia: str
    lenguajes: str
    frameworks: Optional[str] = None
    base_datos: str
    acceso_publico: bool
    estado: str
    creada_en: datetime


# ─── Endpoint ────────────────────────────────────────────────────────────────

@router.get("", response_model=list[CatalogoItem])
def listar_catalogo(db: Session = Depends(get_db)) -> list[CatalogoItem]:
    """Lista todos los proyectos aprobados (catálogo público).

    No requiere autenticación. Solo muestra solicitudes con estado APROBADA.
    """
    repo = SolicitudRepositorySQL(db)
    aprobadas = repo.listar_aprobadas()
    return [
        CatalogoItem(
            id=s.id,
            proyecto=s.proyecto,
            nivel=s.nivel,
            subdominio=s.subdominio,
            descripcion=s.descripcion,
            objetivo_educativo=s.objetivo_educativo,
            arquitectura=s.arquitectura,
            url_repositorio=s.url_repositorio,
            licencia=s.licencia,
            lenguajes=s.lenguajes,
            frameworks=s.frameworks,
            base_datos=s.base_datos,
            acceso_publico=s.acceso_publico,
            estado=s.estado.value,
            creada_en=s.creada_en,
        )
        for s in aprobadas
    ]
