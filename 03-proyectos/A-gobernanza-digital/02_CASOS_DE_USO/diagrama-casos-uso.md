# Diagrama de Casos de Uso — Gobernanza Digital

```mermaid
graph TD
    SOL[👤 Solicitante]
    AT[👤 Admin Técnico]
    DIR[👤 Directivo]
    PUB[👤 Público]

    subgraph "Sistema Gobernanza Digital"
        CU1[CU-01: Solicitar Alojamiento]
        CU2[CU-02: Evaluar Técnicamente]
        CU3[CU-03: Emitir Resolución]
        CU4[CU-04: Gestionar Usuarios]
        CU5[CU-05: Catálogo Público]
        CU6[Ver Estado de Solicitudes]
        CU7[Suspender Servicio]
    end

    SOL --> CU1
    SOL --> CU6
    AT --> CU2
    AT --> CU4
    AT --> CU7
    DIR --> CU3
    DIR --> CU6
    PUB --> CU5
```

| CU | Actor | Complejidad |
|:---|:------|:-----------:|
| CU-01 | Solicitante | Media |
| CU-02 | Admin Técnico | Media |
| CU-03 | Directivo | Baja |
| CU-04 | Admin Técnico | Baja |
| CU-05 | Público | Baja |
| CU-06 | Solicitante, Directivo | Baja |
| CU-07 | Admin Técnico | Baja |
