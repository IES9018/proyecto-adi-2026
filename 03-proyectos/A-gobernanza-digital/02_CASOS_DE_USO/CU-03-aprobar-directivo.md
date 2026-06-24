# CU-03: Emitir Resolución (Aprobar o Rechazar)

**Formato:** Cockburn | **Nivel:** Usuario | **Prioridad:** Alta

---

## Actor principal
Directivo / Consejo Directivo

## Precondición
- Usuario autenticado con rol `directivo`
- Existe una solicitud en estado `pendiente_institucional`
- La solicitud tiene evaluación técnica aprobada y evaluación institucional completada

## Flujo principal

1. El directivo ingresa al panel del Consejo Directivo
2. Ve la lista de solicitudes listas para resolución
3. Selecciona una solicitud
4. El sistema muestra: datos completos + evaluación técnica + evaluación institucional
5. El directivo completa el formulario de resolución:
   - Decisión: Aprobada / Rechazada
   - Fundamentos (obligatorio)
   - Condiciones (opcional, si la aprobación es condicional)
6. El sistema genera automáticamente el número de resolución: `RES-YYYY-NNN`
7. El directivo confirma
8. El sistema guarda la resolución
9. El sistema actualiza el estado de la solicitud: `aprobada` o `rechazada`
10. El sistema envía notificación al solicitante

## Flujos alternativos

**5a. Rechazo**
1. El directivo debe explicar los fundamentos del rechazo
2. Debe indicar si el solicitante puede volver a presentar una versión corregida

**8a. Número de resolución duplicado**
1. El sistema verifica unicidad
2. Si ya existe, genera el siguiente número disponible

## Postcondición
- Resolución guardada con número único
- Estado de la solicitud actualizado
- Notificación enviada
- Auditoría registrada
