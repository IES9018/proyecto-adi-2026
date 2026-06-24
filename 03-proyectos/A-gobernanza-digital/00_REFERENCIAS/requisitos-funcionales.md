# Requisitos Funcionales — Gobernanza Digital

> **Fuente:** [IES9018/gobernanza-servicios-digitales](https://github.com/IES9018/gobernanza-servicios-digitales)
> **Agente:** Analista | **Fecha:** Junio 2026

---

## RF-01: Solicitud de alojamiento

El sistema debe permitir que un usuario registrado complete una solicitud de alojamiento con los siguientes campos:

| Campo | Tipo | Obligatorio | Fuente (doc gobernanza) |
|:------|:-----|:-----------:|:------------------------|
| Nombre del proyecto | Texto | Sí | [Doc 01 §1](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/01_SOLICITUD_ALOJAMIENTO.md) |
| Nivel solicitado (1/2/3) | Select | Sí | [Doc 00 §5](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/00_INDICE.md) |
| Subdominio solicitado | Texto | Sí | [Doc 00 §3](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/00_INDICE.md) |
| Justificación del subdominio | Texto | Sí | [Doc 01 §1] |
| Descripción del servicio | Texto largo | Sí | [Doc 01 §2] |
| Objetivo educativo | Texto largo | Sí | [Doc 01 §2] |
| Arquitectura utilizada | Select + texto | Sí (alumnos) | [Doc 01 §3] |
| Justificación arquitectónica | Texto largo | Sí (alumnos) | [Doc 01 §3] |
| Patrón de diseño principal | Texto | Sí (alumnos) | [Doc 01 §3] |
| URL del repositorio | URL | Sí | [Doc 01 §4] |
| Licencia | Select | Sí | [Doc 01 §4] |
| Lenguajes y frameworks | Texto | Sí | [Doc 01 §5] |
| Base de datos | Texto | Sí | [Doc 01 §5] |
| Puertos necesarios | Texto | Sí | [Doc 01 §5] |
| Almacenamiento requerido | Texto | No | [Doc 01 §5] |
| APIs externas | Texto | No | [Doc 01 §5] |
| Acceso público (Sí/No) | Boolean | Sí | [Doc 01 §6] |
| Método de autenticación | Select | Sí | [Doc 01 §6] |
| Roles de usuario | Texto | No | [Doc 01 §6] |
| ¿Almacena datos personales? | Checkbox | Sí | [Doc 01 §7] |
| Contenido generado por usuarios | Checkbox | Sí | [Doc 01 §8] |
| Declaración de riesgos | Tabla | Sí | [Doc 01 §9] |

---

## RF-02: Evaluación técnica

El admin técnico debe poder completar una evaluación técnica que incluya:

| Sección | Campos | Fuente |
|:--------|:-------|:-------|
| Repositorio y licencia | Repo público, fork IES9018, licencia compatible | [Doc 02 §2](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/02_EVALUACION_TECNICA.md) |
| Justificación arquitectónica | Coherencia con código, patrones verificables | [Doc 02 §3] |
| Seguridad | HTTPS, hash contraseñas, variables entorno, puerto 127.0.0.1, dependencias, headers | [Doc 02 §4] |
| Operación | Dockerizado, logs, backup, responsable, reinicio, contacto | [Doc 02 §5] |
| Infraestructura | Puertos sin conflicto, recursos asignados, subdominio apropiado | [Doc 02 §6] |
| Dictamen | Apto / Condicional / No apto, nivel recomendado, observaciones | [Doc 02 §7] |

---

## RF-03: Evaluación institucional

El directivo debe poder evaluar institucionalmente la solicitud:

- Alineación con el perfil profesional de la carrera
- Contribución educativa del proyecto
- Riesgo institucional
- Recomendación al Consejo Directivo
- Fuente: [Doc 03](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/03_EVALUACION_INSTITUCIONAL.md)

---

## RF-04: Aprobación / Rechazo con resolución

El Consejo Directivo debe poder emitir una resolución que:

- Apruebe o rechace la solicitud
- Incluya fundamentos de la decisión
- Especifique condiciones (si las hay)
- Registre fecha, firmantes y número de resolución
- Fuente: [Doc 08](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/08_RESOLUCION_DIRECTIVA.md)

---

## RF-05: Notificaciones por cambio de estado

El sistema debe notificar por email al solicitante cuando:

- Su solicitud pasa a "en evaluación técnica"
- Su solicitud pasa a "en evaluación institucional"
- Se emite una resolución (aprobación o rechazo)
- Se solicita información adicional

---

## RF-06: Catálogo público de servicios

Cualquier persona (sin autenticación) debe poder ver:

- Listado de servicios activos con: nombre, descripción, responsable, nivel, fecha de aprobación
- Enlace al repositorio del proyecto
- Estado actual del servicio
- Fuente: [Doc 12](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/12_TRANSPARENCIA_COMUNITARIA.md)

---

## RF-07: Gestión de usuarios

El sistema debe soportar tres roles:

| Rol | Permisos |
|:----|:---------|
| **Solicitante** | Crear solicitudes, ver estado de sus solicitudes, editar solicitudes en borrador |
| **Admin Técnico** | Ver todas las solicitudes, completar evaluación técnica, cambiar estado |
| **Directivo** | Ver solicitudes evaluadas, completar evaluación institucional, emitir resolución, suspender servicios |

---

## RF-08: Historial de cambios por solicitud

Cada solicitud debe tener un registro de auditoría que muestre:

- Quién hizo el cambio (usuario y rol)
- Qué cambió (campo, valor anterior, valor nuevo)
- Cuándo cambió (timestamp)
- Fuente: [Doc 09](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/09_AUDITABILIDAD.md)

---

## RF-09: Suspensión de servicios

El admin técnico debe poder suspender un servicio indicando:

- Motivo de la suspensión
- Fecha y hora
- El sistema debe notificar al responsable
- El sistema debe mostrar el servicio como "suspendido" en el catálogo
- Fuente: [Doc 00 §10](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/00_INDICE.md), [Doc 11](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/11_EMERGENCIA_Y_CONTROL.md)

---

## RF-10: Niveles de servicio (SLA)

El sistema debe reflejar los 3 niveles definidos en el marco:

| Nivel | Nombre | Características | Aprobación |
|:------|:-------|:----------------|:-----------|
| 1 | Experimental | Proyectos en desarrollo, sin datos reales, acceso interno (LAN/Tailscale) | Docente tutor |
| 2 | Institucional | Datos institucionales no sensibles, acceso con autenticación | Consejo Directivo |
| 3 | Público | Acceso desde internet, datos personales o de terceros | CD + Declaración + Revisión técnica |

Fuente: [Doc 00 §5](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/00_INDICE.md), [Doc 06](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/06_SLA_EDUCATIVO.md)
