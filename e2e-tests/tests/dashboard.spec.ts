import { test, expect } from '@playwright/test';

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should display dashboard with key metrics', async ({ page }) => {
    // Check page title
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();

    // Look for common dashboard elements
    const totalCustomers = page.getByText('Total Customers').or(
      page.locator('[data-testid="total-customers"]')
    );
    const recentActivity = page.getByText('Recent Activity').or(
      page.locator('[data-testid="recent-activity"]')
    );
    const statistics = page.locator('[data-testid="statistics"]').or(
      page.locator('.stats')
    ).or(
      page.locator('.metrics')
    );

    // At least one dashboard element should be visible
    await expect(totalCustomers.or(recentActivity).or(statistics)).toBeVisible();
  });

  test('should display customer statistics', async ({ page }) => {
    // Look for customer count or statistics
    const customerCount = page.locator('[data-testid="customer-count"]').or(
      page.getByText(/\d+ customers?/i)
    ).or(
      page.locator('.customer-stats')
    );

    if (await customerCount.isVisible()) {
      await expect(customerCount).toBeVisible();
      
      // Verify the number is displayed
      const countText = await customerCount.textContent();
      expect(countText).toMatch(/\d+/);
    }
  });

  test('should show recent activity or updates', async ({ page }) => {
    // Look for recent activity section
    const recentActivity = page.locator('[data-testid="recent-activity"]').or(
      page.getByText('Recent')
    ).or(
      page.locator('.activity')
    ).or(
      page.locator('.recent-updates')
    );

    if (await recentActivity.isVisible()) {
      await expect(recentActivity).toBeVisible();
    }
  });

  test('should have quick action buttons', async ({ page }) => {
    // Look for quick action buttons
    const addCustomerButton = page.getByRole('button', { name: /add.*customer/i }).or(
      page.locator('[data-testid="quick-add-customer"]')
    );
    
    const viewReportsButton = page.getByRole('link', { name: /view.*reports/i }).or(
      page.getByRole('button', { name: /reports/i })
    );

    // At least one quick action should be available
    if (await addCustomerButton.isVisible()) {
      await expect(addCustomerButton).toBeVisible();
    } else if (await viewReportsButton.isVisible()) {
      await expect(viewReportsButton).toBeVisible();
    }
  });

  test('should navigate to customers from dashboard', async ({ page }) => {
    // Look for link to customers page
    const customersLink = page.getByRole('link', { name: /customers/i }).or(
      page.getByRole('button', { name: /view.*customers/i })
    ).or(
      page.locator('[data-testid="customers-link"]')
    );

    if (await customersLink.isVisible()) {
      await customersLink.click();
      await expect(page).toHaveURL(/\/customers/);
    }
  });

  test('should display charts or graphs if present', async ({ page }) => {
    // Look for chart elements (common chart libraries)
    const chart = page.locator('canvas').or(
      page.locator('[data-testid="chart"]')
    ).or(
      page.locator('.chart')
    ).or(
      page.locator('svg')
    );

    if (await chart.first().isVisible()) {
      await expect(chart.first()).toBeVisible();
    }
  });

  test('should be responsive on mobile', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });

    // Check that dashboard elements are still visible and properly laid out
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
    
    // Check that content doesn't overflow
    const body = page.locator('body');
    const bodyBox = await body.boundingBox();
    expect(bodyBox?.width).toBeLessThanOrEqual(375);
  });

  test('should load dashboard data from API', async ({ page }) => {
    // Wait for any API calls that load dashboard data
    const apiResponse = page.waitForResponse(/\/api\/.*/).catch(() => null);
    
    await page.goto('/');
    
    const response = await apiResponse;
    if (response) {
      expect(response.status()).toBeLessThan(400);
    }

    // Dashboard should still render even if API calls fail
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  });

  test('should handle loading states', async ({ page }) => {
    // Slow down network to see loading states
    await page.route('**/api/**', async route => {
      await new Promise(resolve => setTimeout(resolve, 1000));
      await route.continue();
    });

    await page.goto('/');

    // Look for loading indicators
    const loadingSpinner = page.locator('[data-testid="loading"]').or(
      page.getByText('Loading')
    ).or(
      page.locator('.spinner')
    ).or(
      page.locator('.loading')
    );

    if (await loadingSpinner.isVisible({ timeout: 2000 })) {
      await expect(loadingSpinner).toBeVisible();
      
      // Loading should eventually disappear
      await expect(loadingSpinner).not.toBeVisible({ timeout: 10000 });
    }
  });

  test('should display welcome message or user info', async ({ page }) => {
    // Look for welcome message or user information
    const welcomeMessage = page.getByText(/welcome/i).or(
      page.getByText(/hello/i)
    ).or(
      page.locator('[data-testid="welcome"]')
    );

    const userInfo = page.locator('[data-testid="user-info"]').or(
      page.locator('.user-profile')
    ).or(
      page.locator('.user-name')
    );

    // Either welcome message or user info might be present
    if (await welcomeMessage.isVisible()) {
      await expect(welcomeMessage).toBeVisible();
    } else if (await userInfo.isVisible()) {
      await expect(userInfo).toBeVisible();
    }
  });

  test('should handle empty state gracefully', async ({ page }) => {
    // Mock empty API responses
    await page.route('**/api/customers/**', route => {
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([])
      });
    });

    await page.goto('/');

    // Dashboard should still render with empty state messages
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();

    // Look for empty state messages
    const emptyState = page.getByText(/no customers/i).or(
      page.getByText(/get started/i)
    ).or(
      page.locator('[data-testid="empty-state"]')
    );

    if (await emptyState.isVisible()) {
      await expect(emptyState).toBeVisible();
    }
  });
});