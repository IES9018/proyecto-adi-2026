# Apéndice Avanzado — Testing de Consistencia y Trazabilidad

> 📅 **Disponible desde:** cualquier momento · **Carácter:** OPCIONAL y AVANZADO
>
> 🧭 **Prerrequisito:** TP6 mergeado, al menos 5 tests pasando, CI verde.
>
> 📖 **Teoría completa:** [Módulo 07 — Testing de Consistencia y Trazabilidad](https://github.com/IES9018/ADI-teoria-y-recursos/tree/main/unidad-6-herramientas-y-tecnologias/07-testing-consistencia-trazabilidad)

---

## 💡 Por qué este desafío

Los tests E2E no son solo "ver si anda". Son una herramienta para **contrastar** tu implementación contra tus propias decisiones: SPEC, ADR, casos de uso, wireframes. Este desafío te enseña a construir una **matriz de trazabilidad** que conecta cada requisito con su prueba y su evidencia, usando Playwright como herramienta.

El objetivo no es cubrir todo con E2E. Es aprender a **seleccionar** qué vale la pena testear, **preparar** datos sintéticos seguros, y **defender** técnicamente tus decisiones ante el profesor.

---

## 🎯 Qué vas a lograr

Al terminar este desafío vas a tener:

1. Una **matriz de trazabilidad** que conecta tu SPEC con tus tests.
2. Un **flujo crítico** testeado con 3 escenarios significativos.
3. **Datos sintéticos** preparados y documentados.
4. Un **reporte de ejecución** con evidencia.
5. Una **inspección humana** de UI/UX documentada.
6. Un **escaneo de secretos** ejecutado y redactado.
7. Un **postmortem** con al menos un desvío detectado (o la constancia de que no hubo inconsistencias).
8. Material preparado para tu **defensa oral**.

---

## ✅ Pasos del desafío

### Paso 1 — Seleccionar un flujo crítico

Elegí **un solo flujo** de tu sistema que cumpla estos criterios:

- Lo usan todos los días (o sería así en producción).
- Si falla, se pierden datos o hay impacto real.
- Tiene al menos 3 pasos.
- Ya está implementado y funcional en local.

**Ejemplos:**
- Login → ver dashboard
- Crear solicitud → confirmar envío
- Registrar usuario → verificar persistencia

Documentá por qué elegiste ese flujo en `docs/testing/flujo-critico.md`.

---

### Paso 2 — Construir la matriz de trazabilidad

Copiá esta plantilla en `docs/testing/matriz-trazabilidad.md` y completala:

```markdown
# Matriz de Trazabilidad — [Nombre del flujo]

| ID | Fuente | Comportamiento esperado | Tipo de prueba | Evidencia | Resultado |
|:---|:-------|:------------------------|:---------------|:----------|:----------|
| RF-XX | SPEC §X.X | [Descripción del comportamiento] | E2E | Trace + reporte | [Pasa/Falla/Parcial/No evaluado] |
| CU-XX.X | Caso de uso | [Descripción del comportamiento] | E2E + humano | Captura | [Pasa/Falla/Parcial] |
| RN-XX | Regla de negocio | [Descripción del comportamiento] | Unitario + integración | Test | [Pasa/Falla] |
| ADR-XXX | ADR | [Decisión técnica] | Integración/revisión | Test API | [No evaluado por E2E] |
```

**Reglas:**
- Cada fila debe tener un oráculo identificado (¿contra qué comparás?).
- No pongas todo como "E2E". Algunas cosas se prueban con unitarios o integración.
- Si algo no se puede evaluar con tu técnica, poné "No evaluado" y explicá por qué.

---

### Paso 3 — Preparar datos sintéticos

Creá un fixture de usuarios para tus tests. Ejemplo:

```javascript
// e2e/fixtures/users.js
const TEST_USERS = {
  solicitante: {
    email: 'solicitante.e2e@example.test',
    password: 'Test1234!',
    name: 'Juan Pérez (E2E)',
    role: 'solicitante',
  },
  tecnico: {
    email: 'tecnico.e2e@example.test',
    password: 'Test1234!',
    name: 'María García (E2E)',
    role: 'tecnico',
  },
  sinPermiso: {
    email: 'sin-permiso.e2e@example.test',
    password: 'Test1234!',
    name: 'Acceso Restringido (E2E)',
    role: 'viewer',
  },
};

module.exports = { TEST_USERS };
```

**Reglas:**
- Usá dominios `.example.test` o `.test`.
- Nunca uses personas reales.
- Documentá en `docs/testing/datos-sinteticos.md` qué usuarios creaste y por qué.

---

### Paso 4 — Implementar los 3 escenarios

> ⚠️ **Nota:** Los ejemplos de código Playwright a continuación son **adaptables no validados**. Fueron redactados como guía pedagógica y no han sido ejecutados contra un sistema real. Adaptalos a tu stack y verificalos en tu entorno antes de presentarlos como evidencia. El piloto real se realizará cuando exista un proyecto con interfaz ejecutable suficiente.

Creá una carpeta `e2e/` en la raíz de tu proyecto con al menos 3 tests:

#### Escenario 1: Happy path (camino feliz)

```javascript
// e2e/flujo-critico.spec.js
const { test, expect } = require('@playwright/test');
const { TEST_USERS } = require('./fixtures/users');

test.describe('Flujo crítico: [nombre del flujo]', () => {

  test('happy path: usuario completa el flujo exitosamente', async ({ page }) => {
    // 1. Navegar al inicio
    await page.goto('/');
    
    // 2. Login
    await page.getByRole('link', { name: 'Iniciar sesión' }).click();
    await page.getByLabel('Correo electrónico').fill(TEST_USERS.solicitante.email);
    await page.getByLabel('Contraseña').fill(TEST_USERS.solicitante.password);
    await page.getByRole('button', { name: 'Entrar' }).click();
    
    // 3. Verificar que está en el dashboard
    await expect(page).toHaveURL('/dashboard');
    await expect(page.getByText('Bienvenido')).toBeVisible();
    
    // 4. [Pasos específicos de tu flujo]
    // ...
    
    // 5. Verificar resultado
    await expect(page.getByText('Operación exitosa')).toBeVisible();
  });

  test('validación: campos obligatorios vacíos muestran error', async ({ page }) => {
    await page.goto('/registro');
    
    // Enviar formulario vacío
    await page.getByRole('button', { name: 'Registrar' }).click();
    
    // Verificar mensajes de error
    await expect(page.getByText('Este campo es obligatorio')).toBeVisible();
  });

  test('control de acceso: usuario sin permiso es redirigido', async ({ page }) => {
    // Login con usuario de bajo permiso
    await page.goto('/login');
    await page.getByLabel('Correo electrónico').fill(TEST_USERS.sinPermiso.email);
    await page.getByLabel('Contraseña').fill(TEST_USERS.sinPermiso.password);
    await page.getByRole('button', { name: 'Entrar' }).click();
    
    // Intentar acceder a zona restringida
    await page.goto('/admin');
    
    // Verificar redirección o mensaje de acceso denegado
    await expect(page).toHaveURL('/dashboard');
    await expect(page.getByText('No tienes permisos')).toBeVisible();
  });

});
```

---

### Paso 5 — Ejecutar y capturar evidencia

```bash
# Ejecutar la suite
npx playwright test

# Ejecutar con UI visible (para inspección humana)
npx playwright test --headed

# Generar reporte HTML
npx playwright show-report
```

Guardá el reporte en `docs/testing/reporte-ejecucion.md` con:
- Fecha y hora de ejecución
- Cantidad de tests pasados/fallidos
- Screenshots de los tests fallidos (Playwright los genera automáticamente)
- Link al trace si hay fallos

---

### Paso 6 — Inspección humana de UI/UX

Abrí tu aplicación en el navegador y hacé una revisión manual. Documentá en `docs/testing/inspeccion-humana.md`:

| Aspecto | Qué revisar | Resultado | Mejora sugerida |
|:--------|:------------|:----------|:----------------|
| **Feedback** | ¿El usuario sabe que su acción fue recibida? | [OK/Problema] | [Descripción] |
| **Claridad** | ¿Los mensajes son comprensibles? | [OK/Problema] | [Descripción] |
| **Orientación** | ¿El usuario sabe qué hacer después? | [OK/Problema] | [Descripción] |
| **Jerarquía** | ¿Los botones principales son más visibles? | [OK/Problema] | [Descripción] |
| **Errores** | ¿Los errores son útiles (no técnicos)? | [OK/Problema] | [Descripción] |
| **Teclado** | ¿Se puede navegar con Tab? | [OK/Problema] | [Descripción] |
| **Progreso** | ¿Las operaciones largas muestran progreso? | [OK/Problema] | [Descripción] |
| **Persistencia** | ¿Los datos se guardan y persisten? | [OK/Problema] | [Descripción] |

Tomá **1-2 capturas deliberadas** (no más) que ilustren hallazgos. Justificá por qué las capturaste.

---

### Paso 7 — Escaneo de secretos

```bash
# Instalar Gitleaks (si no está instalado)
# Windows: scoop install gitleaks
# macOS: brew install gitleaks

# Escaneo del árbol actual
gitleaks detect --source . --verbose --report-path docs/testing/gitleaks-report.json

# Escaneo del historial (opcional, más completo)
gitleaks detect --source . --log-refs --verbose --report-path docs/testing/gitleaks-historial.json
```

Documentá en `docs/testing/escaneo-secretos.md`:
- Cantidad de hallazgos
- Tipo de hallazgo (API key, contraseña, etc.)
- Archivo afectado (sin revelar el valor)
- Acción tomada (corregido, era falso positivo, etc.)

**Nunca** incluyas el valor del secreto en el reporte. Redactá todo.

---

### Paso 8 — Registrar inconsistencias

En `docs/testing/inconsistencias-encontradas.md`, documentá:

```markdown
# Inconsistencias Encontradas

## Inconsistencia 1: [Título]

- **Fuente A:** SPEC §3.1 — "El sistema debe mostrar confirmación al registrar"
- **Fuente B:** Implementación — No muestra mensaje de confirmación
- **Comportamiento observado:** El formulario se limpia sin mostrar feedback
- **Tipo de prueba:** E2E + humano
- **Estado:** Pendiente de decisión
- **Acción:** [Corregir código / Actualizar SPEC / Consultar profesor]

## Inconsistencia 2: [Título]

[Seguir formato...]
```

Si **no encontrás** inconsistencias, escribí:
> "Se ejecutaron los 3 escenarios del flujo crítico. No se encontraron inconsistencias entre la SPEC, los casos de uso y la implementación. La matriz de trazabilidad completa se adjunta en `docs/testing/matriz-trazabilidad.md`."

**Una comparación correctamente ejecutada sin inconsistencias también constituye evidencia válida.**

---

### Paso 9 — Corrección y postmortem

Si encontraste inconsistencias, corregilas y documentá en `docs/testing/postmortem-testing.md`:

| Inconsistencia | Fuente | Corrección | Evidencia |
|:---------------|:-------|:-----------|:----------|
| [Descripción] | [SPEC/ADR/CU] | [Qué se cambió] | [Link a commit o PR] |

---

### Paso 10 — Preparar la defensa

Prepará respuestas a estas preguntas:

1. ¿Por qué elegiste **ese** flujo como crítico?
2. ¿Cuál es el oráculo de cada test? (¿contra qué comparás?)
3. ¿Qué escenarios probaste y por qué esos?
4. ¿Qué datos sintéticos usaste y por qué no podías usar personas reales?
5. ¿Qué encontraste en la inspección humana de UI/UX?
6. ¿Encontraste algún desvío entre lo documentado y lo implementado?
7. ¿Qué parte generó la IA y qué validaste personalmente?
8. ¿Qué harías distinto si empezaras de cero?
9. ¿Qué harías si encontrás un secreto expuesto en tu repo?

---

## 📮 Entrega

```bash
git checkout -b feature/apendice-testing-consistencia
git add docs/testing/ e2e/
git commit -m "feat: testing de consistencia y trazabilidad (desafío avanzado)"
git push -u origin feature/apendice-testing-consistencia
```

### Checklist antes del PR

- [ ] Matriz de trazabilidad completada con oráculos identificados
- [ ] 3 escenarios implementados (happy path, validación, control de acceso)
- [ ] Datos sintéticos documentados
- [ ] Suite ejecutada con reporte
- [ ] Inspección humana documentada con 1-2 capturas justificadas
- [ ] Escaneo de secretos ejecutado (reporte redactado)
- [ ] Inconsistencias registradas (o constancia de que no hubo)
- [ ] Postmortem si hubo correcciones
- [ ] Preguntas de defensa preparadas

---

## 📊 Rúbrica bonus (+1 punto máximo)

| Criterio | Bonus |
|:---------|------:|
| Matriz de trazabilidad con fuentes vigentes y oráculo identificado | +0,20 |
| Un flujo crítico con tres escenarios significativos (happy path, validación, control de acceso) | +0,25 |
| Datos sintéticos aislados, repetibles y protegidos | +0,20 |
| Comparación ejecutada y resultado documentado (con evidencia de al menos un desvío o constancia de consistencia) | +0,20 |
| Defensa individual satisfactoria | +0,15 |
| **Total máximo** | **+1,00** |

### Reglas de la rúbrica

- Se aplica únicamente al cierre integrador de PP3.
- El trabajo base debe estar aprobado.
- La nota final no puede superar 10.
- No sustituye entregables obligatorios.
- No se duplica en ADI.
- No se exige encontrar un error: una comparación sin inconsistencias también vale.
- Una suite generada por IA que el estudiante no pueda explicar **no recibe bonus**.
- Una prueba sin aserciones significativas no cuenta.
- Una suite inestable (flaky) no cumple determinismo.

---

## 🔗 Conexión con其他 materias

| Materia | Conexión |
|:--------|:---------|
| **Programación** | Tests unitarios, estructuras de datos |
| **Base de Datos** | Persistencia, fixtures, seed |
| **Redes** | HTTP, contratos API, headers |
| **Seguridad** | Secretos, autenticación, OWASP |

---

> 📖 Un término en inglés no te cierra? [Glosario del curso](../glosario.md)
