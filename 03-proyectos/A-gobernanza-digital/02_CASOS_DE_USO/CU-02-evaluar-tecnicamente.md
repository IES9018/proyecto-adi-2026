# CU-02: Evaluar Técnicamente

**Formato:** Cockburn | **Nivel:** Usuario | **Prioridad:** Alta

---

## Actor principal
Admin Técnico

## Precondición
- Usuario autenticado con rol `admin_tecnico`
- Existe una solicitud en estado `pendiente_tecnica`

## Flujo principal

1. El admin técnico ingresa al panel de solicitudes pendientes
2. Selecciona una solicitud en estado `pendiente_tecnica`
3. El sistema muestra los datos de la solicitud
4. El admin técnico completa el checklist de [Doc 02](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/02_EVALUACION_TECNICA.md):
   - Repositorio público y licencia
   - Seguridad (HTTPS, hash, variables de entorno, puertos, headers)
   - Operación (Docker, logs, backup, responsable)
   - Infraestructura (puertos, recursos, subdominio)
5. Para cada ítem: marca ☐ Cumple / ☐ No cumple / ☐ Condicional
6. Agrega observaciones en los ítems que corresponda
7. Emite dictamen: Apto / Condicional / No apto
8. El sistema valida que todos los ítems tengan respuesta
9. El sistema guarda la evaluación y cambia el estado:
   - Si Apto → `pendiente_institucional`
   - Si No apto → `rechazada`
10. El sistema envía notificación al solicitante

## Flujos alternativos

**7a. Dictamen condicional**
1. El admin marca "Condicional"
2. Escribe las condiciones en observaciones
3. La solicitud queda en `pendiente_tecnica` hasta que se cumplan

**7b. Dictamen no apto**
1. El sistema pide confirmación: "¿Rechazar esta solicitud? El solicitante recibirá una notificación con los motivos."
2. El admin confirma.

## Postcondición
- Evaluación técnica guardada
- Estado de la solicitud actualizado
- Notificación enviada al solicitante
- Auditoría registrada
