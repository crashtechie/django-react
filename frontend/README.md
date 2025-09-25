# Frontend - Customer Management System

React TypeScript application with modern tooling and comprehensive testing.

## 🛠️ Tech Stack

- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Testing**: Jest + React Testing Library
- **Package Manager**: pnpm
- **Router**: React Router v6

## 🚀 Development

### Setup
```bash
cd frontend
pnpm install
```

### Scripts
```bash
pnpm dev          # Start development server
pnpm build        # Build for production
pnpm test         # Run Jest tests
pnpm test:watch   # Run tests in watch mode
pnpm test:coverage # Run tests with coverage
pnpm lint         # Run ESLint
```

## 🧪 Testing

The frontend uses Jest with React Testing Library for comprehensive component testing.

### Test Structure
- **Setup**: `src/test/setup.ts` - Global test configuration
- **Helpers**: `src/test/helpers.ts` - Test utility functions
- **Config**: `jest.config.cjs` - Jest configuration

### Running Tests
```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test CustomerForm

# Run tests in watch mode
pnpm test:watch

# Generate coverage report
pnpm test:coverage
```

### Mock System
Global mocks are available via `global.__TEST_MOCKS__` for consistent testing across components.

## 📁 Project Structure

```
src/
├── components/     # Reusable UI components
├── pages/         # Page components
├── services/      # API services
├── types/         # TypeScript type definitions
├── test/          # Test configuration and helpers
└── tests/         # Test files
```

## 🔧 Configuration

- **Vite**: `vite.config.ts`
- **Jest**: `jest.config.cjs`
- **TypeScript**: `tsconfig.json`
- **Tailwind**: `tailwind.config.js`
- **ESLint**: `.eslintrc.cjs`

## 📚 Documentation

- [Testing Guide](./TESTING.md) - Comprehensive testing documentation
- [Issue #16 Analysis](../ISSUE_16_ANALYSIS.md) - React hooks testing resolution