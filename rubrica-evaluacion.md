### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Rúbrica de Evaluación — Arquitectura y Diseño de Interfaces

## Objetivo

Esta rúbrica detalla los criterios que se utilizarán para evaluar los entregables de la materia. Su propósito es proporcionar una guía clara sobre las expectativas del trabajo y cómo se medirá el dominio de los conceptos de arquitectura de software, diseño de interfaces y trabajo colaborativo con agentes IA.

---

## Criterios de Evaluación

| Criterio | Ponderación | Excelente (9-10) | Bueno (7-8) | Suficiente (5-6) | Insuficiente (1-4) |
|:---------|:-----------:|:-----------------|:------------|:-----------------|:-------------------|
| **1. Diseño de Arquitectura y Justificación Técnica** | 30% | La arquitectura está claramente documentada con diagramas C4 (al menos Contexto y Contenedores). Las decisiones técnicas están justificadas con ADRs que explican el contexto, la decisión tomada y las consecuencias. Se aplica correctamente al menos un patrón arquitectónico (Hexagonal, Capas, MVC). | La arquitectura está documentada pero falta alguno de los niveles C4 o algún ADR tiene justificación débil. El patrón arquitectónico se menciona pero no se explica del todo por qué se eligió. | Hay documentación de arquitectura pero incompleta (sin diagramas o sin ADRs). Las decisiones técnicas no están justificadas o se justifican con argumentos vagos. | No hay documentación de arquitectura, o la existente es incomprensible. No se identifica ningún patrón arquitectónico. |
| **2. Diseño de Interfaces y Usabilidad** | 25% | Los wireframes o mockups cubren todos los flujos principales del sistema. Se aplican principios de usabilidad (consistencia, feedback, affordance). Se justifica el diseño de interfaz con criterios de experiencia de usuario (UX). La navegación es clara y predecible. | Los wireframes cubren la mayoría de los flujos pero falta alguno secundario. Se mencionan principios de usabilidad pero no se aplican de forma consistente. | Los wireframes son incompletos o confusos. No se evidencia aplicación de principios de usabilidad. La navegación no está clara. | No hay wireframes ni documentación de interfaz. |
| **3. Integración Tecnológica y Resolución Práctica** | 20% | El stack tecnológico está claramente definido y justificado para el problema (frontend, backend, base de datos). Se identifican servicios externos, APIs o integraciones necesarias. La arquitectura es factible de implementar con las herramientas elegidas. | El stack está definido pero la justificación es parcial. Faltan algunos detalles de integración. | El stack se menciona pero sin justificación. No se analizan integraciones necesarias. | No se define stack tecnológico o la elección es inviable para el proyecto. |
| **4. Documentación de Decisiones y Entregables** | 15% | Todos los archivos están en las carpetas correctas del andamiaje (00_REFERENCIAS a 08_CODIGO_FUENTE). Los ADRs están numerados y siguen el formato estándar. Los diagramas usan Mermaid y se renderizan correctamente en GitHub. El README del proyecto es claro y completo. | La mayoría de los archivos están en las carpetas correctas. Los ADRs existen pero alguno no sigue el formato. Los diagramas se renderizan pero con errores menores. | La estructura de carpetas es inconsistente. Faltan ADRs clave. Los diagramas no se renderizan o están en formato no compatible con GitHub. | No se sigue la estructura de carpetas del andamiaje. No hay ADRs. El README está vacío o es irrelevante. |
| **5. Trabajo Colaborativo y Uso de Agentes IA** | 10% | El historial de Git muestra trabajo incremental con ramas por agente y Conventional Commits. Los Pull Requests tienen descripciones claras y evidencian revisión del trabajo generado por los agentes IA. Se usan issues para seguimiento. El estudiante demuestra haber leído, entendido y validado el output de cada agente antes de avanzar. | Hay uso de ramas y PRs pero los mensajes de commit son genéricos. Se evidencia uso de agentes IA pero sin revisión crítica del output generado. | El trabajo se subió en pocos commits sin ramas. No hay PRs o los PRs no tienen descripción. El output de los agentes se aceptó sin revisión. | No hay uso de Git más allá del push inicial. No se evidencia trabajo con agentes IA o el trabajo es copia directa sin comprensión. |

---

## Sobre el uso de Agentes IA

El andamiaje de agentes IA es una **herramienta de aprendizaje, no un atajo**. Se evaluará positivamente:

- Que el estudiante **lea y entienda** el output de cada agente antes de avanzar.
- Que **cuestione, corrija o pida cambios** cuando el output del agente no sea correcto.
- Que use los agentes para **aprender el porqué** de cada decisión, no solo para generar archivos.
- Que documente en los ADRs sus **propias decisiones**, no solo las sugeridas por el agente.

Se considerará **negativamente**:

- Copiar y pegar outputs de agentes sin leerlos.
- Avanzar automáticamente sin revisar.
- No poder explicar en la defensa oral lo que "documentó" el agente.

---

## Proceso de Calificación

- La calificación final es la suma ponderada de los 5 criterios.
- Es **indispensable** que el repositorio sea público y el profesor tenga acceso.
- Las entregas se realizan por Pull Request desde ramas con nombre descriptivo (`feat/agente-01-analista`).
- La defensa oral puede modificar hasta un 20% de la nota (hacia arriba o hacia abajo) según la capacidad del estudiante de explicar y justificar sus decisiones.

---

## Escala de Calificación

| Nota | Descripción |
|:----:|-------------|
| 10 | Sobresaliente: todos los criterios en nivel Excelente. Defensa oral impecable. |
| 8-9 | Muy Bueno: mayoría de criterios en Excelente, alguno en Bueno. |
| 7 | Bueno: equilibrio entre Excelente y Bueno. |
| 5-6 | Suficiente: criterios mínimos cumplidos. Requiere mejorar para el proyecto integrador. |
| 1-4 | Insuficiente: no alcanza los criterios mínimos. Debe rehacer entregables. |
