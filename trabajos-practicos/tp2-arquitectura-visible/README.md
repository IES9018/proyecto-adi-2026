# TP N° 2: Arquitectura Visible — Modelo C4 y Decisiones Continuas

> 📅 **Se publica:** mar 15 sep · **Entrega:** mar 29 sep · 🧠 Teoría: [Unidad 2 — Arquitectura de Software](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-2-arquitectura-de-software)

> 🧭 **¿Llegaste directo acá?** Volvé siempre al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme). Prerrequisito: **TP1 mergeado** en tu repo (SPEC + ADR-001 + arnés).

---

## 💡 Por qué este TP

En el TP1 especificaste *qué* construís. Ahora respondés *cómo se sostiene*: todo sistema que sobrevive al primer deploy necesita una arquitectura **explicable**. Si no podés dibujarla en dos niveles (contexto y contenedores), tu IA va a generar código sin rumbo y vos no vas a poder auditarla. Este TP convierte tu arquitectura en un artefacto versionado, discutible y evolucionable — y te deja los diagramas que PP3 te va a pedir en el Sprint 2.

## 🎯 Qué vas a lograr

Al terminar tenés tu sistema **dibujado en C4** (contexto + contenedores), **dos decisiones arquitectónicas nuevas documentadas**, y tu SPEC promovida a versión 2 con restricciones explícitas.

---

## ✅ Entregables

### 1. Diagramas C4 — `docs/arquitectura/`
Dos vistas, en Mermaid dentro de Markdown (GitHub las renderiza):

| Archivo | Vista | Debe mostrar mínimamente |
|---|---|---|
| `C4-contexto.md` | Nivel 1 — Contexto | Tu sistema como caja negra, usuarios/actores, sistemas externos (APIs, mail, pagos…) |
| `C4-contenedores.md` | Nivel 2 — Contenedores | Apps, bases de datos, servicios internos, protocolos entre ellos |

> Regla de oro: **si un elemento no aparece en tu SPEC o en algún ADR, no puede aparecer en el diagrama.** El diagrama documenta decisiones tomadas, no deseos.

### 2. ADR-002 — Estilo arquitectónico · `docs/adr/ADR-002-estilo-arquitectonico.md`
Elegí el estilo general de tu sistema y documentalo con la plantilla ADR:
* Mínimo **dos alternativas descartadas** (ej.: monolito modular vs. microservicios vs. serverless) con **criterios objetivos**: tamaño del equipo (¡1 persona!), costo, complejidad operativa, deadlines de PP3.
* Sección **Consecuencias**: qué te facilita y qué te encarece la elección.

### 3. ADR-003 — Persistencia · `docs/adr/ADR-003-persistencia.md`
Misma mecánica: SQL vs. NoSQL vs. archivos/embedded (SQLite). Justificá con el **modelo de datos real de tu SPEC**, no con moda.

### 4. SPEC v2 — actualización versionada
* Nueva sección **"Restricciones arquitectónicas"** que cite ADR-001/002/003 por ID.
* Revisá tus **Non-Goals**: ¿algo que descartaste ahora es factible? ¿algo asumido ahora es Non-Goal? Toda baja/alta de requisito se registra en una tabla `Changelog` al pie de la SPEC (`v1 → v2`, fecha, motivo).

### 5. Arnés v2 — una regla nueva
Agregá a `.opencoderules` una regla que fuerce coherencia arquitectónica. Ejemplo:

```text
- PROHIBIDO introducir frameworks, bases de datos o servicios externos
  que no estén declarados en un ADR aprobado. Ante duda, proponer ADR nuevo.
```

---

## 📮 Entrega

```bash
git checkout -b feature/tp2-arquitectura
git add docs/arquitectura docs/adr SPEC.md .opencoderules
git commit -m "feat: diagramas c4, adr-002/003 y spec v2"
git push -u origin feature/tp2-arquitectura
```

PR hacia `main` de TU repo → checklists completos → mergeás vos. El docente audita después.

## ✅ Checklist antes del PR

- [ ] Los 2 diagramas renderizan correctamente en la vista previa de GitHub
- [ ] Cada elemento de los diagramas es trazable a SPEC o ADR (sin cajas fantasma)
- [ ] ADR-002 y ADR-003 tienen ≥2 alternativas descartadas con criterios objetivos
- [ ] SPEC tiene sección Restricciones + tabla Changelog v1→v2
- [ ] `.opencoderules` incluye la regla anti-dependencias-no-documentadas
- [ ] Commits convencionales y PR con descripción completa

## 🔗 Conexión con PP3

Estos diagramas son exactamente los que pide el **Sprint 2** (`docs/arquitectura/DIAGRAMAS_REFERENCIA`). Haciendo bien este TP, ese entregable queda gratis.

## ❓ FAQ

**¿Puedo usar imágenes en vez de Mermaid?** Podés, pero Mermaid es texto: versionable, diffable y auditable — igual que el código. Preferimos Mermaid.
**¿Mi arquitectura va a cambiar después?** Seguro. Por eso existen los ADR: se agrega un ADR nuevo que supersede al anterior, nunca se borra historia.
