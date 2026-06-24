# Requisitos No Funcionales — Gobernanza Digital

> **Fuente:** [IES9018/gobernanza-servicios-digitales](https://github.com/IES9018/gobernanza-servicios-digitales)
> **Agente:** Analista | **Fecha:** Junio 2026

---

## RNF-01: Seguridad

| ID | Requisito | Prioridad | Fuente |
|:---|:----------|:---------:|:-------|
| RNF-01.1 | Todas las conexiones deben ser sobre HTTPS | Alta | [Doc 02 §4] |
| RNF-01.2 | Contraseñas almacenadas con bcrypt o argon2 (nunca texto plano, nunca MD5) | Alta | [Doc 02 §4] |
| RNF-01.3 | Credenciales y secretos en variables de entorno, nunca hardcodeadas | Alta | [Doc 02 §4] |
| RNF-01.4 | Backend bindea a 127.0.0.1, no a 0.0.0.0 (solo Nginx expone al exterior) | Alta | [Doc 02 §4] |
| RNF-01.5 | Headers de seguridad: CSP, X-Frame-Options, X-Content-Type-Options | Alta | [Doc 02 §4] |
| RNF-01.6 | CORS restringido a orígenes específicos (no `allow_origins=["*"]`) | Alta | [Doc 02 §4] |
| RNF-01.7 | Rate limiting en endpoints de login (5 intentos por minuto) | Media | OWASP |
| RNF-01.8 | Tokens JWT con expiración (access: 30 min, refresh: 7 días) | Alta | [Doc 02 §4] |
| RNF-01.9 | Consultas SQL parametrizadas para prevenir inyección | Alta | [Doc 02 §4] |
| RNF-01.10 | Validación de inputs con Pydantic en backend + validación en frontend | Alta | Defensa en profundidad |

---

## RNF-02: Disponibilidad y SLA

| ID | Requisito | Nivel | Fuente |
|:---|:----------|:------|:------|
| RNF-02.1 | El sistema debe estar disponible en horario escolar (lunes a viernes, 8-22h) | Todos | [Doc 06] |
| RNF-02.2 | Sin garantía de uptime (servidor escolar, no servicio comercial) | Todos | [Doc 06] |
| RNF-02.3 | Backup de base de datos diario (automático, 3AM) | Todos | [Doc 02 §5] |
| RNF-02.4 | Plan de contingencia: si el servidor cae, el sistema se reinicia con Docker | Todos | [Doc 11] |
| RNF-02.5 | Tiempo máximo de inactividad planificada: 2 horas (con aviso 48h antes) | N2, N3 | [Doc 06] |

---

## RNF-03: Rendimiento

| ID | Requisito | Prioridad |
|:---|:----------|:---------:|
| RNF-03.1 | Tiempo de respuesta < 500ms para endpoints CRUD | Media |
| RNF-03.2 | Soportar hasta 50 usuarios concurrentes (escala de la institución) | Media |
| RNF-03.3 | Listado del catálogo paginado (20 servicios por página) | Baja |

---

## RNF-04: Usabilidad

| ID | Requisito | Prioridad |
|:---|:----------|:---------:|
| RNF-04.1 | Interfaz responsive (funciona en celular, tablet y desktop) | Alta |
| RNF-04.2 | Formulario de solicitud con guardado automático de borrador | Media |
| RNF-04.3 | Mensajes de error claros en español (no "500 Internal Server Error") | Alta |
| RNF-04.4 | Feedback visual al guardar, enviar o cambiar estado | Media |

---

## RNF-05: Transparencia y auditoría

| ID | Requisito | Prioridad | Fuente |
|:---|:----------|:---------:|:-------|
| RNF-05.1 | Todo cambio de estado debe quedar registrado con timestamp, usuario y rol | Alta | [Doc 09] |
| RNF-05.2 | Los logs no deben contener datos personales ni contraseñas | Alta | [Doc 09] |
| RNF-05.3 | El catálogo público debe mostrar servicios activos sin requerir autenticación | Alta | [Doc 12] |
| RNF-05.4 | Cualquier miembro de la comunidad puede auditar las políticas públicas | Media | [Doc 12] |

---

## RNF-06: Infraestructura y despliegue

| ID | Requisito | Prioridad |
|:---|:----------|:---------:|
| RNF-06.1 | Backend y frontend dockerizados (Dockerfile + docker-compose) | Alta |
| RNF-06.2 | Variables de entorno documentadas en `.env.example` (sin valores reales) | Alta |
| RNF-06.3 | CI/CD con GitHub Actions: lint + test en cada push a main | Alta |
| RNF-06.4 | Despliegue en servidor Debian 12 con Nginx como reverse proxy | Alta |
| RNF-06.5 | El servidor debe mantener un fork del repositorio del proyecto desplegado | Media |

---

## RNF-07: Mantenibilidad

| ID | Requisito | Prioridad |
|:---|:----------|:---------:|
| RNF-07.1 | Cobertura de tests ≥ 80% en backend | Alta |
| RNF-07.2 | Código documentado con docstrings en funciones públicas | Media |
| RNF-07.3 | Linting automático con ruff + mypy en CI | Alta |
| RNF-07.4 | Conventional Commits para todos los mensajes de commit | Alta |

---

## RNF-08: Legales y ética

| ID | Requisito | Prioridad | Fuente |
|:---|:----------|:---------:|:-------|
| RNF-08.1 | El sistema debe mostrar el descargo de responsabilidad institucional | Alta | [Doc 00 §2] |
| RNF-08.2 | Debe quedar claro que el IES no aprueba ni supervisa contenidos | Alta | [Doc 04] |
| RNF-08.3 | El responsable del proyecto debe aceptar la declaración de responsabilidad | Alta | [Doc 04] |
| RNF-08.4 | El dominio y subdominios son propiedad del IES, revocables en cualquier momento | Alta | [Doc 00 §3] |
