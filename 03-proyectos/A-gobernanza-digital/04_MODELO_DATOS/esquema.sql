-- Esquema SQL — Gobernanza Digital
-- Compatible con SQLite (desarrollo) y PostgreSQL (producción)
-- Agente: Modelador | Fecha: Junio 2026

CREATE TABLE IF NOT EXISTS usuario (
    email TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (rol IN ('solicitante', 'admin_tecnico', 'directivo')),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS solicitud (
    id TEXT PRIMARY KEY,
    proyecto TEXT NOT NULL,
    nivel INTEGER NOT NULL CHECK (nivel IN (1, 2, 3)),
    subdominio TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    objetivo_educativo TEXT NOT NULL,
    arquitectura TEXT NOT NULL,
    justificacion_arquitectura TEXT,
    patron_diseno TEXT,
    url_repositorio TEXT NOT NULL,
    licencia TEXT NOT NULL,
    lenguajes TEXT NOT NULL,
    frameworks TEXT,
    base_datos TEXT NOT NULL,
    puertos TEXT,
    acceso_publico INTEGER DEFAULT 0,
    autenticacion TEXT,
    roles_usuario TEXT,
    datos_personales INTEGER DEFAULT 0,
    contenido_usuarios INTEGER DEFAULT 0,
    estado TEXT NOT NULL DEFAULT 'borrador'
        CHECK (estado IN ('borrador', 'pendiente_tecnica', 'pendiente_institucional', 'aprobada', 'rechazada', 'suspendida')),
    solicitante_email TEXT NOT NULL REFERENCES usuario(email),
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS evaluacion_tecnica (
    id TEXT PRIMARY KEY,
    solicitud_id TEXT NOT NULL UNIQUE REFERENCES solicitud(id),
    evaluador_email TEXT NOT NULL REFERENCES usuario(email),
    repo_publico INTEGER,
    licencia_compatible INTEGER,
    https_configurado INTEGER,
    hash_contrasenas INTEGER,
    vars_entorno INTEGER,
    puerto_localhost INTEGER,
    headers_seguridad INTEGER,
    dockerizado INTEGER,
    logs_configurados INTEGER,
    backup_definido INTEGER,
    dictamen TEXT CHECK (dictamen IN ('apto', 'condicional', 'no_apto')),
    observaciones TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS evaluacion_institucional (
    id TEXT PRIMARY KEY,
    solicitud_id TEXT NOT NULL UNIQUE REFERENCES solicitud(id),
    evaluador_email TEXT NOT NULL REFERENCES usuario(email),
    alineacion_educativa INTEGER,
    contribucion_perfil INTEGER,
    riesgo_institucional INTEGER,
    dictamen TEXT CHECK (dictamen IN ('favorable', 'desfavorable', 'condicional')),
    observaciones TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS resolucion (
    id TEXT PRIMARY KEY,
    solicitud_id TEXT NOT NULL UNIQUE REFERENCES solicitud(id),
    numero TEXT NOT NULL UNIQUE,
    decision TEXT NOT NULL CHECK (decision IN ('aprobada', 'rechazada')),
    fundamentos TEXT NOT NULL,
    condiciones TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auditoria (
    id TEXT PRIMARY KEY,
    solicitud_id TEXT NOT NULL REFERENCES solicitud(id),
    usuario_email TEXT NOT NULL,
    rol TEXT NOT NULL,
    campo_modificado TEXT NOT NULL,
    valor_anterior TEXT,
    valor_nuevo TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para consultas frecuentes
CREATE INDEX IF NOT EXISTS idx_solicitud_estado ON solicitud(estado);
CREATE INDEX IF NOT EXISTS idx_solicitud_solicitante ON solicitud(solicitante_email);
CREATE INDEX IF NOT EXISTS idx_auditoria_solicitud ON auditoria(solicitud_id, timestamp);
CREATE INDEX IF NOT EXISTS idx_auditoria_usuario ON auditoria(usuario_email);
