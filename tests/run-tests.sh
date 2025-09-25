#!/bin/bash
# Test runner script for Linux/Mac

set -e

TYPE=${1:-all}
COVERAGE=${2:-false}

echo "Running tests: $TYPE"

case $TYPE in
    "backend")
        echo "Running backend tests..."
        cd ../backend
        if [ "$COVERAGE" = "true" ]; then
            python -m pytest --cov=customers --cov-report=html ../tests/unit/backend ../tests/integration/backend
        else
            python -m pytest ../tests/unit/backend ../tests/integration/backend
        fi
        ;;
    "frontend")
        echo "Running frontend tests..."
        cd ../frontend
        if [ "$COVERAGE" = "true" ]; then
            npm test -- --coverage --config ../tests/config/jest.config.cjs
        else
            npm test -- --config ../tests/config/jest.config.cjs --watchAll=false
        fi
        ;;
    "e2e")
        echo "Running E2E tests..."
        cd config
        npx playwright test
        ;;
    "all")
        echo "Running all tests..."
        
        # Backend tests
        echo "1. Backend tests..."
        cd ../backend
        python -m pytest ../tests/unit/backend ../tests/integration/backend
        
        # Frontend tests
        echo "2. Frontend tests..."
        cd ../frontend
        npm test -- --config ../tests/config/jest.config.cjs --watchAll=false
        
        # E2E tests
        echo "3. E2E tests..."
        cd ../tests/config
        npx playwright test
        ;;
    *)
        echo "Invalid test type. Use: backend, frontend, e2e, or all"
        exit 1
        ;;
esac

echo "Tests completed!"