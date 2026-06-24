# ADR-006: Estrategia de Testing

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El sistema necesita tests para garantizar calidad, servir como documentación ejecutable y cumplir RNF-07.1 (cobertura ≥80%). Se necesita decidir la pirámide de testing, herramientas y estrategia de mocks.

---

## Decisión

**Pirámide de testing:**

```
        ⬆️  E2E (Playwright, 10%)
      ⬆️⬆️  Integración (pytest + DB real, 20%)
    ⬆️⬆️⬆️  Unitarios (pytest puro, 70%)
```

| Tipo | Herramienta | Qué testea | Cobertura |
|:-----|:------------|:-----------|:---------:|
| Unitarios | pytest | Dominio y casos de uso en aislamiento | 70% |
| Integración | pytest + SQLite real | Repositorios, endpoints, auth | 20% |
| E2E | Playwright (futuro) | Flujos completos en el navegador | 10% |

**Estrategia de mocks:**
- Tests unitarios: repositorio en memoria (dict), no mock.
- Tests de integración: SQLite en memoria (`:memory:`), no mock. Base real, transacciones rollback.
- Nunca mockear el dominio.

---

## Alternativas consideradas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| Solo tests E2E | Lentos, frágiles, no cubren casos borde. La pirámide de testing existe por algo. |
| Mockear todo | Tests que pasan en verde pero no prueban nada real. Falsos positivos. |
| unittest (built-in) | pytest es más legible, tiene fixtures, parametrize y mejor ecosistema. |

---

## Consecuencias

**Positivas:**
- Tests unitarios rápidos (< 1s). Feedback inmediato.
- SQLite en memoria para integración: rápido, no requiere instalar PostgreSQL.
- El dominio se testea sin DB. Los tests son documentación ejecutable de las reglas de negocio.

**Negativas:**
- SQLite no es idéntico a PostgreSQL. Diferencias sutiles pueden escaparse en tests.
- Playwright requiere navegador instalado. Se posterga para fase avanzada.
- Cobertura ≥80% es ambiciosa para un proyecto pedagógico inicial.

---

## 🧠 Analogía del @docente

> Testear software es como **revisar un auto antes de salir a la ruta**. Los tests unitarios son revisar cada pieza del motor individualmente (bujía, filtro, aceite). Los tests de integración son prender el motor y ver que todo funcione junto. Los tests E2E son manejar el auto por una cuadra y volver. Si solo hacés E2E, el auto puede fallar a los 100 km. Si solo hacés unitarios, no sabés si las piezas encajan entre sí.
