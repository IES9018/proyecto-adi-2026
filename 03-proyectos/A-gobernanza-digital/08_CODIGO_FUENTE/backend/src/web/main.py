"""Aplicación principal FastAPI — Gobernanza Digital.

Monta los routers, configura CORS y ejecuta la creación de tablas
al iniciar. Sigue el patrón hexagonal: la capa web es un adaptador
que expone los casos de uso como endpoints HTTP.
"""

import os
from contextlib import asynccontextmanager

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.db import crear_tablas
from src.web.routes import auth, solicitudes, evaluaciones, catalogo, usuarios


limiter = Limiter(key_func=get_remote_address)


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

if os.getenv("ENVIRONMENT") != "testing":
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
else:
    app.state.limiter = Limiter(key_func=get_remote_address, default_limits=[])

# ─── CORS ─────────────────────────────────────────────────────────────────────

cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in cors_origins],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# ─── Routers ──────────────────────────────────────────────────────────────────

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(solicitudes.router, tags=["Solicitudes"])
app.include_router(solicitudes.admin_router, tags=["Admin"])
app.include_router(evaluaciones.router, tags=["Evaluaciones"])
app.include_router(usuarios.router, tags=["Admin"])
app.include_router(catalogo.router, prefix="/catalogo", tags=["Catálogo"])


# ─── Health check ─────────────────────────────────────────────────────────────

@app.get("/", include_in_schema=False)
def raiz() -> dict:
    """Endpoint raíz para verificar que la API está corriendo."""
    return {"mensaje": "Gobernanza Digital API v1.0.0"}
