# Network setup script for Customer Management System (PowerShell)

Write-Host "Setting up Docker networks for Customer Management System..." -ForegroundColor Green

# Create external network if it doesn't exist
try {
    docker network inspect customer_management_external | Out-Null
    Write-Host "✓ External network already exists" -ForegroundColor Green
} catch {
    Write-Host "Creating external network..." -ForegroundColor Yellow
    docker network create `
        --driver bridge `
        --subnet=172.20.0.0/16 `
        --ip-range=172.20.240.0/20 `
        --gateway=172.20.0.1 `
        customer_management_external
    Write-Host "✓ External network created" -ForegroundColor Green
}

# Create internal network if it doesn't exist
try {
    docker network inspect customer_management_internal | Out-Null
    Write-Host "✓ Internal network already exists" -ForegroundColor Green
} catch {
    Write-Host "Creating internal network..." -ForegroundColor Yellow
    docker network create `
        --driver bridge `
        --internal `
        --subnet=172.21.0.0/16 `
        --ip-range=172.21.240.0/20 `
        --gateway=172.21.0.1 `
        customer_management_internal
    Write-Host "✓ Internal network created" -ForegroundColor Green
}

Write-Host "`nNetwork setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Networks:"
Write-Host "- External (customer_management_external): Frontend container only"
Write-Host "- Internal (customer_management_internal): Backend and database communication"
Write-Host ""
Write-Host "Security Features:"
Write-Host "- Internal network blocks external access"
Write-Host "- Frontend acts as reverse proxy to backend"
Write-Host "- Database only accessible from backend"