# Diagrama C4 — Nivel 1: Contexto

> Vista macro del sistema y sus relaciones con actores externos.

```mermaid
graph TD
    SOL[👤 Solicitante<br/>Estudiante / Docente]
    AT[👤 Admin Técnico<br/>Admin del servidor]
    DIR[👤 Directivo<br/>Director / Coordinador]
    CD[👤 Consejo Directivo<br/>Órgano colegiado]
    PUB[👤 Comunidad Educativa<br/>Público sin login]

    SIS[🏛️ Sistema Gobernanza Digital<br/>Gestiona solicitudes, evaluaciones<br/>y resoluciones de alojamiento]

    SOL -->|"Completa solicitud de alojamiento"| SIS
    AT -->|"Evalúa técnicamente"| SIS
    DIR -->|"Evalúa institucionalmente"| SIS
    CD -->|"Aprueba / Rechaza con resolución"| SIS
    PUB -->|"Consulta catálogo público"| SIS

    SIS -->|"Envía notificaciones"| EMAIL[📧 Servicio de Email<br/>SMTP institucional]
    SIS -->|"Lee/escribe"| DB[(💾 Base de Datos)]
```

**Alcance:** El sistema Gobernanza Digital abarca el flujo completo desde la solicitud hasta la resolución, incluyendo evaluaciones, notificaciones y catálogo público. Los actores externos son roles humanos (solicitante, admin técnico, directivo, consejo, comunidad) y un servicio de email institucional.
