# TP N° 1: Transición de Vibe Coding a Spec-Driven Development (SDD)

> 📅 **Vigente desde el inicio del cursado** · 🧠 Teoría necesaria: [Unidad 1](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-1-procesos-y-metodologias)
>
> 🧭 **¿Llegaste directo acá?** Esta consigna vive en `proyecto-adi-2026`. Si te perdés, volvé siempre al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme) — ahí están la ruta completa y el TP vigente. Contexto: [Teoría Unidad 1](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-1-procesos-y-metodologias) · [Coordinación PP3](https://github.com/IES9018/proyecto-pp3-2026)

---

## 🎯 Qué vas a lograr

Al terminar este TP tenés tu proyecto de PP2 **migrado a un repositorio propio dentro de la organización**, gobernado por SDD: especificación formal, primera decisión arquitectónica documentada y un arnés que limita a tu agente IA.

---

## 0´©Å⃣ Paso 0 — Creá tu repositorio de trabajo

1. En GitHub, dentro de la organización [`IES9018`](https://github.com/IES9018), creá un repositorio **público** llamado `<nombre_alumno>-<nombre_proyecto>` (ej.: `analia-crm`, `raul-turnos`).
2. **NO hagas fork** de este repo: creás uno nuevo y vacío (con README inicial opcional).
3. Copiá desde este repo hacia el tuyo:
   - [`templates/SPEC-template.md`](../../templates/SPEC-template.md) → renombralo a `SPEC.md` en la raíz.
   - [`templates/ADR-template.md`](../../templates/ADR-template.md) → a `docs/adr/ADR-template.md`.

---

## ✅ Objetivos (lo que se evalúa)

### 1. Especificación declarativa — `SPEC.md`
Completá la plantilla para tu proyecto integrador:
* Contexto y propósito.
* Requerimientos Funcionales o **RF**: cada función concreta del sistema vista desde afuera (el sistema permite...), numerada (RF-01, RF-02...) para poder probarla y rastrearla.
* **Non-Goals:** qué NO vas a construir en esta etapa.
* Contratos de datos principales.

### 2. Decisión arquitectónica — `docs/adr/ADR-001-stack-tecnologico.md`
Documentá la elección del stack tecnológico usando la plantilla ADR:
* Contexto del problema técnico.
* Decisión tomada.
* Al menos **dos alternativas descartadas** con criterios objetivos.
* Consecuencias (positivas y riesgos).

### 3. Arnés de IA — `.opencoderules`
Creá en la raíz tu primer arnés limitando el comportamiento del agente local (OpenCode):
* Alcance permitido (carpetas, tipos de archivos).
* Estándares técnicos obligatorios (ej.: tipado estricto, sintaxis ECMAScript 2024).
* Prácticas prohibidas (ej.: tipo `any`, dependencias no aprobadas).

Usás otro agente (VS Code+Copilot, Cursor, Windsurf...)? El arnés se adapta al nativo de tu herramienta: [entornos de desarrollo](../../entornos-de-desarrollo.md).

Opcional complementario: `INSTRUCTIONS.md` con instrucciones extendidas del agente.

---

## 📮 Entrega: Pull Request en TU repositorio

El PR es la **evidencia evaluable**. Flujo:

```bash
# en tu repositorio <alumno>-<proyecto>
git checkout -b feature/tp1-sdd
git add SPEC.md docs/adr/ .opencoderules
git commit -m "feat: especificacion inicial, ADR-001 y arnes de IA"
git push -u origin feature/tp1-sdd
```

1. Abrí el **Pull Request** `feature/tp1-sdd` → `main` **de tu propio repositorio**.
2. Completá la plantilla de PR (checklists de calidad y trazabilidad).
3. Revisa tu propio PR contra la plantilla y hace el merge cuando todos los checks esten completos.
4. Merge recién con aprobación — eso registra la entrega.

> ⚠️ Los repos de la cátedra (`ADI-teoria-y-recursos`, `proyecto-adi-2026`) son de **lectura**: ahí no se entregan PRs. Dudas y sugerencias → **Issues**.

---

## 📌 Checklist rápido antes de abrir el PR

- [ ] Repo creado en `IES9018` con nomenclatura correcta y público
- [ ] `SPEC.md` completo, con Non-Goals explícitos
- [ ] `docs/adr/ADR-001-stack-tecnologico.md` con alternativas descartadas
- [ ] `.opencoderules` presente y con reglas propias (no vacío)
- [ ] Commits convencionales (`feat:` / `docs:`)
- [ ] PR abierto hacia `main` de TU repo con descripción completa
