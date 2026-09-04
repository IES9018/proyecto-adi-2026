# TP N° 6: El Arnés Trabajá Solo — CI, Releases y Postmortem

> 📅 **Se publica:** mar 10 nov · **Entrega:** mar 17 nov · 🧠 Teoría: [Unidad 6 — Herramientas, Tecnologías e Integración](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-6-herramientas-y-tecnologias)

> 🧭 **¿Llegaste directo acá?** Volvé al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme). Prerrequisito: **TP5 mergeado**.

---

## 💡 Por qué este TP

Todo el cuatrimestre gobernaste a tu IA con reglas que *vos* hacías cumplir a mano. Este TP automatiza esa vigilancia: un pipeline que lint-ea el contrato OpenAPI, corre tests, mide presupuestos y bloquea PRs defectuosos — sin que nadie recuerde nada. Y como cierre de cuatrimestre, un **postmortem honesto**: los errores que la IA cometió y cómo tu proceso (SPEC → ADR → arnés → CI) los detectó. Ese documento es oro: es la evidencia real de que aprendiste a dirigir, no a teclear.

## 🎯 Qué vas a lograr

Tu repo tiene **CI en verde** que protege `main`, una **release etiquetada v0.1.0**, el arnés consolidado final, y un postmortem con hallazgos verificables.

---

## ✅ Entregables

### 1. Pipeline CI — `.github/workflows/ci.yml`
Workflow que se ejecuta en cada PR hacia `main`:
* **Lint del contrato**: valida `api-contracts.yaml` (`@redocly/cli lint`) — lo sembraste en TP4.
* **Tests**: corre tu suite unitaria; si no tenés ≥5 tests, este TP te los exige ahora.
* **Build**: compila/empaqueta tu proyecto.
* Badge de estado en tu README principal.
* Opcional +1 punto conceptual: job de Lighthouse corriendo un presupuesto del TP5.

> Regla del curso: **PR con CI rojo = merge prohibido** (agregalo como checklist de tu plantilla de PR).

### 2. Release v0.1.0
* `CHANGELOG.md` con formato Keep a Changelog: sección `[0.1.0] - fecha` listando features por categoría.
* Tag anotado `v0.1.0` sobre el commit de release.

### 3. Arnés vFinal — `.opencoderules`
Consolidación de todas las versiones anteriores (v1 TP1, v2 arquitectura, v3 seguridad) en un arnés único, ordenado por secciones (alcance / estándares / prohibiciones / proceso). Sin duplicados ni reglas muertas.

### 4. Postmortem lite — `docs/postmortem-cuatrimestre.md`
Tabla de **mínimo 3 incidentes reales** con IA durante el cuatrimestre:

| Incidente | Qué generó mal la IA | Cómo se detectó | Qué capa lo previene a futuro |
|---|---|---|---|
| … | … | revisión humana / test roto / lint / CI | SPEC · ADR · arnés · pipeline |

* Cada fila cita evidencia (link a PR, issue o commit donde ocurrió).
* Cierre reflexivo de 5 líneas: ¿qué harías distinto arrancando de cero?

### 5. SPEC vFinal
Estado "congelado para la defensa": changelog completo v1→final y trazabilidad ADR ↔ restricciones vigente.

---

## 📮 Entrega

```bash
git checkout -b feature/tp6-ci
git add .github CHANGELOG.md .opencoderules docs SPEC.md
git commit -m "feat: pipeline ci, release v0.1.0, arnes final y postmortem"
git push -u origin feature/tp6-ci
```

PR → checklists (incluye CI verde) → self-merge → tag → auditoría docente posterior.

## ✅ Checklist antes del PR

- [ ] CI corre en el PR y está **verde**
- [ ] Lint de OpenAPI incluido en el pipeline
- [ ] ≥5 tests pasando localmente y en CI
- [ ] Badge visible en README principal
- [ ] CHANGELOG + tag `v0.1.0`
- [ ] Arnés consolidado sin reglas duplicadas
- [ ] Postmortem: 3 incidentes con evidencia enlazada

## 🔗 Conexión con PP3

Este pipeline es la base del área **Testing y calidad (20%)** y del despliegue del **Sprint 3**; el postmortem alimenta directamente tu `auditoria-sprint*.md`.

## 🚀 Desafío avanzado (opcional)

Si querés ir más allá del TP6 y aprender a contrastar tu implementación contra SPEC, ADR y casos de uso mediante E2E, consultá el **Apéndice Avanzado — Testing de Consistencia y Trazabilidad**:

[trabajos-practicos/apendice-avanzado-testing-consistencia/](../apendice-avanzado-testing-consistencia/)

> Este desafío es **opcional** y otorga un bonus de hasta +1 punto sobre la nota final del cierre integrador de PP3. No reemplaza ningún entregable obligatorio.

## ❓ FAQ

**¿Docker es obligatorio?** Si tu stack lo necesita para correr en otra máquina: sí, Dockerfile multi-stage. Si no aplica: Non-Goal justificado en el postmortem.
**¿Puedo usar GitHub Actions de terceros?** Sí, pero cada action externa debe estar justificada en una línea del propio workflow.

> 📖 Un termino en ingles no te cierra? [Glosario del curso](../glosario.md)
