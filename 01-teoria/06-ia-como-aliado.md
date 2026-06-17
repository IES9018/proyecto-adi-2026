### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# La IA como Aliado de Aprendizaje

## El Problema de Fondo

La mayoría de los estudiantes usa la IA de dos formas extremas:

**❌ No la usan.** Creen que es "trampa" o que "no van a aprender". Se pierden una herramienta que, bien usada, acelera el aprendizaje 10x.

**❌ La usan mal.** Le piden a ChatGPT "hacéme el TP de arquitectura" y copian todo sin entender nada. Aprenden cero y después no pueden defender nada en el oral.

Este curso te enseña **el camino del medio**.

---

## La Analogía de la Calculadora Científica

Cuando tus padres iban a la escuela, las cuentas se hacían a mano. Cuando vos fuiste a la primaria, ya existían las calculadoras simples. Hoy cualquier celular resuelve ecuaciones complejas.

**¿Para qué estudiar matemática si la calculadora lo hace?**

Porque la calculadora **no entiende el problema**. Vos tenés que saber qué operación hacer, en qué orden, y si el resultado tiene sentido. La herramienta ejecuta. Vos pensás.

Con la IA pasa lo mismo:

| La IA hace... | Pero vos tenés que... |
|:--------------|:----------------------|
| Generar código | Saber si ese código es correcto y seguro |
| Escribir un ADR | Entender y justificar cada decisión |
| Dibujar un diagrama | Validar que refleje el negocio real |
| Modelar una base de datos | Conocer el dominio lo suficiente para corregirla |
| Sugerir un patrón | Decidir si aplica o no a tu problema |

> **La IA no te reemplaza. Te potencia. Pero solo si sabés lo suficiente para revisar lo que produce.**

---

## Cómo Usar la IA 24/7 como Tutor Personal

Una de las mayores ventajas de la IA es que **está disponible siempre**. No tiene horario de consulta. No se cansa. No juzga.

### Como tutor de teoría

```text
Prompt:
"Actuá como un tutor de Arquitectura de Software.
Explicame qué es la Arquitectura Hexagonal como si
tuviera 15 años. Usá una analogía simple. Después
preguntame si lo entendí."
```

### Como corrector de trabajos

```text
Prompt:
"Acá está mi ADR-002 sobre elección de base de datos.
Revisalo y decime si cumple con el estándar de ADR
(contexto, decisión, opciones, consecuencias).
Si falta algo, decime qué."
```

### Como generador de ejemplos

```text
Prompt:
"Dame 3 ejemplos de sistemas reales que usen
Arquitectura Hexagonal. Para cada uno decime por
qué funciona bien en ese caso."
```

### Como preparador de exámenes

```text
Prompt:
"Simulá ser mi profesor de Arquitectura.
Haceme 5 preguntas de opción múltiple sobre patrones
de diseño. Después de responder, decime si acerté
y por qué."
```

### Como compañero de estudio

```text
Prompt:
"Vamos a estudiar C4 Model juntos. Primero explicame
los 4 niveles. Después de cada nivel, preguntame si
queda claro antes de seguir al siguiente."
```

---

## El Andamiaje de Agentes: El Método Estructurado

Los prompts sueltos están bien para estudiar. Pero cuando **construís un sistema**, necesitás algo más ordenado.

Para eso creamos el **[Andamiaje de Agentes IA](./02-andamiaje-agentes/README.md)**:

```
No es:
    Un solo prompt mágico que genera todo el proyecto.

Es:
    Un equipo de 8 agentes especializados que trabajan
    en orden, cada uno con su rol, revisando el trabajo
    del anterior, bajo tu supervisión.
```

| Agente | Rol | Lo lee el estudiante | Lo entiende |
|:-------|:----|:--------------------:|:-----------:|
| 0 DevOps | Crea repo, .gitignore, ramas | ✅ | ✅ |
| 1 Analista | Documenta requisitos y stakeholders | ✅ | ✅ |
| 2 Arquitecto | Crea ADRs, diagramas C4 | ✅ | ✅ |
| 3 Modelador | Modela entidades y DB | ✅ | ✅ |
| 4 Especificador | Escribe casos de uso | ✅ | ✅ |
| 5 Diseñador UI | Crea wireframes | ✅ | ✅ |
| 6 Tech Lead | Define stack y convenciones | ✅ | ✅ |
| 7 Desarrollador | Escribe código | ✅ | ✅ |

---

## Reglas para el Estudiante

### ✅ Está permitido

- Pedirle al agente que te explique su output
- Cuestionar una decisión y pedir alternativas
- Usar la IA para generar ejemplos de conceptos que no entendés
- Pedirle al agente que genere el ADR y después modificarlo con tus propias palabras
- Usar la IA para practicar para la defensa oral

### ❌ No está permitido

- Copiar el output del agente sin leerlo
- Avanzar de agente sin revisar lo que el anterior generó
- Hacer que el agente haga todo y después no saber explicar nada
- Usar la IA durante el examen final (salvo que se indique lo contrario)

---

## ¿Qué Gana el Estudiante que Usa Bien la IA?

| Estudiante | Sin IA | Con IA mal usada | Con IA bien usada |
|:-----------|:-------|:-----------------|:------------------|
| Velocidad de aprendizaje | Lento, solo en clase | Cree que aprende rápido | Acelerado, aprende más en menos tiempo |
| Comprensión profunda | Depende del estudiante | Superficial (copia y pega) | Profunda (revisa, cuestiona, mejora) |
| Nota en el oral | Bien si entendió | Mal (no sabe explicar) | Muy bien (argumenta con propiedad) |
| Preparación profesional | Aprendió a hacer solo | No aprendió nada | Aprendió a trabajar con herramientas modernas |

---

## Para Recordar

> La IA no te va a robar tu trabajo. La persona que sepa usar IA mejor que vos, sí.
> Usar IA no es trampa. Es usar la herramienta correcta para el trabajo correcto.
> No le pidas al agente que "te haga el proyecto". Pedile que **te ayude a construir** el proyecto.

**Referencia complementaria:** Leé la guía del andamiaje en [`02-andamiaje-agentes/`](./02-andamiaje-agentes/README.md) y practicá con los ejercicios en [`05-ejercicios/`](../05-ejercicios/README.md).
