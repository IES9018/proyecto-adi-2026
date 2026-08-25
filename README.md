# ADI ÔÇö Proyecto Base y Trabajos Pr├ícticos ­ƒøá´©Å

**Arquitectura y Dise├▒o de Interfaces ┬À IES 9-018 ┬À Ciclo 2026**
Tecnicatura Superior en Desarrollo de Software ┬À 3┬░ A├▒o ┬À Prof. Paulo Alvarez

> Este es el **repo de consignas, plantillas y andamiaje**: ac├í busc├ís tu TP y las plantillas para TU repositorio individual. La teor├¡a est├í en [`ADI-teoria-y-recursos`](https://github.com/IES9018/ADI-teoria-y-recursos) y los sprints de PP3 en [`proyecto-pp3-2026`](https://github.com/IES9018/proyecto-pp3-2026).

---

## ­ƒÜª EMPEZ├ü AC├ü (D├¡a 1)

| Paso | Qu├® hacer | D├│nde |
|---|---|---|
| 1 | Instal├í las herramientas del entorno | [instalacion-herramientas-cli.md](./instalacion-herramientas-cli.md) |
| 2 | Le├® el **TP vigente** (hoy: TP 1) | [trabajos-practicos/tp1-sdd-y-arneses/](./trabajos-practicos/tp1-sdd-y-arneses/) |
| 3 | Cre├í **tu repositorio individual** en la org `IES9018` | nomenclatura `<nombre_alumno>-<nombre_proyecto>` (ej. `analia-crm`) ÔÇö **sin forks** |
| 4 | Copi├í a tu repo las plantillas + arn├®s | [templates/](./templates/) ┬À `.opencoderules` (este repo) |
| 5 | Escrib├¡ tu `SPEC.md` con la plantilla | [SPEC-template.md](./templates/SPEC-template.md) |

---

## ­ƒÄ» TP VIGENTE

### TP N┬░ 1 ÔÇö De Vibe Coding a Spec-Driven Development
­ƒôì `trabajos-practicos/tp1-sdd-y-arneses/` ÔåÆ [abrir consigna](./trabajos-practicos/tp1-sdd-y-arneses/README.md)

| Entregable | D├│nde queda en TU repo |
|---|---|
| `SPEC.md` inicial del proyecto (desde PP2) | ra├¡z |
| `docs/adr/ADR-001-stack-tecnologico.md` | docs/adr/ |
| Arn├®s `.opencoderules` (+ `INSTRUCTIONS.md`) | ra├¡z |

Teor├¡a necesaria: [Unidad 1](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-1-procesos-y-metodologias).

---

## ­ƒº¡ Ruta de lectura de este repo

| Orden | Carpeta | Para qu├® |
|---|---|---|
| 1 | [`Planificaciones/`](./Planificaciones/) | Programa oficial + Contrato Pedag├│gico firmado |
| 2 | [`01-teoria/`](./01-teoria/) | Desarrollo ampliado por tema (complementa el repo de teor├¡a) |
| 3 | [`05-ejercicios/`](./05-ejercicios/) | Ejercicios guiados (entrevista arquitecto, C4, ADR, dominio, wireframe, defensa) |
| 4 | [`trabajos-practicos/`](./trabajos-practicos/) | Ô¡É Consignas de los TPs |
| 5 | [`03-proyectos/A-gobernanza-digital/`](./03-proyectos/A-gobernanza-digital/README.md) | Proyecto modelo de referencia punta a punta |
| 6 | [`06-agentes-cli/`](./06-agentes-cli/) | Cat├ílogo de agentes IA de c├ítedra |
| ÔÇö | [`glosario.md`](./glosario.md) | 25 t├®rminos con analog├¡as (consultalo SIEMPRE que un t├®rmino te suene raro) |
| ÔÇö | [`04-github-workflow/`](./04-github-workflow/) | El flujo Git completo explicado |

---

## ­ƒÅù´©Å Estructura obligatoria de TU repositorio individual

Us├í como referencia el andamiaje completo del proyecto modelo:

```
tu-repo/
Ôö£ÔöÇÔöÇ SPEC.md                  ÔåÉ especificaci├│n declarativa (obligatoria)
Ôö£ÔöÇÔöÇ .opencoderules           ÔåÉ arn├®s IA (obligatorio)
Ôö£ÔöÇÔöÇ INSTRUCTIONS.md          ÔåÉ instrucciones del agente (recomendado)
Ôö£ÔöÇÔöÇ docs/
Ôöé   ÔööÔöÇÔöÇ adr/                 ÔåÉ decisiones arquitect├│nicas numeradas
Ôö£ÔöÇÔöÇ 00_REFERENCIAS ÔÇª 08_CODIGO_FUENTE   ÔåÉ ver proyecto modelo
```

Referencia completa: [A-gobernanza-digital](./03-proyectos/A-gobernanza-digital/README.md)

---

## ­ƒöä Flujo de entrega (Pull Request)

1. Rama `feature/<tema>` desde tu rama principal.
2. Commits convencionales (`feat:` `fix:` `docs:`).
3. PR con la plantilla autom├ítica (checklists de calidad + seguridad + trazabilidad a issue).
4. Completa los checklists de la plantilla y **hace el merge vos mismo**.
5. Merge reci├®n con aprobaci├│n.

Plantilla: [.github/PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md)

---

## ­ƒôè Evaluaci├│n (criterios oficiales)

| ├ürea | % |
|---|---|
| Dise├▒o de arquitectura y justificaci├│n t├®cnica | 30% |
| Dise├▒o de interfaces y usabilidad | 25% |
| Integraci├│n tecnol├│gica | 20% |
| Documentaci├│n de decisiones y entregables | 15% |
| Trabajo colaborativo y uso cr├¡tico de agentes IA | 10% |

R├║brica detallada por niveles: [rubrica-evaluacion.md](./rubrica-evaluacion.md)
Marco completo: [Programa oficial](./Planificaciones/Programa-Arquitectura-y-Diseno-de-Interfaces-2026.md) ┬À [Contrato pedag├│gico](./Planificaciones/Contrato-Pedagogico-Arquitectura-y-Diseno-de-Interfaces-2026.md)

---

## ÔØô FAQ r├ípida

| Pregunta | Respuesta corta |
|---|---|
| ┬┐Hago fork de este repo? | **NO.** Cre├ís tu propio repo en `IES9018`. |
| ┬┐Puedo usar IA? | S├¡, con arn├®s configurado y revisi├│n cr├¡tica tuya documentada. |
| ┬┐D├│nde veo c├│mo se ve un proyecto completo? | [Proyecto modelo A-gobernanza-digital](./03-proyectos/A-gobernanza-digital/README.md). |
| ┬┐Qu├® hago si me traba algo t├®cnico? | Issue en este repo + consulta en clase. |
