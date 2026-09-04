# ADR-008: Estrategia de Testing Automatizado (Unitario, Integración y E2E)

- **Estado**: Aceptado
- **Fecha**: 2026-09-04
- **Decisores**: Equipo de desarrollo IES 9-018
- **Referencias**: ADR-002 (Arquitectura Hexagonal), ADR-005 (Despliegue Docker)

## Contexto
El sistema de gobernanza digital requiere garantizar la calidad del código y el funcionamiento de los flujos críticos (autenticación, creación de solicitudes, panel de administración) antes de cada despliegue. El entorno de ejecución es un servidor Debian 12 sin interfaz gráfica (headless), lo que impone restricciones sobre cómo se pueden ejecutar las pruebas de interfaz de usuario.

## Decisión
Se establece la siguiente estrategia de testing en capas:

1. **Backend (Unitario e Integración)**: 
   - Uso de `pytest` para validar la lógica de dominio y los endpoints de la API.
   - **Excepción controlada**: El middleware de rate limiting (SlowAPI) se deshabilita explícitamente cuando `ENVIRONMENT="testing"`. Esto evita falsos positivos (HTTP 429) cuando las pruebas ejecutan múltiples solicitudes de login en milisegundos.

2. **Frontend (E2E)**: 
   - Uso de `Playwright` configurado en modo **headless** (sin ventana visible). Esto permite simular la interacción real del usuario (clics, navegación, envío de formularios) directamente en el servidor Debian 12 sin requerir un entorno de escritorio.

3. **Aislamiento del Entorno**: 
   - Las pruebas se ejecutan en contenedores Docker aislados (`docker-compose.test.yml`), utilizando una base de datos de pruebas independiente para no contaminar datos de desarrollo o producción.

## Consecuencias
- **Positivas**: 
  - Cobertura confiable y detección temprana de regresiones.
  - Ejecución rápida y reproducible, lista para integrarse en un pipeline de CI/CD (GitHub Actions).
  - Validación real de la experiencia de usuario sin depender de entornos gráficos.
- **Negativas**: 
  - Los tests E2E son frágiles ante cambios mayores en la estructura del DOM (ej. cambiar un `<h1>` por un `<h2>` requiere actualizar el selector en el test). Se mitiga usando selectores por `data-testid` cuando sea posible.

## Notas de Implementación
- Para ejecutar tests backend: `pytest tests/ -v`
- Para ejecutar tests E2E: `npx playwright test` (desde el directorio frontend)
