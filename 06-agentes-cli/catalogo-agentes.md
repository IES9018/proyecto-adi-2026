# Catálogo de Agentes — Proyecto de Referencia

> Estos son los agentes que el profesor usa en el proyecto DobleA NexGen y en el proyecto Gobernanza Digital.
> Podés copiarlos a tu proyecto y adaptarlos.
>
> **Fuente original:** `C:\Users\v8_pa\Documents\GitHub\DobleA_NexGen\.opencode\agents\`

---

## Resumen de agentes

| Agente | Edit | Bash | Propósito |
|--------|------|------|-----------|
| `@arquitecto` | deny | deny | Auditar arquitectura, detectar huecos e inconsistencias |
| `@backend` | allow | deny | Implementar lógica de negocio |
| `@committer` | allow | allow | Pipeline de calidad + git commit |
| `@debugger` | deny | allow | Diagnosticar bugs hasta archivo:línea |
| `@docente` | deny | deny | Explicar conceptos con analogías para estudiantes |
| `@documentation` | allow | deny | Mantener documentación, ADRs y estado del proyecto |
| `@infrastructure` | allow | deny | Implementar adaptadores de infraestructura |
| `@review` | deny | allow | Ejecutar linters + tests, aprobar o rechazar |
| `@security` | deny | deny | Auditar vulnerabilidades OWASP Top 10 |
| `@testing` | allow | deny | Escribir tests unitarios, integración y E2E |
| `@ui-tester` | deny | allow | Navegar la app, detectar errores de UI |

---

## @arquitecto

**Permisos:** edit: deny, bash: deny

**Rol:** Arquitecto que audita el proyecto. Detecta huecos, inconsistencias, riesgos y zonas de improvisación antes de implementar.

**Lo que hace:**
- Revisa la arquitectura del proyecto
- Detecta si falta documentación o hay contradicciones
- Sugiere mejoras estructurales
- No programa ni ejecuta comandos

**Cuándo usarlo:** Antes de empezar a codificar, o cuando sientas que el proyecto "se está desordenando".

---

## @backend

**Permisos:** edit: allow, bash: deny

**Rol:** Implementa la lógica de negocio respetando la arquitectura definida.

**Lo que hace:**
- Escribe código en las capas de dominio y aplicación
- Crea servicios, casos de uso y entidades
- No toca infraestructura, base de datos ni frontend

**Cuándo usarlo:** Cuando ya tenés la arquitectura definida y necesitás implementar funcionalidades.

---

## @committer

**Permisos:** edit: allow, bash: allow

**Rol:** Agente de cierre de sesión. Ejecuta el pipeline de calidad y si pasa, hace el commit.

**Lo que hace:**
- Ejecuta linters y tests
- Verifica que no haya errores
- Construye un mensaje de commit en formato convencional
- Hace el commit si todo está bien

**Cuándo usarlo:** Al final de cada sesión de trabajo, antes de cerrar la terminal.

---

## @debugger

**Permisos:** edit: deny, bash: allow

**Rol:** Diagnostica bugs hasta encontrar el archivo y la línea exacta.

**Lo que hace:**
- Recibe un reporte de error
- Reproduce el bug en el código
- Identifica archivo y línea exactos
- Clasifica el bug y genera un brief para el agente que lo va a resolver

**Cuándo usarlo:** Cuando un test falla o la app tiene un comportamiento inesperado.

---

## @docente

**Permisos:** edit: deny, bash: deny

**Rol:** Explica conceptos de arquitectura, diseño e ingeniería de software usando analogías. Adaptado para estudiantes de tecnicatura.

**Lo que hace:**
- Explica conceptos técnicos con analogías de la vida cotidiana
- Busca ejemplos en tu repositorio
- Conecta con materias previas (Modelado, BD, Programación)
- Usa lenguaje coloquial argentino, sin jerga excesiva

**Cuándo usarlo:** Cuando no entendés un concepto, cuando querés repasar para el oral, o cuando necesitás una explicación clara.

> 📖 Ver el archivo completo del agente en [`agentes/docente.md`](./agentes/docente.md)

---

## @documentation

**Permisos:** edit: allow, bash: deny

**Rol:** Mantiene y estandariza toda la documentación del proyecto.

**Lo que hace:**
- Mantiene ADRs, documentación técnica y estado del proyecto
- Verifica que no haya información contradictoria entre documentos
- Revisa que los enlaces sean válidos
- No modifica código fuente ni tests

**Cuándo usarlo:** Cuando necesitás actualizar la documentación, agregar un ADR nuevo, o revisar que todo esté consistente.

---

## @infrastructure

**Permisos:** edit: allow, bash: deny

**Rol:** Implementa adaptadores de infraestructura (bases de datos, APIs externas, servicios).

**Lo que hace:**
- Implementa conexiones a bases de datos
- Crea adaptadores para servicios externos (email, archivos, etc.)
- Maneja graceful degradation cuando algo no está disponible
- No toca lógica de negocio

**Cuándo usarlo:** Cuando necesitás conectar tu aplicación a una base de datos, un servicio de email, o cualquier sistema externo.

---

## @review

**Permisos:** edit: deny, bash: allow

**Rol:** Revisa los cambios propuestos antes del commit.

**Lo que hace:**
- Ejecuta linters y tests
- Revisa el diff en busca de problemas
- Busca secretos, `print()`, código comentado
- Aprueba o rechaza con un checklist detallado
- No modifica ningún archivo

**Cuándo usarlo:** Antes de cada commit importante, o cuando querés asegurarte de que tu código cumple con los estándares.

---

## @security

**Permisos:** edit: deny, bash: deny

**Rol:** Audita el código en busca de vulnerabilidades de seguridad.

**Lo que hace:**
- Revisa vulnerabilidades OWASP Top 10
- Verifica configuración de CORS, JWT, validación de inputs
- Revisa rate limiting, path traversal, sanitización
- Emite reportes clasificados por severidad (CRITICAL/HIGH/MEDIUM/LOW)
- Solo reporta, no modifica código

**Cuándo usarlo:** Antes de poner el proyecto en producción, o cuando trabajás con datos sensibles.

---

## @testing

**Permisos:** edit: allow, bash: deny

**Rol:** Escribe tests unitarios, de integración, contract y E2E.

**Lo que hace:**
- Escribe tests siguiendo la pirámide de testing
- Mantiene cobertura ≥80%
- Crea fixtures y factories reutilizables
- Asegura que los tests sean deterministas

**Cuándo usarlo:** Después de implementar una funcionalidad, o cuando querés mejorar la cobertura de tests.

---

## @ui-tester

**Permisos:** edit: deny, bash: allow

**Rol:** Navega la aplicación web como si fuera un usuario real, detectando errores.

**Lo que hace:**
- Simula un usuario navegando la app con Playwright
- Detecta errores de consola JavaScript
- Encuentra links rotos y problemas de navegación
- Reporta issues de autenticación y sesión

**Cuándo usarlo:** Cuando hay bugs de interfaz que los tests unitarios no detectan, o antes de un deploy.
