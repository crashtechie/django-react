# 🔄 Data Flow Diagrams - Customer Management System

## 📋 Overview
This document provides detailed data flow diagrams for all major operations in the Customer Management System, showing how data moves through the system components.

---

## 🏠 Application Startup Flow

```mermaid
sequenceDiagram
    participant U as User
    participant B as Browser
    participant N as Nginx
    participant R as React App
    participant D as Django API
    participant DB as PostgreSQL
    participant C as Redis Cache
    
    Note over U,C: Application Initialization
    U->>B: Navigate to application
    B->>N: GET /
    N->>R: Serve React app
    R-->>B: HTML + JS bundle
    B->>R: Initialize React
    R->>R: Load components
    R->>D: GET /api/health/
    D->>DB: Check database connection
    DB-->>D: Connection OK
    D->>C: Check cache connection
    C-->>D: Connection OK
    D-->>R: Health status OK
    R->>D: GET /api/customers/stats/
    D->>DB: Query customer statistics
    DB-->>D: Return stats
    D-->>R: Statistics data
    R->>R: Render dashboard
    R-->>U: Display application
```

---

## 👤 Customer Management Flows

### Create Customer Flow
```mermaid
sequenceDiagram
    participant U as User
    participant R as React Form
    participant V as Validation
    participant A as API Service
    participant D as Django API
    participant S as Serializer
    participant M as Model
    participant DB as PostgreSQL
    
    Note over U,DB: Customer Creation Process
    U->>R: Fill customer form
    R->>V: Validate form fields
    V->>V: Check required fields
    V->>V: Validate email format
    V->>V: Validate phone format
    V-->>R: Validation results
    
    alt Validation Success
        R->>A: POST customer data
        A->>D: POST /api/customers/
        D->>S: Deserialize data
        S->>S: Validate business rules
        S->>S: Sanitize input data
        S->>M: Create model instance
        M->>M: Apply model validation
        M->>DB: INSERT INTO customers
        DB-->>M: Return customer ID
        M-->>S: Model instance
        S-->>D: Serialized data
        D-->>A: 201 Created + data
        A-->>R: Success response
        R->>R: Update local state
        R->>R: Show success toast
        R-->>U: Display new customer
    else Validation Error
        V-->>R: Error messages
        R-->>U: Show form errors
    end
```

### Read Customer Flow
```mermaid
sequenceDiagram
    participant U as User
    participant R as React Component
    participant H as useCustomers Hook
    participant A as API Service
    participant D as Django API
    participant C as Cache
    participant DB as PostgreSQL
    
    Note over U,DB: Customer List Retrieval
    U->>R: Navigate to customer list
    R->>H: useCustomers()
    H->>A: GET customers
    A->>D: GET /api/customers/
    D->>C: Check cache
    
    alt Cache Hit
        C-->>D: Return cached data
        D-->>A: Customer list
    else Cache Miss
        D->>DB: SELECT * FROM customers
        DB-->>D: Customer records
        D->>C: Cache results
        D-->>A: Customer list
    end
    
    A-->>H: Customer data
    H->>H: Update state
    H-->>R: Customers array
    R->>R: Render customer cards
    R-->>U: Display customer list
```

### Update Customer Flow
```mermaid
sequenceDiagram
    participant U as User
    participant R as React Form
    participant A as API Service
    participant D as Django API
    participant S as Serializer
    participant M as Model
    participant DB as PostgreSQL
    participant C as Cache
    
    Note over U,C: Customer Update Process
    U->>R: Edit customer form
    R->>R: Pre-populate form
    U->>R: Modify customer data
    R->>A: PUT customer data
    A->>D: PUT /api/customers/{id}/
    D->>S: Validate updated data
    S->>M: Update model instance
    M->>DB: UPDATE customers SET...
    DB-->>M: Affected rows
    M-->>S: Updated instance
    S-->>D: Serialized data
    D->>C: Invalidate cache
    D-->>A: 200 OK + data
    A-->>R: Success response
    R->>R: Update local state
    R-->>U: Show updated customer
```

### Delete Customer Flow
```mermaid
sequenceDiagram
    participant U as User
    participant R as React Component
    participant C as Confirmation Modal
    participant A as API Service
    participant D as Django API
    participant M as Model
    participant DB as PostgreSQL
    participant Cache as Redis Cache
    
    Note over U,Cache: Customer Deletion Process
    U->>R: Click delete button
    R->>C: Show confirmation modal
    C-->>U: Confirm deletion?
    U->>C: Confirm delete
    C->>A: DELETE customer
    A->>D: DELETE /api/customers/{id}/
    D->>M: Get customer instance
    M->>DB: SELECT customer
    DB-->>M: Customer data
    M->>DB: DELETE FROM customers
    DB-->>M: Deletion confirmed
    M-->>D: Success
    D->>Cache: Invalidate cache
    D-->>A: 204 No Content
    A-->>R: Success response
    R->>R: Remove from local state
    R->>R: Show success message
    R-->>U: Updated customer list
```

---

## 🔍 Search and Filter Flow

```mermaid
sequenceDiagram
    participant U as User
    participant S as Search Component
    participant F as Filter Component
    participant A as API Service
    participant D as Django API
    participant Q as Query Builder
    participant DB as PostgreSQL
    
    Note over U,DB: Search and Filter Process
    U->>S: Enter search term
    S->>S: Debounce input (300ms)
    U->>F: Select filters
    F->>F: Update filter state
    
    par Search Query
        S->>A: GET with search params
    and Filter Query
        F->>A: GET with filter params
    end
    
    A->>D: GET /api/customers/?search=...&filter=...
    D->>Q: Build query with filters
    Q->>Q: Add search conditions
    Q->>Q: Add filter conditions
    Q->>Q: Add pagination
    Q->>DB: Execute complex query
    DB-->>Q: Filtered results
    Q-->>D: Query results
    D-->>A: Filtered customer list
    A-->>S: Search results
    A-->>F: Filter results
    S->>S: Update search state
    F->>F: Update filter state
    S-->>U: Display search results
    F-->>U: Display filter results
```

---

## 📊 Dashboard Statistics Flow

```mermaid
sequenceDiagram
    participant U as User
    participant D as Dashboard
    participant H as useStats Hook
    participant A as API Service
    participant API as Django API
    participant C as Cache
    participant DB as PostgreSQL
    
    Note over U,DB: Dashboard Data Loading
    U->>D: Navigate to dashboard
    D->>H: useStats()
    H->>A: GET statistics
    A->>API: GET /api/customers/stats/
    API->>C: Check cached stats
    
    alt Cache Hit (< 5 min old)
        C-->>API: Return cached stats
    else Cache Miss or Expired
        API->>DB: Complex aggregation query
        Note over DB: SELECT COUNT(*), AVG(created_at), etc.
        DB-->>API: Statistics data
        API->>C: Cache stats (5 min TTL)
    end
    
    API-->>A: Statistics response
    A-->>H: Stats data
    H->>H: Update state
    H-->>D: Statistics object
    D->>D: Render charts/metrics
    D-->>U: Display dashboard
    
    Note over U,DB: Real-time Updates (Optional)
    loop Every 30 seconds
        H->>A: Refresh stats
        A->>API: GET /api/customers/stats/
        API->>C: Check cache
        C-->>API: Fresh or cached data
        API-->>A: Updated stats
        A-->>H: New data
        H->>D: Update dashboard
    end
```

---

## 🔐 Authentication Flow

```mermaid
sequenceDiagram
    participant U as User
    participant L as Login Form
    participant A as Auth Service
    participant D as Django API
    participant Auth as Django Auth
    participant DB as PostgreSQL
    participant S as Session Store
    participant R as React App
    
    Note over U,R: Login Process
    U->>L: Enter credentials
    L->>L: Validate form
    L->>A: POST login data
    A->>D: POST /api/auth/login/
    D->>Auth: Authenticate user
    Auth->>DB: Verify credentials
    DB-->>Auth: User data
    
    alt Valid Credentials
        Auth->>S: Create session
        S-->>Auth: Session ID
        Auth-->>D: Authentication success
        D-->>A: Auth token + user data
        A->>A: Store token in localStorage
        A-->>L: Login success
        L->>R: Redirect to dashboard
        R-->>U: Show authenticated app
    else Invalid Credentials
        Auth-->>D: Authentication failed
        D-->>A: 401 Unauthorized
        A-->>L: Login error
        L-->>U: Show error message
    end
    
    Note over U,R: Subsequent API Calls
    loop For each API request
        R->>A: API call
        A->>A: Add auth header
        A->>D: Request with token
        D->>S: Validate session
        
        alt Valid Session
            S-->>D: Session valid
            D->>D: Process request
            D-->>A: Response data
            A-->>R: Success response
        else Invalid Session
            S-->>D: Session expired
            D-->>A: 401 Unauthorized
            A->>A: Clear stored token
            A->>R: Redirect to login
        end
    end
```

---

## ⚠️ Error Handling Flow

```mermaid
sequenceDiagram
    participant C as Component
    participant E as Error Boundary
    participant H as Error Handler
    participant L as Log Sanitizer
    participant A as API Service
    participant D as Django API
    participant Log as Logging System
    
    Note over C,Log: Component Error Flow
    C->>C: Component throws error
    C->>E: Error bubbles up
    E->>H: Handle error
    H->>L: Sanitize error data
    L->>L: Remove sensitive info
    L->>L: Clean stack traces
    L-->>H: Safe error message
    H->>Log: Log sanitized error
    H->>E: Return fallback UI data
    E->>E: Render error UI
    E-->>C: Display error boundary
    
    Note over C,Log: API Error Flow
    C->>A: Make API request
    A->>D: HTTP request
    D-->>A: Error response (4xx/5xx)
    A->>H: Handle API error
    H->>L: Sanitize error response
    L->>L: Remove server details
    L->>L: Clean error messages
    L-->>H: User-friendly message
    H->>Log: Log sanitized error
    H-->>A: Processed error
    A-->>C: User-friendly error
    C->>C: Show error toast/message
    
    Note over C,Log: Network Error Flow
    C->>A: Make API request
    A->>A: Network timeout/failure
    A->>H: Handle network error
    H->>L: Sanitize network error
    L-->>H: Generic network message
    H->>Log: Log network issue
    H-->>A: Network error response
    A-->>C: "Connection error" message
    C->>C: Show retry option
```

---

## 🔄 State Management Flow

```mermaid
sequenceDiagram
    participant U as User Action
    participant C as Component
    participant H as Custom Hook
    participant S as State Manager
    participant A as API Service
    participant L as Local Storage
    
    Note over U,L: State Update Flow
    U->>C: User interaction
    C->>H: Call hook function
    H->>S: Update state
    S->>S: Validate state change
    S->>A: Sync with API (if needed)
    
    par Local State Update
        S->>H: Notify state change
        H->>C: Re-render component
        C-->>U: UI updates
    and Persistence
        S->>L: Persist to localStorage
        L-->>S: Storage confirmed
    and API Sync
        A->>A: Queue API request
        A->>A: Execute request
        A-->>S: API response
        S->>S: Reconcile state
    end
    
    Note over U,L: State Hydration on Load
    C->>H: Component mounts
    H->>S: Initialize state
    S->>L: Load from localStorage
    L-->>S: Cached state
    S->>A: Validate with API
    A-->>S: Fresh data
    S->>S: Merge cached + fresh
    S->>H: Provide hydrated state
    H-->>C: Render with data
```

---

## 📱 Mobile Responsive Flow

```mermaid
sequenceDiagram
    participant M as Mobile User
    participant B as Mobile Browser
    participant R as React App
    participant H as useMediaQuery Hook
    participant C as Components
    
    Note over M,C: Responsive Behavior
    M->>B: Access application
    B->>R: Load React app
    R->>H: Check screen size
    H->>H: Detect mobile viewport
    H-->>R: Mobile breakpoint active
    R->>C: Pass mobile prop
    
    alt Mobile View
        C->>C: Render mobile layout
        C->>C: Stack components vertically
        C->>C: Use mobile navigation
        C->>C: Adjust touch targets
        C-->>M: Mobile-optimized UI
    else Desktop View
        C->>C: Render desktop layout
        C->>C: Use grid layout
        C->>C: Show sidebar navigation
        C->>C: Use hover states
        C-->>M: Desktop UI
    end
    
    Note over M,C: Orientation Change
    M->>B: Rotate device
    B->>R: Resize event
    R->>H: Re-check dimensions
    H-->>R: New breakpoint
    R->>C: Update layout props
    C->>C: Adjust layout
    C-->>M: Optimized for new orientation
```

---

## 🧪 Testing Data Flow

```mermaid
sequenceDiagram
    participant T as Test Suite
    participant M as Mock Service
    participant C as Component
    participant H as Hook
    participant A as API Service
    
    Note over T,A: Test Execution Flow
    T->>M: Setup mocks
    M->>M: Mock API responses
    M->>M: Mock localStorage
    M->>M: Mock external services
    
    T->>C: Render component
    C->>H: Use custom hook
    H->>A: Make API call
    A->>M: Intercepted by mock
    M-->>A: Mock response
    A-->>H: Mocked data
    H-->>C: Update component
    C-->>T: Component rendered
    
    T->>T: Assert expectations
    T->>T: Verify mock calls
    T->>T: Check component state
    T->>T: Validate UI elements
    
    T->>M: Cleanup mocks
    M->>M: Reset mock state
    M-->>T: Cleanup complete
```

---

## 🔒 Security Data Flow

```mermaid
sequenceDiagram
    participant U as User Input
    participant F as Frontend
    participant V as Validation
    participant S as Sanitization
    participant A as API
    participant D as Database
    
    Note over U,D: Secure Data Processing
    U->>F: Submit form data
    F->>V: Client-side validation
    V->>V: Check required fields
    V->>V: Validate formats
    V->>S: Sanitize input
    S->>S: Remove dangerous chars
    S->>S: Escape HTML entities
    S->>S: Validate data types
    S-->>F: Clean data
    
    F->>A: Send sanitized data
    A->>V: Server-side validation
    V->>V: Re-validate all fields
    V->>V: Check business rules
    V->>S: Re-sanitize data
    S->>S: Database-specific escaping
    S->>S: Log sanitization
    S-->>A: Database-safe data
    
    A->>D: Execute query
    D-->>A: Query results
    A->>S: Sanitize output
    S->>S: Remove sensitive data
    S->>S: Format for client
    S-->>A: Safe response
    A-->>F: Sanitized response
    F-->>U: Display safe data
```

---

**Last Updated**: January 27, 2025  
**Version**: 0.2.0  
**Status**: Comprehensive Data Flow Documentation