# Plan Maestro — Gobernanza Digital

**Versión:** v1.0 | **Fecha:** Junio 2026 | **Agente:** Arquitecto

---

## 🏛️ Visión arquitectónica

Construir un sistema web de gobernanza digital que sea:

1. **Transparente** — toda decisión, evaluación y resolución queda registrada y auditable
2. **Modular** — capas desacopladas que permiten cambiar infraestructura sin tocar dominio
3. **Pedagógico** — cada decisión técnica está explicada y justificada para que los estudiantes aprendan
4. **Desplegable** — funciona igual en desarrollo (SQLite) y producción (PostgreSQL en Debian 12)

---

## 🧱 Principios arquitectónicos

### P1: Dependencia hacia adentro
Las dependencias apuntan del exterior al interior. `domain/` no conoce nada externo. `application/` solo conoce `domain/`. `infrastructure/` y `web/` conocen los puertos definidos en `domain/`.

### P2: Separación de responsabilidades
Cada capa tiene una razón para cambiar distinta:
- `domain/` cambia si cambian las reglas del negocio
- `application/` cambia si cambian los casos de uso
- `infrastructure/` cambia si cambia la tecnología externa (DB, email, deploy)
- `web/` cambia si cambia la API o el framework HTTP

### P3: Puertos y adaptadores
Toda comunicación con el exterior pasa por interfaces definidas en `domain/ports/`. Las implementaciones concretas viven en `infrastructure/`.

### P4: Testeabilidad primero
Cada capa se testea de forma aislada. El dominio no necesita base de datos para testearse. Los casos de uso no necesitan HTTP. Los adaptadores se mockean con facilidad.

### P5: Configuración por entorno
Cero valores hardcodeados. Toda configuración sensible va en variables de entorno. `.env.example` documenta todas las variables necesarias.

### P6: Trazabilidad completa
Cada artefacto (código, ADR, caso de uso, test) referencia los requisitos que satisface. Si un requisito cambia, se sabe exactamente qué archivos tocar.

### P7: Documentación viva
Los ADRs, diagramas C4 y READMEs se actualizan cuando cambia el código. La documentación desactualizada es peor que la documentación faltante.

---

## 🎯 Atributos de calidad priorizados

| Atributo | Prioridad | Cómo se garantiza |
|:---------|:---------:|:------------------|
| **Seguridad** | Alta | JWT + bcrypt + CORS + rate limiting + consultas parametrizadas + headers |
| **Mantenibilidad** | Alta | Arquitectura hexagonal + tests ≥80% + linting en CI |
| **Transparencia** | Alta | Log de auditoría + catálogo público + ADRs con justificaciones |
| **Disponibilidad** | Media | Docker restart policy + backup diario + Nginx reverse proxy |
| **Rendimiento** | Baja | FastAPI async + React SPA + paginación en listados |
| **Portabilidad** | Alta | Docker Compose + SQLite/PostgreSQL intercambiables |

---

## 📐 Restricciones técnicas autoimpuestas

1. **FastAPI como único backend.** No se agregan microservicios.
2. **React + Vite como único frontend.** No se usa SSR ni Next.js (por ahora).
3. **Docker obligatorio para deploy.** No se instala nada directamente en el servidor.
4. **SQLite para desarrollo.** Cero configuración necesaria para arrancar.
5. **Conventional Commits.** Todo commit sigue el estándar.
6. **Código abierto.** Licencia MIT. Todo el código es público.
7. **Testing previo al commit.** `pytest` debe pasar antes de pushear (vía CI).

---

## 🧠 Analogía del @docente

> El Plan Maestro es el **plano de la ciudad**. Define dónde van las avenidas principales (capas), qué materiales se pueden usar (stack), qué código de edificación hay que respetar (principios) y qué prioridades tiene la ciudad (atributos de calidad). Los ADRs son los planos de cada edificio. Los C4 son los mapas de la ciudad a distintas escalas. Sin Plan Maestro, cada arquitecto construye con su criterio y la ciudad se vuelve un caos.
