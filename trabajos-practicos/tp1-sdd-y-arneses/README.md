# TP N┬░ 1: Transici├│n de Vibe Coding a Spec-Driven Development (SDD)

> ­ƒôà **Vigente desde el inicio del cursado** ┬À ­ƒºá Teor├¡a necesaria: [Unidad 1](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-1-procesos-y-metodologias)

---

## ­ƒÄ» Qu├® vas a lograr

Al terminar este TP ten├®s tu proyecto de PP2 **migrado a un repositorio propio dentro de la organizaci├│n**, gobernado por SDD: especificaci├│n formal, primera decisi├│n arquitect├│nica documentada y un arn├®s que limita a tu agente IA.

---

## 0´©ÅÔâú Paso 0 ÔÇö Cre├í tu repositorio de trabajo

1. En GitHub, dentro de la organizaci├│n [`IES9018`](https://github.com/IES9018), cre├í un repositorio **p├║blico** llamado `<nombre_alumno>-<nombre_proyecto>` (ej.: `analia-crm`, `raul-turnos`).
2. **NO hagas fork** de este repo: cre├ís uno nuevo y vac├¡o (con README inicial opcional).
3. Copi├í desde este repo hacia el tuyo:
   - [`templates/SPEC-template.md`](../../templates/SPEC-template.md) ÔåÆ renombralo a `SPEC.md` en la ra├¡z.
   - [`templates/ADR-template.md`](../../templates/ADR-template.md) ÔåÆ a `docs/adr/ADR-template.md`.

---

## Ô£à Objetivos (lo que se eval├║a)

### 1. Especificaci├│n declarativa ÔÇö `SPEC.md`
Complet├í la plantilla para tu proyecto integrador:
* Contexto y prop├│sito.
* Requerimientos funcionales (RF-01ÔÇª).
* **Non-Goals:** qu├® NO vas a construir en esta etapa.
* Contratos de datos principales.

### 2. Decisi├│n arquitect├│nica ÔÇö `docs/adr/ADR-001-stack-tecnologico.md`
Document├í la elecci├│n del stack tecnol├│gico usando la plantilla ADR:
* Contexto del problema t├®cnico.
* Decisi├│n tomada.
* Al menos **dos alternativas descartadas** con criterios objetivos.
* Consecuencias (positivas y riesgos).

### 3. Arn├®s de IA ÔÇö `.opencoderules`
Cre├í en la ra├¡z tu primer arn├®s limitando el comportamiento del agente local (OpenCode):
* Alcance permitido (carpetas, tipos de archivos).
* Est├índares t├®cnicos obligatorios (ej.: tipado estricto, sintaxis ECMAScript 2024).
* Pr├ícticas prohibidas (ej.: tipo `any`, dependencias no aprobadas).

Opcional complementario: `INSTRUCTIONS.md` con instrucciones extendidas del agente.

---

## ­ƒô« Entrega: Pull Request en TU repositorio

El PR es la **evidencia evaluable**. Flujo:

```bash
# en tu repositorio <alumno>-<proyecto>
git checkout -b feature/tp1-sdd
git add SPEC.md docs/adr/ .opencoderules
git commit -m "feat: especificacion inicial, ADR-001 y arnes de IA"
git push -u origin feature/tp1-sdd
```

1. Abr├¡ el **Pull Request** `feature/tp1-sdd` ÔåÆ `main` **de tu propio repositorio**.
2. Complet├í la plantilla de PR (checklists de calidad y trazabilidad).
3. Revisa tu propio PR contra la plantilla y hace el merge cuando todos los checks esten completos.
4. Merge reci├®n con aprobaci├│n ÔÇö eso registra la entrega.

> ÔÜá´©Å Los repos de la c├ítedra (`ADI-teoria-y-recursos`, `proyecto-adi-2026`) son de **lectura**: ah├¡ no se entregan PRs. Dudas y sugerencias ÔåÆ **Issues**.

---

## ­ƒôî Checklist r├ípido antes de abrir el PR

- [ ] Repo creado en `IES9018` con nomenclatura correcta y p├║blico
- [ ] `SPEC.md` completo, con Non-Goals expl├¡citos
- [ ] `docs/adr/ADR-001-stack-tecnologico.md` con alternativas descartadas
- [ ] `.opencoderules` presente y con reglas propias (no vac├¡o)
- [ ] Commits convencionales (`feat:` / `docs:`)
- [ ] PR abierto hacia `main` de TU repo con descripci├│n completa
