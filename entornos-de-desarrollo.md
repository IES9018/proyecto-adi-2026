# 🧰 Entornos de Desarrollo Alternativos — Mismo Control, Otra Herramienta

> **Regla de oro:** esta materia evalúa cómo *dirigís* el desarrollo, no qué editor usás. Podés trabajar con OpenCode, VS Code + Copilot, Cursor, Windsurf u otro agente — **siempre que no pierdas el control** y respetes el orden: **primero la documentación, codificar al final.**

---

## 📐 Lo que NO cambia (obligatorio en todos los casos)

| # | Artefacto de control | Por qué |
|---|---|---|
| 1 | `SPEC.md` **antes** que una línea de código | La especificación manda; el código la implementa |
| 2 | `docs/adr/ADR-00x` para cada decisión relevante | Decisiones trazables y reversibles |
| 3 | **Arnés del agente** configurado en la raíz (ver tabla abajo) | Sin límites escritos, tu IA decide por vos |
| 4 | Rama `feature/<tema>` + PR con plantilla + **self-merge** | Historial auditable y reversible |
| 5 | Commits convencionales (`feat:` `fix:` `docs:`…) | Trazabilidad automática |
| 6 | **Auditoría humana**: leés cada línea que genera la IA | Vos firmás el código, no la herramienta |
| 7 | Entregables en los mismos paths (`SPEC.md`, `docs/auditoria/…`) | Tu repo se audita igual que el de todos |

> Si algo de esta lista falta, tu entrega está incompleta **sin importar qué IDE usaste**.

---

## 🗂️ El arnés según tu entorno

El "arnés" es el archivo de instrucciones que tu agente lee solo al arrancar. Cada herramienta tiene el suyo — **usá el nativo del que realmente ejecutás**:

| Entorno | Archivo(s) de arnés | Notas |
|---|---|---|
| **OpenCode** *(estándar de la cátedra)* | `.opencoderules` + `INSTRUCTIONS.md` | El que usan los ejemplos del curso |
| **VS Code + GitHub Copilot** | `.github/copilot-instructions.md` | Copilot lo carga automáticamente como contexto |
| **Cursor** | `.cursor/rules/*.mdc` (moderno) o `.cursorrules` (legado) | Preferí la carpeta `rules/` |
| **Windsurf** | `.windsurfrules` | Equivalente directo |
| **Claude Code** | `CLAUDE.md` | Ídem |
| **Aider** | `CONVENTIONS.md` | Se pasa con `--read` o auto |
| **Codex / agentes multi-tool** | `AGENTS.md` | Estándar emergente multi-herramienta |

**¿Usás más de uno?** Versioná ambos archivos: deben decir lo mismo. Regla práctica: escribí el contenido base una vez y copialo — divergencias entre arneses = comportamiento impredecible de la IA.

---

## ✍️ Contenido mínimo del arnés (idéntico en cualquier formato)

Tres secciones, sin excepciones:

```markdown
# Arnés del proyecto <nombre_proyecto>

## Alcance permitido
- Modificar solo: src/, tests/, docs/
- Prohibido tocar: .github/workflows/, infraestructura, archivos de otros equipos

## Estándares obligatorios
- Tipado estricto / validación de entradas en el borde
- Commits convencionales; todo endpoint nace en el contrato (Sprint 3+)
- Cada feature va en su rama feature/<tema> con su PR

## Prohibiciones
- Ninguna dependencia nueva sin ADR aprobado
- Nunca hardcodear secrets ni credenciales
- No generar código fuera del alcance declarado en SPEC.md
```

Adaptalo a tu stack (el estándar de tipado cambia si usás Python vs TypeScript), **pero mantené las tres secciones**: alcance, estándares, prohibiciones.

---

## 🔁 Flujo idéntico, ejemplo VS Code

```bash
# 0. Escribís SPEC.md y ADR-001 ANTES de abrir el chat de Copilot
git checkout -b feature/tp1-sdd
# 1. Configurás .github/copilot-instructions.md con las 3 secciones
git add SPEC.md docs/adr .github/copilot-instructions.md
git commit -m "feat: especificacion inicial, adr-001 y arnes de ia"
git push -u origin feature/tp1-sdd
# 2. Abrís el PR en TU repo, completás checklists, mergeás vos
```

Después: el docente audita el PR mergeado igual que el de quien usó OpenCode.

---

## ❓ FAQ

**¿Puedo cambiar de entorno a mitad del cuatrimestre?**
Sí. Commiteá el arnés del nuevo agente (los dos pueden convivir) y seguí. El historial de PRs es la evidencia continua, no la herramienta.

**¿La herramienta se evalúa?**
No. Se evalúa el control: SPEC viva, ADRs, arnés presente, PRs prolijos, auditoría crítica honesta. Un alumno con Notepad+disciplina supera a uno con el mejor IDE sin SPEC.

**¿Qué pongo en mi repo para avisar qué uso?**
Una línea en tu `README.md`: *"Entorno: VS Code + Copilot · Arnés: .github/copilot-instructions.md"*. Así el docente sabe dónde mirar.

**¿Los entregables cambian de lugar?**
No. `DEL-SN-XX` apuntan a los mismos paths para todos (`SPEC.md`, `docs/auditoria/auditoria-sprintN.md`, etc.).

---

*Referencia cruzada: consigna [TP1 — Paso 3](./trabajos-practicos/tp1-sdd-y-arneses/README.md) · Checklist del sprint vigente en [proyecto-pp3-2026](https://github.com/IES9018/proyecto-pp3-2026)*
