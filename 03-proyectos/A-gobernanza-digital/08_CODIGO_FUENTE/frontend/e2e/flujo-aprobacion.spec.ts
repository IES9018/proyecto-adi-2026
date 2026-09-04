import { test, expect } from '@playwright/test';

test.describe('Flujo completo de gobernanza digital', () => {

  test('1. Página principal carga correctamente', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('h1')).toContainText('Gobernanza de Servicios Digitales');
    await expect(page.locator('h2')).toContainText('IES 9-018');
    await expect(page.locator('a[href="/catalogo"]')).toBeVisible();
    await expect(page.locator('a[href="/solicitudes/nueva"]')).toBeVisible();
  });

  test('2. Catálogo público muestra servicios', async ({ page }) => {
    await page.goto('/catalogo');
    await expect(page.locator('h1')).toContainText('Servicios Digitales Activos');
    await expect(page.locator('select')).toBeVisible();
    await expect(page.locator('input[placeholder="Buscar..."]')).toBeVisible();
  });

  test('3. Formulario de solicitud carga correctamente', async ({ page }) => {
    await page.goto('/solicitudes/nueva');
    await expect(page.locator('h2')).toContainText('Nueva Solicitud');
    await expect(page.locator('input').first()).toBeVisible();
    await expect(page.locator('select').first()).toBeVisible();
    await expect(page.locator('textarea')).toBeVisible();
    await expect(page.locator('button:has-text("Enviar Solicitud")')).toBeVisible();
  });

  test('4. Navegación entre páginas funciona', async ({ page }) => {
    // Home -> Catálogo
    await page.goto('/');
    await page.click('a[href="/catalogo"]');
    await expect(page).toHaveURL('/catalogo');
    await expect(page.locator('h1')).toContainText('Servicios Digitales Activos');

    // Catálogo -> Home (via back)
    await page.goBack();
    await expect(page).toHaveURL('/');
  });

  test('5. Formulario permite enviar solicitud', async ({ page }) => {
    await page.goto('/solicitudes/nueva');
    
    // Llenar formulario
    await page.fill('input:first-of-type', 'Portal Educativo ADI 2026');
    await page.selectOption('select:first-of-type', '2');
    await page.fill('input:nth-of-type(2)', 'portal-adi');
    await page.fill('textarea', 'Portal de recursos educativos para estudiantes');
    await page.fill('input:nth-of-type(3)', 'https://github.com/IES9018/portal-adi');
    
    // Verificar que el botón está habilitado
    await expect(page.locator('button:has-text("Enviar Solicitud")')).toBeEnabled();
  });
});
