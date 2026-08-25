# TP N° 4: Contratos Antes que Código — API-First y Web Segura

> 📅 **Se publica:** mar 13 oct · **Entrega:** mar 27 oct · 🧠 Teoría: [Unidad 4 — Arquitectura Web](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-4-arquitectura-web)

> 🧭 **¿Llegaste directo acá?** Volvé al [README principal](https://github.com/IES9018/proyecto-adi-2026#readme). Prerrequisito: **TP3 mergeado**.

---

## 💡 Por qué este TP

El error clásico del vibe coding web: la IA inventa endpoints sobre la marcha, el front consume lo que sea, y nadie sabe qué contrato hay entre ambos. Acá invertís el orden: **primero el contrato (OpenAPI), después la implementación**. De paso hacés tu primera mirada seria a seguridad — no un checklist decorativo, sino un mini modelo de amenazas sobre TUS endpoints reales, con mitigaciones concretas que luego tu arnés va a exigir.

## 🎯 Qué vas a lograr

Tu sistema tiene su **API definida en OpenAPI** antes de existir, una **decisión de estrategia web documentada**, un **modelo de amenazas liviano** con mitigaciones, y un arnés que ya prohíbe los errores web más comunes.

---

## ✅ Entregables

### 1. Contrato OpenAPI — `docs/arquitectura/api-contracts.yaml`
Especificación OpenAPI 3.x con los **5 endpoints críticos** de tu SPEC v3:
* Path, método, parámetros, cuerpo request/response con schemas, códigos de error (400/401/404/500 mínimo).
* Autenticación declarada (`securitySchemes`) aunque sea JWT básico.
* Validación obligatoria: el archivo tiene que pasar un linter (ej.: `npx @redocly/cli lint`). Incluí el comando en el README de `docs/arquitectura/`.

### 2. ADR-005 — Estrategia web · `docs/adr/ADR-005-estrategia-web.md`
SPA vs. SSR vs. MPA vs. solo-API+front-existente. Alternativas descartadas con criterios: SEO necesario?, complejidad de estado, hosting objetivo de PP3, tamaño del equipo.

### 3. Modelo de amenazas lite — `docs/seguridad/threat-model-lite.md`
Tabla STRIDE simplificada sobre tus 5 endpoints:
* Mínimo **5 amenazas concretas** (inyección, auth rota, exposición de datos, IDOR, rate-limit ausente…).
* Columna mitigación **referenciando dónde se aplica** (endpoint, capa, o regla de arnés).

### 4. Arnés v3 — reglas de seguridad operativas
Agregá a `.opencoderules`, como mínimo:

```text
- PROHIBIDO hardcodear secrets, tokens o credenciales (usar variables de entorno).
- OBLIGATORIO validar y sanear toda entrada externa en el borde del sistema.
- OBLIGATORIO: todo endpoint nuevo debe estar en api-contracts.yaml ANTES de implementarse.
```

### 5. SPEC v4
* Los contratos de datos ahora **referencian** los schemas de `api-contracts.yaml` por nombre.
* Changelog v3→v4.

---

## 📮 Entrega

```bash
git checkout -b feature/tp4-api-first
git add docs/arquitectura docs/seguridad docs/adr SPEC.md .opencoderules
git commit -m "feat: openapi, adr-005, threat model y arnes seguro"
git push -u origin feature/tp4-api-first
```

PR → checklists → self-merge → auditoría docente posterior.

## ✅ Checklist antes del PR

- [ ] `api-contracts.yaml` pasa el linter sin errores
- [ ] Los 5 endpoints cubren los flujos críticos de tus journeys del TP3
- [ ] ADR-005 con alternativas descartadas y criterios objetivos
- [ ] Threat model: ≥5 amenazas con mitigación ubicable (no "usar buenas prácticas")
- [ ] Arnés con las 3 reglas nuevas
- [ ] SPEC v4 referencia los schemas + changelog

## 🔗 Conexión con PP3

El **Sprint 2** implementa y testea contra estos contratos; el threat model alimenta directamente el área **Seguridad (15%)** de la evaluación.

## ❓ FAQ

**¿Puedo cambiar un endpoint después?** Sí: primero cambiás el contrato (PR), después la implementación. El contrato es la fuente; nunca al revés.
**¿GraphQL en vez de REST?** Posible, pero entonces tu "contrato" es el schema SDL con la misma exigencia de lint. Documentalo en ADR-005.
