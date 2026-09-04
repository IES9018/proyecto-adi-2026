import { test, expect } from '@playwright/test';

test.describe('Gobernanza Digital - Tests E2E', () => {
  
  test('Página principal carga correctamente', async ({ page }) => {
    await page.goto('/');
    
    // Verificar que la página carga con el título correcto
    await expect(page).toHaveTitle(/Gobernanza/);
    
    // Verificar que se muestra el heading principal
    await expect(page.locator('h1')).toContainText('Gobernanza de Servicios Digitales');
    await expect(page.locator('h2')).toContainText('IES 9-018');
  });

  test('Navegación al catálogo funciona', async ({ page }) => {
    await page.goto('/');
    
    // Click en "Ver Catálogo"
    await page.click('text=Ver Catálogo');
    
    // Verificar que navega al catálogo
    await expect(page).toHaveURL(/catalogo/);
    
    // Verificar que la página del catálogo carga
    await expect(page.locator('h1')).toBeVisible();
  });

  test('Navegación a nueva solicitud funciona', async ({ page }) => {
    await page.goto('/');
    
    // Click en "Nueva Solicitud"
    await page.click('text=Nueva Solicitud');
    
    // Verificar que navega a nueva solicitud
    await expect(page).toHaveURL(/solicitudes\/nueva/);
    
    // Verificar que la página de solicitud carga (usa h2)
    await expect(page.locator('h2')).toContainText('Nueva Solicitud');
  });

  test('Catálogo muestra servicios', async ({ page }) => {
    await page.goto('/catalogo');
    
    // Verificar que se muestra contenido
    await expect(page.locator('body')).not.toBeEmpty();
  });

});
