# Ejercicio 05: Wireframe de Interfaz

## Objetivo

Aprender a diseñar la interfaz de usuario de una pantalla usando wireframes en texto y Mermaid. No necesitas herramientas de diseño gráfico.

## ¿Qué es un wireframe?

Un esquema de baja fidelidad que muestra **dónde va cada cosa** en la pantalla. Sin colores, sin imágenes reales, solo rectángulos y texto que indican la estructura.

## Prompt (copiá y pegá en tu terminal de IA)

```text
Actuá como un Diseñador de UI/UX. Necesito diseñar la
pantalla principal de mi sistema.

Mi proyecto es: [NOMBRE]

La pantalla que quiero diseñar: [DESCRIPCIÓN DE LA PANTALLA,
EJ: "pantalla de login", "panel de admin", "formulario de solicitud"]

Usuarios de esta pantalla: [USUARIOS QUE LA USAN]

Acciones principales que deben poder hacer:
1. [ACCIÓN 1]
2. [ACCIÓN 2]
3. [ACCIÓN 3]

Generame:

1. Un wireframe en texto usando caracteres ASCII o Mermaid
   (mostrá dónde va el menú, el contenido, los botones,
   los formularios)
2. Un breve flujo de navegación usando Mermaid sequence

Ejemplo de wireframe en texto:

+--------------------------------------------------+
| [LOGO]         [Inicio] [Productos] [Contacto]    |
+--------------------------------------------------+
|                                                     |
|   BÚSQUEDA: [______________________] [🔍 Buscar]    |
|                                                     |
|   +--------+  +--------+  +--------+               |
|   | Card 1 |  | Card 2 |  | Card 3 |               |
|   | Imagen  |  | Imagen  |  | Imagen  |               |
|   | Texto   |  | Texto   |  | Texto   |               |
|   +--------+  +--------+  +--------+               |
|                                                     |
|   [← Anterior]                    [Siguiente →]    |
+--------------------------------------------------+
```

## Lo que aprendés haciendo esto

- A pensar en la **estructura de la pantalla** antes del diseño visual
- A identificar **qué necesita ver y hacer** el usuario en cada pantalla
- A comunicar diseño sin herramientas complejas
- A usar **Mermaid sequence** para flujos de navegación

## Entrega

1. Carpeta `06_INTERFAZ_USUARIO/`
2. Archivo `06_INTERFAZ_USUARIO/wireframes.md`
3. Commit: `git commit -m "feat: wireframes de interfaz de usuario"`
4. Rama: `feat/ej-05-wireframe`

## Criterios de aprobación

- [ ] El wireframe muestra la estructura completa de la pantalla
- [ ] Se identifica claramente el menú, contenido y acciones principales
- [ ] Incluye un flujo de navegación (Mermaid sequence)
- [ ] Las acciones del usuario están claras
- [ ] Se puede entender el diseño sin explicación adicional
