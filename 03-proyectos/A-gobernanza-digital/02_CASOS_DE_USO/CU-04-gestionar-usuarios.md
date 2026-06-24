# CU-04: Gestionar Usuarios

**Formato:** Cockburn | **Nivel:** Usuario | **Prioridad:** Alta

---

## Actor principal
Admin Técnico

## Precondición
- Usuario autenticado con rol `admin_tecnico`

## Flujo principal

1. El admin técnico ingresa a "Gestión de Usuarios"
2. Ve listado de usuarios con: email, nombre, rol, fecha de registro
3. Puede:
   - **Crear usuario:** email, nombre, contraseña temporal, rol
   - **Cambiar rol:** modifica el rol de un usuario existente
   - **Desactivar:** deshabilita un usuario sin eliminarlo

## Reglas de negocio

- Solo `admin_tecnico` puede crear usuarios con rol `admin_tecnico` o `directivo`
- Un email no puede estar duplicado
- La contraseña temporal se envía por email y expira en 24 horas
- Al cambiar de rol, el usuario debe volver a iniciar sesión

## Postcondición
- Usuario creado/modificado/desactivado
- Email de notificación enviado si aplica
- Auditoría registrada
