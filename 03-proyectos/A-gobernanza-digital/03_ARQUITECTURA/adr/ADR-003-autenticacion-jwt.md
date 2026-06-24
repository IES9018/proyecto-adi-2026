# ADR-003: Autenticación con JWT + OAuth2

**Estado:** Aceptado | **Fecha:** Junio 2026 | **Autor:** Agente Arquitecto

---

## Contexto

El sistema tiene 3 roles (solicitante, admin técnico, directivo) y endpoints protegidos. Necesitamos un mecanismo de autenticación que:
- Sea stateless (no requiera sesiones en el servidor)
- Funcione con una API REST
- Permita distinguir roles para autorización
- Sea seguro según los requisitos del [Doc 02](https://github.com/IES9018/gobernanza-servicios-digitales/blob/main/docs/02_EVALUACION_TECNICA.md)

---

## Decisión

Usar **JWT (JSON Web Tokens) con OAuth2PasswordBearer** siguiendo el estándar de FastAPI.

### Esquema

```
POST /auth/login  →  { access_token, refresh_token, token_type }
Authorization: Bearer <access_token>
```

| Token | Duración | Uso |
|:------|:---------|:----|
| Access token | 30 minutos | Autentica cada request |
| Refresh token | 7 días | Renueva el access token sin volver a loguearse |

### Almacenamiento

- Access token: en memoria del frontend (no en localStorage — vulnerable a XSS)
- Refresh token: en cookie HttpOnly, Secure, SameSite=Strict

### Roles en el token

```json
{
  "sub": "usuario@ies9018.edu.ar",
  "rol": "admin_tecnico",
  "exp": 1719000000
}
```

---

## Alternativas consideradas

| Alternativa | ¿Por qué no? |
|:------------|:-------------|
| Sesiones con cookies | Stateful. Requiere almacenar sesiones en el servidor. No escala con múltiples instancias. |
| API Keys | Sin expiración, sin granularidad de roles. Mejor para machine-to-machine. |
| OAuth2 social (Google, GitHub) | Agrega dependencia externa. El servidor escolar puede no tener acceso a internet o estar detrás de un firewall. |
| Basic Auth | Las credenciales viajan en cada request. Sin expiración. Obsoleto para aplicaciones web. |

---

## Consecuencias

**Positivas:**
- Stateless: el servidor no almacena sesiones. Cada request es autónomo.
- Estándar de industria. Los estudiantes aprenden lo que se usa en el mercado.
- FastAPI tiene soporte nativo para OAuth2PasswordBearer + JWT.

**Negativas:**
- Los tokens no se pueden revocar individualmente (solución: lista negra en Redis, o rotación de secret key).
- El refresh token en cookie agrega complejidad en el frontend.
- Si el access token se filtra, el atacante tiene 30 minutos de acceso.

---

## 🧠 Analogía del @docente

> JWT es como una **pulsera de un festival**. Cuando entrás al predio, mostrás tu DNI (login), y te dan una pulsera (access token). Durante todo el día, los guardias solo miran tu pulsera para dejarte pasar a cada escenario (endpoint). No te piden el DNI cada vez. Si la pulsera se rompe (expira), vas a la carpa de acreditaciones con tu entrada original (refresh token) y te dan una pulsera nueva. Si alguien te roba la pulsera, solo puede usarla hasta que termine el día (30 minutos). Mañana ya no sirve.
