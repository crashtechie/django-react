# Tests Directory

This directory contains all tests for the Django-React Customer Management System, organized by test type and component.

## Directory Structure

```
tests/
├── unit/                    # Unit tests
│   ├── backend/            # Django unit tests
│   └── frontend/           # React component unit tests
├── integration/            # Integration tests
│   ├── backend/            # Django integration tests
│   └── frontend/           # React integration tests
├── e2e/                    # End-to-end tests (Playwright)
├── fixtures/               # Test data and utilities
├── config/                 # Test configuration files
└── README.md              # This file
```

## Test Types

### Unit Tests
- **Backend**: Django model, serializer, and view tests
- **Frontend**: React component tests with Jest and React Testing Library

### Integration Tests
- **Backend**: API endpoint integration tests
- **Frontend**: Component integration tests with mock APIs

### End-to-End Tests
- **E2E**: Full application workflow tests with Playwright

## Running Tests

### All Tests
```bash
# From project root
npm run test:all
```

### Backend Tests Only
```bash
# From project root
cd backend && python -m pytest ../tests/unit/backend ../tests/integration/backend
```

### Frontend Tests Only
```bash
# From project root
cd frontend && npm test -- --config ../tests/config/jest.config.cjs
```

### E2E Tests Only
```bash
# From tests/config directory
cd tests/config && npx playwright test
```

## Configuration Files

- `config/pytest.ini` - Backend test configuration
- `config/jest.config.cjs` - Frontend test configuration  
- `config/playwright.config.ts` - E2E test configuration
- `config/global-setup.ts` - E2E global setup
- `config/global-teardown.ts` - E2E global teardown

## Test Data

- `fixtures/test-data.json` - Sample data for E2E tests
- `fixtures/test-helpers.ts` - Shared test utilities

## Coverage

Test coverage reports are generated in:
- Backend: `backend/htmlcov/`
- Frontend: `frontend/coverage/`
- E2E: `tests/test-results/`