# Local GitHub Actions Testing Guide

## Prerequisites

1. **Install Act:**
   ```powershell
   # Using Chocolatey (recommended)
   choco install act-cli
   
   # Or using Scoop
   scoop install act
   
   # Or using winget
   winget install nektos.act
   ```

2. **Install Docker Desktop** (required for act)
   - Download from https://www.docker.com/products/docker-desktop

3. **PostgreSQL Considerations:**
   - If you have PostgreSQL running locally on port 5432, you may encounter port conflicts
   - See "Troubleshooting PostgreSQL Port Conflicts" section below

## Testing Commands

### Test All Workflows
```powershell
# Run all workflows for push event
act push

# Run all workflows for pull request
act pull_request
```

### Test Specific Jobs
```powershell
# Test only backend
act push -j test-backend

# Test only frontend  
act push -j test-frontend

# Test security scan
act push -j security-scan
```

### Test with Different Events
```powershell
# Test main branch workflow
act push --eventpath .github/workflows/events/push.json

# Dry run (see what would happen)
act push --dry-run

# Verbose output
act push --verbose
```

### Test Individual Steps

Instead of running full workflows, test individual commands:

```powershell
# Test pnpm installation and dependencies
try { pnpm install --frozen-lockfile } catch { pnpm install }

# Test frontend commands (using correct workspace names)
pnpm --filter customer-management-frontend lint
pnpm exec tsc --noEmit --project frontend/tsconfig.json  # TypeScript checking
pnpm --filter customer-management-frontend test:coverage
pnpm --filter customer-management-frontend build

# Test backend commands
cd backend
uv sync
uv run black --check .
uv run isort --check-only .
uv run flake8 .
```

## Configuration Files

- **`.actrc`**: Configuration for act runner
- **`.github/workflows/events/push.json`**: Sample push event payload

## Troubleshooting

### Common Issues

1. **Docker Permission Errors:**
   ```powershell
   # Make sure Docker Desktop is running
   docker ps
   ```

2. **Large Docker Images:**
   ```powershell
   # Use smaller runner images
   act push -P ubuntu-latest=catthehacker/ubuntu:act-latest-micro
   ```

3. **Environment Variables:**
   ```powershell
   # Create .env file for secrets (don't commit this)
   act push --env-file .env.local
   ```

4. **Network Issues:**
   ```powershell
   # Use host network
   act push --use-new-action-cache
   ```

5. **TypeScript Issues:**
   ```powershell
   # ❌ Wrong: npx tsc causes "This is not the tsc command you are looking for"
   # ✅ Correct: Use pnpm with workspace filter for proper context
   pnpm --filter customer-management-frontend exec tsc --noEmit
   
   # Alternative: Run from frontend directory
   cd frontend
   pnpm exec tsc --noEmit
   ```

## 🔧 Troubleshooting PostgreSQL Port Conflicts

### Issue: "Bind for 0.0.0.0:5432 failed: port is already allocated"

This happens when PostgreSQL is already running locally on port 5432.

#### Solution 1: Stop Local PostgreSQL (Temporary)
```powershell
# Stop local PostgreSQL service
net stop postgresql-x64-16  # Adjust version as needed
# Or find the service name:
Get-Service | Where-Object {$_.Name -like "*postgres*"}

# Run your tests
act push -j test-backend

# Start PostgreSQL again
net start postgresql-x64-16
```

#### Solution 2: Use Alternative Test Database (Recommended)
```powershell
# Use Docker Compose for isolated testing
docker-compose -f docker-compose.test.yml up -d

# Run backend tests with alternative port
DATABASE_URL=postgresql://test_user:test_password@localhost:5433/test_db uv run pytest

# Cleanup
docker-compose -f docker-compose.test.yml down
```

#### Solution 3: Configure Act with Dynamic Ports
The CI/CD workflow now uses dynamic port allocation to automatically avoid conflicts:

```yaml
services:
  postgres:
    ports:
      - 5432  # Dynamic port allocation
```

The workflow automatically detects the assigned port and adjusts the database connection.

## ✅ Validation Results

The CI/CD pipeline has been successfully validated with:
- ✅ Local command execution 
- ✅ act (local GitHub Actions runner)  
- ✅ TypeScript check working in workspace context
- ✅ PostgreSQL port conflict resolution
- ✅ All CI/CD commands tested and documented

### Act Limitations

- **Some actions may not work exactly like GitHub**
- **No access to GitHub secrets** (use local .env files)
- **Different runner environment** (catthehacker images vs GitHub runners)
- **Docker-in-Docker may have issues**
- **PostgreSQL services may conflict with local installations**

## Alternative: Branch Testing

If act doesn't work well, create test branches:

```powershell
# Create test branch
git checkout -b test/ci-validation
git push origin test/ci-validation

# Monitor in GitHub Actions tab
# Delete branch when done
git branch -d test/ci-validation
git push origin --delete test/ci-validation
```

## Best Practices

1. **Test locally first** with individual commands
2. **Use act for workflow validation** 
3. **Handle PostgreSQL conflicts proactively**
4. **Create test branches** for final validation
5. **Use draft PRs** to test without affecting main workflow
6. **Monitor GitHub Actions logs** for differences from local runs

## ✅ Resolution Status

**✅ RESOLVED: Issue #13 - PostgreSQL Port Conflict**
- **Status**: Fixed and validated with act
- **Solution**: Dynamic port allocation and workflow consistency  
- **Validation**: Both backend test workflows passing with 44/44 tests

**Key fixes applied:**
1. Updated both CI/CD and semantic-release workflows for dynamic PostgreSQL port allocation
2. Fixed semantic-release.yml to use `uv` instead of `pip install -e .[dev]`
3. Removed problematic `--network bridge` setting from `.actrc`
4. Ensured both workflows use `customer_management.test_settings` consistently

**Local validation results:**
- ✅ "CI/CD Pipeline/Backend Tests" - All 44 tests passed
- ✅ "Automated Semantic Versioning and Release/Test Backend" - All 44 tests passed  
- ✅ PostgreSQL connection working on port 5432
- ✅ All linting, type checking, and dependency installation working properly

## Quick Start

```powershell
# Install act
choco install act-cli

# Test your current workflow
cd C:\Users\crash\Documents\django-react
act push --dry-run

# Run actual test
act push -j test-frontend
```

This will help you catch issues before pushing to GitHub!