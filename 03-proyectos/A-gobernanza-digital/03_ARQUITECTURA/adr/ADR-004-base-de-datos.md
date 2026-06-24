# ADR-004: Base de Datos — SQLite (dev) + PostgreSQL (prod)

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El sistema necesita persistencia para solicitudes, evaluaciones, usuarios y auditoría. Los estudiantes deben poder clonar el proyecto y ejecutarlo sin instalar software adicional. En producción, el sistema corre en un servidor Debian 12 con Docker y PostgreSQL disponible.

---

## Decisión

Usar **SQLite para desarrollo y PostgreSQL para producción**, con SQLModel como ORM que abstrae ambos motores.

### Principio

```
domain/ports/SolicitudRepository  ←  define la interfaz (qué operaciones)
infrastructure/db/SQLiteRepository ←  implementa para desarrollo
infrastructure/db/PostgresRepository ←  implementa para producción
application/                      ←  usa la interfaz, no sabe cuál implementación
```

El cambio de motor se hace con una variable de entorno:
```
DATABASE_URL=sqlite:///data/gobernanza.db     # desarrollo
DATABASE_URL=postgresql://user:pass@db:5432   # producción
```

---

## Alternativas consideradas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| Solo PostgreSQL | Requiere instalar PostgreSQL para desarrollo. Barrera innecesaria para estudiantes. |
| Solo SQLite | No soporta concurrencia real. En producción con múltiples usuarios, puede tener problemas de escritura. |
| MySQL/MariaDB | PostgreSQL tiene mejor soporte para JSON, mejor rendimiento en lecturas complejas y es el estándar en el ecosistema Python actual. |

---

## Consecuencias

**Positivas:**
- Desarrollo: `pip install` y ya funciona. Cero configuración.
- Producción: PostgreSQL con backups, concurrencia y rendimiento.
- La arquitectura hexagonal demuestra su valor: cambiar la DB es cambiar una variable de entorno, no el código.
- SQLModel unifica modelos de dominio con modelos de base de datos (sin duplicación).

**Negativas:**
- SQLite y PostgreSQL tienen diferencias sutiles (tipos de datos, constraints, concurrencia).
- Las migraciones con Alembic son más complejas que SQLite puro.
- SQLModel es una librería joven, puede tener bugs o cambios de API.

---

## 🧠 Analogía del @docente

> SQLite es una **libreta de apuntes**: siempre la tenés encima, no pesa, abrís y escribís. Perfecta para estudiar en tu casa. PostgreSQL es el **sistema de archivos de un ministerio**: maneja cientos de expedientes simultáneos, tiene backups, control de acceso. Lo genial es que el formulario que llenás (la interfaz del repositorio) es el mismo en los dos casos. El empleado (la capa de aplicación) no sabe si está anotando en una libreta o en un sistema ministerial. Eso es arquitectura hexagonal.
