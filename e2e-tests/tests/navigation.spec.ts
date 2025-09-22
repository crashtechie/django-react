import { test, expect } from '@playwright/test';

test.describe('Application Layout and Navigation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should display the main layout correctly', async ({ page }) => {
    // Check page title
    await expect(page).toHaveTitle(/Customer Management/);
    
    // Check main navigation elements
    await expect(page.getByRole('banner')).toBeVisible();
    await expect(page.getByRole('main')).toBeVisible();
    
    // Check navigation links
    await expect(page.getByRole('link', { name: 'Dashboard' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Customers' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Reports' })).toBeVisible();
    
    // Check branding
    await expect(page.getByText('Customer Management')).toBeVisible();
  });

  test('should navigate between pages correctly', async ({ page }) => {
    // Navigate to Customers page
    await page.getByRole('link', { name: 'Customers' }).click();
    await expect(page).toHaveURL(/\/customers/);
    await expect(page.getByRole('heading', { name: 'Customers' })).toBeVisible();
    
    // Navigate to Reports page
    await page.getByRole('link', { name: 'Reports' }).click();
    await expect(page).toHaveURL(/\/reports/);
    await expect(page.getByRole('heading', { name: 'Reports' })).toBeVisible();
    
    // Navigate back to Dashboard
    await page.getByRole('link', { name: 'Dashboard' }).click();
    await expect(page).toHaveURL('/');
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  });

  test('should highlight active navigation item', async ({ page }) => {
    // Check Dashboard is active by default
    const dashboardLink = page.getByRole('link', { name: 'Dashboard' });
    await expect(dashboardLink).toHaveClass(/active|bg-primary|text-primary/);
    
    // Navigate to Customers and check active state
    await page.getByRole('link', { name: 'Customers' }).click();
    const customersLink = page.getByRole('link', { name: 'Customers' });
    await expect(customersLink).toHaveClass(/active|bg-primary|text-primary/);
  });

  test('should be responsive on mobile devices', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Check that the layout adapts to mobile
    await expect(page.getByRole('banner')).toBeVisible();
    await expect(page.getByRole('main')).toBeVisible();
    
    // Check that navigation is still accessible (might be in a mobile menu)
    const navigation = page.getByRole('navigation');
    await expect(navigation).toBeVisible();
  });

  test('should handle keyboard navigation', async ({ page }) => {
    // Test tab navigation through main elements
    await page.keyboard.press('Tab');
    await page.keyboard.press('Tab');
    await page.keyboard.press('Tab');
    
    // Should be able to navigate with keyboard
    const focusedElement = await page.locator(':focus');
    await expect(focusedElement).toBeVisible();
  });
});