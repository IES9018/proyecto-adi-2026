### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Arquitectura y Diseño de Interfaces — 2026

## ¡Bienvenido/a!

Este repositorio contiene todo el material de clase para la materia **Arquitectura y Diseño de Interfaces**. Continuamos el trabajo que comenzamos en Modelado de Software (2025): ahora le damos vida a esa arquitectura diseñada, eligiendo tecnologías, patrones reales y construyendo interfaces completas.

---

## 📋 Contenidos de la Materia

### 1. Procesos y Metodologías
- Metodologías ágiles y tradicionales en el desarrollo
- Patrones de diseño de software: rol, criterios de selección y aplicación

### 2. Arquitectura de Software
- Patrones para estructurar sistemas: capas, tuberías y filtros, tablero
- Otros patrones arquitecturales

### 3. Diseño de Interfaces (HCI)
- Interfaz hombre-máquina, gráficas, usuario
- Abstracción en lenguajes de programación
- Interfaces orientadas a gestos y a comportamientos

### 4. Arquitectura Web
- Tecnologías full stack, modelo cliente-servidor
- Frameworks para desarrollo empresarial
- Servicios y microservicios

### 5. Arquitectura Mobile
- Apps nativas, híbridas
- Servicios y microservicios en mobile

### 6. Herramientas, Tecnologías e Integración
- Herramientas para diseño de interfaces
- Integración de distintas tecnologías
- Gestión de errores del usuario y del sistema

---

## 🗺️ ¿Cómo Usar este Repositorio?

### Flujo de trabajo (igual que en Modelado 2025)

1. **Fork** del repositorio base del curso en IES9018
2. **Clone** a tu máquina local
3. **Commit + Push** de tu trabajo en tu fork
4. **Pull Request** al repositorio base para entregar

```bash
# Opcion con GitHub CLI (recomendada)
gh repo fork IES9018/proyecto-adi-2026 --clone=true
cd proyecto-adi-2026

# Vincular repositorio base (upstream)
git remote add upstream https://github.com/IES9018/proyecto-adi-2026.git
git fetch upstream

# Crear rama para la entrega
git checkout -b feat/entrega-clase-01

# Guardar cambios
git add .
git commit -m "feat: entrega clase 01"
git push -u origin feat/entrega-clase-01

# Abrir PR
gh pr create --base main --head feat/entrega-clase-01 --title "Entrega Clase 01" --body "Actividad resuelta"
```

```bash
# Opcion manual (sin GitHub CLI)
# 1) Hacer fork desde la web de GitHub
# 2) Clonar tu fork
git clone https://github.com/TU-USUARIO/proyecto-adi-2026.git
cd proyecto-adi-2026

# 3) Agregar upstream
git remote add upstream https://github.com/IES9018/proyecto-adi-2026.git
```

### Paso a paso

1. Leer el material de cada clase en orden
2. Realizar los ejercicios prácticos antes de avanzar
3. Consultar el [`glosario`](./glosario.md) ante cualquier término desconocido
4. Entregar mediante Pull Request con descripción clara
5. Usar **issues de GitHub** para consultas y dudas

---

## 📚 Estructura de Archivos

| Archivo | Descripción |
|---------|-------------|
| `README.md` | Esta guía |
| `LISTA_ESTUDIANTES.md` | Repositorios de todos los estudiantes |
| `INDICE_SEGUIMIENTO.md` | Índice de archivos de seguimiento y evaluación |
| `CHANGELOG.md` | Historial de cambios en el material |
| `rubrica-evaluacion.md` | Criterios de evaluación |
| `seguimiento-estudiantes.json` | Estado actualizado por estudiante |
| `Planificaciones/` | Cronograma, programa y planificación anual |
| `feedback/` | Feedbacks individuales por estudiante |

---

## 🔗 Continuidad Curricular

Esta materia es la **continuación directa** de Modelado de Software (2025):

| Materia | Año | Qué se hizo |
|---------|-----|-------------|
| Modelado de Software | 2025 | Diagramas UML, arquitectura MVC, diseño del sistema |
| **Arquitectura y Diseño de Interfaces** | **2026** | **Patrones reales, tecnologías, interfaces concretas** |
| Práctica Profesionalizante III | 2026 | Ejecución del proyecto integrador completo |

---

## 👥 Equipo

**Profesor:** Paulo Alvarez  
**Institución:** IES 9-018 "Gobernador Celso Jaque" — Mendoza  
**Repositorio base:** [IES9018/proyecto-adi-2026](https://github.com/IES9018/proyecto-adi-2026)
