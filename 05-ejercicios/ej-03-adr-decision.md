# Ejercicio 03: Escribir un ADR (Architecture Decision Record)

## Objetivo

Aprender a documentar decisiones arquitectónicas usando el formato estándar ADR. Esta es una de las habilidades más valoradas en la industria.

## ¿Qué es un ADR?

Un documento corto (1 página) que responde:

- **Contexto**: ¿qué problema necesitamos resolver?
- **Decisión**: ¿qué elegimos?
- **Opciones**: ¿qué otras alternativas consideramos?
- **Consecuencias**: ¿qué implica esta decisión?

## Prompt (copiá y pegá en tu terminal de IA)

```text
Actuá como un Arquitecto de Software. Necesito escribir un
ADR (Architecture Decision Record) para documentar una
decisión técnica de mi proyecto.

Mi proyecto es: [NOMBRE]
Tengo que decidir entre: [OPCIÓN A o OPCIÓN B, EJ: SQLite vs PostgreSQL]

Dame más contexto sobre mi proyecto para ayudarme a decidir.
Haceme preguntas como:

1. ¿Cuántos usuarios va a tener el sistema?
2. ¿Necesita concurrencia (varios usuarios escribiendo a la vez)?
3. ¿Los datos son relacionales o documentos?
4. ¿Quién va a administrar la base de datos?
5. ¿Es para desarrollo local o producción?

Después de mis respuestas, generá un ADR completo en markdown
siguiendo este formato:

# ADR-001: [Título]

## Contexto
[Descripción del problema y las circunstancias]

## Decisión
[Qué elegimos y por qué]

## Opciones consideradas
- [Opción A]: [ventajas y desventajas]
- [Opción B]: [ventajas y desventajas]

## Consecuencias
- Positivas:
- Negativas:
- Riesgos:
```

## Lo que aprendés haciendo esto

- A **justificar** cada decisión técnica con argumentos, no con "porque sí"
- A **comparar alternativas** antes de elegir
- A escribir documentación que otros desarrolladores puedan leer y entender
- A usar el formato **ADR** que se usa en empresas como Amazon, Netflix y Spotify

## Entrega

1. Carpeta `03_ARQUITECTURA/adr/`
2. Archivo `03_ARQUITECTURA/adr/ADR-001-nombre-decision.md`
3. Commit: `git commit -m "docs: ADR-001 - [decisión tomada]"`
4. Rama: `feat/ej-03-adr`

## Criterios de aprobación

- [ ] El ADR tiene las 4 secciones obligatorias (Contexto, Decisión, Opciones, Consecuencias)
- [ ] Se consideraron al menos 2 opciones antes de elegir
- [ ] Las consecuencias incluyen riesgos identificados
- [ ] El archivo se llama `ADR-001-algo.md` con el número al inicio
- [ ] Se entiende la decisión sin necesidad de más contexto

## Referencia

Formato completo de ADR: [adr.github.io](https://adr.github.io)
Ejemplos reales en el repositorio de la materia.
