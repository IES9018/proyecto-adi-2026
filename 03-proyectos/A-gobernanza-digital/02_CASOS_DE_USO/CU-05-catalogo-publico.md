# CU-05: Consultar Catálogo Público

**Formato:** Cockburn | **Nivel:** Usuario | **Prioridad:** Media

---

## Actor principal
Cualquier persona (sin autenticación)

## Precondición
Ninguna

## Flujo principal

1. El usuario accede a `/catalogo`
2. El sistema muestra listado de servicios activos con:
   - Nombre del proyecto
   - Descripción breve
   - Responsable
   - Nivel (1/2/3)
   - Fecha de aprobación
   - Enlace al repositorio
3. El usuario puede filtrar por nivel (1, 2, 3)
4. El usuario puede buscar por nombre
5. Los resultados están paginados (20 por página)

## Flujos alternativos

**2a. Sin servicios activos**
1. El sistema muestra: "No hay servicios activos en este momento."

**3a. Servicio suspendido**
1. Se muestra en el listado con etiqueta "Suspendido"
2. Muestra la fecha de suspensión
3. No muestra el enlace al repositorio

## Postcondición
Ninguna (el catálogo es de solo lectura, no modifica datos)
