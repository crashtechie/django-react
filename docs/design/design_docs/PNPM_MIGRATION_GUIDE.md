# pnpm Migration Guide

## Overview

This project has migrated from npm to pnpm for improved workspace management, faster installs, and better CI/CD reliability.

## What Changed

### Package Manager
- **Before:** npm with workspace support
- **After:** pnpm with workspace configuration

### Key Files Modified
- `.github/workflows/ci-cd.yml` - Updated to use pnpm/action-setup
- `package.json` - Scripts converted to `pnpm --filter` commands
- `pnpm-workspace.yaml` - New workspace configuration file
- `.gitignore` - Added pnpm-specific ignore patterns
- Documentation updated throughout

## Installation

### Global pnpm Installation
```powershell
npm install -g pnpm
```

### Project Dependencies
```powershell
# Install all workspace dependencies
pnpm install

# Install dependencies for specific workspace
pnpm --filter frontend install
pnpm --filter e2e-tests install
```

## Available Commands

### Root Level Scripts
```powershell
# Frontend commands
pnpm dev:frontend       # Start frontend dev server
pnpm build:frontend     # Build frontend for production
pnpm test:frontend      # Run frontend tests
pnpm lint:frontend      # Lint frontend code

# E2E test commands  
pnpm dev:e2e           # Start E2E test environment
pnpm test:e2e          # Run E2E tests
```

### Direct Workspace Commands
```powershell
# Run commands in specific workspaces
pnpm --filter frontend dev
pnpm --filter frontend build
pnpm --filter frontend test
pnpm --filter customer-management-frontend lint

pnpm --filter e2e-tests dev
pnpm --filter e2e-tests test
```

## Workspace Configuration

The project uses `pnpm-workspace.yaml` to define workspaces:
```yaml
packages:
  - 'frontend'
  - 'e2e-tests'
```

## Benefits of pnpm Migration

### 🚀 Performance
- Faster dependency installation with symlink-based node_modules
- Efficient dependency deduplication
- Reduced disk space usage

### 🔧 Workspace Management
- Superior workspace dependency resolution
- Better handling of optional dependencies (fixes Rollup issues)
- More reliable CI/CD pipeline

### 🛡️ Security
- Strict dependency isolation
- Better handling of peer dependencies
- Improved lockfile security

### 🔄 CI/CD Improvements
- Resolved npm workspace bugs that caused CI failures
- More reliable `pnpm install` vs `npm ci` issues
- Better optional dependency handling for Rollup

## Troubleshooting

### Common Issues

#### "No projects matched the filters"
- Ensure you're in the project root directory
- Check `pnpm-workspace.yaml` exists and is properly formatted
- Use exact workspace names from `pnpm list -r`

#### Build Failures
- Clear pnpm cache: `pnpm store prune`
- Delete node_modules and reinstall: `rm -rf node_modules && pnpm install`
- Check for lockfile conflicts: `git status pnpm-lock.yaml`

#### VS Code IntelliSense Issues
- Ensure pnpm dependencies are installed: `pnpm install`
- Restart VS Code after installation
- Check TypeScript version compatibility

### Migration from npm

If switching from npm:
1. Remove old lockfiles: `rm package-lock.json frontend/package-lock.json`
2. Install pnpm globally: `npm install -g pnpm`
3. Install dependencies: `pnpm install`
4. Update scripts to use `pnpm --filter` syntax

### CI/CD Debugging

The CI pipeline now uses:
```yaml
- uses: pnpm/action-setup@v4
  with:
    version: latest
    
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'pnpm'
    
- run: pnpm install
- run: pnpm --filter frontend build
- run: pnpm --filter frontend test
```

## Resources

- [pnpm Official Documentation](https://pnpm.io/)
- [pnpm Workspace Guide](https://pnpm.io/workspaces)
- [pnpm vs npm Comparison](https://pnpm.io/motivation)
- [GitHub Actions pnpm Setup](https://github.com/pnpm/action-setup)

## Support

For issues related to the pnpm migration:
1. Check this troubleshooting guide
2. Review the project's `ISSUE_RESOLUTION.md`
3. Consult pnpm documentation
4. Create an issue with detailed error messages and environment info