### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Andamiaje de Agentes IA — Guía del Estudiante

## ¿Qué es esto?

Un método de trabajo con 8 agentes IA especializados que trabajan **en orden, uno a la vez, bajo tu supervisión**.

No es un solo prompt que genera todo el proyecto. Es un **equipo de desarrollo virtual** donde cada agente tiene un rol específico, produce artefactos en su carpeta correspondiente, y no avanza hasta que vos revises y apruebes.

---

## Los 8 Agentes

| # | Agente | Carpeta | ¿Qué produce? | ¿Qué hace el estudiante? |
|:-:|:-------|:--------|:--------------|:--------------------------|
| 0 | **DevOps** | Raíz del proyecto | `.gitignore`, README inicial, primer commit, configuración del repo | Crear el repo en GitHub, dar acceso al equipo |
| 1 | **Analista** | `00_REFERENCIAS/` | Requisitos funcionales y no funcionales, stakeholders | Responder preguntas del agente sobre el proyecto |
| 2 | **Arquitecto** | `01_PLAN_MAESTRO/` + `03_ARQUITECTURA/` | Visión arquitectónica, diagramas C4, ADRs | Revisar diagramas, aprobar o pedir cambios |
| 3 | **Modelador** | `04_MODELO_DATOS/` | Entidades DDD, esquema DB, relaciones | Validar que el modelo refleje el negocio real |
| 4 | **Especificador** | `02_CASOS_DE_USO/` | Casos de uso detallados (Cockburn), diagramas UML | Verificar que los flujos sean correctos |
| 5 | **Diseñador UI** | `06_INTERFAZ_USUARIO/` | Wireframes, flujos de navegación | Decidir el diseño final, aprobar cambios |
| 6 | **Tech Lead** | `07_IMPLEMENTACION/` | Stack tecnológico, convenciones de código, setup del proyecto | Elegir las tecnologías, definir estándares |
| 7 | **Desarrollador** | `08_CODIGO_FUENTE/` | Código funcional con tests | Revisar el código, probar, reportar bugs |

---

## Flujo de Trabajo

```
AGENTE 0: DevOps           → Crea repo, .gitignore, rama
    ↓ (PR → revisión → merge)
AGENTE 1: Analista         → Documenta requisitos
    ↓ (PR → revisión → merge)
AGENTE 2: Arquitecto       → C4 + ADRs
    ↓ (PR → revisión → merge)
AGENTE 3: Modelador        → Entidades + DB
    ↓ (PR → revisión → merge)
AGENTE 4: Especificador    → Casos de uso
    ↓ (PR → revisión → merge)
AGENTE 5: Diseñador UI     → Wireframes
    ↓ (PR → revisión → merge)
AGENTE 6: Tech Lead        → Stack + setup
    ↓ (PR → revisión → merge)
AGENTE 7: Desarrollador    → Código + tests
```

**Cada flecha es un Pull Request.** No avanzás al siguiente agente sin que el docente apruebe el PR del anterior.

---

## Cómo Empezar

### 1. Instalá un CLI de IA

Tenés estas opciones (elegí una):

```bash
# opencode (recomendada, gratuita)
curl -fsSL https://opencode.ai/install | bash

# gemini-cli (Google, gratuita con API key de AI Studio)
npm install -g @google/gemini-cli
```

### 2. Creá tu repositorio

```bash
gh repo create IES9018/mi-proyecto --public --clone
cd mi-proyecto
```

### 3. Iniciá la sesión con Prompt 1

Copiá el contenido de [`prompt-1-definicion.md`](./prompt-1-definicion.md) en tu terminal de IA. La IA te va a entrevistar para definir tu proyecto.

### 4. Seguí con Prompt 2

Cuando la IA te diga que pasés al siguiente prompt, copiá [`prompt-2-orquestacion.md`](./prompt-2-orquestacion.md) más el resumen de tu proyecto.

### 5. Trabajá un agente a la vez

Cada agente produce archivos, vos los revisás, creás un PR, el docente lo revisa, y recién ahí pasás al siguiente.

---

## Reglas de Oro

| Regla | Explicación |
|:------|:------------|
| **Una rama por agente** | `feat/agente-01-analista`, `feat/agente-02-arquitecto`... |
| **Un PR por agente** | No acumules varios agentes en un mismo PR |
| **Revisá antes de avanzar** | Leé el output del agente. Si no lo entendés, pedile que te lo explique |
| **El agente propone, vos disponés** | Podés rechazar sugerencias del agente y pedir cambios |
| **Commit atómico** | `git commit -m "feat: completa agente 01 - requisitos"` |
| **Nunca `git push --force`** | Podés borrar commits de otros. Preguntá antes al docente |

---

---

## 🧑‍🏫 ¡Conocé al @docente!

Además de los 8 agentes de construcción, tenés disponible un **Arquitecto Docente** que podés invocar en cualquier momento:

```
@docente explicame esto: ADR
```

Este agente:

- **Busca un ejemplo real** en tu repositorio
- **Explica el concepto general** en lenguaje claro
- **Justifica para qué sirve**, quién lo usa y por qué es importante
- **Te da una analogía** para que nunca más lo olvides

> 📖 Ver [`agente-docente.md`](./agente-docente.md) para instrucciones y el banco de analogías.

Las analogías que vas descubriendo se agregan al banco compartido. Cada vez que encontrás una buena, podés abrir un Issue o un PR para que quede disponible para todos.

---

## 🤝 Filosofía Colaborativa

### Este repositorio es de todos

Cada estudiante tiene algo valioso para aportar. Tal vez descubriste una analogía que te hizo click. Tal vez modificaste un prompt del andamiaje para que funcione mejor. Tal vez creaste un **Agente 9** nuevo.

**Todo eso se comparte.**

```
1. Descubriste algo útil
       ↓
2. Abrís un Issue o un PR
       ↓
3. Se revisa y se incorpora
       ↓
4. Todos los estudiantes (presentes y futuros) se benefician
```

### Cómo contribuir con agentes

Si creaste un agente nuevo o mejoraste uno existente:

1. **Discutilo primero**: abrí un Issue con la etiqueta `agente`
2. **Creamos o modificamos** el prompt en `02-andamiaje-agentes/`
3. **Hacés un PR** al repositorio principal [IES9018/proyecto-adi-2026](https://github.com/IES9018/proyecto-adi-2026)
4. **Tu nombre queda registrado** como autor del agente

> 📖 Guía completa de contribución en [`CONTRIBUTING.md`](../CONTRIBUTING.md)

---

## 📝 Proyecto Personal para Rendir

Al final del año, cada estudiante debe rendir con un **proyecto personal** que demuestre todo lo aprendido.

Es **altamente recomendable** que uses el andamiaje de agentes para construirlo:

| Fase | Herramienta |
|:-----|:------------|
| Definir el proyecto | Prompt 1 (scoping) |
| Construir el sistema | Prompt 2 (agentes 0 a 7) |
| Entender conceptos | @docente |
| Documentar decisiones | ADRs generados por el Arquitecto |
| Presentar la defensa | Ej-06 (defensa oral) |

> El proyecto que construyas con este andamiaje **es el mismo que presentás para rendir**. No es trabajo extra: es el trabajo bien hecho.

---

## Qué Aprende el Estudiante con Este Método

| Habilidad | Cómo se aprende |
|:----------|:----------------|
| Pensamiento arquitectónico | Revisando y aprobando ADRs del agente Arquitecto |
| Modelado de dominio | Validando entidades y relaciones del agente Modelador |
| Diseño de interfaces | Decidiendo wireframes del agente Diseñador UI |
| Documentación técnica | Leyendo y entendiendo los archivos que el agente genera |
| Trabajo en equipo | Coordinando con compañeros en el mismo repo, usando PRs |
| Uso profesional de IA | Orquestando agentes, no pidiendo "hacéme todo" |
| Control de versiones | Ramas, commits, PRs, merge: el flujo real de la industria |
| Comunicación | Escribiendo PRs claros, code review, feedback |

---

## Para Recordar

> La IA no te va a hacer el proyecto. Te va a ayudar a construirlo.
> Vos sos el director del equipo. Los agentes son tus asistentes.
> Si no entendés lo que el agente produjo, no avances. Pedí explicación.
> El aprendizaje está en la revisión, no en la generación automática.
>
> Este repositorio es tuyo también. Lo que aprendas, compartilo.
> En 5 años, cuando estés trabajando en serio, tu analogía o tu agente
> va a estar ayudando a otro estudiante que recién empieza.
