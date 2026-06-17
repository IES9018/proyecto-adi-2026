# Ejercicio 04: Modelo de Dominio con DDD

## Objetivo

Aprender a modelar las entidades de un sistema usando Domain-Driven Design (DDD): identificar entidades, value objects, agregados y sus relaciones.

## Prompt (copiá y pegá en tu terminal de IA)

```text
Actuá como un Modelador de Dominio experto en DDD.

Voy a describirte un sistema, y quiero que me ayudes a modelar
sus entidades principales.

Mi proyecto es: [NOMBRE]
Descripción: [DESCRIPCIÓN DEL SISTEMA]

Usuarios: [USUARIOS]

Funcionalidades principales:
1. [FUNCIONALIDAD 1]
2. [FUNCIONALIDAD 2]
3. [FUNCIONALIDAD 3]

Antes de darme el modelo, haceme estas preguntas para
entender mejor el dominio:

1. ¿Qué información guarda cada usuario cuando usa el sistema?
2. ¿Hay datos que siempre viajan juntos? (ej: una dirección
   siempre con un usuario)
3. ¿Qué reglas de negocio hay? (ej: "un usuario no puede
   tener más de 3 pedidos activos")
4. ¿Cómo se relacionan las entidades entre sí?

Después de mis respuestas, generame:

1. Lista de entidades con sus atributos principales
2. Un diagrama Mermaid de entidad-relación
3. Identificación de Agregados (grupos de entidades que
   siempre se persisten juntas)
4. Reglas de negocio identificadas
```

## Lo que aprendés haciendo esto

- A pensar en **entidades del mundo real**, no en tablas de base de datos
- A identificar **reglas de negocio** antes de escribir código
- A usar **DDD** para modelar sistemas complejos
- A distinguir entre entidades (tienen identidad) y value objects (son intercambiables)

## Entrega

1. Carpeta `04_MODELO_DATOS/`
2. Archivo `04_MODELO_DATOS/modelo-dominio.md`
3. Commit: `git commit -m "feat: modelo de dominio con entidades y relaciones"`
4. Rama: `feat/ej-04-modelo-dominio`

## Criterios de aprobación

- [ ] Identificaste al menos 4 entidades
- [ ] Cada entidad tiene atributos con tipo de dato
- [ ] Las relaciones entre entidades están definidas
- [ ] Hay al menos 2 reglas de negocio documentadas
- [ ] Incluye un diagrama Mermaid que se renderiza en GitHub
