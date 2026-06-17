# Cómo Contribuir a este Repositorio

## Filosofía

> Este repositorio no es solo del docente. **Es de todos los estudiantes**, pasado, presente y futuro.

Cada estudiante que cursa Arquitectura y Diseño de Interfaces tiene algo valioso para aportar. Tal vez descubriste una analogía que te hizo click. Tal vez modificaste un prompt del andamiaje y funcionó mejor. Tal vez encontraste un error en la documentación.

**Este espacio es para eso.**

---

## Formas de Contribuir

### 1. Reportar un problema o sugerir una mejora (Issues)

Cualquier persona puede abrir un Issue para:

- Reportar errores en la documentación
- Sugerir nuevas analogías para el agente @docente
- Proponer mejoras a los prompts del andamiaje
- Pedir un tema que no está cubierto en la teoría
- Reportar un enlace roto o información desactualizada

```bash
# Con GitHub CLI
gh issue create \
  --title "Nueva analogía para Arquitectura Hexagonal" \
  --label "mejora" \
  --body "Propongo esta analogía: ..."
```

**Labels disponibles:**

| Label | Para qué usarla |
|:------|:----------------|
| `mejora` | Sugerencia de mejora o contenido nuevo |
| `bug` | Error en la documentación |
| `analogía` | Aporte de nueva analogía para @docente |
| `agente` | Nuevo agente o mejora de agente existente |
| `duda` | Consulta sobre un concepto |
| `herramienta` | Nueva herramienta CLI o guía de instalación |
| `proyecto` | Aporte sobre los proyectos (Gobernanza, Messi, Crianceros) |

### 2. Crear o mejorar un agente del andamiaje

Si modificaste un prompt del andamiaje para que funcione mejor, o creaste un agente nuevo:

1. **Abrí un Issue** primero para discutir el cambio
2. **Hacé un fork** del repositorio
3. **Creá tu rama**: `git checkout -b feat/mi-nuevo-agente`
4. **Modificá o creá** el archivo en `02-andamiaje-agentes/`
5. **Commit**: `git commit -m "feat: nuevo agente para explicar patrones con memes"`
6. **Push y PR**: abrí un Pull Request explicando qué hace el agente

### 3. Agregar una analogía nueva

Cada analogía que descubrís ayuda a otro estudiante que está trabado en el mismo concepto.

Editá [`02-andamiaje-agentes/agente-docente.md`](./02-andamiaje-agentes/agente-docente.md) y agregá tu analogía en la sección "Analogías descubiertas por estudiantes".

Formato:

```markdown
| **Nombre del Concepto** | Tu analogía: [descripción breve] — *descubierto por [Tu nombre]* |
```

O abrí un Issue con la etiqueta `analogía`.

### 4. Agregar una nueva herramienta CLI

Si instalaste una herramienta de IA por terminal que no está en la guía, compartí cómo la instalaste.

Editá [`instalacion-herramientas-cli.md`](./instalacion-herramientas-cli.md) y agregá:

```markdown
### [Nombre de la herramienta]

**Web oficial:** [link]

```bash
# Instalación que funcionó en mi máquina
comando de instalación
```

**Ventajas:** [por qué la recomendás]  
**Descubierto por:** [Tu nombre]
```

### 5. Corregir errores

¿Encontraste un error ortográfico, un link roto, o una explicación confusa? Corregilo y abrí un PR directo. No necesitas permiso.

---

## Flujo de Contribución

```
1. Idea o error encontrado
       ↓
2. Issue abierto (discutimos)
       ↓
3. Fork + rama nueva
       ↓
4. Cambios + commit
       ↓
5. Pull Request
       ↓
6. Revisión por docente y/o compañeros
       ↓
7. Merge → disponible para todos
```

---

## Beneficios de Contribuir

| Qué hacés | Qué ganás |
|:----------|:----------|
| Reportás un error | Ayudás a toda la cursada, te ganás el respeto del equipo |
| Proponés una analogía | Tu nombre queda en el repositorio público, tu aporte ayuda a futuros estudiantes |
| Mejorás un agente | El agente que creaste lo usa toda la organización IES9018 |
| Agregás una herramienta | Compartís tu descubrimiento, todos aprenden |
| Corregís documentación | Demostrás que entendiste el tema y sabés comunicarlo |

---

## Código de Conducta

- **Respeto ante todo.** No hay preguntas tontas ni aportes chicos.
- **Las críticas son sobre el contenido, no sobre la persona.**
- **Todos empiezan sin saber.** Este repositorio existe para que entre todos construyamos conocimiento.
- **Si no estás seguro de algo, preguntá igual.** Un Issue es bienvenido siempre.

---

## Para Recordar

> La documentación viva es mejor que la documentación perfecta.
> Este repo mejora con cada PR, cada Issue, cada analogía compartida.
> En unos años, cuando seas profesional, vas a poder mirar atrás y decir:
> "Yo aporté a esto cuando estaba aprendiendo. Y mi aporte sigue ayudando a otros."
