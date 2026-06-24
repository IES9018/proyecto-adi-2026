# ADR-002: Arquitectura Hexagonal (Puertos y Adaptadores)

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El sistema Gobernanza Digital necesita una arquitectura que separe claramente la lógica de negocio de los detalles de infraestructura. Los estudiantes deben poder estudiar cómo se estructura un proyecto profesional y aplicar el mismo patrón en sus propios proyectos.

---

## Decisión

Usar **Arquitectura Hexagonal (Puertos y Adaptadores)**, también conocida como Clean Architecture.

### Estructura de capas

```
src/
├── domain/           ← Reglas de negocio puras (no depende de nada externo)
│   ├── models/       ← Entidades: Solicitud, Evaluacion, Usuario
│   └── ports/        ← Interfaces: SolicitudRepository, EmailService
│
├── application/      ← Casos de uso (depende solo de domain)
│   └── services/     ← CrearSolicitud, EvaluarTecnicamente, EmitirResolucion
│
├── infrastructure/   ← Adaptadores concretos (implementan los puertos)
│   ├── db/           ← SQLAlchemy, modelos ORM
│   └── email/        ← SMTP, SendGrid
│
└── web/              ← Capa de presentación (FastAPI)
    ├── api/          ← Endpoints REST
    └── dependencies/ ← Inyección de dependencias
```

### Regla de dependencia

Las dependencias apuntan **hacia adentro**:
```
infrastructure → domain ← application
     web       → domain ← application
```

`domain/` no importa nada de `application/`, `infrastructure/` ni `web/`. Es el núcleo puro.

---

## Alternativas consideradas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| MVC tradicional | El controlador mezcla lógica de negocio con HTTP. No escala bien para proyectos que cambian de infraestructura. |
| Sin arquitectura (todo en un archivo) | Imposible de mantener, imposible de testear, no enseña nada. |
| Microservicios | Excesivo para este proyecto. No hay necesidad de escalar módulos independientemente. |

---

## Consecuencias

**Positivas:**
- Cambiar SQLite por PostgreSQL no requiere tocar dominio ni aplicación. Solo infrastructure.
- Cada capa se testea de forma aislada. El dominio no necesita base de datos para testearse.
- Los estudiantes aprenden un patrón que se usa en la industria (Clean Architecture, Hexagonal, DDD).
- El código es autodocumentado: la estructura de carpetas cuenta la historia de la arquitectura.

**Negativas:**
- Más archivos y carpetas que un enfoque monolítico simple. Curva de aprendizaje inicial.
- La inyección de dependencias agrega código "ceremonial" (pero necesario).
- Para un proyecto muy chico, puede ser sobre-arquitectura. Para este (10 funcionalidades, 3 roles), es adecuado.

---

## 🧠 Analogía del @docente

> La arquitectura hexagonal es como un **tomacorriente universal**. Tu lógica de negocio es el electrodoméstico. El enchufe (puerto) está estandarizado. Del otro lado de la pared puede haber un generador, una batería, paneles solares o la red eléctrica (adaptadores). El electrodoméstico no sabe ni le importa de dónde viene la electricidad. Cambiar la fuente de energía no requiere cambiar el electrodoméstico.
>
> En nuestro caso: el dominio (Solicitud, Evaluación) es el electrodoméstico. El puerto (SolicitudRepository) es el enchufe. SQLite y PostgreSQL son dos fuentes de energía distintas. El dominio funciona igual con cualquiera.
