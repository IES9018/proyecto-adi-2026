# TP N° 3: Interfaces que no Confunden — Diseño HCI con Criterios

> 📅 **Se publica:** mar 29 sep · **Entrega:** mar 13 oct · 🧠 Teoría: [Unidad 3 — Diseño de Interfaces (HCI)](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-3-diseno-de-interfaces)

> 🧭 **¿Llegaste directo acá?** Volvé al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme). Prerrequisito: **TP2 mergeado** (C4 + ADRs + SPEC v2).

---

## 💡 Por qué este TP

La IA genera pantallas en segundos — el problema es que genera pantallas que **nadie pidió**. Sin usuarios definidos, sin recorridos críticos y sin criterios de accesibilidad, la interfaz es decoración con botones. Este TP te obliga a decidir *para quién*, *para qué tarea* y *bajo qué estándar* antes de dejar que la IA pinte un solo componente. Es la diferencia entre "vibe UI" y diseño con criterios verificables.

## 🎯 Qué vas a lograr

Tu proyecto tiene **usuarios con nombre y apellido**, **recorridos críticos dibujados**, las **2 pantallas más importantes diseñadas en baja fidelidad**, una **auditoría heurística honesta**, y la decisión de stack de UI documentada como ADR.

---

## ✅ Entregables

### 1. Personas y recorridos — `docs/diseno/usuarios.md`
* **2 personas**: ficha breve (nombre, rol, objetivo, frustración principal, contexto de uso). Basadas en tu dominio real del SPEC, no genéricas.
* **2 user journeys en Mermaid**: los 2 flujos más críticos de tu sistema (ej.: *alta de turno* / *cobro*), indicando en cada paso: qué hace el usuario, qué ve el sistema, punto de posible abandono.

### 2. Wireframes de baja fidelidad — `docs/diseno/wireframes/`
Las **2 pantallas críticas** identificadas arriba:
* Un archivo `.md` por pantalla con wireframe en Mermaid (`graph` o bloques ASCII) **o** imagen exportada si preferís herramientas visuales.
* Cada wireframe acompaña: objetivo de la pantalla, entrada principal, error más probable del usuario y cómo la pantalla lo previene.

> Baja fidelidad = cero colores bonitos. Acá se discute estructura y flujo, no paletas.

### 3. Auditoría heurística propia — `docs/diseno/auditoria-heuristica.md`
Aplicá las **10 heurísticas de Nielsen** sobre tus 2 wireframes:
* Tabla: heurística | ¿cumple? | evidencia | corrección propuesta.
* Mínimo **3 problemas reales detectados y corregidos** (un hallazgo sin corrección no cuenta).

### 4. ADR-004 — Stack de UI · `docs/adr/ADR-004-stack-ui.md`
Framework/librería de interfaz + design system si aplica. Alternativas descartadas con criterios: curva de aprendizaje solo, ecosistema, accesibilidad out-of-the-box, compatibilidad con tu ADR-002.

### 5. SPEC v3
* Los RF de interfaz ahora tienen **criterios de aceptación estilo Given/When/Then**.
* Un requisito nuevo obligatorio: **accesibilidad básica** (navegación por teclado + contraste AA) en las 2 pantallas críticas.
* Changelog v2→v3 al pie.

---

## 📮 Entrega

```bash
git checkout -b feature/tp3-hci
git add docs/diseno docs/adr SPEC.md
git commit -m "feat: personas, journeys, wireframes, auditoria heuristica y adr-004"
git push -u origin feature/tp3-hci
```

PR → checklists → self-merge → auditoría docente posterior.

## ✅ Checklist antes del PR

- [ ] Las personas salen de TU dominio (no "usuario genérico")
- [ ] Los 2 journeys marcan puntos de abandono y cómo se mitigan
- [ ] Wireframes: estructura clara, anotados con objetivo y error prevenido
- [ ] Auditoría heurística: ≥3 hallazgos CON corrección aplicada al wireframe
- [ ] ADR-004 con alternativas descartadas objetivas
- [ ] SPEC v3 con Gherkin + requisito de accesibilidad + changelog

## 🔗 Conexión con PP3

El núcleo funcional del **Sprint 2** implementa estas pantallas: sin este TP, el sprint construye UI a ciegas.

## ❓ FAQ

**¿Puedo usar Figma y pegar capturas?** Sí, pero el archivo `.fig` no vive en tu repo ni tiene diff. Lo mínimo versionable (texto Mermaid) va al repo; Figma es complemento.
**¿WCAG completo?** No: alcance AA en navegación por teclado y contraste para tus 2 pantallas críticas. Non-Goal explícito todo lo demás.
