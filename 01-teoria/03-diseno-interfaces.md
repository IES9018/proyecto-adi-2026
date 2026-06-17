### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Diseño de Interfaces (HCI y UX)

## La Diferencia entre UX y UI

La gente suele confundirlos. Son dos caras de la misma moneda.

```
UX = User Experience  →  Cómo SE SIENTE usar el sistema
UI = User Interface   →  Cómo SE VE el sistema
```

| Pregunta | UX | UI |
|:---------|:---|:---|
| ¿El usuario encuentra lo que busca? | ✅ | |
| ¿Los botones son del color correcto? | | ✅ |
| ¿El usuario se siente frustrado? | ✅ | |
| ¿La tipografía es legible? | | ✅ |
| ¿El flujo de 3 pasos se puede hacer en 1? | ✅ | |
| ¿El logo está centrado? | | ✅ |

**Analogía:** UX es el motor, la dirección y la suspensión de un auto. UI es el color de la pintura, el tapizado y las luces LED. Si el motor anda mal, no importa qué lindo sea el color.

---

## HCI (Human-Computer Interaction)

Estudia cómo las personas interactúan con las computadoras. No es solo "hacer pantallas lindas", es **entender cómo piensa y se comporta un usuario**.

### Principios básicos de HCI

| Principio | Explicación |
|:-----------|:-----------|
| **Consistencia** | Botones similares hacen cosas similares en todo el sistema. El usuario no tiene que reaprender cada pantalla. |
| **Feedback** | Cuando el usuario hace clic, algo debe pasar (un color cambia, un mensaje aparece, una animación). Si no pasa nada, el usuario cree que no funcionó. |
| **Affordance** | Un botón debe verse como botón (sombra, relieve, color distinto). Si parece una etiqueta plana, el usuario no va a saber que puede hacer clic. |
| **Visibilidad** | Las acciones importantes deben verse. Si "Guardar" está escondido en un menú de 3 puntos, nadie va a guardar. |
| **Tolerancia al error** | Si el usuario se equivoca, que pueda deshacer. "¿Estás seguro?" es mejor que borrar sin preguntar. |

---

## Wireframes, Mockups y Prototipos

Tres niveles de fidelidad en el diseño de interfaces:

| Tipo | Fidelidad | Tiempo | Sirve para... |
|:-----|:---------:|:------:|:--------------|
| **Wireframe** | Baja | 5 min | Definir estructura, sin colores ni estilos |
| **Mockup** | Alta | 1-2 hs | Mostrar el diseño final, colores, tipografía |
| **Prototipo** | Interactiva | 4-8 hs | Simular el funcionamiento, probar flujos |

### Wireframe

Es un esquema en blanco y negro, como un plano de arquitectura. Sin colores, sin imágenes reales, solo rectángulos que representan contenido.

```
+--------------------------------------------------+
| [LOGO]           [Inicio]  [Productos] [Contacto] |
+--------------------------------------------------+
|                                                    |
|   +------------------+  +------------------+       |
|   |  Imagen          |  |  Texto           |       |
|   |  principal       |  |  de bienvenida   |       |
|   |  (rectángulo)    |  |  (líneas)        |       |
|   +------------------+  +------------------+       |
|                                                    |
|   [Botón: Ver más]        [Botón: Contactar]      |
+--------------------------------------------------+
|  Footer: links, redes, copyright                   |
+--------------------------------------------------+
```

**Analogía:** Es el plano de la casa a lápiz. Marcás dónde va la cocina, el baño, los dormitorios. No definís color de paredes ni muebles.

### Mockup

Ya tiene colores, imágenes reales, tipografía definida. Es "cómo se ve" el producto final, pero todavía no funciona.

### Prototipo

Es un mockup que funciona: hacés clic en un botón y la pantalla cambia. Se usa para probar con usuarios antes de programar.

---

## Diseño Responsive

Una misma página que se adapta a cualquier pantalla (celular, tablet, computadora).

**Sin responsive:** el celular muestra la página de la compu en miniatura, ilegible.
**Con responsive:** los elementos se reacomodan, el menú se vuelve hamburguesa, las imágenes se achican.

**Analogía:** Es como agua que toma la forma del recipiente. El mismo contenido se adapta a una botella, un vaso o un plato.

---

## Accesibilidad

Diseñar para que **todas las personas** puedan usar el sistema, incluyendo personas con discapacidades.

| Práctica | ¿Por qué? |
|:---------|:----------|
| Contraste suficiente | Personas con baja visión puedan leer |
| Texto alternativo en imágenes | Lectores de pantalla para personas ciegas |
| Navegación por teclado | Personas que no pueden usar mouse |
| Tamaño de fuente ajustable | Usuarios con vista cansada |
| No solo color para indicar estado | Personas daltónicas (no usen rojo/verde como único indicador) |

---

## El Agente Arquitecto como Aliado

En nuestro andamiaje, el **Agente 5 (Diseñador de UI/UX)** puede:

- Generar wireframes en Mermaid a partir de una descripción
- Sugerir flujos de navegación alternativos
- Evaluar la interfaz contra principios de usabilidad
- Proponer mejoras de accesibilidad

Pero **vos** decidís el diseño final. El agente propone, vos disponés.

---

## Para Recordar

> La mejor interfaz es la que el usuario no nota.
> Si tenés que explicarle a un usuario cómo usar tu sistema, ya perdiste.
> Probá con un compañero antes de programar. 5 minutos de prueba ahorran 5 horas de corrección.

**Referencia recomendada:** Steve Krug — *No me hagas pensar* (el libro más famoso de usabilidad, corto y práctico).
