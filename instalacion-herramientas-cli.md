# Instalación de Herramientas CLI para Agentes IA

Guía completa para instalar asistentes de IA por terminal. Cada herramienta te permite usar los prompts del andamiaje directamente desde la consola.

---

## 📋 Antes de Empezar

### Node.js y npm

Muchas herramientas se instalan con npm. Si npm no es lo tuyo, cada herramienta tiene alternativas.

**Opción A: Instalar Node.js vía nvm (recomendada)**

```bash
# nvm permite cambiar de versión sin conflictos
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 22
```

**Opción B: Instalar Node.js directo**

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Alternativas a npm:**

| Alternativa | Instalación |
|:------------|:------------|
| **pnpm** | `curl -fsSL https://get.pnpm.io/install.sh | sh -` |
| **yarn** | `npm install -g yarn` |
| **bun** | `curl -fsSL https://bun.sh/install | bash` |

Si npm te da problemas de permisos, usá `pnpm` o `bun`.

---

## 🤖 Herramientas CLI de IA

### 1. opencode ⭐ (Recomendada)

Open source, gratuita, funciona con modelos gratuitos incluidos o con tu propia API key.

```bash
# Instalación oficial (recomendada)
curl -fsSL https://opencode.ai/install | bash

# Alternativa con npm
npm install -g @anthropic-ai/opencode

# Alternativa con brew (macOS/Linux)
brew install opencode

# Verificar
opencode --version
```

**Web oficial:** [opencode.ai](https://opencode.ai)  
**GitHub:** [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)  
**Ventajas:** Sin costo, 100% open source, podés inspeccionar cómo funciona

---

### 2. Claude Code (Anthropic)

CLI oficial de Anthropic para Claude.

```bash
# Instalación con npm
npm install -g @anthropic-ai/claude-code

# O sin npm, vía curl (recomendado si no querés npm)
curl -fsSL https://claude.ai/install/cli.sh | bash

# Verificar
claude --version
```

**Web oficial:** [anthropic.com/claude-code](https://docs.anthropic.com/en/docs/claude-code)  
**Ventajas:** Modelos Claude de última generación, excelente para código  
**Requiere:** API key de Anthropic o suscripción a Claude Pro/Max

---

### 3. Gemini CLI (Google)

CLI oficial de Google para modelos Gemini.

```bash
# Instalación con npm
npm install -g @google/gemini-cli

# Alternativa con curl
curl -fsSL https://sdk.cloud.google.com/gemini-cli/install.sh | bash

# Verificar
gemini --version

# Configurar API key
export GEMINI_API_KEY="tu-api-key-de-google-ai-studio"
echo 'export GEMINI_API_KEY="tu-api-key"' >> ~/.bashrc
source ~/.bashrc
```

**Web oficial:** [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
**Obtener API key:** [aistudio.google.com/apikey](https://aistudio.google.com/apikey)  
**Ventajas:** Cuota gratuita generosa de Google AI Studio, modelo Gemini 2.5 Flash excelente para código

---

### 4. GitHub Copilot CLI

```bash
# No necesita npm. Se instala como extensión de GitHub CLI
gh extension install github/gh-copilot

# Verificar
gh copilot --version

# Usar
gh copilot explain "qué hace este comando git"
gh copilot suggest "cómo hago un servidor web en Python"
```

**Web oficial:** [docs.github.com/copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-cli)  
**Requiere:** Suscripción a GitHub Copilot (gratuita para estudiantes verificados)

---

### 5. Aider (Open Source)

CLI de programación con IA, open source, funciona con cualquier modelo.

```bash
# Instalación con pip (Python)
pip install aider-chat

# Alternativa con curl
curl -fsSL https://aider.chat/install.sh | bash

# Verificar
aider --version
```

**Web oficial:** [aider.chat](https://aider.chat)  
**GitHub:** [github.com/Aider-AI/aider](https://github.com/Aider-AI/aider)  
**Ventajas:** Open source, funciona con modelos locales (Ollama), ideal si no querés depender de APIs externas

---

### 6. Continue.dev

Extensión de VS Code + CLI open source.

```bash
# Instalación con npm
npm install -g @continuedev/continue

# O instalar desde el marketplace de VS Code
# Buscar "Continue" en extensiones
```

**Web oficial:** [continue.dev](https://continue.dev)  
**GitHub:** [github.com/continuedev/continue](https://github.com/continuedev/continue)  
**Ventajas:** Open source, funciona con modelos locales (Ollama, LM Studio), privacidad total

---

### 7. Kimi CLI (Moonshot AI)

```bash
# Instalación (verificar web oficial para método actualizado)
npm install -g kimi-cli

# O mediante Docker
docker pull moonshotai/kimi-cli
```

**Web oficial:** [kimi.moonshot.cn](https://kimi.moonshot.cn)  
**Nota:** Verificar disponibilidad del CLI según región

---

### 8. Tabla Comparativa

| Herramienta | Open Source | Sin costo | npm | Alternativa sin npm |
|:------------|:-----------:|:---------:|:---:|:--------------------|
| **opencode** | ✅ | ✅ | ✅ | `curl \| bash` |
| **Claude Code** | ❌ | ❌ | ✅ | `curl \| bash` |
| **Gemini CLI** | ❌ | ✅* | ✅ | `curl \| bash` |
| **Copilot CLI** | ❌ | ❌ | ❌ | Extensión gh |
| **Aider** | ✅ | ✅ | ❌ | `pip install` |
| **Continue** | ✅ | ✅ | ✅ | Extensión VS Code |
| **Kimi** | ❌ | ✅* | ✅ | Docker |

*\* Con cuota gratuita limitada*

---

## 🧪 Probar que funciona

```bash
# opencode
echo "Decime en una línea qué es un ADR" | opencode --model free

# gemini
echo "Decime en una línea qué es un ADR" | gemini

# copilot
gh copilot explain "qué es un ADR en arquitectura de software"
```

---

## ❓ Problemas Comunes

| Problema | Solución |
|:---------|:---------|
| `npm: command not found` | Instalar Node.js (ver sección arriba) |
| `EACCES: permission denied` | Usar `nvm` o `pnpm` en vez de npm global |
| `curl: command not found` | `sudo apt install curl -y` |
| Error de API key | Verificar que la variable de entorno esté exportada en `~/.bashrc` |
| `gh: command not found` | `sudo apt install gh -y` (ver [github.com/cli/cli](https://github.com/cli/cli)) |

---

## 🔗 Referencias Rápidas

| Herramienta | Link |
|:------------|:-----|
| opencode | [opencode.ai](https://opencode.ai) |
| Claude Code | [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code) |
| Gemini CLI | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| GitHub Copilot | [docs.github.com/copilot](https://docs.github.com/en/copilot) |
| Aider | [aider.chat](https://aider.chat) |
| Continue | [continue.dev](https://continue.dev) |
| nvm | [github.com/nvm-sh/nvm](https://github.com/nvm-sh/nvm) |
| pnpm | [pnpm.io/installation](https://pnpm.io/installation) |
| bun | [bun.sh](https://bun.sh) |

---

> ¿Probaste una herramienta que no está acá? Abrí un Issue o un PR para agregarla.
> ¿Encontraste un comando que funciona mejor? Compartilo, todos se benefician.
