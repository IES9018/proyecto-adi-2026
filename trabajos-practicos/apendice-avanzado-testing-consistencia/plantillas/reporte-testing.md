# Reporte de Testing e Inconsistencias — [Nombre del Proyecto]

> **Fecha:** [Fecha]
> **Suite ejecutada:** [Nombre de la suite o archivo]
> **Entorno:** [Local / CI / Otro]

---

## Resumen de ejecución

| Métrica | Valor |
|:--------|:------|
| Tests ejecutados | [N] |
| Tests pasados | [N] |
| Tests fallidos | [N] |
| Tests pendientes | [N] |
| Tiempo total | [N s] |

---

## Detalle por test

| Test | Escenario | Estado | Tiempo | Observaciones |
|:-----|:----------|:------:|-------:|:--------------|
| [nombre del test] | [happy path / validación / control de acceso] | ✅ / ❌ | [N ms] | [Observaciones si falla] |

---

## Inconsistencias encontradas

### Inconsistencia 1: [Título]

- **Fuente A:** [SPEC §X.X / Caso de uso / ADR] — [Cita textual o referencia]
- **Fuente B:** [Implementación / Otra fuente] — [Qué se observó]
- **Comportamiento observado:** [Descripción detallada]
- **Tipo de prueba:** [E2E / Integración / Unitario / Humano]
- **Estado:** [Pendiente de decisión / Corregido / Descartado]
- **Acción:** [Corregir código / Actualizar SPEC / Consultar profesor]
- **Evidencia:** [Link a commit, PR o captura]

### Inconsistencia 2: [Título]

[Seguir formato...]

---

## Inspección humana de UI/UX

| Aspecto | Resultado | Mejora sugerida |
|:--------|:----------|:----------------|
| Feedback al usuario | [OK / Problema] | [Descripción] |
| Claridad de mensajes | [OK / Problema] | [Descripción] |
| Orientación post-acción | [OK / Problema] | [Descripción] |
| Jerarquía visual | [OK / Problema] | [Descripción] |
| Errores comprensibles | [OK / Problema] | [Descripción] |
| Navegación con teclado | [OK / Problema] | [Descripción] |
| Indicador de progreso | [OK / Problema] | [Descripción] |
| Persistencia de datos | [OK / Problema] | [Descripción] |

### Capturas de inspección

| Captura | Propósito | Archivo |
|:--------|:----------|:--------|
| [Descripción] | [Por qué se capturó] | [Ruta del archivo] |

---

## Escaneo de secretos

| Herramienta | Alcance | Hallazgos | Falsos positivos | Acciones tomadas |
|:------------|:--------|:----------|:-----------------:|:-----------------|
| [Gitleaks / otro] | [Árbol actual / Historial] | [N] | [N] | [Descripción] |

> **Nota:** Los valores de los secretos NUNCA se incluyen en este reporte. Todo está redactado.

---

## Conclusión

[Resumen breve: qué se probó, qué se encontró, qué quedó pendiente]
