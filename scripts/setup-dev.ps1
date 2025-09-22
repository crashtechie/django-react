# Development setup script for Customer Management System (PowerShell)

Write-Host "🚀 Setting up Customer Management System for development..." -ForegroundColor Green

# Check if Docker and Docker Compose are installed
try {
    docker --version | Out-Null
    Write-Host "✅ Docker is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker is not installed. Please install Docker Desktop first." -ForegroundColor Red
    exit 1
}

try {
    docker-compose --version | Out-Null
    Write-Host "✅ Docker Compose is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker Compose is not installed. Please install Docker Desktop first." -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed for local development
try {
    node --version | Out-Null
    Write-Host "✅ Node.js is installed" -ForegroundColor Green
    
    # Install frontend dependencies for better IntelliSense
    Write-Host "📦 Installing frontend dependencies for IntelliSense..." -ForegroundColor Yellow
    Push-Location frontend
    npm install
    Pop-Location
} catch {
    Write-Host "⚠️ Node.js not found. Frontend dependencies won't be installed locally." -ForegroundColor Yellow
    Write-Host "   The application will still work in Docker containers." -ForegroundColor Yellow
}

# Create necessary directories
Write-Host "📁 Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path "logs/backend" -Force | Out-Null
New-Item -ItemType Directory -Path "logs/database" -Force | Out-Null
New-Item -ItemType Directory -Path "logs/web_server" -Force | Out-Null
New-Item -ItemType Directory -Path "secrets" -Force | Out-Null

# Set up secrets if they don't exist
if (-not (Test-Path "secrets/db_password.txt")) {
    Write-Host "🔐 Generating database password..." -ForegroundColor Yellow
    $timestamp = Get-Date -UFormat "%s"
    "secure_db_password_$timestamp" | Out-File -FilePath "secrets/db_password.txt" -Encoding utf8 -NoNewline
}

# Set up networks
Write-Host "🌐 Setting up Docker networks..." -ForegroundColor Yellow
& "scripts/setup-networks.ps1"

# Build and start services
Write-Host "🐳 Building and starting services..." -ForegroundColor Yellow
docker-compose up --build -d

# Wait for services to be healthy
Write-Host "⏳ Waiting for services to be healthy..." -ForegroundColor Yellow
$timeout = 300
$elapsed = 0
do {
    Start-Sleep -Seconds 10
    $elapsed += 10
    $status = docker-compose ps --format json | ConvertFrom-Json
    $healthy = $status | Where-Object { $_.Health -eq "healthy" }
    Write-Host "Waiting... ($elapsed/${timeout}s)" -ForegroundColor Cyan
} while ($healthy.Count -lt 3 -and $elapsed -lt $timeout)

if ($elapsed -ge $timeout) {
    Write-Host "❌ Services failed to become healthy within timeout" -ForegroundColor Red
    exit 1
}

# Run initial migrations
Write-Host "🗃️ Running database migrations..." -ForegroundColor Yellow
docker-compose exec backend uv run python manage.py migrate

# Create superuser (optional)
Write-Host "👤 Creating Django superuser..." -ForegroundColor Yellow
$createSuperuserScript = @"
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"@

docker-compose exec backend uv run python manage.py shell -c $createSuperuserScript

Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🎉 Customer Management System is ready!" -ForegroundColor Green
Write-Host ""
Write-Host "🔗 Access URLs:" -ForegroundColor Cyan
Write-Host "   - Frontend: http://localhost" -ForegroundColor White
Write-Host "   - Backend API: http://localhost/api/" -ForegroundColor White
Write-Host "   - Django Admin: http://localhost/admin/ (admin/admin123)" -ForegroundColor White
Write-Host ""
Write-Host "📋 Useful commands:" -ForegroundColor Cyan
Write-Host "   - View logs: docker-compose logs -f" -ForegroundColor White
Write-Host "   - Stop services: docker-compose down" -ForegroundColor White
Write-Host "   - Restart services: docker-compose restart" -ForegroundColor White
Write-Host "   - Access backend shell: docker-compose exec backend uv run python manage.py shell" -ForegroundColor White
Write-Host "   - Access database: docker-compose exec database psql -U postgres -d customer_management" -ForegroundColor White