# Proyectos Reales — Arquitectura y Diseño de Interfaces

Esta carpeta documenta **3 proyectos reales** que los estudiantes pueden desarrollar aplicando el andamiaje de agentes IA y los contenidos de la materia.

---

## Justificación Pedagógica

| ¿Por qué proyectos reales? | ¿Qué aprenden? |
|:---------------------------|:---------------|
| El problema existe de verdad | A trabajar con requisitos reales, no inventados |
| Hay un cliente real o simulado | A comunicarse con stakeholders |
| El sistema se va a usar | A tomar decisiones con consecuencias reales |
| Hay restricciones reales | A negociar alcance y prioridades |

---

## Los 3 Proyectos

| Proyecto | Complejidad | Tipo | ¿Qué enseña? |
|:---------|:-----------:|:----|:-------------|
| **A. Gobernanza Digital** | Intermedia | Web con formularios + flujos de aprobación | Arquitectura hexagonal, RBAC, workflow de estados, CI/CD, deploy en servidor real |
| **B. Fundación Messi** | Inicial | Web institucional (landing + blog) | Diseño de interfaces, responsive, SEO, contenido dinámico |
| **C. Crianceros de Malargüe** | Avanzada | App mobile/web con geolocalización | Modo offline, mapas, trazabilidad, catálogo de animales |

---

## Proyecto A: Gobernanza Digital (Recomendado)

**¿Por qué este es el proyecto principal?**

Este proyecto tiene el marco institucional completo en el repositorio [IES9018/gobernanza-servicios-digitales](https://github.com/IES9018/gobernanza-servicios-digitales). Los estudiantes no parten de cero: hay 12 documentos que definen el proceso, los roles y los flujos de trabajo.

Además, **se alinea directamente con Práctica Profesionalizante III**, ya que el sistema final se desplegaría en el servidor institucional del IES 9-018.

Ver detalles → [`A-gobernanza-digital/README.md`](./A-gobernanza-digital/README.md)

---

## Proyecto B: Fundación Messi

**¿Por qué?**

Una web institucional para mostrar las actividades de la Fundación Messi. Ideal para aprender diseño de interfaces profesionales con un cliente de alto perfil (simulado).

**Características:**
- Landing page con secciones: quiénes somos, programas, galería, contacto
- Blog de noticias
- Formulario de contacto
- Panel admin básico para gestionar contenido
- Diseño responsive y accesible

---

## Proyecto C: Crianceros de Malargüe

**¿Por qué?**

Los crianceros (ganaderos trashumantes) de Malargüe necesitan una herramienta digital para registrar y hacer seguimiento de sus animales, pasturas y movimientos. Es un problema real con un usuario posta.

**Características:**
- Registro de animales con datos: especie, raza, edad, peso, estado sanitario
- Mapa con ubicación de pasturas y aguadas
- Trazabilidad de movimientos trashumantes
- Modo offline (sin señal en la montaña)
- Reportes básicos para el SENASA

---

## ¿Cuál elegir?

| Si te gusta... | Elegí... |
|:---------------|:---------|
| Diseñar interfaces lindas | **B - Fundación Messi** |
| Sistemas con reglas de negocio y flujos | **A - Gobernanza Digital** |
| Apps con mapas y sin señal de internet | **C - Crianceros** |
| No sabés por dónde arrancar | Empezá por **B**, es el más simple |
