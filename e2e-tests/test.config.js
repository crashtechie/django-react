module.exports = {
  // Test environment configuration
  testEnvironment: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    apiURL: process.env.API_URL || 'http://localhost:8000',
  },

  // Test data configuration
  testData: {
    defaultCustomer: {
      name: 'Test Customer',
      email: 'test@example.com',
      phone: '+1-555-1234',
      address: '123 Test St, Test City, TC 12345'
    },
    adminUser: {
      username: process.env.ADMIN_USERNAME || 'admin',
      password: process.env.ADMIN_PASSWORD || 'admin123'
    }
  },

  // Test timeouts (in milliseconds)
  timeouts: {
    default: 30000,
    navigation: 10000,
    api: 5000,
    loading: 3000
  },

  // Browser configuration for different environments
  browsers: {
    development: ['chromium'],
    ci: ['chromium', 'firefox'],
    full: ['chromium', 'firefox', 'webkit']
  },

  // Test tags for organizing test runs
  tags: {
    smoke: '@smoke',
    regression: '@regression',
    api: '@api',
    ui: '@ui',
    accessibility: '@a11y',
    performance: '@perf'
  },

  // Retry configuration
  retries: {
    development: 0,
    ci: 2
  },

  // Screenshot and video settings
  artifacts: {
    screenshots: 'only-on-failure',
    videos: 'retain-on-failure',
    traces: 'on-first-retry'
  }
};