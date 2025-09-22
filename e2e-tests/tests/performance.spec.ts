import { test, expect } from '@playwright/test';

test.describe('Performance', () => {
  test('should load the main page within acceptable time', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/');
    
    // Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');
    
    const loadTime = Date.now() - startTime;
    
    // Page should load within 5 seconds
    expect(loadTime).toBeLessThan(5000);
    
    console.log(`Page load time: ${loadTime}ms`);
  });

  test('should have good Core Web Vitals', async ({ page }) => {
    await page.goto('/');
    
    // Wait for page to load completely
    await page.waitForLoadState('networkidle');
    
    // Measure Web Vitals using browser APIs
    const webVitals = await page.evaluate(() => {
      return new Promise<{lcp?: number, cls?: number}>((resolve) => {
        const vitals: {lcp?: number, cls?: number} = {};
        
        // Largest Contentful Paint (LCP)
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1] as any;
          vitals.lcp = lastEntry.startTime;
        }).observe({ entryTypes: ['largest-contentful-paint'] });
        
        // First Input Delay would require actual user interaction
        // Cumulative Layout Shift (CLS)
        new PerformanceObserver((list) => {
          let clsValue = 0;
          for (const entry of list.getEntries()) {
            const layoutShiftEntry = entry as any;
            if (!layoutShiftEntry.hadRecentInput) {
              clsValue += layoutShiftEntry.value;
            }
          }
          vitals.cls = clsValue;
        }).observe({ entryTypes: ['layout-shift'] });
        
        // Wait a bit for measurements
        setTimeout(() => resolve(vitals), 2000);
      });
    });
    
    console.log('Web Vitals:', webVitals);
    
    // LCP should be under 2.5 seconds (2500ms)
    if (webVitals.lcp) {
      expect(webVitals.lcp).toBeLessThan(2500);
    }
    
    // CLS should be under 0.1
    if (webVitals.cls) {
      expect(webVitals.cls).toBeLessThan(0.1);
    }
  });

  test('should load customers page efficiently', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/customers');
    
    // Wait for customer data to load
    await page.waitForResponse(/\/api\/customers\//).catch(() => {});
    
    const loadTime = Date.now() - startTime;
    
    // Should load within reasonable time
    expect(loadTime).toBeLessThan(3000);
    
    console.log(`Customers page load time: ${loadTime}ms`);
  });

  test('should handle large datasets efficiently', async ({ page }) => {
    // Mock large dataset
    await page.route('**/api/customers/**', route => {
      const largeDataset = Array.from({ length: 1000 }, (_, i) => ({
        id: i + 1,
        name: `Customer ${i + 1}`,
        email: `customer${i + 1}@example.com`,
        phone: `+1-555-${i.toString().padStart(4, '0')}`
      }));
      
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(largeDataset)
      });
    });
    
    const startTime = Date.now();
    
    await page.goto('/customers');
    
    // Wait for data to render
    await page.waitForTimeout(2000);
    
    const renderTime = Date.now() - startTime;
    
    // Should handle large dataset within reasonable time
    expect(renderTime).toBeLessThan(5000);
    
    console.log(`Large dataset render time: ${renderTime}ms`);
  });

  test('should have minimal network requests', async ({ page }) => {
    const requests: string[] = [];
    
    page.on('request', request => {
      requests.push(request.url());
    });
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    console.log(`Total network requests: ${requests.length}`);
    console.log('Requests:', requests);
    
    // Reasonable number of requests for initial page load
    expect(requests.length).toBeLessThan(20);
    
    // Check for duplicate requests (inefficient)
    const uniqueRequests = new Set(requests);
    expect(uniqueRequests.size).toBe(requests.length);
  });

  test('should have optimized bundle size', async ({ page }) => {
    const responses: Array<{url: string, size: string}> = [];
    
    page.on('response', response => {
      if (response.url().includes('.js') || response.url().includes('.css')) {
        responses.push({
          url: response.url(),
          size: response.headers()['content-length'] || '0'
        });
      }
    });
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    console.log('Asset sizes:', responses);
    
    // Check for reasonable asset sizes
    for (const response of responses) {
      const size = parseInt(response.size || '0');
      if (size > 0) {
        // Individual assets shouldn't be too large
        expect(size).toBeLessThan(1000000); // 1MB
      }
    }
  });

  test('should cache static assets', async ({ page }) => {
    // First visit
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    const firstVisitRequests: string[] = [];
    page.on('request', request => {
      firstVisitRequests.push(request.url());
    });
    
    // Second visit (reload)
    await page.reload();
    await page.waitForLoadState('networkidle');
    
    // Check for cache headers or reduced requests
    // This is a basic check - real tests would verify cache headers
    console.log(`Requests on reload: ${firstVisitRequests.length}`);
  });

  test('should scroll smoothly with many items', async ({ page }) => {
    // Mock large dataset
    await page.route('**/api/customers/**', route => {
      const largeDataset = Array.from({ length: 500 }, (_, i) => ({
        id: i + 1,
        name: `Customer ${i + 1}`,
        email: `customer${i + 1}@example.com`,
        phone: `+1-555-${i.toString().padStart(4, '0')}`
      }));
      
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(largeDataset)
      });
    });
    
    await page.goto('/customers');
    await page.waitForTimeout(2000);
    
    // Test scrolling performance
    const startTime = Date.now();
    
    // Scroll down multiple times
    for (let i = 0; i < 5; i++) {
      await page.keyboard.press('PageDown');
      await page.waitForTimeout(100);
    }
    
    const scrollTime = Date.now() - startTime;
    
    // Scrolling should be responsive
    expect(scrollTime).toBeLessThan(2000);
    
    console.log(`Scroll performance: ${scrollTime}ms`);
  });

  test('should handle rapid user interactions', async ({ page }) => {
    await page.goto('/customers');
    
    // Test rapid clicking
    const addButton = page.getByRole('button', { name: 'Add Customer' });
    
    if (await addButton.isVisible()) {
      const startTime = Date.now();
      
      // Rapid clicks
      for (let i = 0; i < 5; i++) {
        await addButton.click();
        await page.waitForTimeout(50);
        
        // Close dialog if it opens
        const dialog = page.locator('[role="dialog"]');
        if (await dialog.isVisible()) {
          await page.keyboard.press('Escape');
        }
      }
      
      const interactionTime = Date.now() - startTime;
      
      // Should handle rapid interactions smoothly
      expect(interactionTime).toBeLessThan(2000);
      
      console.log(`Rapid interaction time: ${interactionTime}ms`);
    }
  });

  test('should maintain performance on mobile devices', async ({ page }) => {
    // Emulate mobile device
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Throttle CPU to simulate lower-end device
    const client = await page.context().newCDPSession(page);
    await client.send('Emulation.setCPUThrottlingRate', { rate: 2 });
    
    const startTime = Date.now();
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    const loadTime = Date.now() - startTime;
    
    // Should still load reasonably fast on mobile
    expect(loadTime).toBeLessThan(8000);
    
    console.log(`Mobile load time: ${loadTime}ms`);
    
    // Restore CPU throttling
    await client.send('Emulation.setCPUThrottlingRate', { rate: 1 });
  });

  test('should have efficient memory usage', async ({ page }) => {
    await page.goto('/customers');
    
    // Get initial memory usage
    const initialMemory = await page.evaluate(() => {
      const perfMemory = (performance as any).memory;
      return perfMemory ? {
        usedJSHeapSize: perfMemory.usedJSHeapSize,
        totalJSHeapSize: perfMemory.totalJSHeapSize
      } : null;
    });
    
    if (initialMemory) {
      console.log('Initial memory usage:', initialMemory);
      
      // Perform some actions that might cause memory leaks
      for (let i = 0; i < 10; i++) {
        const addButton = page.getByRole('button', { name: 'Add Customer' });
        if (await addButton.isVisible()) {
          await addButton.click();
          await page.keyboard.press('Escape');
        }
        await page.waitForTimeout(100);
      }
      
      // Get final memory usage
      const finalMemory = await page.evaluate(() => {
        const perfMemory = (performance as any).memory;
        return perfMemory ? {
          usedJSHeapSize: perfMemory.usedJSHeapSize,
          totalJSHeapSize: perfMemory.totalJSHeapSize
        } : null;
      });
      
      if (finalMemory) {
        console.log('Final memory usage:', finalMemory);
        
        // Memory shouldn't grow too much
        const memoryGrowth = finalMemory.usedJSHeapSize - initialMemory.usedJSHeapSize;
        expect(memoryGrowth).toBeLessThan(10000000); // 10MB
      }
    }
  });
});