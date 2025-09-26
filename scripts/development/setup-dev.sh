#!/bin/bash
# Development setup script for Customer Management System

set -e

echo "🚀 Setting up Customer Management System for development..."

# Check if Docker and Docker Compose are installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs/{backend,database,web_server}
mkdir -p secrets

# Set up secrets if they don't exist
if [ ! -f "secrets/db_password.txt" ]; then
    echo "🔐 Generating database password..."
    echo "secure_db_password_$(date +%s)" > secrets/db_password.txt
fi

# Set up networks
echo "🌐 Setting up Docker networks..."
chmod +x scripts/setup-networks.sh
./scripts/setup-networks.sh

# Build and start services
echo "🐳 Building and starting services..."
docker-compose up --build -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
timeout 300 bash -c 'until docker-compose ps | grep -q "healthy"; do echo "Waiting..."; sleep 10; done'

# Run initial migrations
echo "🗃️  Running database migrations..."
docker-compose exec backend uv run python manage.py migrate

# Create superuser (optional)
echo "👤 Creating Django superuser..."
docker-compose exec backend uv run python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Load sample data
echo "📊 Loading sample customer data..."
docker-compose exec backend uv run python manage.py shell -c "
import csv
from customers.models import Customer
from django.core.files import File

if Customer.objects.count() == 0:
    with open('/app/../design_docs/sample_customers.csv', 'r') as file:
        reader = csv.DictReader(file)
        customers = []
        for row in reader:
            customers.append(Customer(
                first_name=row['first_name'].strip('\"'),
                last_name=row['last_name'].strip('\"'),
                email=row['email'].strip('\"'),
                phone=row['phone'].strip('\"')
            ))
        Customer.objects.bulk_create(customers)
        print(f'Created {len(customers)} sample customers')
else:
    print('Sample data already exists')
"

echo "✅ Setup complete!"
echo ""
echo "🎉 Customer Management System is ready!"
echo ""
echo "🔗 Access URLs:"
echo "   - Frontend: http://localhost"
echo "   - Backend API: http://localhost/api/"
echo "   - Django Admin: http://localhost/admin/ (admin/admin123)"
echo ""
echo "📋 Useful commands:"
echo "   - View logs: docker-compose logs -f"
echo "   - Stop services: docker-compose down"
echo "   - Restart services: docker-compose restart"
echo "   - Access backend shell: docker-compose exec backend uv run python manage.py shell"
echo "   - Access database: docker-compose exec database psql -U postgres -d customer_management"