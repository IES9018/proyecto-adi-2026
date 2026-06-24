# Historias de Usuario — Gobernanza Digital

> **Agente:** Analista | **Formato:** "Como [rol], quiero [acción] para [beneficio]"

---

## HU-01: Solicitar alojamiento

**Como** estudiante o docente  
**Quiero** completar un formulario de solicitud de alojamiento con todos los campos requeridos  
**Para** pedir formalmente que mi proyecto sea alojado en el servidor escolar

**Criterios de aceptación:**
- [ ] El formulario tiene todos los campos del [Doc 01](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/01_SOLICITUD_ALOJAMIENTO.md)
- [ ] Campos obligatorios validados antes de enviar
- [ ] Se puede guardar como borrador y continuar después
- [ ] Al enviar, la solicitud queda en estado "pendiente de evaluación técnica"
- [ ] El solicitante recibe confirmación por email

**Prioridad:** Alta | **Complejidad:** Media

---

## HU-02: Ver estado de mis solicitudes

**Como** solicitante  
**Quiero** ver un panel con todas mis solicitudes y su estado actual  
**Para** saber en qué etapa está cada una sin tener que preguntar

**Criterios de aceptación:**
- [ ] Listado de solicitudes con: nombre, fecha, estado, última actualización
- [ ] Estados visibles: borrador, pendiente evaluación técnica, en evaluación institucional, aprobada, rechazada, suspendida
- [ ] Cada solicitud muestra su historial de cambios

**Prioridad:** Alta | **Complejidad:** Baja

---

## HU-03: Evaluar técnicamente una solicitud

**Como** admin técnico  
**Quiero** completar el checklist de evaluación técnica sobre una solicitud  
**Para** verificar que el proyecto cumple los requisitos de seguridad y operación antes de aprobarlo

**Criterios de aceptación:**
- [ ] Checklist con todas las secciones del [Doc 02](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/02_EVALUACION_TECNICA.md)
- [ ] Campos: cumple/no cumple/condicional con observaciones
- [ ] Al completar, la solicitud pasa a "en evaluación institucional" o "rechazada"
- [ ] Se notifica al solicitante

**Prioridad:** Alta | **Complejidad:** Media

---

## HU-04: Evaluar institucionalmente una solicitud

**Como** directivo  
**Quiero** revisar una solicitud que pasó la evaluación técnica y emitir una evaluación institucional  
**Para** asegurar que el proyecto está alineado con los objetivos educativos

**Criterios de aceptación:**
- [ ] Ver los datos de la solicitud y la evaluación técnica
- [ ] Campos de evaluación institucional (alineación, contribución, riesgo)
- [ ] Emitir dictamen: favorable / desfavorable / condicional
- [ ] La solicitud pasa al Consejo Directivo para resolución final

**Prioridad:** Alta | **Complejidad:** Media

---

## HU-05: Emitir resolución (aprobar o rechazar)

**Como** miembro del Consejo Directivo  
**Quiero** emitir una resolución formal que apruebe o rechace una solicitud  
**Para** formalizar la decisión institucional con trazabilidad

**Criterios de aceptación:**
- [ ] Ver la solicitud completa + evaluación técnica + evaluación institucional
- [ ] Emitir resolución: aprobada / rechazada, con fundamentos
- [ ] Número de resolución autogenerado
- [ ] Fecha y firmantes registrados
- [ ] Se notifica al solicitante por email

**Prioridad:** Alta | **Complejidad:** Baja

---

## HU-06: Ver catálogo público de servicios

**Como** cualquier persona (sin autenticación)  
**Quiero** ver un listado de los servicios digitales activos en el servidor escolar  
**Para** conocer qué proyectos están funcionando y quién los mantiene

**Criterios de aceptación:**
- [ ] Acceso público, sin login
- [ ] Listado con: nombre, descripción, responsable, nivel, fecha de aprobación, enlace al repo
- [ ] Filtro por nivel (1/2/3) y estado
- [ ] Los servicios suspendidos se muestran como tales

**Prioridad:** Media | **Complejidad:** Baja

---

## HU-07: Registrar usuario y gestionar roles

**Como** admin técnico  
**Quiero** crear cuentas de usuario y asignar roles (solicitante, admin técnico, directivo)  
**Para** controlar quién puede hacer cada cosa en el sistema

**Criterios de aceptación:**
- [ ] Registro con email, nombre, rol
- [ ] Contraseña con políticas de seguridad (mínimo 8 caracteres)
- [ ] Cambio de contraseña
- [ ] El admin técnico es el único que puede crear usuarios con rol "admin técnico" o "directivo"

**Prioridad:** Alta | **Complejidad:** Media

---

## HU-08: Suspender un servicio

**Como** admin técnico  
**Quiero** suspender un servicio activo indicando el motivo  
**Para** proteger el servidor ante incidentes de seguridad o abandono

**Criterios de aceptación:**
- [ ] Seleccionar un servicio activo
- [ ] Registrar motivo de suspensión
- [ ] El servicio pasa a estado "suspendido"
- [ ] Se notifica al responsable
- [ ] El servicio suspendido sigue visible en el catálogo pero marcado

**Prioridad:** Media | **Complejidad:** Baja

---

## HU-09: Iniciar sesión

**Como** usuario registrado  
**Quiero** iniciar sesión con email y contraseña  
**Para** acceder a las funcionalidades según mi rol

**Criterios de aceptación:**
- [ ] Login con email + contraseña
- [ ] JWT con access token (30 min) y refresh token (7 días)
- [ ] Protección contra fuerza bruta (rate limiting)
- [ ] Redirección según rol después del login

**Prioridad:** Alta | **Complejidad:** Media

---

## HU-10: Ver historial de cambios

**Como** admin técnico o directivo  
**Quiero** ver el historial completo de cambios de una solicitud  
**Para** auditar quién hizo qué y cuándo

**Criterios de aceptación:**
- [ ] Registro cronológico de cambios
- [ ] Muestra: usuario, rol, campo modificado, valor anterior, valor nuevo, timestamp
- [ ] Filtrable por tipo de cambio (estado, evaluación, resolución)

**Prioridad:** Media | **Complejidad:** Baja
