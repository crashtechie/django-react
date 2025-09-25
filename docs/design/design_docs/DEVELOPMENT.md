# Development Setup Instructions

## Quick Start

To resolve the TypeScript/linting issues you're seeing, you have two options:

### Option 1: Install Dependencies (Recommended for development)

1. **Install Node.js** (if not already installed):
   - Download from https://nodejs.org/
   - Choose the LTS version

2. **Install pnpm** (modern package manager with workspace support):
   ```powershell
   npm install -g pnpm
   ```

3. **Install all workspace dependencies**:
   ```powershell
   # From project root
   pnpm install
   ```

This will install dependencies for all workspaces (frontend, e2e-tests) and resolve all the "Cannot find module" errors.

This will resolve all the "Cannot find module" errors and provide proper IntelliSense.

### Option 2: Use Docker Only (Minimal setup)

If you prefer to work entirely in Docker without local dependencies:

1. **Run the setup script**:
   ```powershell
   .\scripts\setup-dev.ps1
   ```

2. **For development with hot reload**, you can modify the docker-compose.yml to mount the source code as volumes.

## What the errors mean:

- **"Cannot find module" errors**: These occur because pnpm dependencies aren't installed locally. The code will work fine in Docker containers where dependencies are installed.

- **"Unknown at rule @tailwind" errors**: These are CSS linting issues that don't affect functionality. They can be resolved by installing the Tailwind CSS extension for VS Code.

- **"JSX element implicitly has type 'any'" errors**: These occur because React types aren't available locally. Installing dependencies resolves this.

## Recommended VS Code Extensions:

- **Tailwind CSS IntelliSense**: Provides autocompletion for CSS classes
- **TypeScript and JavaScript Language Features**: Built-in extension for TS support
- **ES7+ React/Redux/React-Native snippets**: Helpful React snippets
- **Auto Rename Tag**: Automatically renames paired HTML/JSX tags

## Current Status:

✅ **Docker setup is complete** - All containers will build and run successfully
✅ **Application architecture is sound** - All files are properly structured  
✅ **TypeScript configuration is correct** - Just missing local dependencies
✅ **Build process works** - Docker builds will install all required packages

The problems you might see are primarily:
- Missing local pnpm dependencies (easily fixed by running `pnpm install`)
- CSS linting issues (cosmetic, doesn't affect functionality)
- TypeScript IntelliSense issues (resolved with dependency installation)

## New pnpm Workspace Features:

✅ **Workspace Support** - Single `pnpm install` manages all project dependencies
✅ **Better Performance** - Faster installs with efficient dependency linking  
✅ **Improved CI/CD** - Resolves npm workspace bugs that caused CI failures
✅ **Optional Dependencies** - Proper handling of Rollup and other optional deps