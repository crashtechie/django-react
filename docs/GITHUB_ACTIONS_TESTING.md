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
   # ✅ Correct: Use pnpm exec to access workspace TypeScript
   pnpm exec tsc --noEmit --project frontend/tsconfig.json
   ```

### Act Limitations

- **Some actions may not work exactly like GitHub**
- **No access to GitHub secrets** (use local .env files)
- **Different runner environment** (catthehacker images vs GitHub runners)
- **Docker-in-Docker may have issues**

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
3. **Create test branches** for final validation
4. **Use draft PRs** to test without affecting main workflow
5. **Monitor GitHub Actions logs** for differences from local runs

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