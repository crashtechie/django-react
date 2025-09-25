import { Page, expect } from '@playwright/test';

/**
 * Common test utilities and helper functions
 */

export class TestHelpers {
  constructor(private page: Page) {}

  /**
   * Navigate to a page and wait for it to load
   */
  async navigateTo(path: string) {
    await this.page.goto(path);
    await this.page.waitForLoadState('networkidle');
  }

  /**
   * Fill a form with customer data
   */
  async fillCustomerForm(data: {
    name: string;
    email: string;
    phone?: string;
    address?: string;
  }) {
    await this.page.getByLabel('Name').fill(data.name);
    await this.page.getByLabel('Email').fill(data.email);
    
    if (data.phone) {
      const phoneField = this.page.getByLabel('Phone');
      if (await phoneField.isVisible()) {
        await phoneField.fill(data.phone);
      }
    }
    
    if (data.address) {
      const addressField = this.page.getByLabel('Address');
      if (await addressField.isVisible()) {
        await addressField.fill(data.address);
      }
    }
  }

  /**
   * Wait for a toast/notification message
   */
  async waitForToast(message?: string) {
    const toast = this.page.locator('[data-testid="toast"]')
      .or(this.page.locator('.toast'))
      .or(this.page.locator('.notification'))
      .or(this.page.locator('[role="alert"]'));

    await expect(toast).toBeVisible();
    
    if (message) {
      await expect(toast).toContainText(message);
    }
    
    return toast;
  }

  /**
   * Wait for loading to complete
   */
  async waitForLoading() {
    const loadingSpinner = this.page.locator('[data-testid="loading"]')
      .or(this.page.locator('.spinner'))
      .or(this.page.locator('.loading'))
      .or(this.page.getByText('Loading...'));

    // Wait for loading to appear (optional)
    await loadingSpinner.isVisible().catch(() => {});
    
    // Wait for loading to disappear
    await expect(loadingSpinner).not.toBeVisible({ timeout: 10000 });
  }

  /**
   * Open the add customer dialog
   */
  async openAddCustomerDialog() {
    await this.page.getByRole('button', { name: 'Add Customer' }).click();
    
    const dialog = this.page.locator('[data-testid="add-customer-dialog"]')
      .or(this.page.getByRole('dialog'))
      .or(this.page.locator('.modal'));
    
    await expect(dialog).toBeVisible();
    return dialog;
  }

  /**
   * Close any open dialog
   */
  async closeDialog() {
    // Try multiple ways to close dialog
    const closeButton = this.page.getByRole('button', { name: 'Close' })
      .or(this.page.getByRole('button', { name: 'Cancel' }))
      .or(this.page.locator('[data-testid="close-dialog"]'))
      .or(this.page.locator('.close-button'));

    if (await closeButton.isVisible()) {
      await closeButton.click();
    } else {
      await this.page.keyboard.press('Escape');
    }

    // Wait for dialog to close
    await expect(this.page.getByRole('dialog')).not.toBeVisible();
  }

  /**
   * Generate unique test data
   */
  generateTestCustomer() {
    const timestamp = Date.now();
    return {
      name: `Test Customer ${timestamp}`,
      email: `test.${timestamp}@example.com`,
      phone: `+1-555-${Math.floor(Math.random() * 10000).toString().padStart(4, '0')}`,
      address: `${Math.floor(Math.random() * 9999)} Test St, Test City, TC 12345`
    };
  }

  /**
   * Wait for API request to complete
   */
  async waitForApiRequest(urlPattern: string) {
    return await this.page.waitForResponse(response => 
      response.url().includes(urlPattern) && response.status() < 400
    );
  }

  /**
   * Mock API responses
   */
  async mockApiResponse(urlPattern: string, responseData: any, status = 200) {
    await this.page.route(`**${urlPattern}**`, route => {
      route.fulfill({
        status,
        contentType: 'application/json',
        body: JSON.stringify(responseData)
      });
    });
  }

  /**
   * Take a screenshot with a descriptive name
   */
  async takeScreenshot(name: string) {
    await this.page.screenshot({ 
      path: `test-results/screenshots/${name}-${Date.now()}.png`,
      fullPage: true 
    });
  }

  /**
   * Check if element is in viewport
   */
  async isInViewport(locator: any) {
    return await locator.evaluate((element: HTMLElement) => {
      const rect = element.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= window.innerHeight &&
        rect.right <= window.innerWidth
      );
    });
  }

  /**
   * Scroll element into view
   */
  async scrollIntoView(locator: any) {
    await locator.scrollIntoViewIfNeeded();
  }

  /**
   * Get table data as array of objects
   */
  async getTableData() {
    const table = this.page.locator('table').first();
    
    if (!await table.isVisible()) {
      return [];
    }

    return await table.evaluate((tableElement: HTMLTableElement) => {
      const headers = Array.from(tableElement.querySelectorAll('thead th'))
        .map(th => th.textContent?.trim() || '');
      
      const rows = Array.from(tableElement.querySelectorAll('tbody tr'));
      
      return rows.map(row => {
        const cells = Array.from(row.querySelectorAll('td'));
        const rowData: Record<string, string> = {};
        
        cells.forEach((cell, index) => {
          if (headers[index]) {
            rowData[headers[index]] = cell.textContent?.trim() || '';
          }
        });
        
        return rowData;
      });
    });
  }

  /**
   * Wait for page to be fully loaded
   */
  async waitForPageLoad() {
    await this.page.waitForLoadState('networkidle');
    await this.page.waitForFunction(() => document.readyState === 'complete');
  }

  /**
   * Retry an action with exponential backoff
   */
  async retryAction(action: () => Promise<void>, maxRetries = 3, baseDelay = 1000) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        await action();
        return;
      } catch (error) {
        if (attempt === maxRetries) {
          throw error;
        }
        
        const delay = baseDelay * Math.pow(2, attempt - 1);
        await this.page.waitForTimeout(delay);
      }
    }
  }

  /**
   * Check accessibility of current page
   */
  async checkAccessibility() {
    // Basic accessibility checks
    const issues = await this.page.evaluate(() => {
      const problems: string[] = [];
      
      // Check for images without alt text
      const images = document.querySelectorAll('img');
      images.forEach((img, index) => {
        if (!img.getAttribute('alt')) {
          problems.push(`Image ${index + 1} missing alt text`);
        }
      });
      
      // Check for form inputs without labels
      const inputs = document.querySelectorAll('input, select, textarea');
      inputs.forEach((input, index) => {
        const id = input.getAttribute('id');
        const ariaLabel = input.getAttribute('aria-label');
        const ariaLabelledby = input.getAttribute('aria-labelledby');
        
        if (id) {
          const label = document.querySelector(`label[for="${id}"]`);
          if (!label && !ariaLabel && !ariaLabelledby) {
            problems.push(`Form input ${index + 1} missing label`);
          }
        }
      });
      
      // Check for heading hierarchy
      const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
      let previousLevel = 0;
      headings.forEach((heading, index) => {
        const level = parseInt(heading.tagName.charAt(1));
        if (index === 0 && level !== 1) {
          problems.push('Page should start with h1');
        }
        if (level > previousLevel + 1) {
          problems.push(`Heading hierarchy issue: ${heading.tagName} follows h${previousLevel}`);
        }
        previousLevel = level;
      });
      
      return problems;
    });
    
    return issues;
  }
}

/**
 * Database helpers for test data management
 */
export class DatabaseHelpers {
  /**
   * Create test customer in database
   */
  static async createTestCustomer(customerData?: any) {
    const defaultData = {
      name: `Test Customer ${Date.now()}`,
      email: `test.${Date.now()}@example.com`,
      phone: '+1-555-1234',
      address: '123 Test St, Test City, TC 12345'
    };
    
    const data = { ...defaultData, ...customerData };
    
    // This would make actual API call to create test data
    // Implementation depends on your backend API
    const response = await fetch('http://localhost:8000/api/customers/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    
    return await response.json();
  }
  
  /**
   * Clean up test data
   */
  static async cleanupTestData() {
    // This would clean up any test data created during tests
    // Implementation depends on your backend API
    try {
      const response = await fetch('http://localhost:8000/api/test/cleanup/', {
        method: 'POST',
      });
      return response.ok;
    } catch (error) {
      console.warn('Failed to cleanup test data:', error);
      return false;
    }
  }
}

/**
 * Common assertions and expectations
 */
export class CustomAssertions {
  static async expectToast(page: Page, message: string) {
    const helper = new TestHelpers(page);
    const toast = await helper.waitForToast(message);
    await expect(toast).toBeVisible();
  }
  
  static async expectLoadingComplete(page: Page) {
    const helper = new TestHelpers(page);
    await helper.waitForLoading();
  }
  
  static async expectPageTitle(page: Page, title: string) {
    await expect(page).toHaveTitle(new RegExp(title, 'i'));
  }
  
  static async expectUrl(page: Page, urlPattern: string) {
    await expect(page).toHaveURL(new RegExp(urlPattern));
  }
}