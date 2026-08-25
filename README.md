# ADI — Proyecto Base y Trabajos Prácticos 🛠️

**Arquitectura y Diseño de Interfaces · IES 9-018 · Ciclo 2026**
Tecnicatura Superior en Desarrollo de Software · 3° Año · Prof. Paulo Alvarez

> Este es el **repo de consignas, plantillas y andamiaje**: acá buscás tu TP y las plantillas para TU repositorio individual. La teoría está en [`ADI-teoria-y-recursos`](https://github.com/IES9018/ADI-teoria-y-recursos) y los sprints de PP3 en [`proyecto-pp3-2026`](https://github.com/IES9018/proyecto-pp3-2026).

---

## 🚦 EMPEZÁ ACÁ (Día 1)

| Paso | Qué hacer | Dónde |
|---|---|---|
| 1 | Instalá las herramientas del entorno | [instalacion-herramientas-cli.md](./instalacion-herramientas-cli.md) |
| 2 | Leé el **TP vigente** (hoy: TP 1) | [trabajos-practicos/tp1-sdd-y-arneses/](./trabajos-practicos/tp1-sdd-y-arneses/) |
| 3 | Creá **tu repositorio individual** en la org `IES9018` | nomenclatura `<nombre_alumno>-<nombre_proyecto>` (ej. `analia-crm`) — **sin forks** |
| 4 | Copiá a tu repo las plantillas + arnés | [templates/](./templates/) · `.opencoderules` (este repo) |
| 5 | Escribí tu `SPEC.md` con la plantilla | [SPEC-template.md](./templates/SPEC-template.md) |

---

## 🎯 TP VIGENTE

### TP N° 1 — De Vibe Coding a Spec-Driven Development
📍 `trabajos-practicos/tp1-sdd-y-arneses/` → [abrir consigna](./trabajos-practicos/tp1-sdd-y-arneses/README.md)

| Entregable | Dónde queda en TU repo |
|---|---|
| `SPEC.md` inicial del proyecto (desde PP2) | raíz |
| `docs/adr/ADR-001-stack-tecnologico.md` | docs/adr/ |
| Arnés `.opencoderules` (+ `INSTRUCTIONS.md`) | raíz |

Teoría necesaria: [Unidad 1](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-1-procesos-y-metodologias).

---

## 🧭 Ruta de lectura de este repo

| Orden | Carpeta | Para qué |
|---|---|---|
| 1 | [`Planificaciones/`](./Planificaciones/) | Programa oficial + Contrato Pedagógico firmado |
| 2 | [`01-teoria/`](./01-teoria/) | Desarrollo ampliado por tema (complementa el repo de teoría) |
| 3 | [`05-ejercicios/`](./05-ejercicios/) | Ejercicios guiados (entrevista arquitecto, C4, ADR, dominio, wireframe, defensa) |
| 4 | [`trabajos-practicos/`](./trabajos-practicos/) | ⭐ Consignas de los TPs |
| 5 | [`03-proyectos/A-gobernanza-digital/`](./03-proyectos/A-gobernanza-digital/README.md) | Proyecto modelo de referencia punta a punta |
| 6 | [`06-agentes-cli/`](./06-agentes-cli/) | Catálogo de agentes IA de cátedra |
| — | [`glosario.md`](./glosario.md) | 25 términos con analogías (consultalo SIEMPRE que un término te suene raro) |
| — | [`04-github-workflow/`](./04-github-workflow/) | El flujo Git completo explicado |

---

## 🏗️ Estructura obligatoria de TU repositorio individual

Usá como referencia el andamiaje completo del proyecto modelo:

```
tu-repo/
├── SPEC.md                  ← especificación declarativa (obligatoria)
├── .opencoderules           ← arnés IA (obligatorio)
├── INSTRUCTIONS.md          ← instrucciones del agente (recomendado)
├── docs/
│   └── adr/                 ← decisiones arquitectónicas numeradas
├── 00_REFERENCIAS … 08_CODIGO_FUENTE   ← ver proyecto modelo
```

Referencia completa: [A-gobernanza-digital](./03-proyectos/A-gobernanza-digital/README.md)

---

## 🔄 Flujo de entrega (Pull Request)

1. Rama `feature/<tema>` desde tu rama principal.
2. Commits convencionales (`feat:` `fix:` `docs:`).
3. PR con la plantilla automática (checklists de calidad + seguridad + trazabilidad a issue).
4. El docente revisa como **Capataz de Obra**: aprueba o pide cambios.
5. Merge recién con aprobación.

Plantilla: [.github/PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md)

---

## 📊 Evaluación (criterios oficiales)

| Área | % |
|---|---|
| Diseño de arquitectura y justificación técnica | 30% |
| Diseño de interfaces y usabilidad | 25% |
| Integración tecnológica | 20% |
| Documentación de decisiones y entregables | 15% |
| Trabajo colaborativo y uso crítico de agentes IA | 10% |

Rúbrica detallada por niveles: [rubrica-evaluacion.md](./rubrica-evaluacion.md)
Marco completo: [Programa oficial](./Planificaciones/Programa-Arquitectura-y-Diseno-de-Interfaces-2026.md) · [Contrato pedagógico](./Planificaciones/Contrato-Pedagogico-Arquitectura-y-Diseno-de-Interfaces-2026.md)

---

## ❓ FAQ rápida

| Pregunta | Respuesta corta |
|---|---|
| ¿Hago fork de este repo? | **NO.** Creás tu propio repo en `IES9018`. |
| ¿Puedo usar IA? | Sí, con arnés configurado y revisión crítica tuya documentada. |
| ¿Dónde veo cómo se ve un proyecto completo? | [Proyecto modelo A-gobernanza-digital](./03-proyectos/A-gobernanza-digital/README.md). |
| ¿Qué hago si me traba algo técnico? | Issue en este repo + consulta en clase. |
