### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Trabajo Colaborativo con Git y GitHub

## El Desarrollador no es Solo el que Hace Código

Una idea errónea muy común es pensar que un desarrollador de software solo escribe código. La realidad del trabajo profesional incluye:

- **Control de versiones**: cada cambio queda registrado con autor, fecha y motivo
- **Revisión de código**: nadie escribe directo a producción, todo pasa por revisión
- **Gestión de tareas**: issues, tableros, sprints, prioridades
- **Documentación**: decisiones técnicas, manuales, comentarios
- **Despliegue**: cómo llega el código a producción
- **Comunicación**: con el equipo, con el cliente, con los usuarios

Este módulo te enseña la parte de **trabajo colaborativo** que es tan importante como saber programar.

---

## Flujo de Trabajo Profesional

```
[Issue/ Tarea] → [Rama] → [Commits] → [PR] → [Code Review] → [Merge] → [Deploy]
     ↓            ↓           ↓          ↓          ↓            ↓          ↓
  GitHub      git branch  git commit  gh pr      comentarios   git merge  CI/CD
  Projects                 feat: xxx   create     y cambios                Actions
```

Cada flecha es un **hábito profesional**. Si salteás alguno, el equipo pierde trazabilidad.

---

## Creación del Repositorio

### Opción 1: Desde cero para un proyecto nuevo

Cada proyecto de la materia se aloja en un repositorio dentro de la **organización IES9018** en GitHub.

El docente o el líder del equipo crea el repositorio:

```bash
# Con GitHub CLI
gh repo create IES9018/nombre-del-proyecto --public --clone

# Agregar colaboradores (el resto del equipo)
gh repo add-collaborator IES9018/nombre-del-proyecto usuario-github
```

### Opción 2: Fork del repositorio base de la materia

Para entregas individuales, se forkear el repositorio base:

```bash
gh repo fork IES9018/proyecto-adi-2026 --clone=true
cd proyecto-adi-2026

# Vincular upstream para recibir actualizaciones
git remote add upstream https://github.com/IES9018/proyecto-adi-2026.git
```

### Reglas del repositorio

- **Siempre público** (excepto que haya datos sensibles)
- **README obligatorio** con descripción del proyecto
- **.gitignore obligatorio** (no subir node_modules/, .env, __pycache__/)
- **LICENSE obligatorio** (MIT, Apache 2.0 o GPL3)
- **CHANGELOG obligatorio** con cambios de cada versión

---

## Convenciones de Commits

Usamos **Conventional Commits** de forma estricta. No se aceptan commits sin el prefijo adecuado.

### Formato

```
<tipo>: <descripción breve>

[opcional: cuerpo explicando por qué]
```

### Tipos válidos

```
feat:     nueva funcionalidad
fix:      corrección de error
docs:     documentación
refactor: mejora de código sin cambiar funcionalidad
test:     tests
chore:    mantenimiento (config, builds)
style:    formato (espacios, comas)
```

### Ejemplos para esta materia

```bash
git commit -m "feat: agrega ADR-003 sobre elección de base de datos"
git commit -m "docs: completa README con instrucciones de instalación"
git commit -m "fix: corrige error en diagrama C4 de contexto"
git commit -m "refactor: separa lógica de autenticación en módulo propio"
```

### Frecuencia ideal

> **Un commit por cada cambio atómico.** Si termina una sección del ADR, commit. Si agrega un diagrama, commit. Si implementa una función, commit.

No esper a tener 20 archivos cambiados para commitear. Los commits chicos permiten:
- Entender el progreso del proyecto
- Revertir un cambio específico sin perder otros
- Hacer code review por partes pequeñas

---

## Ramas (Branches)

### Estrategia

```
main                    ← código estable, siempre funcional
├── feat/agente-00-devops     ← setup del repo
├── feat/agente-01-analista   ← requisitos
├── feat/agente-02-arquitecto ← arquitectura
├── feat/agente-03-modelador  ← modelo de datos
├── feat/agente-04-casos-uso  ← casos de uso
├── feat/agente-05-ui         ← diseño de interfaces
├── feat/agente-06-techlead   ← stack técnico
├── feat/agente-07-desarrollo ← código fuente
├── fix/error-adr-003         ← hotfix
└── docs/actualizar-readme    ← documentación
```

### Reglas

- **Nunca trabajar directo en `main`**
- Cada agente del andamiaje tiene su propia rama
- Una vez aprobado el PR y hecho el merge, la rama se borra
- Nombre de rama: `feat/agente-NN-nombre` o `fix/descripcion-corta`

```bash
# Crear rama
git checkout -b feat/agente-01-analista

# Ver en qué rama estoy
git branch

# Cambiar a otra rama
git checkout main
```

---

## Pull Requests

El PR es el mecanismo formal de **entrega y revisión**.

### Cuándo abrir un PR

- Cuando terminaste un agente completo del andamiaje
- Cuando querés feedback del docente o del equipo
- **Nunca** cuando el código no compila o está a medio hacer

### Cómo crear un PR

```bash
gh pr create \
  --base main \
  --head feat/agente-01-analista \
  --title "Agente 01: Análisis de Requisitos" \
  --body "## Qué hice
- Entrevisté al cliente con el agente
- Documenté requisitos funcionales y no funcionales
- Identifiqué stakeholders

## Archivos
- 00_REFERENCIAS/requisitos.md
- 00_REFERENCIAS/stakeholders.md

## Decisiones
- Se priorizó autenticación por sobre búsqueda avanzada"
```

### Qué debe tener un buen PR

- [ ] Título descriptivo
- [ ] Resumen de lo que se hizo (3-5 líneas)
- [ ] Lista de archivos creados/modificados
- [ ] Decisiones clave tomadas
- [ ] Captura de pantalla si hay cambios visuales

---

## Issues y Gestión de Tareas

Cada tarea del proyecto se representa con un **Issue** en GitHub.

### Tipos de issues

| Label | Para... |
|:------|:--------|
| `agente-01` | Tareas del Agente Analista |
| `agente-02` | Tareas del Agente Arquitecto |
| `bug` | Errores encontrados |
| `mejora` | Funcionalidad opcional o futura |
| `duda` | Consultas para el docente |
| `urgente` | Bloqueante, necesita atención inmediata |

### Flujo de trabajo con issues

```
Issue abierto → Asignado a un miembro → Rama vinculada
→ PR que referencia el issue → Merge → Issue cerrado
```

```bash
# Crear issue desde CLI
gh issue create \
  --title "Modelar entidades del sistema de solicitudes" \
  --label "agente-03" \
  --assignee @me
```

---

## Code Review (Revisión de Código)

No es "corregir errores". Es **compartir conocimiento**.

### Para el que revisa

- ¿El código hace lo que dice el ADR?
- ¿Sigue los patrones definidos?
- ¿Hay algo que no entiendo? (preguntá)
- ¿Faltan tests? ¿Falta documentación?
- **Sé constructivo**: "Acá podríamos usar un enumerador en vez de strings"

### Para el que recibe revisión

- No te lo tomes personal. El code review es sobre el código, no sobre vos
- Si no entendés un comentario, preguntá
- Agradecé las sugerencias
- Corregí y actualizá el PR con nuevos commits

---

## CI/CD y Automatización

Con GitHub Actions podés automatizar:

- **Tests automáticos**: cada PR ejecuta los tests y muestra si pasan
- **Linting**: verifica que el código siga el formato definido
- **Deploy automático**: cuando se fusiona a `main`, se despliega solo

### Pipeline básico

```yaml
# .github/workflows/ci.yml (ejemplo)
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test
```

Esto lo configuraremos más adelante, pero es importante saber que **existe y que es el estándar de la industria**.

---

## Checklist Antes de Cada Entrega

Antes de abrir un PR o pedir revisión, verificá:

- [ ] ¿Estoy en la rama correcta? (`git branch`)
- [ ] ¿Hice commit de todo? (`git status` sin nada pendiente)
- [ ] ¿Los commits siguen Conventional Commits?
- [ ] ¿Hice push?
- [ ] ¿El PR tiene título, descripción y archivos listados?
- [ ] ¿No subí `.env`, contraseñas ni archivos binarios?
- [ ] ¿El `.gitignore` cubre lo necesario?
- [ ] ¿El código/documentación es revisable por otro?

---

## Para Recordar

> El historial de Git cuenta la historia de tu proyecto.
> Si el docente puede leer tus commits y entender qué hiciste,
> cuándo y por qué, vas por buen camino.
> Un desarrollador profesional no es el que escribe más código.
> Es el que escribe código que otros pueden leer, entender y mantener.
