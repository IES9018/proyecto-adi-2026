# Flujo de Navegación — Gobernanza Digital

```mermaid
graph TD
    HOME["/ (público)"] --> CATALOGO["/catalogo"]
    HOME --> LOGIN["/login"]

    LOGIN -->|"rol: solicitante"| DASH_SOL["/panel/solicitante"]
    LOGIN -->|"rol: admin_tecnico"| DASH_ADMIN["/panel/admin"]
    LOGIN -->|"rol: directivo"| DASH_DIR["/panel/directivo"]

    DASH_SOL --> NUEVA["/solicitudes/nueva"]
    DASH_SOL --> VER_SOL["/solicitudes/:id"]

    DASH_ADMIN --> LISTA_PEND["/solicitudes?estado=pendiente_tecnica"]
    DASH_ADMIN --> EVALUAR["/solicitudes/:id/evaluar"]
    DASH_ADMIN --> USUARIOS["/admin/usuarios"]
    DASH_ADMIN --> CATALOGO

    DASH_DIR --> RESOLVER["/solicitudes/:id/resolver"]

    subgraph "Rutas protegidas (requieren JWT)"
        DASH_SOL
        DASH_ADMIN
        DASH_DIR
        NUEVA
        VER_SOL
        LISTA_PEND
        EVALUAR
        USUARIOS
        RESOLVER
    end

    subgraph "Rutas públicas"
        HOME
        CATALOGO
        LOGIN
    end
```

**Reglas de navegación:**
- `/catalogo`: acceso público, sin login
- `/login`: acceso público, redirige según rol
- `/panel/*`: requiere JWT válido, redirige según rol
- Si un usuario con rol `solicitante` intenta acceder a `/panel/admin`, recibe 403
