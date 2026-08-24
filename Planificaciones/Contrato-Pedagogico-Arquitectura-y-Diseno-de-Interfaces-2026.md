# Contrato Pedagógico - Arquitectura y Diseño de Interfaces 2026

**CARRERA:** TECNICATURA SUPERIOR EN DESARROLLO DE SOFTWARE  
**ESPACIO CURRICULAR:** ARQUITECTURA Y DISEÑO DE INTERFACES  
**PROFESOR:** Paulo Alvarez  
**CURSO:** 3° AÑO - Comisión 1  
**AÑO LECTIVO:** 2026  
**FORMATO:** MATERIA  
**RÉGIMEN:** ANUAL  
**CARGA HORARIA:** 4 horas cátedra semanales  
**TOTAL ANUAL:** 120 horas cátedra

---

## 1. PRESENTACIÓN DEL ESPACIO CURRICULAR

### ¿Qué es Arquitectura y Diseño de Interfaces?

Es el espacio curricular donde se define cómo se estructura técnicamente una solución de software y cómo se presenta de forma usable para las personas usuarias. Retoma lo trabajado en Modelado de Software y lo proyecta hacia decisiones concretas de arquitectura, selección tecnológica e interfaces.

### ¿Por qué es importante?

Porque permite transformar modelos conceptuales en decisiones implementables:

- Seleccionar patrones y estilos arquitectónicos según el problema.
- Diseñar experiencias de uso claras, accesibles y consistentes.
- Justificar decisiones técnicas con criterios de calidad.
- Preparar la base del proyecto que se ejecutará en PP III.

### Formato de trabajo

- Clases con integración teórico-práctica.
- Actividades aplicadas sobre casos y proyecto de cohorte.
- Entregas iterativas con evidencia en repositorios.
- Retroalimentación continua y mejora progresiva.

---

## 2. OBJETIVOS DEL ESPACIO

Al finalizar este espacio, el estudiante será capaz de:

1. Analizar alternativas de arquitectura de software según contexto.
2. Aplicar patrones de diseño y criterios de modularidad.
3. Diseñar interfaces centradas en la experiencia de usuario.
4. Seleccionar tecnologías web y mobile acordes a requerimientos.
5. Integrar componentes y servicios en propuestas viables.
6. Documentar decisiones de arquitectura e interfaz de forma técnica.
7. Comunicar y defender decisiones para la ejecución en PP III.

---

## 3. CONTENIDOS Y ORGANIZACIÓN

### Unidades de trabajo

| Unidad | Eje | Duración estimada |
|--------|-----|-------------------|
| 1 | Procesos y metodologías | Marzo |
| 2 | Arquitectura de software | Abril - Mayo |
| 3 | Diseño de interfaces (HCI) | Junio |
| 4 | Arquitectura web | Agosto |
| 5 | Arquitectura mobile | Septiembre |
| 6 | Herramientas e integración | Octubre - Noviembre |

### Articulación curricular

- Continuidad de Modelado de Software: de la representación a la decisión técnica.
- Vinculación directa con PP III: insumo para la implementación del proyecto integrador.
- Los diseños producidos deben considerar que el proyecto se desplegará bajo la [Política de Gobernanza de Servicios Digitales](https://github.com/IES9018/gobernanza-servicios-digitales) del IES 9-018, que exige repositorio público y licencia open source compatible con uso educativo.

---

## 4. METODOLOGÍA DE TRABAJO

### Enfoque

- Resolución de problemas y estudio de casos.
- Producción incremental de decisiones de arquitectura e interfaz.
- Trabajo colaborativo con revisión técnica.

### Flujo de trabajo utilizado en la cohorte

- Repositorio de materia y repositorios de estudiantes en GitHub.
- Trabajo por ramas con entregas por Pull Request.
- Seguimiento de tareas y consultas por issues.
- Registro de decisiones en documentación técnica.

---

## 5. EVALUACIÓN

### Criterios de evaluación

| Área | Porcentaje |
|------|------------|
| Diseño de arquitectura y justificación técnica | 30% |
| Diseño de interfaces y usabilidad | 25% |
| Integración tecnológica y resolución práctica | 20% |
| Documentación de decisiones y entregables | 15% |
| Participación, seguimiento y trabajo colaborativo | 10% |

### Regularidad

- Asistencia mínima del 75%.
- Entregas parciales aprobadas según cronograma.
- Participación activa en actividades de análisis, diseño y revisión.

### Acreditación

- Cumplimiento de entregables integradores de arquitectura e interfaz.
- Instancia final de presentación y argumentación técnica aprobada.

---

## 6. DERECHOS Y RESPONSABILIDADES

### Derechos del estudiante

- Acceder a consignas y criterios de evaluación claros.
- Recibir acompañamiento docente y feedback oportuno.
- Ser evaluado con criterios públicos y consistentes.

### Responsabilidades del estudiante

- Cumplir entregas en tiempo y forma.
- Sostener trazabilidad de su trabajo técnico.
- Participar de manera colaborativa y respetuosa.
- Evitar plagio y uso no ético de herramientas.

### Compromisos del docente

- Garantizar coherencia entre objetivos, actividades y evaluación.
- Acompañar la construcción de decisiones técnicas fundamentadas.
- Promover un entorno de aprendizaje profesional y colaborativo.

---

## 7. ACUERDO PEDAGÓGICO

La firma de este contrato implica el acuerdo de estudiantes y docente sobre objetivos, metodología, evaluación y responsabilidades para el ciclo lectivo 2026 en Arquitectura y Diseño de Interfaces.

---

## ANEXO I - Metodología SDD y Arnés de IA (OpenCode)

Vigente ciclo lectivo 2026. Complementa las secciones de metodología de este documento.

1. **Spec-Driven Development (SDD):** toda funcionalidad se especifica primero en `SPEC.md` (plantilla institucional) y sus decisiones técnicas relevantes se registran en `docs/adr/` utilizando la plantilla ADR de la cátedra.
2. **Arnés de IA obligatorio:** cada repositorio incluye `.opencoderules` y opcionalmente `INSTRUCTIONS.md` en su raíz, que limitan el comportamiento del agente local **OpenCode** (alcance, estilo y estándares técnicos).
3. **Supervisión crítica:** todo código asistido por IA se revisa línea por línea por el estudiante antes del commit; la revisión queda evidenciada en Pull Requests con la plantilla institucional.
4. **Sin forks:** los proyectos se crean directamente dentro de la organización `IES9018` con nomenclatura `<nombre_alumno>-<nombre_proyecto>`.
5. **Auditoría docente (Capataz/Arquitecto de Obra):** se evalúan como evidencia primaria la SPEC, los ADRs, el arnés configurado y los Pull Requests.
6. Las herramientas internas de administración del docente quedan fuera del alcance del estudiante.