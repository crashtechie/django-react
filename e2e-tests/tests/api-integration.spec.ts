import { test, expect } from '@playwright/test';

test.describe('API Integration', () => {
  let apiContext;

  test.beforeAll(async ({ playwright }) => {
    apiContext = await playwright.request.newContext({
      baseURL: 'http://localhost:8000',
      extraHTTPHeaders: {
        'Content-Type': 'application/json',
      },
    });
  });

  test.afterAll(async () => {
    await apiContext.dispose();
  });

  test('should connect to backend API', async () => {
    // Test health endpoint
    const response = await apiContext.get('/api/health/');
    expect(response.ok()).toBeTruthy();
    expect(response.status()).toBe(200);
  });

  test('should fetch customers from API', async ({ page }) => {
    // Navigate to customers page
    await page.goto('/customers');

    // Wait for API call to complete
    const response = await page.waitForResponse('**/api/customers/**');
    expect(response.status()).toBe(200);

    // Verify data is displayed
    await expect(page.locator('[data-testid="customers-list"]').or(
      page.getByRole('table')
    )).toBeVisible();
  });

  test('should handle API errors gracefully', async ({ page }) => {
    // Intercept and mock API error
    await page.route('**/api/customers/**', route => {
      route.fulfill({
        status: 500,
        contentType: 'application/json',
        body: JSON.stringify({ error: 'Internal Server Error' })
      });
    });

    // Navigate to customers page
    await page.goto('/customers');

    // Check error handling
    const errorMessage = page.getByText('Error loading customers').or(
      page.getByText('Something went wrong')
    ).or(
      page.locator('[data-testid="error-message"]')
    );
    await expect(errorMessage).toBeVisible();
  });

  test('should handle network timeouts', async ({ page }) => {
    // Intercept and delay API response
    await page.route('**/api/customers/**', async route => {
      await new Promise(resolve => setTimeout(resolve, 10000)); // 10 second delay
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([])
      });
    });

    // Navigate to customers page
    await page.goto('/customers');

    // Check loading state
    const loadingSpinner = page.locator('[data-testid="loading"]').or(
      page.getByText('Loading...')
    ).or(
      page.locator('.spinner')
    );
    await expect(loadingSpinner).toBeVisible();
  });

  test('should create customer via API', async ({ page }) => {
    await page.goto('/customers');

    // Listen for POST request
    const createRequest = page.waitForRequest(request => 
      request.url().includes('/api/customers/') && request.method() === 'POST'
    );

    // Open add customer dialog and fill form
    await page.getByRole('button', { name: 'Add Customer' }).click();
    
    const testCustomerName = `API Test Customer ${Date.now()}`;
    await page.getByLabel('Name').fill(testCustomerName);
    await page.getByLabel('Email').fill(`api-test${Date.now()}@example.com`);
    await page.getByLabel('Phone').fill('+1-555-1234');

    // Submit form
    await page.getByRole('button', { name: 'Save' }).or(
      page.getByRole('button', { name: 'Create' })
    ).click();

    // Verify API request was made
    const request = await createRequest;
    expect(request.method()).toBe('POST');
    
    const requestBody = request.postDataJSON();
    expect(requestBody.name).toBe(testCustomerName);
  });

  test('should update customer via API', async ({ page }) => {
    await page.goto('/customers');

    // Look for edit button on first customer
    const editButton = page.getByRole('button', { name: 'Edit' }).first();
    
    if (await editButton.isVisible()) {
      // Listen for PUT/PATCH request
      const updateRequest = page.waitForRequest(request => 
        request.url().includes('/api/customers/') && 
        (request.method() === 'PUT' || request.method() === 'PATCH')
      );

      await editButton.click();

      // Update customer name
      const nameField = page.getByLabel('Name');
      const updatedName = `Updated via API ${Date.now()}`;
      await nameField.clear();
      await nameField.fill(updatedName);

      // Save changes
      await page.getByRole('button', { name: 'Save' }).or(
        page.getByRole('button', { name: 'Update' })
      ).click();

      // Verify API request was made
      const request = await updateRequest;
      expect(request.method()).toMatch(/PUT|PATCH/);
      
      const requestBody = request.postDataJSON();
      expect(requestBody.name).toBe(updatedName);
    }
  });

  test('should delete customer via API', async ({ page }) => {
    await page.goto('/customers');

    // Look for delete button on first customer
    const deleteButton = page.getByRole('button', { name: 'Delete' }).first();
    
    if (await deleteButton.isVisible()) {
      // Listen for DELETE request
      const deleteRequest = page.waitForRequest(request => 
        request.url().includes('/api/customers/') && request.method() === 'DELETE'
      );

      await deleteButton.click();

      // Confirm deletion if dialog appears
      const confirmButton = page.getByRole('button', { name: 'Yes' }).or(
        page.getByRole('button', { name: 'Delete' }).last()
      );
      
      if (await confirmButton.isVisible()) {
        await confirmButton.click();
      }

      // Verify API request was made
      const request = await deleteRequest;
      expect(request.method()).toBe('DELETE');
    }
  });

  test('should handle CORS properly', async ({ page }) => {
    // Navigate to app
    await page.goto('/');

    // Make API request and check for CORS errors
    const response = await page.evaluate(async () => {
      try {
        const res = await fetch('http://localhost:8000/api/customers/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        return { status: res.status, ok: res.ok };
      } catch (error) {
        return { error: error instanceof Error ? error.message : 'Unknown error' };
      }
    });

    // Should not have CORS errors
    expect(response.error).toBeUndefined();
    expect(response.status).toBeDefined();
  });

  test('should handle authentication if required', async ({ page }) => {
    // This test would be relevant if your app has authentication
    await page.goto('/customers');

    // Check if authentication is required
    const loginForm = page.locator('form[action*="login"]').or(
      page.getByText('Please log in')
    );

    if (await loginForm.isVisible()) {
      // Handle authentication flow
      await page.getByLabel('Username').fill('testuser');
      await page.getByLabel('Password').fill('testpass');
      await page.getByRole('button', { name: 'Login' }).click();

      // Verify successful authentication
      await expect(page.getByRole('heading', { name: 'Customers' })).toBeVisible();
    }
  });
});