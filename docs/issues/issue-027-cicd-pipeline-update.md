# Issue #27: Update CI/CD Pipelines for New Test Structure

## Bug Description
GitHub Actions workflows may reference old test paths after test structure migration

## Steps to Reproduce
1. Push changes with new test structure
2. Check CI/CD pipeline execution
3. Look for test discovery failures

## Expected Behavior
CI/CD should discover and run all tests in new structure

## Actual Behavior
Potential test path references need updating in workflow files

## Environment
- GitHub Actions
- Jest test runner
- Node.js environment

## Priority
- [ ] Critical (Production down)
- [x] High (Major feature broken)
- [ ] Medium (Minor issue)
- [ ] Low (Enhancement)

## Files to Update
- `.github/workflows/frontend-tests.yml`
- `.github/workflows/backend-tests.yml`
- `package.json` test scripts

## Estimated Story Points
8