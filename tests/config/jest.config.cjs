const path = require('path');

module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  rootDir: path.resolve(__dirname, '../../frontend'),
  roots: [
    '<rootDir>',
    '<rootDir>/../tests'
  ],
  setupFilesAfterEnv: ['<rootDir>/../tests/unit/frontend/setup.ts'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
  },
  testMatch: [
    '<rootDir>/../tests/unit/frontend/**/*.test.ts',
    '<rootDir>/../tests/unit/frontend/**/*.test.tsx',
    '<rootDir>/../tests/unit/frontend/**/*.spec.ts',
    '<rootDir>/../tests/unit/frontend/**/*.spec.tsx',
    '<rootDir>/../tests/integration/frontend/**/*.test.ts',
    '<rootDir>/../tests/integration/frontend/**/*.test.tsx',
    '<rootDir>/../tests/integration/frontend/**/*.spec.ts',
    '<rootDir>/../tests/integration/frontend/**/*.spec.tsx',
  ],
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  collectCoverageFrom: [
    'src/**/*.(ts|tsx)',
    '!src/**/*.d.ts',
  ],
  globals: {
    'ts-jest': {
      tsconfig: {
        jsx: 'react-jsx',
      },
    },
  },
  extensionsToTreatAsEsm: ['.ts', '.tsx'],
};