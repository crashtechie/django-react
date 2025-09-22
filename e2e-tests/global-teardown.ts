import { FullConfig } from '@playwright/test';

async function globalTeardown(config: FullConfig) {
  console.log('🧹 Starting global teardown for E2E tests...');
  
  try {
    // Cleanup test data
    console.log('🗑️ Cleaning up test data...');
    
    // You can add any cleanup tasks here, such as:
    // - Removing test users
    // - Cleaning up test database records
    // - Clearing uploaded files
    // - Resetting configuration
    
  } catch (error) {
    console.error('❌ Global teardown failed:', error);
    // Don't throw error to avoid failing the entire test suite
  }
  
  console.log('✅ Global teardown completed');
}

export default globalTeardown;