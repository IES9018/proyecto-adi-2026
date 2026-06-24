"""Aplicación principal FastAPI — Gobernanza Digital.

Monta los routers, configura CORS y ejecuta la creación de tablas
al iniciar. Sigue el patrón hexagonal: la capa web es un adaptador
que expone los casos de uso como endpoints HTTP.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.db import crear_tablas
from src.web.routes import auth, solicitudes, evaluaciones, catalogo


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestión del ciclo de vida de la aplicación.

    Al iniciar: crea las tablas de la base de datos si no existen.
    Al cerrar: libera recursos si fuera necesario.
    """
    crear_tablas()
    yield


app = FastAPI(
    title="Gobernanza Digital API",
    description=(
        "API REST para la gestión de solicitudes de alojamiento "
        "de proyectos digitales educativos del IES9018."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# ─── CORS ─────────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routers ──────────────────────────────────────────────────────────────────

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(solicitudes.router, tags=["Solicitudes"])
app.include_router(solicitudes.admin_router, tags=["Admin"])
app.include_router(evaluaciones.router, tags=["Evaluaciones"])
app.include_router(catalogo.router, prefix="/catalogo", tags=["Catálogo"])


# ─── Health check ─────────────────────────────────────────────────────────────

@app.get("/", include_in_schema=False)
def raiz() -> dict:
    """Endpoint raíz para verificar que la API está corriendo."""
    return {"mensaje": "Gobernanza Digital API v1.0.0"}
