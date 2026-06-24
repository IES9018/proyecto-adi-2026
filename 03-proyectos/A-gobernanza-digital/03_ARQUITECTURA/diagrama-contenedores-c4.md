# Diagrama C4 — Nivel 2: Contenedores

> Vista de despliegue: cómo se distribuye el sistema en contenedores.

```mermaid
graph TD
    SOL[👤 Solicitante] -->|HTTPS| NX
    AT[👤 Admin Técnico] -->|HTTPS| NX
    DIR[👤 Directivo] -->|HTTPS| NX
    PUB[👤 Público] -->|HTTPS| NX

    subgraph "Servidor Escolar — Debian 12"
        NX[Nginx<br/>Reverse Proxy<br/>:80, :443]
        FE[React + Vite<br/>Frontend SPA<br/>:3000]
        BE[FastAPI<br/>Backend API<br/>:8000]
        PG[(PostgreSQL 16<br/>Base de datos<br/>:5432)]
        NX -->|"/*"| FE
        NX -->|"/api/*"| BE
        BE -->|"SQLAlchemy"| PG
    end

    BE -->|"SMTP"| EMAIL[📧 Servicio Email]
    FE -->|"fetch /api/*"| NX
```

**Contenedores:**
| Contenedor | Tecnología | Responsabilidad |
|:-----------|:-----------|:----------------|
| Nginx | nginx:alpine | Reverse proxy, HTTPS, rate limiting, servir estáticos |
| Frontend | React 19 + Vite | Interfaz de usuario, formularios, paneles |
| Backend | Python 3.12 + FastAPI | API REST, lógica de negocio, autenticación JWT |
| PostgreSQL | postgres:16 | Persistencia de datos, backups |
