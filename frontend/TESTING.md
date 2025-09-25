# Frontend Testing Guide

## Testing Framework
The frontend uses **Jest** with React Testing Library for component testing.

## Mock System

### Overview
The frontend uses a centralized mock system to ensure consistent test behavior across all test files.

### Global Mocks
All mocks are available via `global.__TEST_MOCKS__`:

```typescript
// Router mocks
global.__TEST_MOCKS__.navigate
global.__TEST_MOCKS__.useParams

// API mocks
global.__TEST_MOCKS__.customerApi.getCustomer
global.__TEST_MOCKS__.customerApi.createCustomer
global.__TEST_MOCKS__.customerApi.updateCustomer
// ... other API methods

// Toast mocks
global.__TEST_MOCKS__.toast.success
global.__TEST_MOCKS__.toast.error
```

### Test Helpers
Use helpers from `src/test/helpers.ts`:

```typescript
import { getMocks, resetAllMocks, setEditMode, setCreateMode } from '../test/helpers'

describe('MyComponent', () => {
  beforeEach(() => {
    resetAllMocks() // Reset all mocks to defaults
  })

  it('should work in edit mode', () => {
    setEditMode('123') // Sets useParams to return { id: '123' }
    // ... test code
  })

  it('should work in create mode', () => {
    setCreateMode() // Sets useParams to return { id: undefined }
    // ... test code
  })
})
```

### Best Practices
1. Always use `resetAllMocks()` in `beforeEach`
2. Use helper functions instead of direct mock manipulation
3. Access mocks via `getMocks()` for type safety
4. Don't mix global mocks with local mocks in the same test file

### Configuration
- Setup: `src/test/setup.ts`
- Helpers: `src/test/helpers.ts`
- Config: `jest.config.cjs`

## Troubleshooting

### React Hooks Error
**Issue**: `Cannot read properties of null (reading 'useState')`

**Status**: ✅ **RESOLVED** (Issue #16)

**Solution**: Migrated from vitest to Jest with proper React 18 support

**What was done**:
1. Installed Jest with React 18 compatibility
2. Created `jest.config.cjs` with proper TypeScript support
3. Updated test setup and helpers for Jest
4. Removed vitest and related packages

**Result**: React hooks now work properly in all component tests