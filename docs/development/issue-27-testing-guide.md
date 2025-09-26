# Issue #27 Testing Guide: CI/CD Pipeline Updates

## Overview
This guide provides comprehensive testing procedures for the CI/CD pipeline updates made to resolve Issue #27.

## Changes Summary

### 1. CI/CD Pipeline Updates
- **File**: `.github/workflows/ci-cd.yml`
- **Changes**: 
  - Added `working-directory: ./frontend` to test step
  - Updated test command to use centralized Jest config

### 2. Frontend Package Updates
- **File**: `frontend/package.json`
- **Changes**: Updated all test scripts to reference centralized config

### 3. Jest Configuration Fixes
- **File**: `tests/config/jest.config.cjs`
- **Changes**: Fixed path resolution for frontend directory execution

## Testing Procedures

### Local Testing

#### 1. Basic Configuration Test
```powershell
# Run the verification script
.\scripts\utilities\test-jest-config.ps1
```

#### 2. Manual Jest Testing
```bash
# Test from frontend directory
cd frontend

# Test configuration loading
pnpm exec jest --config ../tests/config/jest.config.cjs --listTests

# Test with no tests (should pass)
pnpm test --passWithNoTests

# Test coverage generation
pnpm test:coverage --passWithNoTests
```

#### 3. Path Resolution Verification
```bash
# Verify test file discovery
cd frontend
pnpm exec jest --config ../tests/config/jest.config.cjs --listTests | grep -E "(unit|integration)"

# Check if setup file is found
pnpm exec jest --config ../tests/config/jest.config.cjs --showConfig | grep setupFilesAfterEnv
```

### CI/CD Simulation

#### 1. Simulate GitHub Actions Environment
```bash
# Create clean environment
cd django-react
rm -rf node_modules frontend/node_modules

# Install dependencies (as CI would)
pnpm install --frozen-lockfile

# Run frontend tests (as CI would)
cd frontend
pnpm test:coverage --config ../tests/config/jest.config.cjs
```

#### 2. Coverage Report Verification
```bash
# After running tests, verify coverage files exist
ls -la frontend/coverage/
# Should see: clover.xml, lcov.info, coverage-final.json
```

## Expected Results

### ✅ Success Indicators
1. **Jest Config Loads**: No configuration errors
2. **Test Discovery**: Finds tests in `tests/unit/frontend/` and `tests/integration/frontend/`
3. **Path Resolution**: All imports resolve correctly
4. **Coverage Generation**: Creates coverage files in `frontend/coverage/`
5. **CI/CD Compatibility**: Works with GitHub Actions workflow

### ❌ Failure Indicators
1. **Config Errors**: Jest fails to load configuration
2. **Path Errors**: Cannot resolve test files or setup files
3. **Import Errors**: Module resolution failures
4. **Coverage Errors**: Cannot generate coverage reports

## Troubleshooting

### Common Issues

#### Issue: "Cannot resolve module '@/components/...'"
**Solution**: Verify `moduleNameMapper` in Jest config points to correct path

#### Issue: "Setup file not found"
**Solution**: Check `setupFilesAfterEnv` path in Jest config

#### Issue: "No tests found"
**Solution**: Verify `testMatch` patterns in Jest config

#### Issue: "Coverage files not generated"
**Solution**: Check `collectCoverageFrom` patterns and output directory

### Debug Commands

```bash
# Show Jest configuration
pnpm exec jest --config ../tests/config/jest.config.cjs --showConfig

# List all test files Jest would run
pnpm exec jest --config ../tests/config/jest.config.cjs --listTests

# Run Jest in debug mode
pnpm exec jest --config ../tests/config/jest.config.cjs --verbose --no-cache
```

## Integration with Issue #26

This issue overlaps with Issue #26 (Test Path Verification). The changes made here should resolve path issues identified in Issue #26.

### Verification Steps for Issue #26 Integration
1. Run tests from `tests/unit/frontend/` directory
2. Verify all relative imports work correctly
3. Check that `../../../../../frontend/src/` paths are resolved
4. Ensure no circular dependencies or import errors

## Post-Deployment Verification

After merging changes, verify in actual CI/CD environment:

1. **Monitor GitHub Actions**: Check that frontend tests pass
2. **Coverage Reports**: Verify Codecov receives coverage data
3. **Build Process**: Ensure no regression in build pipeline
4. **Test Execution Time**: Monitor for performance impacts

## Documentation Updates

Related documentation that may need updates:
- `frontend/TESTING.md` - Update with new test commands
- `tests/README.md` - Update with configuration changes
- Main `README.md` - Update quick start commands if needed

## Success Metrics

- ✅ CI/CD pipeline passes without test configuration errors
- ✅ All existing tests continue to pass
- ✅ Coverage reports generate correctly
- ✅ No increase in build time due to configuration changes
- ✅ Test discovery works for both unit and integration tests