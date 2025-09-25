# Automated Semantic Versioning Guide

This project implements automated semantic versioning following the [SemVer specification](https://semver.org/) using conventional commits and automated release workflows.

## Overview

- **Frontend**: Uses `semantic-release` with conventional commits
- **Backend**: Uses `setuptools-scm` with Git tags for version generation
- **CI/CD**: GitHub Actions workflow handles automated versioning and releases

## Version Format

We follow **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (incompatible API changes)
- **MINOR**: New features (backward-compatible functionality)
- **PATCH**: Bug fixes (backward-compatible fixes)

## Conventional Commit Format

All commits must follow the [Conventional Commits](https://conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types

| Type | Description | Version Impact |
|------|-------------|----------------|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `perf` | Performance improvement | PATCH |
| `refactor` | Code refactoring | PATCH |
| `docs` | Documentation changes | PATCH (README only) |
| `style` | Code style changes | No release |
| `test` | Test changes | No release |
| `chore` | Maintenance tasks | No release |
| `ci` | CI/CD changes | No release |
| `build` | Build system changes | No release |
| `revert` | Revert previous commit | Depends on reverted commit |

### Breaking Changes

For **MAJOR** version bumps, include `BREAKING CHANGE:` in the commit footer:

```
feat!: add new authentication system

BREAKING CHANGE: removed support for legacy API endpoints
```

Or use the `!` notation after the type:

```
feat!: redesign customer API endpoints
```

## Commit Examples

### Good Commits ✅

```bash
feat: add customer search functionality
fix: resolve validation error in customer form
perf: optimize database queries for customer list
docs: update API documentation
feat!: redesign authentication system

BREAKING CHANGE: JWT tokens now required for all endpoints
```

### Bad Commits ❌

```bash
Fixed bug                    # Missing type
feature: Add new stuff       # Wrong type capitalization
fix: Fix the thing.          # Ends with period
FEAT: add customer search    # Wrong case
```

## Automated Release Process

### How It Works

1. **Commit Analysis**: When code is pushed to `main`, GitHub Actions analyzes commit messages
2. **Version Calculation**: Based on commit types, determines the next version number
3. **Frontend Release**: Updates `package.json`, creates Git tag, generates changelog
4. **Backend Release**: Updates version via `setuptools-scm`, creates backend-specific tag
5. **GitHub Release**: Creates GitHub release with automated release notes

### Release Workflow

The automated release process includes:

- ✅ Run all tests (frontend + backend)
- ✅ Lint code
- ✅ Calculate next version
- ✅ Update package.json (frontend)
- ✅ Generate _version.py (backend)
- ✅ Create Git tags
- ✅ Generate CHANGELOG.md
- ✅ Create GitHub release
- ✅ Sync versions across components

### Manual Release (if needed)

To trigger a manual release:

```bash
# Frontend only
cd frontend
npm run semantic-release

# Full release via GitHub Actions
git push origin main
```

## Version Access

### Frontend (React)
```typescript
// Access version from package.json
import packageJson from '../package.json';
console.log('Version:', packageJson.version);
```

### Backend (Django)
```python
# Access version in Django
from django.conf import settings
print(f"Backend version: {settings.VERSION}")

# Or directly from version file
from customer_management._version import __version__
print(f"Version: {__version__}")
```

## Development Workflow

### 1. Create Feature Branch
```bash
git checkout -b feature/customer-search
```

### 2. Make Changes with Conventional Commits
```bash
git add .
git commit -m "feat: add advanced customer search filters"
```

### 3. Push and Create PR
```bash
git push origin feature/customer-search
# Create PR to main branch
```

### 4. Merge to Main
- PR gets merged to `main`
- Automated release workflow runs
- New version is automatically created if commits warrant a release

## Commit Message Validation

We use `commitlint` with `husky` to enforce conventional commit format:

- **Pre-commit hook**: Validates commit messages before they're committed
- **CI validation**: GitHub Actions also validates commit format
- **Local setup**: Run `npm install` in project root to set up hooks

### Setup Development Environment

```bash
# Install root dependencies (commitlint, husky)
npm install

# Install frontend dependencies
cd frontend && npm install

# Install backend dependencies
cd backend && pip install -e .[dev]
```

## Configuration Files

- **Frontend**: `.releaserc.json` - Semantic-release configuration
- **Backend**: `pyproject.toml` - setuptools-scm configuration
- **Commits**: `.commitlintrc.json` - Commit message linting rules
- **Hooks**: `.husky/commit-msg` - Pre-commit validation
- **CI/CD**: `.github/workflows/semantic-release.yml` - Automated release workflow

## Troubleshooting

### Common Issues

1. **Commit message rejected**: Follow conventional commit format
2. **No release created**: Ensure commits include `feat:`, `fix:`, or breaking changes
3. **Version mismatch**: Check that both frontend and backend versions are synced
4. **Release failed**: Check GitHub Actions logs for specific errors

### Force Release (Emergency)

If you need to force a release:

```bash
# Create emergency tag
git tag -a "v1.2.3" -m "Emergency release v1.2.3"
git push origin v1.2.3

# This will trigger release workflows
```

## Resources

- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://conventionalcommits.org/)
- [semantic-release](https://github.com/semantic-release/semantic-release)
- [setuptools-scm](https://github.com/pypa/setuptools_scm)
- [commitlint](https://commitlint.js.org/)