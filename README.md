# Customer Management System

Version: 0.2.0

A modern, full-stack customer management application built with Django, React, and Docker, designed with security and scalability in mind.

> **Note**: Currently on `develop` branch for testing GitHub Actions workflows.

## 🏗️ Architecture

- **Frontend**: React TypeScript with Vite, Tailwind CSS, Nginx, and pnpm workspaces
- **Backend**: Django with Python 3.13, PostgreSQL, and uv package management
- **Database**: Encrypted PostgreSQL with connection pooling
- **Infrastructure**: Docker Compose with multi-stage builds
- **CI/CD**: GitHub Actions with comprehensive testing and automated versioning
- **Security**: Multi-layer security with internal/external networks
- **Versioning**: Semantic versioning with conventional commits

## ✨ Features

- 📊 **Customer Management**: Full CRUD operations for customer data
- 🔍 **Advanced Search**: Search and filter customers by multiple criteria  
- 📈 **Dashboard**: Real-time statistics and insights
- 🔐 **Security**: HTTPS, encrypted database, secure networks
- 🚀 **Performance**: Caching, optimized queries, CDN-ready
- 📱 **Responsive**: Mobile-first design with modern UI
- 🧪 **Testing**: Unit, integration, and E2E testing
- 📝 **Logging**: Comprehensive logging and monitoring
- 🔄 **CI/CD**: Automated testing, deployment, and semantic versioning

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Git
- pnpm (for frontend development)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django-react
   ```

2. **Run the setup script**
   
   **Linux/Mac:**
   ```bash
   chmod +x scripts/development/setup-dev.sh
   ./scripts/development/setup-dev.sh
   ```
   
   **Windows (PowerShell):**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\scripts\development\setup-dev.ps1
   ```

3. **Access the application**
   - Frontend: http://localhost
   - API: http://localhost/api/
   - Admin: http://localhost/admin/ (admin/admin123)

## 🛠️ Development

### Project Structure

```
django-react/
├── backend/                    # Django application
│   ├── customer_management/    # Django project
│   ├── customers/             # Customer app
│   └── Dockerfile
├── frontend/                  # React application  
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   └── types/          # TypeScript definitions
│   └── Dockerfile
├── docs/                      # All documentation
│   ├── api/                  # API documentation
│   ├── development/          # Development guides
│   ├── design/              # Design documents
│   └── troubleshooting/     # Issue resolution
├── config/                    # System configurations
│   ├── docker/              # Docker configs
│   ├── nginx/               # Nginx configs
│   └── logging/             # Logging configs
├── scripts/                   # Development scripts
│   ├── development/         # Setup scripts
│   └── utilities/           # Utility scripts
├── tools/                     # Development tools
│   └── github/              # GitHub automation
├── .github/workflows/         # CI/CD pipelines
├── logs/                      # Application logs
└── docker-compose.yml         # Container orchestration
```

## 📝 API Documentation

### Customer Endpoints

- `GET /api/customers/` - List all customers
- `POST /api/customers/` - Create new customer
- `GET /api/customers/{id}/` - Get customer details
- `PUT /api/customers/{id}/` - Update customer
- `DELETE /api/customers/{id}/` - Delete customer
- `GET /api/customers/stats/` - Get customer statistics

### Query Parameters

- `search` - Search across name, email, phone
- `is_active` - Filter by active status
- `ordering` - Sort by field
- `page` - Pagination

## 🚀 Getting Started

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\scripts\development\setup-dev.ps1
```

**Linux/Mac:**
```bash
chmod +x scripts/development/setup-dev.sh
./scripts/development/setup-dev.sh
```

The setup script will:
- Create Docker networks
- Build and start all containers
- Run database migrations
- Create a Django superuser (admin/admin123)
- Load sample customer data
- Display access URLs and useful commands

## 🔒 Security Features

- **Network Isolation**: Internal network for backend services
- **Database Encryption**: PostgreSQL with encrypted connections
- **HTTPS**: SSL/TLS termination at Nginx
- **Security Headers**: OWASP-recommended headers
- **Input Validation**: Comprehensive data validation
- **Rate Limiting**: API rate limiting and DDoS protection

## 🧪 Testing

The project includes comprehensive testing:
- Unit tests for backend and frontend (Jest + React Testing Library)
- Integration tests with Docker
- Security scanning with Trivy
- Automated CI/CD with GitHub Actions

## 📊 Monitoring

- Application logs in `logs/` directory
- Health checks for all services
- Performance monitoring ready
- Log rotation configured

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Follow conventional commit format (see [VERSIONING.md](./VERSIONING.md))
5. Submit a pull request

## 📚 Documentation

- [**Documentation Index**](./docs/README.md) - Complete documentation overview
- [**Versioning Guide**](./docs/development/versioning.md) - Semantic versioning and conventional commits
- [**API Documentation**](./backend/README.md) - Backend API reference
- [**Frontend Guide**](./frontend/README.md) - React application documentation
- [**Frontend Testing**](./frontend/TESTING.md) - Frontend testing and mock system guide
- [**Issue #16 Analysis**](./docs/troubleshooting/issue-16-analysis.md) - React hooks test environment troubleshooting
- [**E2E Testing**](./e2e-tests/README.md) - End-to-end testing setup
- [**DevOps Tools**](./tools/README.md) - Infrastructure and monitoring tools
- [**Local GitHub Actions**](./docs/development/local-github-actions.md) - Running CI/CD pipelines locally with act

## 🏷️ Versioning

This project uses [Semantic Versioning](https://semver.org/) with automated releases based on [Conventional Commits](https://conventionalcommits.org/).

- **Major**: Breaking changes (e.g., `feat!: redesign API`)  
- **Minor**: New features (e.g., `feat: add customer search`)
- **Patch**: Bug fixes (e.g., `fix: resolve validation error`)

See [VERSIONING.md](./docs/development/versioning.md) for detailed information.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with modern web technologies and best practices for security, performance, and scalability.**