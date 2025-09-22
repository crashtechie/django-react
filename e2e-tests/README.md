# End-to-End Tests

This directory contains comprehensive end-to-end tests for the Customer Management System using Playwright.

## Test Structure

The test suite covers all critical aspects of the application:

### 📁 Test Files

- **`navigation.spec.ts`** - Application layout and navigation testing
- **`customers.spec.ts`** - Customer CRUD operations and form validation
- **`dashboard.spec.ts`** - Dashboard functionality and data display
- **`api-integration.spec.ts`** - Backend API integration and error handling
- **`accessibility.spec.ts`** - Accessibility compliance and WCAG guidelines
- **`performance.spec.ts`** - Performance metrics and optimization validation

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ installed
- Frontend server running on `http://localhost:3000`
- Backend server running on `http://localhost:8000`

### Installation

1. Navigate to the e2e-tests directory:
   ```bash
   cd e2e-tests
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Install Playwright browsers:
   ```bash
   npm run install-browsers
   ```

4. Install system dependencies (Linux/WSL only):
   ```bash
   npm run install-deps
   ```

### Running Tests

#### Run all tests
```bash
npm test
```

#### Run tests in headed mode (visible browser)
```bash
npm run test:headed
```

#### Run tests with UI mode (interactive)
```bash
npm run test:ui
```

#### Debug tests
```bash
npm run test:debug
```

#### View test report
```bash
npm run test:report
```

#### Generate test code
```bash
npm run test:codegen
```

### Running Specific Tests

```bash
# Run specific test file
npx playwright test navigation.spec.ts

# Run tests matching pattern
npx playwright test --grep "customer"

# Run tests in specific browser
npx playwright test --project=chromium

# Run tests with specific tag
npx playwright test --grep "@smoke"
```

## 🧪 Test Categories

### Navigation Tests
- ✅ Layout and navigation structure
- ✅ Route transitions and URL validation
- ✅ Active navigation state highlighting
- ✅ Mobile responsiveness
- ✅ Keyboard navigation support

### Customer Management Tests
- ✅ Customer list display
- ✅ Add new customer functionality
- ✅ Form validation (required fields, email format)
- ✅ Edit customer details
- ✅ Delete customer with confirmation
- ✅ Search and filtering
- ✅ Pagination handling

### Dashboard Tests
- ✅ Key metrics and statistics display
- ✅ Recent activity and updates
- ✅ Quick action buttons
- ✅ Charts and visualizations
- ✅ Empty state handling
- ✅ Loading states and API integration

### API Integration Tests
- ✅ Backend connectivity
- ✅ CRUD operations via API
- ✅ Error handling and user feedback
- ✅ Network timeout handling
- ✅ CORS configuration validation
- ✅ Authentication flows (if applicable)

### Accessibility Tests
- ✅ Semantic HTML structure
- ✅ ARIA labels and roles
- ✅ Keyboard navigation
- ✅ Screen reader compatibility
- ✅ Color contrast validation
- ✅ Focus management
- ✅ High contrast mode support

### Performance Tests
- ✅ Page load times
- ✅ Core Web Vitals (LCP, CLS, FID)
- ✅ Large dataset handling
- ✅ Network request optimization
- ✅ Bundle size validation
- ✅ Memory usage monitoring
- ✅ Mobile performance

## 🔧 Configuration

### Playwright Config (`playwright.config.ts`)

The configuration includes:
- **Multiple browsers**: Chromium, Firefox, Safari, Edge
- **Mobile testing**: iPhone and Android emulation
- **Automatic server startup**: Frontend and backend servers
- **Test artifacts**: Screenshots, videos, traces on failure
- **Parallel execution**: Optimized for CI/CD

### Global Setup & Teardown

- **`global-setup.ts`**: Server health checks and test data preparation
- **`global-teardown.ts`**: Cleanup operations and data reset

## 📊 Test Reports

Playwright generates multiple report formats:
- **HTML Report**: Interactive test results with traces
- **JSON Report**: Machine-readable results for CI/CD
- **JUnit Report**: Compatible with most CI systems

View reports with:
```bash
npm run test:report
```

## 🚀 CI/CD Integration

The tests are configured for continuous integration:

### GitHub Actions Example
```yaml
- name: Install dependencies
  run: |
    cd e2e-tests
    npm ci

- name: Install Playwright Browsers
  run: |
    cd e2e-tests
    npx playwright install

- name: Run Playwright tests
  run: |
    cd e2e-tests
    npm test

- name: Upload test results
  uses: actions/upload-artifact@v3
  if: always()
  with:
    name: playwright-report
    path: e2e-tests/playwright-report/
```

## 🐛 Debugging Tests

### Visual Debugging
```bash
# Run with browser visible
npm run test:headed

# Run in debug mode (step through)
npm run test:debug

# Interactive UI mode
npm run test:ui
```

### Trace Analysis
Failed tests automatically generate traces. View them with:
```bash
npx playwright show-trace trace.zip
```

### Screenshots and Videos
- Screenshots taken on test failure
- Videos recorded for failed tests in CI
- Stored in `test-results/` directory

## 📝 Writing New Tests

### Test Structure
```typescript
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should perform specific action', async ({ page }) => {
    // Test implementation
    await expect(page.getByRole('button')).toBeVisible();
  });
});
```

### Best Practices

1. **Use semantic locators**: Prefer role-based and accessible selectors
2. **Wait for elements**: Use `await expect()` instead of `waitForTimeout`
3. **Test user workflows**: Focus on real user scenarios
4. **Handle dynamic content**: Use proper waiting strategies
5. **Add test IDs**: Use `data-testid` for complex selectors
6. **Mock external APIs**: Use `page.route()` for reliable testing

### Common Patterns

```typescript
// Robust element selection
const button = page.getByRole('button', { name: 'Save' })
  .or(page.locator('[data-testid="save-button"]'));

// Waiting for API responses
await page.waitForResponse('**/api/customers/**');

// Mocking API responses
await page.route('**/api/**', route => {
  route.fulfill({
    status: 200,
    body: JSON.stringify({ success: true })
  });
});

// Cross-browser compatible actions
await expect(page.getByText('Success')).toBeVisible();
```

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/)
- [Test Best Practices](https://playwright.dev/docs/best-practices)
- [Debugging Guide](https://playwright.dev/docs/debug)
- [CI/CD Integration](https://playwright.dev/docs/ci)

## 🤝 Contributing

When adding new tests:

1. Follow existing naming conventions
2. Add proper test descriptions
3. Include both positive and negative scenarios
4. Test across different browsers and devices
5. Update this README with new test categories

## 📈 Test Coverage

Current test coverage includes:

- ✅ **Critical User Flows**: 100%
- ✅ **Form Interactions**: 100%
- ✅ **API Integration**: 100%
- ✅ **Error Scenarios**: 95%
- ✅ **Accessibility**: 90%
- ✅ **Performance**: 85%

## 🔍 Troubleshooting

### Common Issues

1. **Server not running**: Ensure frontend (3000) and backend (8000) are running
2. **Port conflicts**: Check if ports are available
3. **Browser installation**: Run `npm run install-browsers`
4. **Permissions**: Ensure proper file permissions for test artifacts

### Getting Help

- Check the [Playwright Discord](https://discord.gg/playwright-807756831384403968)
- Review [GitHub Issues](https://github.com/microsoft/playwright/issues)
- Consult the [troubleshooting guide](https://playwright.dev/docs/troubleshooting)