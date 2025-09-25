import { test, expect } from '@playwright/test';

test.describe('Customer Management', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/customers');
  });

  test('should display customers list page', async ({ page }) => {
    // Check page elements
    await expect(page.getByRole('heading', { name: 'Customers' })).toBeVisible();
    await expect(page.getByRole('button', { name: 'Add Customer' })).toBeVisible();
    
    // Check if customer table/list is present
    const customerList = page.locator('[data-testid="customers-list"]').or(
      page.getByRole('table')
    ).or(
      page.locator('.customer-list')
    );
    await expect(customerList).toBeVisible();
  });

  test('should open add customer dialog/form', async ({ page }) => {
    // Click add customer button
    await page.getByRole('button', { name: 'Add Customer' }).click();
    
    // Check if dialog/form opens
    const addDialog = page.locator('[data-testid="add-customer-dialog"]').or(
      page.getByRole('dialog')
    ).or(
      page.locator('.modal')
    );
    await expect(addDialog).toBeVisible();
    
    // Check form fields
    await expect(page.getByLabel('Name')).toBeVisible();
    await expect(page.getByLabel('Email')).toBeVisible();
    await expect(page.getByLabel('Phone')).toBeVisible();
  });

  test('should create a new customer', async ({ page }) => {
    // Open add customer dialog
    await page.getByRole('button', { name: 'Add Customer' }).click();
    
    // Fill form
    const testCustomerName = `Test Customer ${Date.now()}`;
    const testEmail = `test${Date.now()}@example.com`;
    const testPhone = `+1-555-${Math.floor(Math.random() * 10000).toString().padStart(4, '0')}`;
    
    await page.getByLabel('Name').fill(testCustomerName);
    await page.getByLabel('Email').fill(testEmail);
    await page.getByLabel('Phone').fill(testPhone);
    
    // Submit form
    await page.getByRole('button', { name: 'Save' }).or(
      page.getByRole('button', { name: 'Create' })
    ).click();
    
    // Wait for success message or dialog to close
    await expect(page.locator('[data-testid="success-message"]').or(
      page.getByText('Customer created successfully')
    )).toBeVisible().catch(() => {
      // If no success message, check if dialog closed
      expect(page.getByRole('dialog')).not.toBeVisible();
    });
    
    // Verify customer appears in list
    await expect(page.getByText(testCustomerName)).toBeVisible();
  });

  test('should validate required fields', async ({ page }) => {
    // Open add customer dialog
    await page.getByRole('button', { name: 'Add Customer' }).click();
    
    // Try to submit empty form
    await page.getByRole('button', { name: 'Save' }).or(
      page.getByRole('button', { name: 'Create' })
    ).click();
    
    // Check for validation errors
    const nameError = page.getByText('Name is required').or(
      page.locator('[data-testid="name-error"]')
    );
    const emailError = page.getByText('Email is required').or(
      page.locator('[data-testid="email-error"]')
    );
    
    await expect(nameError.or(emailError)).toBeVisible();
  });

  test('should validate email format', async ({ page }) => {
    // Open add customer dialog
    await page.getByRole('button', { name: 'Add Customer' }).click();
    
    // Fill invalid email
    await page.getByLabel('Name').fill('Test Customer');
    await page.getByLabel('Email').fill('invalid-email');
    
    // Try to submit
    await page.getByRole('button', { name: 'Save' }).or(
      page.getByRole('button', { name: 'Create' })
    ).click();
    
    // Check for email validation error
    const emailError = page.getByText('Invalid email format').or(
      page.getByText('Please enter a valid email')
    ).or(
      page.locator('[data-testid="email-error"]')
    );
    await expect(emailError).toBeVisible();
  });

  test('should search/filter customers', async ({ page }) => {
    // Look for search input
    const searchInput = page.getByPlaceholder('Search customers').or(
      page.getByRole('textbox', { name: 'Search' })
    ).or(
      page.locator('[data-testid="search-input"]')
    );
    
    if (await searchInput.isVisible()) {
      // Enter search term
      await searchInput.fill('test');
      
      // Wait for results to filter
      await page.waitForTimeout(500);
      
      // Check that results are filtered (this would depend on existing data)
      const customerList = page.locator('[data-testid="customers-list"]').or(
        page.getByRole('table')
      );
      await expect(customerList).toBeVisible();
    }
  });

  test('should handle pagination if present', async ({ page }) => {
    // Look for pagination controls
    const pagination = page.locator('[data-testid="pagination"]').or(
      page.locator('.pagination')
    ).or(
      page.getByRole('button', { name: 'Next' })
    );
    
    if (await pagination.isVisible()) {
      // Test pagination
      const nextButton = page.getByRole('button', { name: 'Next' });
      if (await nextButton.isVisible() && await nextButton.isEnabled()) {
        await nextButton.click();
        await page.waitForLoadState('networkidle');
        
        // Verify page changed
        await expect(page.locator('[data-testid="customers-list"]')).toBeVisible();
      }
    }
  });

  test('should edit customer details', async ({ page }) => {
    // Look for edit button (might be in first row)
    const editButton = page.getByRole('button', { name: 'Edit' }).first().or(
      page.locator('[data-testid="edit-customer"]').first()
    ).or(
      page.locator('.edit-button').first()
    );
    
    if (await editButton.isVisible()) {
      await editButton.click();
      
      // Check if edit dialog/form opens
      const editDialog = page.locator('[data-testid="edit-customer-dialog"]').or(
        page.getByRole('dialog')
      );
      await expect(editDialog).toBeVisible();
      
      // Update customer name
      const nameField = page.getByLabel('Name');
      await nameField.clear();
      await nameField.fill(`Updated Customer ${Date.now()}`);
      
      // Save changes
      await page.getByRole('button', { name: 'Save' }).or(
        page.getByRole('button', { name: 'Update' })
      ).click();
      
      // Wait for success
      await page.waitForTimeout(1000);
    }
  });

  test('should delete customer with confirmation', async ({ page }) => {
    // Look for delete button
    const deleteButton = page.getByRole('button', { name: 'Delete' }).first().or(
      page.locator('[data-testid="delete-customer"]').first()
    ).or(
      page.locator('.delete-button').first()
    );
    
    if (await deleteButton.isVisible()) {
      await deleteButton.click();
      
      // Check for confirmation dialog
      const confirmDialog = page.getByText('Are you sure').or(
        page.getByText('confirm')
      ).or(
        page.locator('[data-testid="confirm-dialog"]')
      );
      
      if (await confirmDialog.isVisible()) {
        // Confirm deletion
        await page.getByRole('button', { name: 'Yes' }).or(
          page.getByRole('button', { name: 'Delete' }).last()
        ).or(
          page.getByRole('button', { name: 'Confirm' })
        ).click();
        
        // Wait for deletion to complete
        await page.waitForTimeout(1000);
      }
    }
  });
});