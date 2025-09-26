# 🏗️ System Architecture - Customer Management System

## 📋 Overview
This document outlines the system architecture for the Django-React Customer Management System, including component relationships, data flow, and infrastructure design.

---

## 🏛️ High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        Browser[Web Browser]
        Mobile[Mobile Browser]
    end
    
    subgraph "Load Balancer & Proxy"
        Nginx[Nginx Reverse Proxy]
    end
    
    subgraph "Frontend Layer"
        React[React TypeScript App]
        Vite[Vite Dev Server]
        Static[Static Assets]
    end
    
    subgraph "Backend Layer"
        Django[Django REST API]
        DRF[Django REST Framework]
        Auth[Authentication]
    end
    
    subgraph "Data Layer"
        PostgreSQL[(PostgreSQL Database)]
        Redis[(Redis Cache)]
    end
    
    subgraph "Infrastructure"
        Docker[Docker Containers]
        Networks[Docker Networks]
        Volumes[Docker Volumes]
    end
    
    Browser --> Nginx
    Mobile --> Nginx
    Nginx --> React
    Nginx --> Django
    React --> DRF
    Django --> PostgreSQL
    Django --> Redis
    
    Docker --> React
    Docker --> Django
    Docker --> PostgreSQL
    Docker --> Redis
    Docker --> Nginx
```

---

## 🔧 Component Architecture

### Frontend Architecture
```mermaid
graph TD
    subgraph "React Application"
        App[App.tsx]
        Router[React Router]
        
        subgraph "Pages"
            Dashboard[Dashboard]
            CustomerList[Customer List]
            CustomerDetail[Customer Detail]
            CustomerForm[Customer Form]
        end
        
        subgraph "Components"
            Header[Header]
            Sidebar[Sidebar]
            LoadingSpinner[Loading Spinner]
            ErrorBoundary[Error Boundary]
            CustomerCard[Customer Card]
        end
        
        subgraph "Services"
            ApiService[API Service]
            AuthService[Auth Service]
            ErrorHandler[Error Handler]
        end
        
        subgraph "Hooks"
            useCustomers[useCustomers]
            useErrorHandler[useErrorHandler]
            useAuth[useAuth]
        end
        
        subgraph "Utils"
            Validation[Form Validation]
            Formatting[Data Formatting]
            LogSanitization[Log Sanitization]
        end
    end
    
    App --> Router
    Router --> Dashboard
    Router --> CustomerList
    Router --> CustomerDetail
    Router --> CustomerForm
    
    Dashboard --> CustomerCard
    CustomerList --> CustomerCard
    CustomerForm --> Validation
    
    Pages --> ApiService
    Pages --> useCustomers
    Pages --> useErrorHandler
    
    ApiService --> ErrorHandler
    ErrorHandler --> LogSanitization
```

### Backend Architecture
```mermaid
graph TD
    subgraph "Django Application"
        URLs[URL Configuration]
        Views[API Views]
        Serializers[DRF Serializers]
        Models[Django Models]
        
        subgraph "Customer App"
            CustomerModel[Customer Model]
            CustomerView[Customer ViewSet]
            CustomerSerializer[Customer Serializer]
            CustomerAdmin[Customer Admin]
        end
        
        subgraph "Middleware"
            CORS[CORS Middleware]
            Security[Security Middleware]
            Auth[Authentication]
        end
        
        subgraph "Settings"
            BaseSettings[Base Settings]
            DevSettings[Development]
            ProdSettings[Production]
        end
    end
    
    URLs --> Views
    Views --> Serializers
    Serializers --> Models
    
    CustomerView --> CustomerSerializer
    CustomerSerializer --> CustomerModel
    
    Views --> Middleware
    Middleware --> Auth
```

---

## 🌐 Network Architecture

```mermaid
graph TB
    subgraph "External Network"
        Internet[Internet]
        CDN[CDN/CloudFlare]
    end
    
    subgraph "Docker Networks"
        subgraph "External Network (customer-management-external)"
            NginxExt[Nginx:80/443]
        end
        
        subgraph "Internal Network (customer-management-internal)"
            ReactInt[React:3000]
            DjangoInt[Django:8000]
            PostgreSQLInt[PostgreSQL:5432]
            RedisInt[Redis:6379]
        end
    end
    
    Internet --> CDN
    CDN --> NginxExt
    NginxExt --> ReactInt
    NginxExt --> DjangoInt
    DjangoInt --> PostgreSQLInt
    DjangoInt --> RedisInt
    
    style NginxExt fill:#e1f5fe
    style ReactInt fill:#f3e5f5
    style DjangoInt fill:#e8f5e8
    style PostgreSQLInt fill:#fff3e0
    style RedisInt fill:#ffebee
```

---

## 💾 Data Architecture

### Database Schema
```mermaid
erDiagram
    Customer {
        int id PK
        string name
        string email UK
        string phone
        text address
        boolean is_active
        datetime created_at
        datetime updated_at
    }
    
    User {
        int id PK
        string username UK
        string email UK
        string password_hash
        boolean is_staff
        boolean is_active
        datetime created_at
        datetime last_login
    }
    
    Session {
        string session_key PK
        text session_data
        datetime expire_date
    }
    
    User ||--o{ Customer : manages
    User ||--o{ Session : has
```

### API Data Models
```mermaid
classDiagram
    class CustomerModel {
        +int id
        +string name
        +string email
        +string phone
        +string address
        +boolean is_active
        +datetime created_at
        +datetime updated_at
        +validate_email()
        +validate_phone()
        +__str__()
    }
    
    class CustomerSerializer {
        +Meta class
        +validate_email()
        +validate_phone()
        +create()
        +update()
    }
    
    class CustomerViewSet {
        +queryset
        +serializer_class
        +list()
        +create()
        +retrieve()
        +update()
        +destroy()
        +get_stats()
    }
    
    CustomerModel --> CustomerSerializer
    CustomerSerializer --> CustomerViewSet
```

---

## 🔄 Data Flow Diagrams

### Customer CRUD Operations
```mermaid
sequenceDiagram
    participant U as User
    participant R as React App
    participant N as Nginx
    participant D as Django API
    participant DB as PostgreSQL
    
    Note over U,DB: Create Customer Flow
    U->>R: Fill customer form
    R->>R: Validate form data
    R->>N: POST /api/customers/
    N->>D: Forward request
    D->>D: Validate & sanitize data
    D->>DB: INSERT customer
    DB-->>D: Return customer ID
    D-->>N: Return customer data
    N-->>R: Forward response
    R->>R: Update UI state
    R-->>U: Show success message
    
    Note over U,DB: Read Customer Flow
    U->>R: Navigate to customer list
    R->>N: GET /api/customers/
    N->>D: Forward request
    D->>DB: SELECT customers
    DB-->>D: Return customer data
    D-->>N: Return JSON response
    N-->>R: Forward response
    R->>R: Render customer cards
    R-->>U: Display customer list
```

### Authentication Flow
```mermaid
sequenceDiagram
    participant U as User
    participant R as React App
    participant D as Django API
    participant DB as PostgreSQL
    participant S as Session Store
    
    U->>R: Enter credentials
    R->>D: POST /api/auth/login/
    D->>DB: Validate user
    DB-->>D: Return user data
    D->>S: Create session
    S-->>D: Return session ID
    D-->>R: Return auth token
    R->>R: Store token
    R-->>U: Redirect to dashboard
    
    Note over U,S: Subsequent API Calls
    U->>R: Perform action
    R->>D: API call with token
    D->>S: Validate session
    S-->>D: Session valid
    D-->>R: Return data
    R-->>U: Update UI
```

### Error Handling Flow
```mermaid
sequenceDiagram
    participant R as React App
    participant E as Error Boundary
    participant H as Error Handler
    participant L as Log Sanitizer
    participant A as API Service
    participant D as Django API
    
    R->>A: API Request
    A->>D: HTTP Request
    D-->>A: Error Response (4xx/5xx)
    A->>H: Handle error
    H->>L: Sanitize error data
    L-->>H: Clean error message
    H->>E: Trigger error boundary
    E->>R: Display error UI
    H->>H: Log sanitized error
    
    Note over R,D: Component Error Flow
    R->>R: Component throws error
    R->>E: Error caught by boundary
    E->>H: Process error
    H->>L: Sanitize error
    L-->>H: Safe error message
    E->>R: Render fallback UI
```

---

## 🔒 Security Architecture

### Security Layers
```mermaid
graph TD
    subgraph "Security Layers"
        subgraph "Network Security"
            Firewall[Docker Network Isolation]
            SSL[SSL/TLS Termination]
            CORS[CORS Policy]
        end
        
        subgraph "Application Security"
            Auth[Authentication]
            CSRF[CSRF Protection]
            XSS[XSS Prevention]
            Validation[Input Validation]
        end
        
        subgraph "Data Security"
            Encryption[Database Encryption]
            Sanitization[Log Sanitization]
            Secrets[Secret Management]
        end
    end
    
    Internet --> Firewall
    Firewall --> SSL
    SSL --> CORS
    CORS --> Auth
    Auth --> CSRF
    CSRF --> XSS
    XSS --> Validation
    Validation --> Encryption
    Encryption --> Sanitization
    Sanitization --> Secrets
```

### Security Data Flow
```mermaid
sequenceDiagram
    participant C as Client
    participant N as Nginx (SSL)
    participant D as Django
    participant S as Sanitizer
    participant DB as Database
    
    Note over C,DB: Secure Request Flow
    C->>N: HTTPS Request
    N->>N: SSL Termination
    N->>D: HTTP to Django
    D->>D: CSRF Validation
    D->>D: Authentication Check
    D->>S: Sanitize Input
    S-->>D: Clean Data
    D->>DB: Encrypted Query
    DB-->>D: Encrypted Response
    D->>S: Sanitize Output
    S-->>D: Safe Response
    D-->>N: JSON Response
    N-->>C: HTTPS Response
```

---

## 🚀 Deployment Architecture

### Container Architecture
```mermaid
graph TB
    subgraph "Docker Compose Stack"
        subgraph "Web Tier"
            NginxC[nginx:alpine]
            ReactC[node:18-alpine]
        end
        
        subgraph "Application Tier"
            DjangoC[python:3.13-slim]
        end
        
        subgraph "Data Tier"
            PostgreSQLC[postgres:15-alpine]
            RedisC[redis:7-alpine]
        end
        
        subgraph "Volumes"
            StaticVol[static_volume]
            MediaVol[media_volume]
            DBVol[postgres_data]
            RedisVol[redis_data]
        end
        
        subgraph "Networks"
            ExtNet[customer-management-external]
            IntNet[customer-management-internal]
        end
    end
    
    NginxC --> StaticVol
    NginxC --> MediaVol
    DjangoC --> StaticVol
    DjangoC --> MediaVol
    PostgreSQLC --> DBVol
    RedisC --> RedisVol
    
    NginxC --> ExtNet
    ReactC --> IntNet
    DjangoC --> IntNet
    PostgreSQLC --> IntNet
    RedisC --> IntNet
```

### CI/CD Pipeline Architecture
```mermaid
graph LR
    subgraph "Development"
        Dev[Developer]
        Git[Git Repository]
    end
    
    subgraph "CI/CD Pipeline"
        GHA[GitHub Actions]
        Build[Build & Test]
        Security[Security Scan]
        Deploy[Deploy]
    end
    
    subgraph "Environments"
        Test[Test Environment]
        Staging[Staging Environment]
        Prod[Production Environment]
    end
    
    Dev --> Git
    Git --> GHA
    GHA --> Build
    Build --> Security
    Security --> Deploy
    Deploy --> Test
    Deploy --> Staging
    Deploy --> Prod
```

---

## 📊 Performance Architecture

### Caching Strategy
```mermaid
graph TD
    subgraph "Caching Layers"
        Browser[Browser Cache]
        CDN[CDN Cache]
        Nginx[Nginx Cache]
        Redis[Redis Cache]
        DB[Database Query Cache]
    end
    
    User --> Browser
    Browser --> CDN
    CDN --> Nginx
    Nginx --> React
    React --> Django
    Django --> Redis
    Redis --> DB
    
    style Browser fill:#e3f2fd
    style CDN fill:#f1f8e9
    style Nginx fill:#fff3e0
    style Redis fill:#fce4ec
    style DB fill:#f3e5f5
```

### Monitoring Architecture
```mermaid
graph TB
    subgraph "Application Monitoring"
        App[Application Metrics]
        Logs[Application Logs]
        Health[Health Checks]
    end
    
    subgraph "Infrastructure Monitoring"
        Docker[Container Metrics]
        System[System Metrics]
        Network[Network Metrics]
    end
    
    subgraph "Monitoring Stack"
        Prometheus[Prometheus]
        Grafana[Grafana]
        AlertManager[Alert Manager]
    end
    
    App --> Prometheus
    Logs --> Prometheus
    Health --> Prometheus
    Docker --> Prometheus
    System --> Prometheus
    Network --> Prometheus
    
    Prometheus --> Grafana
    Prometheus --> AlertManager
```

---

## 🔧 Technology Stack Summary

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React 18 + TypeScript | User interface |
| **Build Tool** | Vite | Fast development and building |
| **Styling** | Tailwind CSS | Utility-first CSS framework |
| **Backend** | Django 4.2 + DRF | REST API and business logic |
| **Database** | PostgreSQL 15 | Primary data storage |
| **Cache** | Redis 7 | Session storage and caching |
| **Web Server** | Nginx | Reverse proxy and static files |
| **Container** | Docker + Docker Compose | Containerization |
| **Testing** | Jest + React Testing Library | Frontend testing |
| **Testing** | pytest + Django Test | Backend testing |
| **CI/CD** | GitHub Actions | Automated testing and deployment |
| **Security** | OWASP Best Practices | Security hardening |

---

**Last Updated**: January 27, 2025  
**Version**: 0.2.0  
**Status**: Production Ready Architecture