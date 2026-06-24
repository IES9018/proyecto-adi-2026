# Entidades — Gobernanza Digital

**Agente:** Modelador

---

## Usuario

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `email` | String(255) | PK, formato email, único |
| `nombre` | String(200) | Not null |
| `password_hash` | String(255) | Not null, bcrypt |
| `rol` | Enum | `solicitante`, `admin_tecnico`, `directivo` |
| `creado_en` | DateTime | Auto now |

**Reglas:**
- Solo `admin_tecnico` puede crear usuarios con rol `admin_tecnico` o `directivo`
- Un email no puede tener más de un rol
- La contraseña se hashea con bcrypt antes de persistir

---

## Solicitud

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `id` | String(36) | PK, UUID4 |
| `proyecto` | String(200) | Not null |
| `nivel` | Integer | 1, 2 o 3 |
| `subdominio` | String(100) | Not null, sin el dominio base |
| `descripcion` | Text | Not null |
| `objetivo_educativo` | Text | Not null |
| `arquitectura` | String(50) | `monolitica`, `microservicios`, `capas`, `hexagonal` |
| `justificacion_arquitectura` | Text | Obligatorio para alumnos |
| `patron_diseno` | String(100) | Ej: `MVC`, `Repository` |
| `url_repositorio` | String(500) | Debe ser URL válida de GitHub |
| `licencia` | String(50) | `MIT`, `GPL-3.0`, `Apache-2.0`, etc. |
| `lenguajes` | String(500) | Ej: `Python, TypeScript` |
| `frameworks` | String(500) | Ej: `FastAPI, React` |
| `base_datos` | String(100) | Ej: `PostgreSQL` |
| `puertos` | String(200) | Ej: `8000, 3000` |
| `acceso_publico` | Boolean | Default false |
| `autenticacion` | String(100) | `JWT`, `OAuth2`, `ninguna` |
| `roles_usuario` | String(500) | Ej: `admin, operador, cliente` |
| `datos_personales` | Boolean | Default false |
| `contenido_usuarios` | Boolean | Default false |
| `estado` | Enum | `borrador`, `pendiente_tecnica`, `pendiente_institucional`, `aprobada`, `rechazada`, `suspendida` |
| `solicitante_email` | String(255) | FK → Usuario |
| `creada_en` | DateTime | Auto now |
| `actualizada_en` | DateTime | Auto now |

---

## Evaluación Técnica

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `id` | String(36) | PK, UUID4 |
| `solicitud_id` | String(36) | FK → Solicitud, único |
| `evaluador_email` | String(255) | FK → Usuario |
| `repo_publico` | Boolean | |
| `licencia_compatible` | Boolean | |
| `https_configurado` | Boolean | |
| `hash_contraseñas` | Boolean | |
| `vars_entorno` | Boolean | |
| `puerto_localhost` | Boolean | |
| `headers_seguridad` | Boolean | |
| `dockerizado` | Boolean | |
| `logs_configurados` | Boolean | |
| `backup_definido` | Boolean | |
| `dictamen` | Enum | `apto`, `condicional`, `no_apto` |
| `observaciones` | Text | |
| `fecha` | DateTime | Auto now |

---

## Evaluación Institucional

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `id` | String(36) | PK, UUID4 |
| `solicitud_id` | String(36) | FK → Solicitud, único |
| `evaluador_email` | String(255) | FK → Usuario |
| `alineacion_educativa` | Boolean | |
| `contribucion_perfil` | Boolean | |
| `riesgo_institucional` | Boolean | |
| `dictamen` | Enum | `favorable`, `desfavorable`, `condicional` |
| `observaciones` | Text | |
| `fecha` | DateTime | Auto now |

---

## Resolución

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `id` | String(36) | PK, UUID4 |
| `solicitud_id` | String(36) | FK → Solicitud, único |
| `numero` | String(30) | Único, formato `RES-YYYY-NNN` |
| `decision` | Enum | `aprobada`, `rechazada` |
| `fundamentos` | Text | Not null |
| `condiciones` | Text | Nullable |
| `fecha` | DateTime | Auto now |

---

## Auditoría

| Atributo | Tipo | Restricciones |
|:---------|:-----|:--------------|
| `id` | String(36) | PK, UUID4 |
| `solicitud_id` | String(36) | FK → Solicitud |
| `usuario_email` | String(255) | Quién hizo el cambio |
| `rol` | String(50) | Rol del usuario al momento del cambio |
| `campo_modificado` | String(100) | Nombre del campo |
| `valor_anterior` | Text | Nullable (si es creación) |
| `valor_nuevo` | Text | |
| `timestamp` | DateTime | Auto now |
