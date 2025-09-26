# Test Jest Configuration Verification Script
# This script verifies that the Jest configuration works correctly with the new centralized setup

Write-Host "Testing Jest Configuration for Issue #27..." -ForegroundColor Green

# Change to frontend directory
Set-Location "c:\Users\crash\Documents\django-react\frontend"

Write-Host "Current directory: $(Get-Location)" -ForegroundColor Yellow

# Test Jest config resolution
Write-Host "`nTesting Jest config resolution..." -ForegroundColor Cyan
$configResult = & pnpm exec jest --config ../tests/config/jest.config.cjs --listTests --passWithNoTests 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success: Jest config loads successfully" -ForegroundColor Green
} else {
    Write-Host "Error: Jest config failed to load: $configResult" -ForegroundColor Red
}

# Test if Jest can find test files
Write-Host "`nTesting test file discovery..." -ForegroundColor Cyan
$testFiles = & pnpm exec jest --config ../tests/config/jest.config.cjs --listTests 2>&1
if ($LASTEXITCODE -eq 0 -and $testFiles) {
    Write-Host "Success: Jest discovered test files:" -ForegroundColor Green
    $testFiles | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
} else {
    Write-Host "Warning: No test files discovered or error occurred" -ForegroundColor Yellow
    Write-Host "Output: $testFiles" -ForegroundColor Gray
}

# Test package.json scripts
Write-Host "`nTesting package.json test scripts..." -ForegroundColor Cyan
Write-Host "Testing pnpm test command..." -ForegroundColor Gray
$testResult = & pnpm test --listTests --passWithNoTests 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success: pnpm test script works" -ForegroundColor Green
} else {
    Write-Host "Error: pnpm test script failed: $testResult" -ForegroundColor Red
}

Write-Host "`nJest configuration test completed!" -ForegroundColor Green
Write-Host "If all tests passed the CI/CD pipeline should work correctly." -ForegroundColor Yellow