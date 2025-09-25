# Local GitHub Actions with Act

This document explains how to run GitHub Actions locally using `act` for testing CI/CD pipelines before pushing to GitHub.

## Setup

### Prerequisites
- Docker Desktop running
- `act` installed (version 0.2.81+)

### Configuration
The project includes `.actrc` configuration file:
```
-P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## Running Tests Locally

### Backend Tests (✅ Working)
```bash
act push -W .github/workflows/ci-cd.yml -j test-backend --pull=false
```

**Results**: All 44 tests passing with full coverage

### Frontend Tests (⚠️ Partial)
```bash
act push -W .github/workflows/ci-cd.yml -j test-frontend --pull=false
```

**Status**: 
- ✅ Linting: Passing
- ❌ Type checking: Mixed vitest/Jest imports causing errors

### All Jobs
```bash
act push -W .github/workflows/ci-cd.yml --pull=false
```

## Current Issues

### Frontend Type Checking Errors
TypeScript compilation fails due to mixed testing framework imports:
- Old vitest imports in test files
- Jest configuration not fully recognized by TypeScript
- Mixed `vi` and `jest` global references

### Next Steps to Fix
1. Remove all vitest imports from test files
2. Update TypeScript configuration for Jest
3. Clean up mixed testing framework references
4. Verify all tests pass locally before pushing

## Benefits of Local Testing
- Test CI/CD pipeline without GitHub API rate limits
- Faster feedback loop during development
- Catch issues before they appear in GitHub Actions
- No impact on GitHub Actions minutes/quota