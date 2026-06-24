# Guía de Setup — Gobernanza Digital

**Agente:** Tech Lead

---

## Requisitos previos

- Python 3.12+
- Node.js 20+
- Docker y Docker Compose (opcional para desarrollo)

---

## 🔧 Desarrollo local (sin Docker)

### Backend

```bash
cd 08_CODIGO_FUENTE/backend

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Crear base de datos SQLite
python -c "from src.infrastructure.db import crear_tablas; crear_tablas()"

# Ejecutar servidor
uvicorn src.web.main:app --reload --host 127.0.0.1 --port 8000
```

### Frontend

```bash
cd 08_CODIGO_FUENTE/frontend

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run dev
```

---

## 🐳 Desarrollo con Docker

```bash
docker compose up -d
```

Accesos:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Swagger docs: http://localhost:8000/docs

---

## 📋 Variables de entorno (`.env`)

```env
# Backend
DATABASE_URL=sqlite:///data/gobernanza.db
SECRET_KEY=dev-secret-cambiar-en-produccion
ENVIRONMENT=development
SMTP_HOST=localhost
SMTP_PORT=1025

# Frontend
VITE_API_URL=http://localhost:8000
```

> **Importante:** `.env` nunca se commitea. `.env.example` sí.
