### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Arquitectura y Diseño de Interfaces — 2026

## ¡Bienvenido/a!

Este repositorio contiene todo el material de clase para la materia **Arquitectura y Diseño de Interfaces**. Continuamos el trabajo de Modelado de Software (2025): ahora le damos vida a esa arquitectura diseñada, eligiendo tecnologías, patrones reales y construyendo interfaces completas.

---

## 🧭 Navegación del Repositorio

| Carpeta/Archivo | ¿Qué contiene? |
|:----------------|:---------------|
| `01-teoria/` | Fundamentos: arquitectura, patrones, diseño de interfaces, estándares globales, IA como aliado |
| `02-andamiaje-agentes/` | Metodología de agentes IA: 2 prompts, flujo de 8 agentes, ejemplos reales |
| `03-proyectos/` | 3 proyectos reales para aplicar la teoría (Gobernanza Digital, Fundación Messi, Crianceros) |
| `04-github-workflow/` | Guía completa de trabajo colaborativo: repo, ramas, PRs, issues, CI/CD |
| `05-ejercicios/` | 6 ejercicios prácticos con prompts listos para copiar y pegar en tu IA |
| `glosario.md` | 25 términos de arquitectura con analogías y referencias |
| `rubrica-evaluacion.md` | Criterios de evaluación con 5 dimensiones y 4 niveles |
| `LISTA_ESTUDIANTES.md` | Repositorios de todos los estudiantes |
| `PLanificaciones/` | Contrato pedagógico, programa y planificación anual |
| `feedback/` | Feedbacks individuales por estudiante |

---

## 🗺️ ¿Cómo Usar este Repositorio?

### Flujo de trabajo semanal

1. **Leé la teoría** en `01-teoria/` en orden (del 01 al 06)
2. **Consultá el glosario** en `glosario.md` si hay términos que no entendés
3. **Hacé el ejercicio** correspondiente en `05-ejercicios/`
4. **Si trabajás en un proyecto**, seguí el andamiaje de `02-andamiaje-agentes/`
5. **Entregá por Pull Request** siguiendo `04-github-workflow/`

### Flujo de trabajo con Git (fork del repo base)

```bash
# Fork desde tu cuenta
gh repo fork IES9018/proyecto-adi-2026 --clone=true
cd proyecto-adi-2026

# Vincular repositorio base (upstream)
git remote add upstream https://github.com/IES9018/proyecto-adi-2026.git

# Crear rama para la entrega
git checkout -b feat/entrega-clase-01

# Guardar cambios
git add .
git commit -m "feat: entrega clase 01"
git push -u origin feat/entrega-clase-01

# Abrir PR
gh pr create --base main --head feat/entrega-clase-01 \
  --title "Entrega Clase 01" --body "Actividad resuelta"
```

> 📖 **Guía completa de Git y GitHub** en [`04-github-workflow/`](./04-github-workflow/)

---

## 🎯 Metodología de la Materia

Esta materia usa el **Andamiaje de Agentes IA** como método de trabajo estructurado. No se trata de pedirle a la IA que "te haga el proyecto", sino de orquestar un equipo de agentes especializados que trabajan bajo tu supervisión.

| Fase | Qué hacés |
|:-----|:----------|
| **Fase 0 — Scoping** | Usás el **Prompt 1** para que la IA te entreviste y definas tu proyecto |
| **Fase 1 — Construcción** | Usás el **Prompt 2** para desplegar 8 agentes que construyen el sistema paso a paso |

Cada agente produce archivos, vos los revisás, creás un PR, y recién después de aprobado pasás al siguiente.

> 📖 **Guía completa del andamiaje** en [`02-andamiaje-agentes/`](./02-andamiaje-agentes/README.md)

---

## 📘 Contenidos de la Materia

### 1. Procesos y Metodologías
- Metodologías ágiles y tradicionales
- Patrones de diseño de software: rol, criterios de selección y aplicación

### 2. Arquitectura de Software
- Patrones para estructurar sistemas: capas, tuberías y filtros, tablero
- Arquitectura Hexagonal, MVC, C4 Model, ADRs

### 3. Diseño de Interfaces (HCI)
- Interfaz hombre-máquina, gráficas, usuario
- UX vs UI, wireframes, mockups, prototipos
- Accesibilidad y diseño responsive

### 4. Arquitectura Web
- Tecnologías full stack, modelo cliente-servidor
- Frontend (React, Next.js), Backend (FastAPI, NestJS), Base de Datos (PostgreSQL)

### 5. Arquitectura Mobile
- Apps nativas, híbridas, cross-platform
- Servicios y microservicios en mobile

### 6. Herramientas, Tecnologías e Integración
- Herramientas para diseño de interfaces
- Integración de distintas tecnologías
- CI/CD, Docker, GitHub Actions

---

## 🧠 La IA como Aliado (No como Atajo)

En esta materia, la IA es tu **tutor 24/7**. La idea no es que la IA te haga el trabajo, sino que te ayude a **pensar mejor**:

- **¿No entendés un concepto?** Pedile a la IA que te lo explique con una analogía.
- **¿No sabés qué patrón usar?** El agente Arquitecto te guía con preguntas.
- **¿Querés practicar para el oral?** La IA simula ser tu profesor y te hace preguntas.

> 📖 **Guía completa: la IA como aliado** en [`01-teoria/06-ia-como-aliado.md`](./01-teoria/06-ia-como-aliado.md)

---

## 🔗 Continuidad Curricular

| Materia | Año | Qué se hizo |
|:--------|:---:|:------------|
| Modelado de Software | 2025 | Diagramas UML, arquitectura MVC, diseño del sistema |
| **Arquitectura y Diseño de Interfaces** | **2026** | **Patrones reales, tecnologías, interfaces concretas** |
| Práctica Profesionalizante III | 2026 | Ejecución del proyecto integrador completo |

---

## 👥 Equipo

**Profesor:** Paulo Alvarez  
**Institución:** IES 9-018 "Gobernador Celso Jaque" — Mendoza  
**Repositorio base:** [IES9018/proyecto-adi-2026](https://github.com/IES9018/proyecto-adi-2026)
