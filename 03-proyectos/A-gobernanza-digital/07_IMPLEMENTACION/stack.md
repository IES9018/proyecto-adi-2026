# Stack Tecnológico — Guía de Implementación

**Agente:** Tech Lead | **Fecha:** Junio 2026

---

## Stack completo

| Componente | Elección | Versión |
|:-----------|:---------|:--------|
| Lenguaje backend | Python | 3.12+ |
| Framework API | FastAPI | 0.115+ |
| ORM | SQLModel | 0.0.22+ |
| Migraciones | Alembic | 1.14+ |
| Auth | python-jose + passlib + bcrypt | — |
| Testing | pytest + pytest-cov + httpx | 8.x |
| Linting | ruff + mypy | — |
| Lenguaje frontend | TypeScript | 5.x |
| Framework UI | React | 19.x |
| Build tool | Vite | 6.x |
| Routing | React Router | 7.x |
| HTTP client | fetch (nativo) | — |
| Contenedores | Docker + Docker Compose | — |
| Reverse proxy | Nginx | alpine |
| Base de datos | PostgreSQL (prod) / SQLite (dev) | 16 / — |
| CI/CD | GitHub Actions | — |
