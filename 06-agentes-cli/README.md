# 🧠 Agentes CLI — Catálogo y Tutorial

Este directorio contiene los **agentes de IA para terminal** que usamos en la materia. Son archivos de configuración para herramientas como **opencode** (recomendada) que convierten a la IA en asistentes especializados con roles, permisos y comportamientos definidos.

---

## 🎯 ¿Qué es un agente CLI?

**Analogía:** Un agente CLI es como un **empleado con una descripción de puesto clarísima**. No le decís "hacé lo que sea", sino:

> *"Vos sos el Arquitecto. Tu único trabajo es revisar diagramas y documentar decisiones. No tocás código, no ejecutás comandos."*

Cada agente sabe exactamente:
- **Qué puede hacer** (leer archivos, editarlos, ejecutar comandos)
- **Qué NO puede hacer** (para no pisar el trabajo de otros agentes)
- **Qué debe producir** (archivos, reportes, diagramas)
- **Cómo debe pensar** (con qué criterios, usando qué estándares)

---

## 🗂️ Agentes disponibles

Los agentes se dividen en dos familias:

### Familia A: Agentes del Profesor (DobleA NexGen)

Estos son los agentes reales que el profesor usa para construir el proyecto DobleA NexGen. Están acá para que los **estudies, los entiendas y los adaptes** a tu proyecto.

Ver [`catalogo-agentes.md`](./catalogo-agentes.md).

| Agente | Rol |
|:-------|:----|
| `@arquitecto` | Audita arquitectura, detecta inconsistencias |
| `@backend` | Implementa lógica de negocio |
| `@committer` | Pipeline de calidad + git commit |
| `@debugger` | Diagnostica bugs hasta archivo:línea |
| `@docente` | Explica conceptos con analogías |
| `@documentation` | Mantiene documentación y ADRs |
| `@infrastructure` | Implementa adaptadores de infraestructura |
| `@review` | Ejecuta ruff + mypy + pytest, aprueba/rechaza |
| `@security` | Audita vulnerabilidades OWASP |
| `@testing` | Escribe tests |
| `@ui-tester` | Navega la app con Playwright |

### Familia B: Agentes del Andamiaje ADI

Los prompts de [`02-andamiaje-agentes/`](../02-andamiaje-agentes/) definen 8 agentes con roles específicos (Analista, Arquitecto, Modelador, etc.). Esos no son archivos de configuración, sino **prompts conversacionales** que copiás en tu terminal.

---

## 🚀 Tutorial: Cómo usar agentes en tu proyecto

### Paso 1: Elegí una herramienta CLI

Primero necesitás un asistente de IA en tu terminal. Si todavía no tenés uno, revisá la guía de instalación:

> 📖 [`instalacion-herramientas-cli.md`](../instalacion-herramientas-cli.md)

**Recomendada para agentes:** opencode (soporte nativo para subagentes)

```bash
curl -fsSL https://opencode.ai/install | bash
```

### Paso 2: Creá la carpeta de agentes en tu proyecto

```bash
cd tu-proyecto
mkdir -p .opencode/agents
```

### Paso 3: Copiá un agente

Copiá el archivo `.md` del agente que querés usar a la carpeta `.opencode/agents/` de tu proyecto.

Por ejemplo, para tener al @docente en tu proyecto:

```bash
cp 06-agentes-cli/agentes/docente.md tu-proyecto/.opencode/agents/
```

### Paso 4: Personalizá el agente (opcional)

Abrí el archivo copiado y ajustá la `description` y los permisos según tu proyecto.

```yaml
# Ejemplo: cambiar la descripción para tu proyecto
description: Docente que explica conceptos del Sistema de Gestion de Biblioteca
```

### Paso 5: Usá el agente

Invocá al agente desde tu terminal:

```
@docente explicame esto: ADR
Encontrame un ADR en mi repo y explicame qué significa.
```

### Paso 6: Usá múltiples agentes

Podés tener varios agentes activos al mismo tiempo. Cada uno hace su trabajo sin interferir:

```
@arquitecto revisame los diagramas C4 del proyecto
 @backend implementame el caso de uso "Crear Solicitud"
```

---

## ⚙️ Anatomía de un agente opencode

Cada agente es un archivo Markdown con metadatos YAML al inicio. Esta es la estructura:

```yaml
---
description: Una frase que describe al agente (lo ve el orquestador)
mode: subagent            # Siempre va "subagent"
permission:
  read: allow              # ¿puede leer archivos? allow | deny
  glob: allow              # ¿puede buscar archivos? allow | deny
  grep: allow              # ¿puede buscar contenido? allow | deny
  edit: allow              # ¿puede modificar archivos? allow | deny
  bash: deny               # ¿puede ejecutar comandos? allow | deny
  task: allow              # ¿puede lanzar otros agentes? allow | deny
---
```

**Reglas de permisos:**

| Permiso | `allow` | `deny` |
|:--------|:--------|:-------|
| `read` | Puede leer archivos del proyecto | Solo ve lo que le pasás |
| `edit` | Puede crear y modificar archivos | Solo lectura |
| `bash` | Puede ejecutar comandos | No ejecuta nada |
| `task` | Puede invocar otros agentes | Trabaja solo |

**Analogía:** Los permisos son como las **llaves de las habitaciones de una oficina**. Al Arquitecto le das la llave de la sala de planos (lectura de diagramas) pero no la del servidor (ejecución de comandos). Al Desarrollador le das la llave del código (escritura) pero no la de la sala de servidores.

---

## 🧪 Buenas prácticas con agentes

| Práctica | Explicación |
|:---------|:------------|
| **Un agente a la vez** | No le pidas a un agente que haga el trabajo de otro |
| **Permisos mínimos** | Si un agente solo necesita leer, poné `edit: deny` |
| **Descripción clara** | La `description` es lo que usa el orquestador para elegir al agente correcto |
| **Rol único** | Cada agente hace UNA cosa bien |
| **Probá antes de compartir** | Verificá que el agente haga lo que promete |

---

## 💡 ¿Creaste un agente nuevo?

Si modificaste un agente existente o creaste uno nuevo, **compartilo** con la comunidad:

1. Abrí un Issue con la etiqueta `agente` en el [repositorio principal](https://github.com/IES9018/proyecto-adi-2026)
2. Describí qué hace tu agente y cómo se usa
3. Si querés, abrí un Pull Request para agregarlo al catálogo

> 📖 Ver [`CONTRIBUTING.md`](../CONTRIBUTING.md) para más detalles.

---

## 🔗 Referencias

| Recurso | Link |
|:--------|:-----|
| Documentación de opencode | [opencode.ai](https://opencode.ai) |
| Agentes del profesor | [`catalogo-agentes.md`](./catalogo-agentes.md) |
| Agentes listos para copiar | [`agentes/`](./agentes/) |
| Guía de instalación CLI | [`instalacion-herramientas-cli.md`](../instalacion-herramientas-cli.md) |
| Andamiaje de 8 agentes | [`02-andamiaje-agentes/`](../02-andamiaje-agentes/) |
