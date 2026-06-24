# 🏛️ Proyecto Ejemplar: Gobernanza de Servicios Digitales

> **Proyecto transversal** — Aplica a Arquitectura y Diseño de Interfaces, Práctica Profesionalizante III, Programación III, Base de Datos y Laboratorio de Servidores.

---

## 🧠 Analogía del @docente

> *Imaginate que el IES 9-018 es una **ciudad** y el servidor institucional es el **terreno donde se construyen los edificios** (sitios web). Hasta ahora, cada persona que quería construir iba directamente al terreno y ponía los ladrillos sin permiso. Algunos edificios quedaban abandonados, otros se caían, y nadie llevaba un registro de quién construyó qué.*
>
> *La **Gobernanza de Servicios Digitales** es el **código de planeamiento urbano** de esa ciudad. Define: quién puede construir, qué documentos necesita presentar, quién aprueba los planos, cómo se mantienen los edificios, y qué pasa cuando un edificio se abandona.*
>
> *Tu trabajo como equipo de desarrollo es construir la **ventanilla única** donde los ciudadanos presentan sus solicitudes, los técnicos revisan los planos, el intendente firma los permisos, y todo queda registrado para la historia.*

---

## 📋 ¿Qué es este proyecto?

Es un **proyecto ejemplar** que muestra cómo construir un sistema completo desde cero, con **toda la documentación y el código funcional**, usando el andamiaje de agentes IA.

El sistema digitaliza el proceso de solicitud y aprobación de alojamiento web en el servidor institucional del IES 9-018.

---

## 🔗 Materias involucradas

| Materia | Qué aporta al proyecto |
|:--------|:-----------------------|
| **Arquitectura y Diseño de Interfaces** | Patrones arquitectónicos (Hexagonal, MVC), ADRs, C4 Model, wireframes, diseño UX/UI |
| **Práctica Profesionalizante III** | Proyecto integrador real con stakeholders reales, despliegue, documentación profesional |
| **Programación III** | Arquitectura web, WebSockets para notificaciones en tiempo real, MQTT para eventos |
| **Base de Datos** | Modelo de datos, entidades, relaciones, consultas, migraciones |
| **Laboratorio de Servidores** | Despliegue en servidor institucional, Docker, CI/CD, monitoreo, backups |

---

## 🗂️ Estructura del proyecto ejemplar

```
gobernanza-digital/
│
├── 00_REFERENCIAS/          ← Análisis y requisitos
│   ├── requisitos.md
│   ├── stakeholders.md
│   └── glosario-dominio.md
│
├── 01_PLAN_MAESTRO/         ← Visión y decisiones estratégicas
│   ├── vision.md
│   └── principios-arquitectonicos.md
│
├── 02_CASOS_DE_USO/         ← Requisitos funcionales detallados
│   ├── CU-01-solicitar-alojamiento.md
│   ├── CU-02-evaluar-tecnicamente.md
│   ├── CU-03-aprobar-directivo.md
│   ├── CU-04-notificar-cambio-estado.md
│   └── diagramas-casos-uso.md
│
├── 03_ARQUITECTURA/         ← Diseño arquitectónico
│   ├── diagrama-contexto-c4.md
│   ├── diagrama-contenedores-c4.md
│   ├── diagrama-componentes-c4.md
│   ├── hexagonal.md
│   └── adr/                 ← Architecture Decision Records
│       ├── ADR-001-stack-tecnologico.md
│       ├── ADR-002-arquitectura-hexagonal.md
│       ├── ADR-003-base-de-datos.md
│       ├── ADR-004-autenticacion.md
│       └── ADR-005-frontend.md
│
├── 04_MODELO_DATOS/         ← Dominio y persistencia
│   ├── modelo-dominio.md
│   ├── entidades.md
│   ├── esquema-db.sql
│   └── diagrama-entidad-relacion.md
│
├── 05_AGENTES_IA/           ← Metodología de agentes aplicada
│   └── sesiones/            ← Outputs de cada agente (ejemplos reales)
│
├── 06_INTERFAZ_USUARIO/     ← Diseño de UI/UX
│   ├── wireframes/
│   ├── flujo-navegacion.md
│   └── guia-estilos.md
│
├── 07_IMPLEMENTACION/       ← Guías técnicas y setup
│   ├── stack.md
│   ├── setup.md
│   ├── ci-cd.md
│   └── deploy.md
│
├── 08_CODIGO_FUENTE/        ← Código funcional
│   ├── src/
│   │   ├── domain/          ← Entidades, puertos, lógica de negocio
│   │   ├── application/     ← Casos de uso, servicios
│   │   ├── infrastructure/  ← DB, email, adaptadores
│   │   └── web/             ← API endpoints, middlewares
│   └── tests/
│       ├── unit/
│       ├── integration/
│       └── e2e/
│
└── README.md
```

> **Analogía del @docente:** Esta estructura de carpetas es como los **cajones de un escritorio ordenado**. Cada cajón tiene un propósito: uno para los planos (arquitectura), otro para los contratos (casos de uso), otro para las herramientas (código). Cuando necesitás algo, sabés exactamente en qué cajón buscarlo. Un escritorio desordenado es un proyecto sin estructura: todo está mezclado y encontrar algo lleva horas.

---

## 🎯 Funcionalidades del sistema

| # | Funcionalidad | Prioridad | Materia relacionada |
|:-:|:--------------|:---------:|:--------------------|
| 1 | Formulario de solicitud de alojamiento | Alta | ADI (UX), Programación III |
| 2 | Evaluación técnica con checklist | Alta | PP III, Lab Servidores |
| 3 | Panel de aprobación directiva | Alta | PP III |
| 4 | Notificaciones por email + WS | Alta | Programación III (WebSockets) |
| 5 | Catálogo público de servicios activos | Media | ADI, Base de Datos |
| 6 | Historial de cambios por solicitud | Media | Base de Datos |
| 7 | Roles: Solicitante, Admin Técnico, Directivo | Alta | ADI (patrones), Programación III |
| 8 | Despliegue automatizado con CI/CD | Media | Lab Servidores |

---

## 🧱 Stack tecnológico

| Capa | Tecnología | ¿Por qué? (justificación en ADR) |
|:-----|:-----------|:---------------------------------|
| Frontend | React + Vite | ADR-005: Componentes modulares, ecosistema maduro |
| Backend | Python + FastAPI | ADR-001: Tipado, documentación automática, async |
| Base de Datos | PostgreSQL | ADR-003: Madurez, soporte institucional |
| ORM | SQLModel | ADR-003: Unifica modelos Python con DB |
| Autenticación | JWT + OAuth2 | ADR-004: Stateless, compatible con API |
| Infraestructura | Docker + Docker Compose | ADR-002: Entorno reproducible, mismo en desarrollo y producción |
| CI/CD | GitHub Actions | ADR-001: Integración nativa con GitHub |
| Testing | pytest + Playwright | Pirámide de testing: unitarios, integración, E2E |

---

## 🧠 Analogías del @docente en cada capa

### Arquitectura Hexagonal (Capa de Dominio)

> *Es como un **tomacorriente universal**. Tu lógica de negocio (el dispositivo) se enchufa a cualquier pared: podés usar SQLite para desarrollo, PostgreSQL para producción, o incluso archivos JSON para pruebas. El dominio no sabe ni le importa qué hay del otro lado del enchufe.*

### API REST (Capa Web)

> *Es como la **carta de un restaurante**. Cada endpoint es un plato del menú: `POST /solicitudes` es "pedir una solicitud nueva", `GET /solicitudes/{id}` es "consultar el estado de mi pedido". Si la carta está bien diseñada, los clientes saben exactamente qué pedir y cómo.*

### Base de Datos (Capa de Persistencia)

> *Es como el **archivero de una oficina pública**. Cada solicitud es un expediente con número único. Los expedientes tienen estados (pendiente, en revisión, aprobado, rechazado). Los funcionarios buscan expedientes, los actualizan y los archivan. Si el archivero está bien organizado, encontrar un expediente lleva segundos.*

### Notificaciones en Tiempo Real (WebSockets)

> *Es como el **tablero de una estación de tren**. Cuando el estado de tu solicitud cambia, el tablero se actualiza solo, sin que tengas que recargar la página. No necesitás preguntar "¿ya está?" — el sistema te avisa.*

---

## 📚 Documentación de referencia

Toda la documentación del marco de gobernanza original está en:

> [IES9018/gobernanza-servicios-digitales](https://github.com/IES9018/gobernanza-servicios-digitales)

| Documento | Descripción |
|:----------|:------------|
| [01_SOLICITUD_ALOJAMIENTO](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/01_SOLICITUD_ALOJAMIENTO.md) | Formulario que completa el solicitante |
| [02_EVALUACION_TECNICA](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/02_EVALUACION_TECNICA.md) | Checklist del admin técnico |
| [03_EVALUACION_INSTITUCIONAL](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/03_EVALUACION_INSTITUCIONAL.md) | Evaluación del directivo |
| [04_DECLARACION_RESPONSABILIDAD](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/04_DECLARACION_RESPONSABILIDAD.md) | Términos que acepta el solicitante |
| [05_POLITICA_USO_ACEPTABLE](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/05_POLITICA_USO_ACEPTABLE.md) | Reglas de uso del servidor |
| [06_SLA_EDUCATIVO](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/06_SLA_EDUCATIVO.md) | Acuerdo de nivel de servicio |
| [07_SOLICITUD_USUARIO](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/07_SOLICITUD_USUARIO.md) | Solicitud de cuenta de usuario |
| [08_RESOLUCION_DIRECTIVA](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/08_RESOLUCION_DIRECTIVA.md) | Resolución que aprueba/rechaza |
| [09_AUDITABILIDAD](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/09_AUDITABILIDAD.md) | Registro de auditoría |
| [10_GLOSARIO](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/10_GLOSARIO.md) | Términos del marco de gobernanza |
| [11_EMERGENCIA_Y_CONTROL](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/11_EMERGENCIA_Y_CONTROL.md) | Procedimientos de emergencia |
| [12_TRANSPARENCIA_COMUNITARIA](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/12_TRANSPARENCIA_COMUNITARIA.md) | Catálogo público de servicios |
| [13_PREVISION_INFRAESTRUCTURA](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/13_PREVISION_INFRAESTRUCTURA.md) | Planificación de capacidad |

---

## 🚀 Cómo se construyó este proyecto (para estudiar)

Cada carpeta del proyecto fue generada por un **agente del andamiaje**, en orden:

| Paso | Agente | Archivos generados | Cómo estudiarlo |
|:-----|:-------|:-------------------|:----------------|
| 1 | **Analista** | `00_REFERENCIAS/` | Leé los requisitos y preguntate: ¿cubren todas las funcionalidades? |
| 2 | **Arquitecto** | `01_PLAN_MAESTRO/`, `03_ARQUITECTURA/` | Revisá los ADRs: cada decisión está justificada, con alternativas y consecuencias |
| 3 | **Modelador** | `04_MODELO_DATOS/` | Compará el modelo con los requisitos: ¿cada requisito tiene su entidad? |
| 4 | **Especificador** | `02_CASOS_DE_USO/` | Seguí un flujo completo: desde que el solicitante completa el formulario hasta que recibe la notificación |
| 5 | **Diseñador UI** | `06_INTERFAZ_USUARIO/` | Los wireframes muestran cada pantalla. Compralos con los casos de uso |
| 6 | **Tech Lead** | `07_IMPLEMENTACION/` | El stack tecnológico está justificado en los ADRs |
| 7 | **Desarrollador** | `08_CODIGO_FUENTE/` | El código sigue la arquitectura hexagonal. Cada caso de uso tiene su test |

---

## 📖 Para estudiantes: cómo estudiar este proyecto

### Si estás en ADI
- Empezá por `03_ARQUITECTURA/adr/` — leé las decisiones en orden
- Después `03_ARQUITECTURA/diagrama-contenedores-c4.md`
- Después `06_INTERFAZ_USUARIO/wireframes/`
- Finalmente, compará los wireframes con el código del frontend

### Si estás en PP III
- Empezá por `00_REFERENCIAS/` — los requisitos son el contrato con el cliente
- Después `02_CASOS_DE_USO/` — cada caso de uso es un entregable
- Después `07_IMPLEMENTACION/deploy.md` — cómo se despliega en el servidor real

### Si estás en Programación III
- Empezá por `03_ARQUITECTURA/adr/ADR-001-stack-tecnologico.md`
- Después `08_CODIGO_FUENTE/src/web/` — los endpoints de la API
- Después los WebSockets para notificaciones en tiempo real

### Si estás en Base de Datos
- Empezá por `04_MODELO_DATOS/entidades.md`
- Después `04_MODELO_DATOS/esquema-db.sql`
- Después compará con `04_MODELO_DATOS/diagrama-entidad-relacion.md`

### Si estás en Laboratorio de Servidores
- Empezá por `07_IMPLEMENTACION/setup.md`
- Después `07_IMPLEMENTACION/ci-cd.md`
- Después `07_IMPLEMENTACION/deploy.md`

---

## 🧪 ¿Qué podés hacer con este proyecto?

| Como estudiante... | Podés... |
|:-------------------|:----------|
| **Leerlo** | Estudiar la estructura, los ADRs, los diagramas C4, los tests |
| **Ejecutarlo** | Clonar, instalar dependencias, correr el servidor local |
| **Modificarlo** | Agregar una funcionalidad nueva, mejorar un test, corregir un bug |
| **Extenderlo** | Agregar integración con Slack, exportar a PDF, estadísticas |
| **Analizarlo** | Usar el @arquitecto para auditar, el @docente para entender |

> Todo lo que aprendas acá lo podés aplicar a **tu propio proyecto personal** para rendir.

---

## 📜 Licencia

Este proyecto es **código abierto** bajo licencia MIT. Podés usarlo, estudiarlo, modificarlo y compartirlo.

---

## 🧠 Palabras finales del @docente

> *Estudiar un proyecto ya terminado es como **disecar un reloj para entender cómo funciona**. Podés ver todas las piezas, cómo encajan, qué hace cada una. Pero la magia no está en las piezas, sino en cómo se sincronizan para medir el tiempo.*
>
> *Este proyecto es tu reloj para diseccionar. No tengas miedo de desarmarlo, romperlo y volverlo a armar. Cada vez que lo hagas, vas a entender mejor cómo funciona la arquitectura de software.*
>
> *Y cuando llegue el momento de construir TU proyecto, vas a tener un modelo en la cabeza de cómo hacerlo bien.*
