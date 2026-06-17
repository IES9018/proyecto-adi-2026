### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# ¿Qué es Arquitectura de Software?

## La Analogía del Edificio

Antes de poner un ladrillo, un arquitecto de edificios dibuja **planos**. Define dónde va cada caño de agua, cada cable de luz, dónde están las columnas que sostienen el peso, por dónde entra la luz natural.

En software es **exactamente igual**: antes de escribir `if` y `for`, definís dónde vive la lógica de negocio, cómo se comunican los módulos, qué base de datos usás, cómo se autentican los usuarios.

> Si ponés ladrillos sin plano, el edificio se cae.
> Si escribís código sin arquitectura, el sistema colapsa o es imposible de mantener.

Una clase de Arquitectura de Software no te enseña a programar mejor. Te enseña a **pensar antes de programar**.

---

## ¿Qué es entonces?

Es la **estructura fundamental** de un sistema de software:

- **Las piezas**: módulos, capas, componentes, servicios
- **Las relaciones**: cómo se comunican entre sí (API, eventos, llamadas directas)
- **Las reglas**: qué puede hacer cada pieza, qué no, qué permisos tiene
- **Los principios**: buenas prácticas que guían todas las decisiones

### Ejemplo concreto

Un sistema de biblioteca puede tener:

```
[Interfaz Web] ←→ [API REST] ←→ [Lógica de Préstamos] ←→ [Base de Datos]
                                 ↓
                          [Servicio de Email] ← [Notificaciones]
```

La arquitectura **define que**:
- La interfaz web **nunca** accede directo a la base de datos
- La lógica de préstamos vive en su propia capa, separada de notificaciones
- Si cambiás de base de datos, el resto del sistema no se entera

---

## ¿Por qué importa?

| Sin arquitectura | Con arquitectura |
|:-----------------|:-----------------|
| Agregar una funcionalidad rompe otra | Cada pieza sabe su lugar |
| El nuevo desarrollador no entiende el código | Leés la documentación de arquitectura y entendés el mapa |
| Cambiar de base de datos es imposible | Cambiás el adaptador y listo |
| El sistema es frágil y lento | Podés escalar partes por separado |
| No sabés por qué tomaste cada decisión | Tenés ADRs que lo explican |

---

## ¿Qué NO es arquitectura?

- **No es elegir el framework más famoso.** La arquitectura es cómo organizás el código, no qué librería usás. React o Vue son herramientas, no arquitectura.
- **No es "hacer diagramas bonitos".** Los diagramas documentan la arquitectura, pero la arquitectura es lo que el código hace, no lo que el dibujo muestra.
- **No es para proyectos gigantes.** Un proyecto chico bien arquitecturado es más fácil de mantener que uno chico mal hecho. La arquitectura es para todos los proyectos.

---

## El Rol del Arquitecto en el Andamiaje

En nuestro método de trabajo, el **Agente Arquitecto** del andamiaje de IA:

- **No escribe código** (solo lectura)
- **Habla en tu lenguaje**, no en jerga técnica
- Te guía con **preguntas estructuradas** para definir las decisiones clave
- **Documenta** cada decisión en un ADR

Vos sos el **Arquitecto en Jefe**. El agente es tu asistente que te ayuda a pensar con orden.

---

## Para Recordar

> Arquitectura de software = las decisiones importantes sobre la estructura de tu sistema.
> Las decisiones equivocadas se pagan caro. Las decisiones bien documentadas se pagan una sola vez.

**Próximo paso:** Leé `02-patrones-diseno.md` para conocer las soluciones probadas que podés aplicar.
