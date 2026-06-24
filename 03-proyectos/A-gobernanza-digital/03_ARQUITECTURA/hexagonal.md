# Arquitectura Hexagonal — Gobernanza Digital

> Documentación de la estructura hexagonal del proyecto.

---

## Regla de dependencia

```
  ┌──────────────────────────────────────┐
  │          infrastructure/             │
  │  ┌────────────────────────────────┐  │
  │  │        web/ (FastAPI)          │  │
  │  │  ┌──────────────────────────┐  │  │
  │  │  │    application/          │  │  │
  │  │  │  ┌────────────────────┐  │  │  │
  │  │  │  │    domain/        │  │  │  │
  │  │  │  │  • models/       │  │  │  │
  │  │  │  │  • ports/        │  │  │  │
  │  │  │  └────────────────────┘  │  │  │
  │  │  └──────────────────────────┘  │  │
  │  └────────────────────────────────┘  │
  └──────────────────────────────────────┘

  Las flechas de dependencia apuntan HACIA ADENTRO.
  domain/ no importa nada externo.
```

---

## Capas detalladas

### `domain/` — El núcleo

```python
# domain/models/solicitud.py
from dataclasses import dataclass
from enum import Enum

class EstadoSolicitud(Enum):
    BORRADOR = "borrador"
    PENDIENTE_TECNICA = "pendiente_tecnica"
    PENDIENTE_INSTITUCIONAL = "pendiente_institucional"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"
    SUSPENDIDA = "suspendida"

@dataclass
class Solicitud:
    id: str
    proyecto: str
    nivel: int
    subdominio: str
    solicitante_email: str
    estado: EstadoSolicitud
    # ... resto de campos del Doc 01
```

```python
# domain/ports/repositories.py
from abc import ABC, abstractmethod

class SolicitudRepository(ABC):
    @abstractmethod
    def guardar(self, solicitud: Solicitud) -> None: ...
    @abstractmethod
    def buscar_por_id(self, id: str) -> Solicitud | None: ...
    @abstractmethod
    def listar_por_solicitante(self, email: str) -> list[Solicitud]: ...
    @abstractmethod
    def listar_todas(self) -> list[Solicitud]: ...
```

### `application/` — Casos de uso

```python
# application/crear_solicitud.py
class CrearSolicitud:
    def __init__(self, repo: SolicitudRepository):
        self.repo = repo  # Inyección de dependencia

    def ejecutar(self, datos: dict) -> Solicitud:
        solicitud = Solicitud(
            id=generar_id(),
            estado=EstadoSolicitud.PENDIENTE_TECNICA,
            **datos
        )
        self.repo.guardar(solicitud)
        return solicitud
```

### `infrastructure/` — Adaptadores concretos

```python
# infrastructure/db/solicitud_repo_sql.py
class SolicitudRepositorySQL(SolicitudRepository):
    def __init__(self, session: Session):
        self.session = session

    def guardar(self, solicitud: Solicitud) -> None:
        orm = SolicitudORM.from_domain(solicitud)
        self.session.add(orm)
        self.session.commit()
```

### `web/` — Capa HTTP

```python
# web/api/routes/solicitudes.py
@router.post("/solicitudes")
def crear_solicitud(
    datos: SolicitudCreate,
    usuario: User = Depends(get_current_user),
    caso_uso: CrearSolicitud = Depends(get_crear_solicitud),
):
    solicitud = caso_uso.ejecutar(datos.dict())
    return solicitud
```

---

## Beneficios en este proyecto

| Beneficio | Ejemplo concreto |
|:----------|:-----------------|
| **Cambiar DB sin tocar dominio** | `DATABASE_URL=sqlite:///` → `DATABASE_URL=postgresql://...` |
| **Testear dominio sin DB** | `test_crear_solicitud.py` usa un repo en memoria |
| **Cambiar email sin tocar negocio** | SMTP en prod, `print()` en consola para desarrollo |
| **Agregar frontend alternativo** | La API no sabe si la consume React o un script CLI |

---

## 🧠 Analogía del @docente

> La arquitectura hexagonal es como un **cargador USB-C**. Tu celular (el dominio) no sabe si está enchufado a la pared, a la computadora, a una batería externa o a un auto. Solo recibe energía por el puerto. Cambiar la fuente de energía (infraestructura) no requiere cambiar el celular. Ese nivel de desacople es lo que buscamos en cada capa del proyecto.
