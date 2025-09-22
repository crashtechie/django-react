# Customer Management System Makefile
.PHONY: help build up down restart logs shell test clean setup

help:  ## Show this help message
	@echo "Customer Management System - Available Commands:"
	@echo "================================================"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

setup: ## Initial project setup
	@echo "Setting up Customer Management System..."
	@chmod +x scripts/setup-dev.sh
	@./scripts/setup-dev.sh

build: ## Build all containers
	docker-compose build

up: ## Start all services
	docker-compose up -d

down: ## Stop all services
	docker-compose down

restart: ## Restart all services
	docker-compose restart

logs: ## View logs from all services
	docker-compose logs -f

shell-backend: ## Access backend Django shell
	docker-compose exec backend uv run python manage.py shell

shell-db: ## Access database shell
	docker-compose exec database psql -U postgres -d customer_management

test-backend: ## Run backend tests
	docker-compose exec backend uv run pytest --cov=. --cov-report=html

test-frontend: ## Run frontend tests
	docker-compose exec frontend npm test

lint-backend: ## Run backend linting
	docker-compose exec backend uv run black --check .
	docker-compose exec backend uv run isort --check-only .
	docker-compose exec backend uv run flake8 .

lint-frontend: ## Run frontend linting
	docker-compose exec frontend npm run lint

migrate: ## Run Django migrations
	docker-compose exec backend uv run python manage.py migrate

makemigrations: ## Create Django migrations
	docker-compose exec backend uv run python manage.py makemigrations

collectstatic: ## Collect static files
	docker-compose exec backend uv run python manage.py collectstatic --noinput

superuser: ## Create Django superuser
	docker-compose exec backend uv run python manage.py createsuperuser

loaddata: ## Load sample data
	docker-compose exec backend uv run python manage.py shell -c "exec(open('/app/scripts/load_sample_data.py').read())"

clean: ## Clean up containers and volumes
	docker-compose down -v
	docker system prune -f

backup-db: ## Backup database
	docker-compose exec database pg_dump -U postgres customer_management > backup_$(shell date +%Y%m%d_%H%M%S).sql

restore-db: ## Restore database (usage: make restore-db FILE=backup.sql)
	docker-compose exec -T database psql -U postgres -d customer_management < $(FILE)

health: ## Check service health
	@echo "Checking service health..."
	@curl -f http://localhost/health || echo "Frontend health check failed"
	@curl -f http://localhost/api/customers/ || echo "Backend API health check failed"

dev-setup: ## Setup development environment
	@echo "Setting up development environment..."
	cd frontend && npm install
	cd backend && uv sync --dev

production: ## Deploy to production
	@echo "Deploying to production..."
	docker-compose -f docker-compose.prod.yml up --build -d