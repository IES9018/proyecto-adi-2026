# 📅 Cronograma Integral de TPs y Sprints — Ciclo 2026

> **Fuente de verdad del calendario ADI + PP3** · Prof. Paulo Alvarez · Última actualización: 25 ago 2026
> Clases nocturnas · ADI: **martes** (última clase jue 19/11) · PP3: **lunes + jueves** (cierre mar 17/11)

---

## Filosofía de cadencia

* **1 TP cada 2 semanas (quincenal)** en ADI. Cada TP implica el ciclo completo *rama → PR → checklists → self-merge → auditoría docente*: la quincena es la unidad mínima que permite auditar 15 repos con calidad.
* El **TP N se publica el día que se entrega el TP N−1** (lo ves en clase, lo empezás esa noche).
* Cada TP de ADI produce exactamente lo que el sprint vigente de PP3 necesita.

## 🗓️ Calendario ADI (martes)

| TP | Unidad / Tema | Se publica (mar) | **Entrega (mar)** |
|---|---|---|---|
| **TP1** SDD + Arnés *(publicado)* | U1 | 24 ago ✅ | **15 sep** |
| **TP2** Arquitectura Visible (C4 + ADR-002/003) | U2 | 15 sep | **29 sep** |
| **TP3** Diseño de Interfaces (HCI) | U3 | 29 sep | **13 oct** |
| **TP4** Contratos API-First + Web segura | U4 | 13 oct | **27 oct** |
| **TP5** Estrategia Mobile medible | U5 | 27 oct | **10 nov** |
| **TP6** CI, Releases y Postmortem | U6 | 10 nov | **17 nov** |
| **Integrador Final** — defensa del repo | transversal | continuo | **jue 19 nov** |

## 🗓️ Calendario PP3 (lunes + jueves)

| Sprint | Período | Entregable estrella | Entrega |
|---|---|---|---|
| **S1** *(vigente)* | 24 ago – 18 sep | SPEC + arnés + `auditoria-sprint1` | jue **17 sep** |
| **S2** | 21 sep – 16 oct | Núcleo funcional + tests | jue **15 oct** |
| **S3** | 19 oct – 13 nov | Seguridad + despliegue | jue **12 nov** |
| **Cierre** | hasta 17 nov | Informe final + demo | mar **17 nov** |

## 🔗 Mapa de sinergia ADI → PP3

| TP ADI | Insumo que produce | Sprint PP3 que lo consume |
|---|---|---|
| TP1 | SPEC + arnés v1 | S1 (entregables DEL-S1-01..03) |
| TP2 | Diagramas C4 + ADRs | S2 (`DIAGRAMAS_REFERENCIA`) |
| TP3 | Personas, wireframes, accesibilidad AA | S2 (UI del núcleo) |
| TP4 | OpenAPI + threat model lite | S2 testing · área Seguridad (15%) |
| TP5 | RNF medibles + presupuestos | S3 (verificación al desplegar) |
| TP6 | Pipeline CI + release v0.1.0 + postmortem | S3 despliegue · Testing (20%) · informes |
| Integrador | Defensa integral | Cierre 17 nov |

## 🚦 Estrategia de publicación

Las consignas completas se publican en este repo **el día de apertura de cada TP** (rama `main`, commit `docs: abrir TP N`). Antes de esa fecha existen como borradores internos de cátedra. La fila "TP vigente" del [README principal](../README.md) se actualiza en cada apertura.
