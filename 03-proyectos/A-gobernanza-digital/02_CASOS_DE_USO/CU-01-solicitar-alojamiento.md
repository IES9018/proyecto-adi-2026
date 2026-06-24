# CU-01: Solicitar Alojamiento

**Formato:** Cockburn | **Nivel:** Usuario | **Prioridad:** Alta

---

## Actor principal
Solicitante (estudiante o docente autenticado)

## Precondición
- Usuario autenticado con rol `solicitante`
- No tiene otra solicitud pendiente para el mismo subdominio

## Flujo principal

1. El solicitante selecciona "Nueva Solicitud"
2. El sistema muestra el formulario con los campos del [Doc 01](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/01_SOLICITUD_ALOJAMIENTO.md)
3. El solicitante completa: nombre del proyecto, nivel, subdominio, descripción, objetivo educativo, arquitectura, URL repositorio, licencia, tecnologías
4. El solicitante completa la justificación de arquitectura (obligatorio si es alumno)
5. El solicitante completa la declaración de riesgos
6. Opcional: guarda como borrador
7. El solicitante presiona "Enviar Solicitud"
8. El sistema valida los campos obligatorios
9. El sistema crea la solicitud con estado `pendiente_tecnica`
10. El sistema registra el evento en la tabla de auditoría
11. El sistema envía email de confirmación al solicitante

## Flujos alternativos

**6a. Guardar borrador**
1. El solicitante presiona "Guardar borrador"
2. El sistema guarda con estado `borrador`
3. El solicitante puede retomar después

**8a. Validación fallida**
1. El sistema muestra los campos con error resaltados
2. El solicitante corrige y reintenta

## Flujos de excepción

**3a. Subdominio duplicado**
1. El sistema verifica que el subdominio no esté en uso
2. Si está en uso, muestra mensaje: "Este subdominio ya está asignado"
3. Sugiere alternativas

**9a. Error de sistema**
1. Si falla el guardado, muestra "Error al crear la solicitud. Intente nuevamente."
2. No pierde los datos del formulario

## Postcondición
- Solicitud creada con estado `pendiente_tecnica`
- Email enviado al solicitante
- Auditoría registrada
