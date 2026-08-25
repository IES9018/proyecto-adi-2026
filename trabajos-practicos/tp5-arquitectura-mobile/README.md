# TP N° 5: Tu Sistema en el Bolsillo — Estrategia Mobile Medible

> 📅 **Se publica:** mar 27 oct · **Entrega:** mar 10 nov · 🧠 Teoría: [Unidad 5 — Arquitectura Mobile](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-5-arquitectura-mobile)

> 🧭 **¿Llegaste directo acá?** Volvé al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme). Prerrequisito: **TP4 mergeado**.

---

## 💡 Por qué este TP

"Y en el celular, ¿funciona?" es la pregunta que revienta proyectos enteros en la demo final. La respuesta pro no es "le agregamos responsive un domingo": es una **decisión arquitectónica documentada** (responsive / PWA / nativa / híbrida) con **presupuestos de rendimiento medibles**. Este TP te hace comprometerte con números verificables — porque lo que no se mide, no se audita, y lo que no se audita lo decide la IA por vos.

## 🎯 Qué vas a lograr

Tu estrategia mobile está decidida y fundamentada, tus requisitos no funcionales son **números**, tenés la forma automática de medirlos, y sabés exactamente qué pasa sin conexión.

---

## ✅ Entregables

### 1. ADR-006 — Estrategia mobile · `docs/adr/ADR-006-estrategia-mobile.md`
Responsive web vs. PWA vs. nativa vs. híbrida (Flutter/RN/Capacitor):
* **Matriz de decisión explícita**: filas = criterios (costo de mantenimiento 1 persona, offline necesario?, acceso a hardware?, tiempo hasta PP3 cierre), columnas = opciones, celdas justificadas.
* Decisión + consecuencias (qué NO vas a poder hacer, escrito antes de sufrirlo).

### 2. Presupuestos de rendimiento — `docs/arquitectura/presupuestos-rendimiento.md`
Tabla de objetivos numéricos para las 2 pantallas críticas del TP3:

| Métrica | Presupuesto | Cómo se mide |
|---|---|---|
| LCP móvil | < 2.5 s (4G) | Lighthouse CI |
| INP | < 200 ms | Lighthouse CI |
| Peso inicial JS | < 200 KB gzip | `source-map-explorer` |

* Cada presupuesto incluye la **herramienta concreta** que lo verifica.
* Al menos uno debe poder correrse en CI (preparando el terreno del TP6).

### 3. Offline-first o Non-Goal justificado — `docs/arquitectura/offline-sync.md`
Según tu dominio:
* Si el uso offline es real (ej.: campo, depósitos): estrategia simple (cache + cola de sincronización) descrita en ≤1 página con diagrama Mermaid de secuencia.
* Si NO aplica: archivo con el **Non-Goal declarado**, el motivo, y qué condición futura lo reabriría. Los Non-Goals argumentados valen igual que los features.

### 4. Wireframe adaptativo — `docs/diseno/wireframes/`
Las 2 pantallas críticas del TP3 reinterpretadas en breakpoint móvil (< 400 px):
* Comparación lado a lado (desktop vs. móvil) con nota de qué cambió y por qué (targets táctiles ≥48px según Material/web.dev — Apple HIG usa el equivalente 44pt —, jerarquía, contenido recortado).

### 5. SPEC v5
* Sección **Requisitos No Funcionales** con los presupuestos como requisitos medibles (RNF-01…).
* Changelog v4→v5.

---

## 📮 Entrega

```bash
git checkout -b feature/tp5-mobile
git add docs SPEC.md
git commit -m "feat: adr-006, presupuestos de rendimiento, offline y wireframes moviles"
git push -u origin feature/tp5-mobile
```

PR → checklists → self-merge → auditoría docente posterior.

## ✅ Checklist antes del PR

- [ ] Matriz de decisión del ADR-006 con criterios de TU contexto (1 desarrollador, fechas PP3)
- [ ] Los presupuestos tienen herramienta de medición asignada
- [ ] Offline: estrategia O Non-Goal justificado (no silencio)
- [ ] Wireframes móviles anotan los cambios respecto a desktop
- [ ] RNF numerados y trazables desde los presupuestos

## 🔗 Conexión con PP3

Los RNF medibles son los que el **Sprint 3** verifica al desplegar; llegar sin ellos significa aceptar cualquier performance que produzca la IA.

## ❓ FAQ

**¿Tengo que escribir una app nativa?** No. Para la mayoría de sus proyectos, responsive/PWA bien ejecutada gana la matriz. El TP premia la decisión fundamentada, no la tecnología cara.
