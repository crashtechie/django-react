#!/usr/bin/env pwsh
# Test runner script for Windows PowerShell

param(
    [string]$Type = "all",
    [switch]$Coverage = $false
)

$ErrorActionPreference = "Stop"

Write-Host "Running tests: $Type" -ForegroundColor Green

switch ($Type.ToLower()) {
    "backend" {
        Write-Host "Running backend tests..." -ForegroundColor Yellow
        Set-Location "../backend"
        if ($Coverage) {
            python -m pytest --cov=customers --cov-report=html ../tests/unit/backend ../tests/integration/backend
        } else {
            python -m pytest ../tests/unit/backend ../tests/integration/backend
        }
    }
    "frontend" {
        Write-Host "Running frontend tests..." -ForegroundColor Yellow
        Set-Location "../frontend"
        if ($Coverage) {
            npm test -- --coverage --config ../tests/config/jest.config.cjs
        } else {
            npm test -- --config ../tests/config/jest.config.cjs
        }
    }
    "e2e" {
        Write-Host "Running E2E tests..." -ForegroundColor Yellow
        Set-Location "config"
        npx playwright test
    }
    "all" {
        Write-Host "Running all tests..." -ForegroundColor Yellow
        
        # Backend tests
        Write-Host "1. Backend tests..." -ForegroundColor Cyan
        Set-Location "../backend"
        python -m pytest ../tests/unit/backend ../tests/integration/backend
        
        # Frontend tests
        Write-Host "2. Frontend tests..." -ForegroundColor Cyan
        Set-Location "../frontend"
        npm test -- --config ../tests/config/jest.config.cjs --watchAll=false
        
        # E2E tests
        Write-Host "3. E2E tests..." -ForegroundColor Cyan
        Set-Location "../tests/config"
        npx playwright test
    }
    default {
        Write-Host "Invalid test type. Use: backend, frontend, e2e, or all" -ForegroundColor Red
        exit 1
    }
}

Write-Host "Tests completed!" -ForegroundColor Green