module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/../unit/frontend/setup.ts'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/../../frontend/src/$1',
  },
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
  },
  testMatch: [
    '<rootDir>/../unit/frontend/**/*.(test|spec).(ts|tsx)',
    '<rootDir>/../integration/frontend/**/*.(test|spec).(ts|tsx)',
  ],
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  collectCoverageFrom: [
    '../../frontend/src/**/*.(ts|tsx)',
    '!../../frontend/src/**/*.d.ts',
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