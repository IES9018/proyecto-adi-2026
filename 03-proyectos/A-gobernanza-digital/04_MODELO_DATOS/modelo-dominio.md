# Modelo de Dominio — Gobernanza Digital

**Agente:** Modelador | **Fecha:** Junio 2026

---

## Entidades principales

```mermaid
erDiagram
    Usuario ||--o{ Solicitud : "crea"
    Usuario ||--o{ EvaluacionTecnica : "realiza"
    Usuario ||--o{ EvaluacionInstitucional : "realiza"
    Solicitud ||--|| EvaluacionTecnica : "tiene"
    Solicitud ||--o| EvaluacionInstitucional : "tiene"
    Solicitud ||--o| Resolucion : "recibe"
    Solicitud ||--o{ Auditoria : "registra"

    Usuario {
        string email PK
        string nombre
        string password_hash
        enum rol "solicitante | admin_tecnico | directivo"
    }

    Solicitud {
        string id PK
        string proyecto
        int nivel "1 2 3"
        string subdominio
        string descripcion
        string objetivo_educativo
        string arquitectura
        string url_repositorio
        string licencia
        string lenguajes
        enum estado "borrador | pendiente_tecnica | pendiente_institucional | aprobada | rechazada | suspendida"
        string solicitante_email FK
        datetime creada
        datetime actualizada
    }

    EvaluacionTecnica {
        string id PK
        string solicitud_id FK
        string evaluador_email FK
        boolean repo_publico
        boolean licencia_compatible
        boolean https_configurado
        boolean hash_contraseñas
        boolean vars_entorno
        boolean puerto_localhost
        boolean dockerizado
        boolean logs_configurados
        enum dictamen "apto | condicional | no_apto"
        string observaciones
        datetime fecha
    }

    EvaluacionInstitucional {
        string id PK
        string solicitud_id FK
        string evaluador_email FK
        boolean alineacion_educativa
        boolean contribucion_perfil
        boolean riesgo_institucional
        enum dictamen "favorable | desfavorable | condicional"
        string observaciones
        datetime fecha
    }

    Resolucion {
        string id PK
        string solicitud_id FK
        string numero "RES-2026-001"
        enum decision "aprobada | rechazada"
        string fundamentos
        string condiciones
        datetime fecha
    }

    Auditoria {
        string id PK
        string solicitud_id FK
        string usuario_email
        string rol
        string campo_modificado
        string valor_anterior
        string valor_nuevo
        datetime timestamp
    }
```

---

## Value Objects

| VO | Campos | Reglas |
|:---|:-------|:-------|
| `Email` | valor: str | Debe contener `@` y un dominio |
| `Subdominio` | nombre: str | Solo letras, números y guiones. Sin `ies9018malargue.edu.ar` |
| `NivelServicio` | valor: int | 1, 2 o 3 |
| `EstadoSolicitud` | valor: str | Enum con 6 valores. Transiciones controladas |

---

## Agregados

**Solicitud** es la raíz de agregado. Contiene:
- `Solicitud` (raíz)
- `EvaluacionTecnica` (parte del agregado)
- `EvaluacionInstitucional` (parte del agregado)
- `Resolucion` (parte del agregado)

Regla: todos los cambios a una solicitud y sus evaluaciones pasan por la raíz del agregado. No se modifica una evaluación directamente sin pasar por la solicitud.

---

## Invariantes de dominio

1. Una solicitud en estado `borrador` no puede ser evaluada
2. Una solicitud `aprobada` no puede volver a `pendiente`
3. Solo `admin_tecnico` puede crear `EvaluacionTecnica`
4. Solo `directivo` puede crear `EvaluacionInstitucional`
5. Toda transición de estado genera un registro de auditoría
6. El subdominio solicitado no puede estar en uso por otro servicio activo

---

## 🧠 Analogía del @docente

> El modelo de dominio es como el **registro civil** de una ciudad. Cada entidad es un acta: nacimiento (solicitud), matrimonio (evaluación), defunción (resolución). Las actas tienen fecha, firma y número único. No podés casar a alguien que no nació (invariante 1), ni des-casar a alguien (invariante 2). Todo queda registrado para siempre (auditoría).
