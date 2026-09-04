# Matriz de Trazabilidad — [Nombre del Proyecto]

> **Fecha:** [Fecha]
> **Flujo crítico seleccionado:** [Nombre del flujo]
> **Por qué es crítico:** [Razón de la selección]

---

## Matriz

| ID | Fuente | Comportamiento esperado | Tipo de prueba | Evidencia | Resultado |
|:---|:-------|:------------------------|:---------------|:----------|:----------|
| RF-01 | SPEC §X.X | [Descripción] | E2E | Trace + reporte | [Pasa/Falla/Parcial/No evaluado] |
| RF-02 | SPEC §X.X | [Descripción] | E2E | Trace + reporte | [Pasa/Falla/Parcial/No evaluado] |
| CU-01.1 | Caso de uso | [Descripción] | E2E + humano | Captura | [Pasa/Falla/Parcial] |
| CU-01.2 | Caso de uso | [Descripción] | E2E + humano | Captura | [Pasa/Falla/Parcial] |
| RN-01 | Regla de negocio | [Descripción] | Unitario + integración | Test | [Pasa/Falla] |
| ADR-00X | ADR | [Decisión técnica] | Integración/revisión | Test API | [No evaluado por E2E] |

---

## Leyenda de estados

| Estado | Significado |
|:-------|:------------|
| **Pasa** | El comportamiento observado coincide con el oráculo |
| **Falla** | El comportamiento observado no coincide |
| **Parcial** | Cumple parcialmente, falta algo |
| **No evaluado** | No se pudo verificar con esta técnica |
| **Bloqueado** | No se puede evaluar por contradicción entre fuentes |

---

## Notas

- Cada fila debe tener un oráculo identificado (¿contra qué comparás?).
- No pongas todo como "E2E". Algunas cosas se prueban con unitarios o integración.
- Si algo no se puede evaluar con tu técnica, poné "No evaluado" y explicá por qué en las notas.
