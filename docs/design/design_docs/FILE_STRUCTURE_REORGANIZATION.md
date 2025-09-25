# File Structure Reorganization Plan

## Current Issues Identified

1. **Root Directory Clutter**: Too many files in root directory
2. **Mixed Documentation**: Documentation scattered across multiple locations
3. **Cache Files**: `.mypy_cache` should be in `.gitignore` and cleaned up
4. **Inconsistent Naming**: Mixed naming conventions
5. **Tool Scripts**: Development tools mixed with core project files

## Proposed New Structure

```
django-react/
├── .github/                    # GitHub configuration (keep as-is)
├── .husky/                     # Git hooks (keep as-is)
├── backend/                    # Django application (keep as-is)
├── frontend/                   # React application (keep as-is)
├── e2e-tests/                  # End-to-end tests (keep as-is)
├── config/                     # System configurations
│   ├── docker/                 # Docker-specific configs
│   ├── nginx/                  # Nginx configurations
│   └── logging/                # Logging configurations
├── database/                   # Database configurations (keep as-is)
├── docs/                       # All documentation
│   ├── api/                    # API documentation
│   ├── deployment/             # Deployment guides
│   ├── development/            # Development guides
│   ├── design/                 # Design documents
│   └── troubleshooting/        # Issue resolution docs
├── scripts/                    # Development and deployment scripts
│   ├── development/            # Development setup scripts
│   ├── deployment/             # Deployment scripts
│   └── utilities/              # Utility scripts
├── tools/                      # Development tools and automation
│   ├── github/                 # GitHub automation tools
│   ├── testing/                # Testing utilities
│   └── monitoring/             # Monitoring tools
├── logs/                       # Application logs (keep as-is)
├── secrets/                    # Secrets and certificates (keep as-is)
├── .gitignore                  # Git ignore rules
├── .commitlintrc.json          # Commit linting
├── docker-compose.yml          # Main compose file
├── docker-compose.test.yml     # Test compose file
├── Makefile                    # Build automation
├── package.json                # Root package.json for workspaces
├── pnpm-workspace.yaml         # PNPM workspace config
├── README.md                   # Main project documentation
└── CHANGELOG.md                # Version history
```

## Migration Steps

### Step 1: Create New Directory Structure
```bash
mkdir -p docs/{api,deployment,development,design,troubleshooting}
mkdir -p config/{docker,nginx,logging}
mkdir -p scripts/{development,deployment,utilities}
mkdir -p tools/{github,testing,monitoring}
```

### Step 2: Move Documentation Files
- `design_docs/` → `docs/design/`
- `ISSUE_16_ANALYSIS.md` → `docs/troubleshooting/`
- `ISSUE_RESOLUTION.md` → `docs/troubleshooting/`
- `LOCAL_GITHUB_ACTIONS.md` → `docs/development/`
- `VERSIONING.md` → `docs/development/`
- `docs/GITHUB_ACTIONS_TESTING.md` → `docs/development/`

### Step 3: Move Configuration Files
- `config/logrotate.conf` → `config/logging/`
- `frontend/nginx.conf` → `config/nginx/`

### Step 4: Reorganize Scripts
- `scripts/setup-dev.*` → `scripts/development/`
- `scripts/setup-networks.*` → `scripts/development/`
- `scripts/generate_version.py` → `scripts/utilities/`
- `scripts/version.py` → `scripts/utilities/`

### Step 5: Move Tools
- `tools/` GitHub-related files → `tools/github/`
- Keep `tools/README.md` as overview

### Step 6: Clean Up Root Directory
- Move `project_organization_plan.md` → `docs/development/`
- Create `CHANGELOG.md` from version history
- Remove `.mypy_cache/` (add to .gitignore)

### Step 7: Update References
- Update all import paths in scripts
- Update Docker compose file paths
- Update GitHub Actions workflow paths
- Update documentation links

## Files to Move

### Documentation Consolidation
```
Current → New Location
design_docs/ → docs/design/
ISSUE_16_ANALYSIS.md → docs/troubleshooting/issue-16-analysis.md
ISSUE_RESOLUTION.md → docs/troubleshooting/issue-resolution.md
LOCAL_GITHUB_ACTIONS.md → docs/development/local-github-actions.md
VERSIONING.md → docs/development/versioning.md
project_organization_plan.md → docs/development/project-organization.md
docs/GITHUB_ACTIONS_TESTING.md → docs/development/github-actions-testing.md
```

### Configuration Reorganization
```
Current → New Location
config/logrotate.conf → config/logging/logrotate.conf
frontend/nginx.conf → config/nginx/default.conf
```

### Scripts Reorganization
```
Current → New Location
scripts/setup-dev.sh → scripts/development/setup-dev.sh
scripts/setup-dev.ps1 → scripts/development/setup-dev.ps1
scripts/setup-networks.sh → scripts/development/setup-networks.sh
scripts/setup-networks.ps1 → scripts/development/setup-networks.ps1
scripts/generate_version.py → scripts/utilities/generate_version.py
scripts/version.py → scripts/utilities/version.py
```

### Tools Reorganization
```
Current → New Location
tools/create_github_*.py → tools/github/
tools/debug_github_project.py → tools/github/
tools/generate_github_issues.py → tools/github/
tools/github_project_*.* → tools/github/
tools/GITHUB_PROJECT_SETUP_GUIDE.md → tools/github/README.md
```

## Benefits of Reorganization

1. **Cleaner Root Directory**: Only essential files at root level
2. **Logical Grouping**: Related files grouped together
3. **Better Navigation**: Easier to find specific types of files
4. **Scalability**: Structure supports project growth
5. **Documentation Centralization**: All docs in one place
6. **Tool Organization**: Development tools properly categorized

## Implementation Priority

1. **High Priority**: Documentation consolidation (improves developer experience)
2. **Medium Priority**: Configuration reorganization (improves maintainability)
3. **Low Priority**: Tools reorganization (nice to have)

## Backward Compatibility

- Update all scripts to use new paths
- Update Docker configurations
- Update GitHub Actions workflows
- Update documentation links
- Create symlinks for critical files if needed during transition