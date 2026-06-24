# ADR-007: Arquitectura del Frontend

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El frontend necesita estructura, patrón de componentes y gestión de estado. Los estudiantes de la tecnicatura deben poder leer y entender la organización del código React.

---

## Decisión

**Patrón: Feature-based con componentes funcionales y hooks.**

```
frontend/src/
├── components/          ← Componentes reutilizables (botones, inputs, cards)
├── pages/               ← Páginas completas (Login, Solicitud, PanelAdmin, Catalogo)
├── services/            ← Cliente HTTP (fetch wrapper + interceptors)
├── hooks/               ← Hooks personalizados (useAuth, useSolicitudes)
└── context/             ← Context API para estado global (auth)
```

**Stack:**
| Herramienta | Propósito |
|:------------|:----------|
| React 19 | Componentes funcionales, hooks |
| Vite | Build tool rápido, HMR |
| React Router 7 | Navegación y rutas protegidas |
| Context API | Estado global de autenticación |
| CSS Modules | Estilos encapsulados por componente |

---

## Alternativas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| Redux / Zustand | Overkill para este proyecto. Con 3 roles y 10 funcionalidades, Context API alcanza. |
| Next.js / SSR | Agrega complejidad de servidor Node. Este proyecto tiene backend separado. |
| Tailwind CSS | Agrega dependencia y curva de aprendizaje. CSS Modules es nativo, sin dependencias. |
| Class components | Obsoletos. La industria usa hooks desde 2019. |

---

## 🧠 Analogía del @docente

> Organizar componentes React es como organizar una **cocina profesional**. `components/` son los utensilios comunes (cuchillos, sartenes) que usan todos. `pages/` son los platos terminados. `services/` es el proveedor que trae los ingredientes (API). `hooks/` son las técnicas de cocina que repetís (sofreír, blanquear). Si mezclás todo en un cajón, cocinar es un caos.
