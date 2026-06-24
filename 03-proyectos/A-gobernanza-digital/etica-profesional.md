# Ética Profesional en el Desarrollo de Software

> **Agente:** @docente | **Fecha:** Junio 2026

---

## 🧠 Analogía del @docente

> Construir software es como **construir un edificio**. El código es la estructura, los tests son las inspecciones de obra, los ADRs son los planos aprobados. Pero hay algo más importante que los ladrillos: **quién firma los planos**. Si vos firmás un plano que no hiciste, el edificio se cae y la culpa es tuya. Si alguien firma tus planos sin tu permiso, te roba el crédito. La ética profesional es saber cuándo poner tu firma y cuándo decir "esto no lo hice yo".

---

## Principios

### 1. Autoría transparente

Cada commit tiene un autor. Cada PR tiene un responsable. Cada ADR tiene quien lo escribió. Si usaste IA para generar código, está bien — siempre que lo entiendas, lo revises y te hagas responsable de cada línea.

**No hagas:**
- Commitear código generado por IA sin leerlo
- Presentar como propio un proyecto construido íntegramente por otra persona
- Borrar el historial de Git para ocultar la autoría real

**Sí hacé:**
- Revisar cada línea antes de commitear
- Documentar las decisiones en ADRs con tu nombre
- Mantener un historial de Git limpio y honesto

### 2. Código abierto y licencias

Todo proyecto alojado en el servidor escolar requiere repositorio público y licencia compatible con uso educativo (MIT, GPL, Apache 2.0). Esto garantiza:

- Transparencia con la comunidad educativa
- Posibilidad de auditoría
- Que otros estudiantes puedan aprender de tu código
- Que tu trabajo sea parte de tu portfolio profesional

**El dominio y subdominios son propiedad del IES.** El nombre `ies9018malargue.edu.ar` representa a la institución. Lo que publiques bajo ese dominio habla de la escuela tanto como de vos.

### 3. Responsabilidad sobre los datos

Si tu sistema almacena datos de personas reales:
- Avisá qué datos guardás y por qué
- No compartas datos con terceros sin consentimiento
- Borrá los datos cuando ya no sean necesarios
- Protegé el acceso con autenticación y autorización

### 4. Seguridad como práctica, no como adorno

La seguridad no es una feature que se agrega al final. Es parte del diseño desde el día 1:
- Contraseñas hasheadas, nunca en texto plano
- HTTPS siempre
- Variables de entorno para secretos
- Validación de inputs del lado del servidor (nunca confíes en el frontend)

### 5. Contribución a la comunidad

El software que construís en la tecnicatura no es solo para aprobar una materia:

- **Es tu portfolio.** Cuando busques trabajo, van a mirar tu GitHub.
- **Es tu carta de presentación.** Un proyecto bien documentado, con tests y ADRs, habla más que 10 páginas de CV.
- **Es tu legado.** Otros estudiantes van a aprender de tu código, como vos aprendiste del de otros.

---

## 📋 Checklist ético antes de deployar

- [ ] ¿El repositorio es público y tiene licencia MIT/GPL/Apache?
- [ ] ¿Todas las decisiones están documentadas en ADRs?
- [ ] ¿Los commits tienen autoría clara (no `root`, no `admin`)?
- [ ] ¿Las contraseñas y secretos están en variables de entorno, no en el código?
- [ ] ¿El código que no es mío está correctamente atribuido?
- [ ] ¿Los datos de usuarios reales están protegidos?
- [ ] ¿El README explica claramente qué hace el sistema y quién lo hizo?

---

## 🎓 Para tu portfolio y LinkedIn

Cuando termines tu proyecto:

1. **Subilo a tu GitHub personal** (público, con README completo)
2. **Agregalo a LinkedIn** en la sección de proyectos
3. **Escribí un post** contando qué problema resuelve tu sistema y qué aprendiste
4. **Compartí el link** en las issues del repo de la materia para que otros lo vean

> *"Tu GitHub es tu nuevo CV. Cada commit es una línea. Cada PR es una recomendación. Cada proyecto es una experiencia comprobable."*
