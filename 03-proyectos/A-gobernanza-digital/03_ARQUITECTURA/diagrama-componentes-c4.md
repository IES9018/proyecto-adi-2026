# Diagrama C4 — Nivel 3: Componentes (Backend)

> Vista interna del backend: capas hexagonales y sus componentes.

```mermaid
graph TD
    subgraph "Capa Web (FastAPI)"
        ROUTES[api/routes/<br/>Endpoints REST]
        DEPS[api/dependencies/<br/>Inyección de dependencias]
        MID[api/middleware/<br/>CORS, rate limit]
    end

    subgraph "Capa de Aplicación"
        CU1[CrearSolicitud]
        CU2[EvaluarTecnicamente]
        CU3[EmitirResolucion]
        CU4[NotificarCambioEstado]
        CU5[GestionarUsuarios]
    end

    subgraph "Capa de Dominio"
        ENT[models/<br/>Solicitud, Evaluacion,<br/>Usuario, Auditoria]
        PORTS[ports/<br/>SolicitudRepo, EmailService,<br/>UserRepo]
    end

    subgraph "Capa de Infraestructura"
        DB_ADAPTER[db/repository.py<br/>SQLAlchemyAdapter]
        EMAIL_ADAPTER[email/smtp.py<br/>SMTPAdapter]
    end

    ROUTES --> CU1
    ROUTES --> CU2
    ROUTES --> CU3
    DEPS --> DB_ADAPTER
    DEPS --> EMAIL_ADAPTER
    CU1 --> PORTS
    CU2 --> PORTS
    CU3 --> PORTS
    DB_ADAPTER -.->|"implementa"| PORTS
    EMAIL_ADAPTER -.->|"implementa"| PORTS
    ENT --> PORTS

    DB_ADAPTER --> DB[(PostgreSQL)]
    EMAIL_ADAPTER --> SMTP[📧 SMTP]
```

**Componentes:**
| Capa | Componente | Responsabilidad |
|:-----|:-----------|:----------------|
| Web | `api/routes/` | Endpoints REST: `/solicitudes`, `/auth`, `/catalogo` |
| Web | `api/dependencies/` | `get_db()`, `get_current_user()`, `get_role()` |
| Web | `api/middleware/` | CORS, rate limiting, logging |
| Aplicación | Casos de uso | Orquestan el dominio: validan, llaman repos, emiten eventos |
| Dominio | `models/` | Entidades puras sin dependencias externas |
| Dominio | `ports/` | Interfaces: `SolicitudRepository`, `EmailService` |
| Infraestructura | `db/` | Implementación concreta con SQLAlchemy |
| Infraestructura | `email/` | Adaptador SMTP con soporte para modo consola en dev |
