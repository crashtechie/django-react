import { chromium, FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
  console.log('🚀 Starting global setup for E2E tests...');
  
  // Launch browser for setup tasks
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  try {
    // Wait for frontend to be ready
    console.log('⏳ Waiting for frontend server...');
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    console.log('✅ Frontend server is ready');
    
    // Wait for backend to be ready
    console.log('⏳ Waiting for backend server...');
    const response = await page.request.get('http://localhost:8000/api/health/');
    if (response.ok()) {
      console.log('✅ Backend server is ready');
    } else {
      console.log('⚠️ Backend server health check failed, continuing anyway...');
    }
    
    // Setup test data if needed
    console.log('📝 Setting up test data...');
    
    // You can add any global setup tasks here, such as:
    // - Creating test users
    // - Setting up test database state
    // - Configuring authentication tokens
    
  } catch (error) {
    console.error('❌ Global setup failed:', error);
    throw error;
  } finally {
    await browser.close();
  }
  
  console.log('✅ Global setup completed successfully');
}

export default globalSetup;