# ADR-001: Stack Tecnológico

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El sistema Gobernanza Digital necesita un stack tecnológico que permita construir una aplicación web completa (backend, frontend, base de datos) que se despliegue en el servidor escolar (Debian 12, Docker, Nginx). El proyecto es pedagógico: debe servir como material de estudio para estudiantes de la tecnicatura.

---

## Decisión

| Capa | Tecnología elegida | Versión |
|:-----|:-------------------|:--------|
| Frontend | React + Vite | 19.x |
| Backend | Python + FastAPI | 3.12+ |
| ORM | SQLModel (SQLAlchemy + Pydantic) | 0.0.22+ |
| Base de datos (dev) | SQLite | — |
| Base de datos (prod) | PostgreSQL | 16 |
| Autenticación | JWT (python-jose) + OAuth2PasswordBearer | — |
| Contenedores | Docker + Docker Compose | — |
| Reverse proxy | Nginx | — |
| CI/CD | GitHub Actions | — |
| Testing | pytest + pytest-cov | 8.x |
| Linting | ruff + mypy | — |

---

## Alternativas consideradas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| Django + Django REST | Más pesado que FastAPI para una API. Los estudiantes ya vieron Django en Programación III. FastAPI complementa sin duplicar. |
| Next.js (full stack) | Mezcla frontend y backend en un solo proyecto. Para enseñar arquitectura hexagonal, la separación clara de capas es pedagógicamente superior. |
| MongoDB | No relacional. El dominio de gobernanza (solicitudes, evaluaciones, usuarios) es naturalmente relacional. |
| Flask | Sin validación automática de datos, sin OpenAPI/Swagger nativo, sin async. FastAPI resuelve todo eso out of the box. |

---

## Consecuencias

**Positivas:**
- React es lo que el mercado pide. Los estudiantes salen con experiencia en una tecnología demandada.
- FastAPI genera documentación Swagger automática. Los estudiantes pueden probar la API sin Postman.
- SQLite para desarrollo elimina la barrera de instalar PostgreSQL. `pip install` y ya funciona.
- La separación backend/frontend en containers distintos enseña arquitectura distribuida.

**Negativas:**
- Dos proyectos separados (frontend/backend) implican dos procesos de build. Complejidad inicial mayor.
- JWT requiere manejo de refresh tokens. Más complejo que sesiones tradicionales, pero más realista.
- SQLModel es una capa de abstracción que puede confundir si no se entiende SQLAlchemy primero.

---

## 🧠 Analogía del @docente

> Elegir un stack tecnológico es como elegir los **materiales de construcción**. FastAPI es estructura de acero (liviana, resistente, moderna). React es revestimiento de vidrio (lo que se ve, lo que el usuario toca). PostgreSQL es la losa de hormigón (donde se asienta todo). Docker es el container que transporta los materiales de la fábrica a la obra. No elegís materiales porque "están de moda", los elegís porque son los adecuados para el edificio que querés construir y para los obreros que tenés.
