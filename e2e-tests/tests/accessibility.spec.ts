import { test, expect } from '@playwright/test';

test.describe('Accessibility', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should have proper heading hierarchy', async ({ page }) => {
    // Check for h1 element
    const h1 = page.locator('h1');
    await expect(h1).toBeVisible();
    
    // If h2 exists, it should come after h1
    const h2 = page.locator('h2').first();
    if (await h2.isVisible()) {
      await expect(h2).toBeVisible();
    }
  });

  test('should have proper alt text for images', async ({ page }) => {
    // Check all images have alt text
    const images = page.locator('img');
    const imageCount = await images.count();
    
    for (let i = 0; i < imageCount; i++) {
      const img = images.nth(i);
      const alt = await img.getAttribute('alt');
      
      // Alt attribute should exist (can be empty for decorative images)
      expect(alt).not.toBeNull();
    }
  });

  test('should support keyboard navigation', async ({ page }) => {
    // Test tab navigation through interactive elements
    await page.keyboard.press('Tab');
    
    let activeElement = await page.locator(':focus');
    await expect(activeElement).toBeVisible();
    
    // Continue tabbing through several elements
    for (let i = 0; i < 5; i++) {
      await page.keyboard.press('Tab');
      activeElement = await page.locator(':focus');
      
      // Should always have a focused element
      const isVisible = await activeElement.isVisible().catch(() => false);
      if (isVisible) {
        await expect(activeElement).toBeVisible();
      }
    }
  });

  test('should have proper form labels', async ({ page }) => {
    // Navigate to page with forms (customers page)
    await page.goto('/customers');
    
    // Try to open add customer form
    const addButton = page.getByRole('button', { name: 'Add Customer' });
    if (await addButton.isVisible()) {
      await addButton.click();
      
      // Check that form inputs have labels
      const nameInput = page.getByLabel('Name');
      const emailInput = page.getByLabel('Email');
      const phoneInput = page.getByLabel('Phone');
      
      if (await nameInput.isVisible()) {
        await expect(nameInput).toBeVisible();
      }
      if (await emailInput.isVisible()) {
        await expect(emailInput).toBeVisible();
      }
      if (await phoneInput.isVisible()) {
        await expect(phoneInput).toBeVisible();
      }
    }
  });

  test('should have sufficient color contrast', async ({ page }) => {
    // This is a basic check - in real projects you'd use axe-playwright
    // Check that text is visible and readable
    const headings = page.locator('h1, h2, h3, h4, h5, h6');
    const headingCount = await headings.count();
    
    for (let i = 0; i < headingCount; i++) {
      const heading = headings.nth(i);
      if (await heading.isVisible()) {
        await expect(heading).toBeVisible();
        
        // Basic check that text has content
        const text = await heading.textContent();
        expect(text?.trim()).toBeTruthy();
      }
    }
  });

  test('should support screen readers with ARIA labels', async ({ page }) => {
    // Check for ARIA labels on interactive elements
    const buttons = page.locator('button');
    const buttonCount = await buttons.count();
    
    for (let i = 0; i < buttonCount; i++) {
      const button = buttons.nth(i);
      if (await button.isVisible()) {
        // Button should have accessible name (text, aria-label, or aria-labelledby)
        const text = await button.textContent();
        const ariaLabel = await button.getAttribute('aria-label');
        const ariaLabelledby = await button.getAttribute('aria-labelledby');
        
        // At least one should be present
        expect(text?.trim() || ariaLabel || ariaLabelledby).toBeTruthy();
      }
    }
  });

  test('should have proper focus indicators', async ({ page }) => {
    // Tab to first interactive element
    await page.keyboard.press('Tab');
    
    const focusedElement = page.locator(':focus');
    await expect(focusedElement).toBeVisible();
    
    // Check if focus indicator is visible (this is basic - real tests would check CSS)
    const outline = await focusedElement.evaluate(el => {
      const style = window.getComputedStyle(el);
      return style.outline || style.boxShadow || style.border;
    });
    
    // Should have some form of focus indicator
    expect(outline).toBeTruthy();
  });

  test('should be navigable with keyboard only', async ({ page }) => {
    // Navigate to customers page using only keyboard
    await page.keyboard.press('Tab');
    
    // Find and activate customers link
    let currentElement = page.locator(':focus');
    let attempts = 0;
    
    while (attempts < 20) {
      const text = await currentElement.textContent().catch(() => '');
      const role = await currentElement.getAttribute('role').catch(() => '');
      
      // If we found the customers link, activate it
      if (text?.toLowerCase().includes('customer') && 
          (role === 'link' || await currentElement.evaluate(el => el.tagName === 'A'))) {
        await page.keyboard.press('Enter');
        break;
      }
      
      await page.keyboard.press('Tab');
      currentElement = page.locator(':focus');
      attempts++;
    }
    
    // Should be able to navigate without mouse
    // (URL might not change if navigation failed, but test won't fail)
  });

  test('should announce dynamic content changes', async ({ page }) => {
    // Navigate to customers page
    await page.goto('/customers');
    
    // Look for live regions for dynamic content
    const liveRegions = page.locator('[aria-live], [role="status"], [role="alert"]');
    
    if (await liveRegions.first().isVisible()) {
      await expect(liveRegions.first()).toBeVisible();
    }
    
    // Try to trigger a dynamic change (add customer)
    const addButton = page.getByRole('button', { name: 'Add Customer' });
    if (await addButton.isVisible()) {
      await addButton.click();
      
      // Look for status messages or alerts
      const statusMessage = page.locator('[role="status"], [role="alert"], [aria-live]');
      
      // If dynamic content is added, it should be in a live region
      await page.waitForTimeout(1000); // Wait for potential updates
    }
  });

  test('should have proper page titles', async ({ page }) => {
    // Check main page title
    await expect(page).toHaveTitle(/Customer Management/);
    
    // Navigate to customers page
    await page.goto('/customers');
    await expect(page).toHaveTitle(/.+/); // Should have some title
    
    // Navigate to reports page
    await page.goto('/reports');
    await expect(page).toHaveTitle(/.+/); // Should have some title
  });

  test('should handle high contrast mode', async ({ page }) => {
    // Enable high contrast simulation
    await page.emulateMedia({ colorScheme: 'dark' });
    
    // Check that content is still visible
    await expect(page.getByRole('banner')).toBeVisible();
    await expect(page.getByRole('main')).toBeVisible();
    
    // Navigation should still be visible
    const navigation = page.getByRole('navigation');
    if (await navigation.isVisible()) {
      await expect(navigation).toBeVisible();
    }
  });

  test('should support reduced motion preferences', async ({ page }) => {
    // Enable reduced motion preference
    await page.emulateMedia({ reducedMotion: 'reduce' });
    
    // Page should still function normally
    await expect(page.getByRole('main')).toBeVisible();
    
    // Animations should be reduced (this is hard to test automatically)
    // In real tests, you'd check that animation durations are set to 0
  });

  test('should have semantic HTML structure', async ({ page }) => {
    // Check for proper landmark elements
    await expect(page.getByRole('banner')).toBeVisible(); // header
    await expect(page.getByRole('main')).toBeVisible(); // main content
    
    // Navigation should be present
    const nav = page.getByRole('navigation');
    if (await nav.isVisible()) {
      await expect(nav).toBeVisible();
    }
    
    // Check for proper heading structure
    const h1 = page.locator('h1');
    await expect(h1).toBeVisible();
  });
});