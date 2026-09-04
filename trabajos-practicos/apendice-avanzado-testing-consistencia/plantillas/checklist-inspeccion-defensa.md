# Checklist de Inspección Humana y Defensa — [Nombre del Proyecto]

> **Fecha:** [Fecha]
> **Estudiante:** [Nombre]

---

## Inspección humana de UI/UX

- [ ] Abrí la aplicación en el navegador
- [ ] Completé el happy path manualmente
- [ ] Verifiqué que los mensajes de error sean comprensibles
- [ ] Verifiqué que el usuario sepa qué hacer después de cada acción
- [ ] Revisé la jerarquía visual de botones principales vs secundarios
- [ ] Probé la navegación con teclado (Tab, Enter, Escape)
- [ ] Verifiqué que las operaciones largas muestran progreso
- [ ] Verifiqué que los datos persisten después de cerrar y reabrir
- [ ] Tomé [1-2] capturas con justificación
- [ ] Documenté hallazgos en `docs/testing/inspeccion-humana.md`

---

## Escaneo de secretos

- [ ] Instalé Gitleaks (o herramienta equivalente)
- [ ] Ejecuté escaneo del árbol actual
- [ ] Ejecuté escaneo del historial (opcional)
- [ ] Revisé los hallazgos
- [ ] Corregí secretos reales (si los hubo)
- [ ] Documenté resultados en `docs/testing/escaneo-secretos.md`
- [ ] Todos los valores están redactados en el reporte

---

## Defensa oral — Preguntas preparadas

### Sobre el módulo

- [ ] ¿Por qué un E2E no puede validar que se respete un ADR de arquitectura hexagonal?
- [ ] ¿Qué es un test oracle y por qué es indispensable?
- [ ] ¿Qué diferencia hay entre un fixture y un seed?
- [ ] ¿Por qué un test exitoso no significa que el sistema cumple el requisito?
- [ ] ¿Cuándo es legítimo usar `data-testid` como selector?

### Sobre la trazabilidad

- [ ] ¿Qué pasa si tu SPEC dice una cosa y tu código hace otra?
- [ ] ¿Cuál es el oráculo primario en un test de aceptación?
- [ ] ¿Cómo decidís qué flujo seleccionar como crítico?

### Sobre los datos sintéticos

- [ ] ¿Por qué no podés usar personas reales en tus tests?
- [ ] ¿Qué es la idempotencia y por qué importa en los fixtures?
- [ ] ¿Qué protección técnica debés implementar para evitar ejecutar tests contra producción?

### Sobre UI, UX y QA

- [ ] Definí UI, UX y QA con tus palabras. Dá un ejemplo de cada una.
- [ ] ¿Por qué la UX no puede automatizarse completamente?
- [ ] ¿Qué tipo de screenshot debés tomar y cuándo?

### Sobre IA y secretos

- [ ] ¿Qué preguntas le harías a la IA antes de aceptar un test que generó?
- [ ] ¿Por qué un secreto en un commit público debe considerarse comprometido aunque lo borres?
- [ ] ¿Cuál es el primer paso ante un secreto expuesto: borrar el commit o rotar la credencial?

---

## Autoevaluación

| Criterio | ¿Lo cumplí? | Evidencia |
|:---------|:-----------:|:----------|
| Matriz de trazabilidad completada | [ ] Sí / [ ] No | [Link o ruta] |
| 3 escenarios implementados | [ ] Sí / [ ] No | [Link o ruta] |
| Datos sintéticos documentados | [ ] Sí / [ ] No | [Link o ruta] |
| Suite ejecutada con reporte | [ ] Sí / [ ] No | [Link o ruta] |
| Inspección humana documentada | [ ] Sí / [ ] No | [Link o ruta] |
| Escaneo de secretos ejecutado | [ ] Sí / [ ] No | [Link o ruta] |
| Inconsistencias registradas | [ ] Sí / [ ] No / [ ] No hubo | [Link o ruta] |
| Postmortem (si hubo correcciones) | [ ] Sí / [ ] No aplica | [Link o ruta] |
| Preguntas de defensa preparadas | [ ] Sí / [ ] No | — |
