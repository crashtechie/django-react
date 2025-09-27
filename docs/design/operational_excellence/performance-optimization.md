# IT Performance Optimization and Operational Excellence

## Executive Summary

This document establishes comprehensive performance optimization practices for IT operations, covering application performance, infrastructure optimization, database tuning, and monitoring strategies. These practices ensure optimal system performance, scalability, and user experience while maintaining cost efficiency.

## 1. Application Performance Framework

### 1.1 Frontend Performance Optimization

**React Application Performance:**
```typescript
// Performance-optimized React components
import { memo, useMemo, useCallback, lazy, Suspense } from 'react'
import { debounce } from 'lodash'

// Memoized component to prevent unnecessary re-renders
const CustomerCard = memo(({ customer, onEdit, onDelete }) => {
  const handleEdit = useCallback(() => {
    onEdit(customer.id)
  }, [customer.id, onEdit])

  const handleDelete = useCallback(() => {
    onDelete(customer.id)
  }, [customer.id, onDelete])

  const formattedDate = useMemo(() => {
    return new Date(customer.created_at).toLocaleDateString()
  }, [customer.created_at])

  return (
    <div className="customer-card">
      <h3>{customer.name}</h3>
      <p>Created: {formattedDate}</p>
      <button onClick={handleEdit}>Edit</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  )
})

// Code splitting with lazy loading
const CustomerForm = lazy(() => import('./CustomerForm'))
const Dashboard = lazy(() => import('./Dashboard'))

// Optimized search with debouncing
const useOptimizedSearch = (searchTerm: string, delay: number = 300) => {
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)

  const debouncedSearch = useMemo(
    () => debounce(async (term: string) => {
      if (!term.trim()) {
        setResults([])
        return
      }

      setLoading(true)
      try {
        const response = await searchAPI(term)
        setResults(response.data)
      } catch (error) {
        console.error('Search failed:', error)
        setResults([])
      } finally {
        setLoading(false)
      }
    }, delay),
    [delay]
  )

  useEffect(() => {
    debouncedSearch(searchTerm)
    return () => debouncedSearch.cancel()
  }, [searchTerm, debouncedSearch])

  return { results, loading }
}

// Virtual scrolling for large lists
const VirtualizedCustomerList = ({ customers }) => {
  const [visibleRange, setVisibleRange] = useState({ start: 0, end: 50 })
  const containerRef = useRef<HTMLDivElement>(null)

  const handleScroll = useCallback(
    throttle(() => {
      if (!containerRef.current) return

      const { scrollTop, clientHeight } = containerRef.current
      const itemHeight = 100 // Estimated item height
      const start = Math.floor(scrollTop / itemHeight)
      const end = Math.min(start + Math.ceil(clientHeight / itemHeight) + 5, customers.length)

      setVisibleRange({ start, end })
    }, 16), // 60fps
    [customers.length]
  )

  const visibleCustomers = customers.slice(visibleRange.start, visibleRange.end)

  return (
    <div 
      ref={containerRef}
      className="virtualized-list"
      onScroll={handleScroll}
      style={{ height: '600px', overflowY: 'auto' }}
    >
      <div style={{ height: visibleRange.start * 100 }} />
      {visibleCustomers.map((customer, index) => (
        <CustomerCard 
          key={customer.id} 
          customer={customer}
          style={{ height: '100px' }}
        />
      ))}
      <div style={{ height: (customers.length - visibleRange.end) * 100 }} />
    </div>
  )
}
```

**Bundle Optimization:**
```javascript
// Webpack optimization configuration
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
          priority: 10
        },
        common: {
          name: 'common',
          minChunks: 2,
          chunks: 'all',
          priority: 5,
          reuseExistingChunk: true
        }
      }
    },
    usedExports: true,
    sideEffects: false,
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true,
            drop_debugger: true
          }
        }
      })
    ]
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
}

// Service Worker for caching
const CACHE_NAME = 'app-cache-v1'
const urlsToCache = [
  '/',
  '/static/js/bundle.js',
  '/static/css/main.css',
  '/api/customers'
]

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  )
})

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached version or fetch from network
        return response || fetch(event.request)
      })
  )
})
```

### 1.2 Backend Performance Optimization

**Django Performance Optimization:**
```python
# Database query optimization
from django.db import models
from django.db.models import Prefetch, Count, Q
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class OptimizedCustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        """Optimized queryset with selective prefetching."""
        queryset = Customer.objects.select_related('company', 'created_by')
        
        # Conditional prefetching based on request
        if self.action == 'list':
            # For list view, only fetch essential fields
            queryset = queryset.only(
                'id', 'first_name', 'last_name', 'email', 
                'phone', 'is_active', 'created_at'
            )
        elif self.action == 'retrieve':
            # For detail view, prefetch related data
            queryset = queryset.prefetch_related(
                'orders__items',
                'addresses',
                'notes'
            )
        
        return queryset
    
    @method_decorator(cache_page(60 * 5))  # Cache for 5 minutes
    def list(self, request, *args, **kwargs):
        """Cached list view with pagination."""
        return super().list(request, *args, **kwargs)
    
    def get_customer_stats(self, request):
        """Optimized statistics calculation."""
        cache_key = 'customer_stats'
        stats = cache.get(cache_key)
        
        if stats is None:
            stats = Customer.objects.aggregate(
                total_customers=Count('id'),
                active_customers=Count('id', filter=Q(is_active=True)),
                inactive_customers=Count('id', filter=Q(is_active=False))
            )
            
            # Cache for 10 minutes
            cache.set(cache_key, stats, 600)
        
        return Response(stats)

# Database connection optimization
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customer_db',
        'USER': 'app_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'MAX_CONNS': 20,
            'MIN_CONNS': 5,
        },
        'CONN_MAX_AGE': 600,  # Connection pooling
    }
}

# Redis caching configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True,
            }
        },
        'KEY_PREFIX': 'customer_app',
        'TIMEOUT': 300,  # 5 minutes default
    }
}

# Async task processing with Celery
from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True, max_retries=3)
def send_customer_notification(self, customer_id, message):
    """Async email notification task."""
    try:
        customer = Customer.objects.get(id=customer_id)
        send_mail(
            subject='Customer Notification',
            message=message,
            from_email='noreply@company.com',
            recipient_list=[customer.email],
            fail_silently=False
        )
    except Exception as exc:
        # Retry with exponential backoff
        raise self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))
```

**API Response Optimization:**
```python
# Response compression and optimization
from django.middleware.gzip import GZipMiddleware
from django.http import JsonResponse
import json
from decimal import Decimal

class OptimizedJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for better performance."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class PerformanceMiddleware:
    """Custom middleware for performance optimization."""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Add performance headers
        response = self.get_response(request)
        
        # Enable compression
        if response.get('Content-Type', '').startswith('application/json'):
            response['Content-Encoding'] = 'gzip'
        
        # Add caching headers
        if request.method == 'GET':
            response['Cache-Control'] = 'public, max-age=300'
            response['ETag'] = self.generate_etag(response.content)
        
        return response
    
    def generate_etag(self, content):
        """Generate ETag for response caching."""
        import hashlib
        return hashlib.md5(content).hexdigest()

# Pagination optimization
class OptimizedPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })
```

## 2. Database Performance Optimization

### 2.1 PostgreSQL Optimization

**Database Configuration:**
```sql
-- PostgreSQL performance configuration
-- Memory settings
shared_buffers = '256MB'                    -- 25% of RAM
effective_cache_size = '1GB'                -- 75% of RAM
work_mem = '4MB'                           -- Per connection
maintenance_work_mem = '64MB'              -- For maintenance operations

-- Connection settings
max_connections = 100
shared_preload_libraries = 'pg_stat_statements'

-- Query optimization
random_page_cost = 1.1                     -- For SSD storage
effective_io_concurrency = 200             -- For SSD storage
default_statistics_target = 100            -- Query planner statistics

-- WAL settings for performance
wal_buffers = '16MB'
checkpoint_completion_target = 0.9
wal_writer_delay = '200ms'

-- Logging for performance monitoring
log_min_duration_statement = 1000          -- Log slow queries (1 second)
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on
```

**Index Optimization:**
```sql
-- Performance-optimized indexes
-- Composite index for common queries
CREATE INDEX CONCURRENTLY idx_customers_active_created 
ON customers (is_active, created_at DESC) 
WHERE is_active = true;

-- Partial index for active customers
CREATE INDEX CONCURRENTLY idx_customers_email_active 
ON customers (email) 
WHERE is_active = true;

-- GIN index for full-text search
CREATE INDEX CONCURRENTLY idx_customers_search 
ON customers USING gin(to_tsvector('english', first_name || ' ' || last_name || ' ' || email));

-- Index for JSON data
CREATE INDEX CONCURRENTLY idx_customers_metadata 
ON customers USING gin(metadata);

-- Analyze index usage
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- Find unused indexes
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexname NOT LIKE '%_pkey';
```

**Query Optimization:**
```sql
-- Optimized queries with proper indexing
-- Before: Slow query
SELECT * FROM customers 
WHERE created_at > '2023-01-01' 
AND is_active = true 
ORDER BY created_at DESC;

-- After: Optimized query
SELECT id, first_name, last_name, email, phone, created_at
FROM customers 
WHERE is_active = true 
AND created_at > '2023-01-01'::date
ORDER BY created_at DESC
LIMIT 50;

-- Use EXPLAIN ANALYZE to check query performance
EXPLAIN (ANALYZE, BUFFERS) 
SELECT c.*, co.name as company_name
FROM customers c
LEFT JOIN companies co ON c.company_id = co.id
WHERE c.is_active = true
ORDER BY c.created_at DESC
LIMIT 25;

-- Materialized view for complex aggregations
CREATE MATERIALIZED VIEW customer_stats AS
SELECT 
    DATE_TRUNC('month', created_at) as month,
    COUNT(*) as total_customers,
    COUNT(*) FILTER (WHERE is_active = true) as active_customers,
    AVG(EXTRACT(EPOCH FROM (NOW() - created_at))/86400) as avg_age_days
FROM customers
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month;

-- Refresh materialized view periodically
CREATE OR REPLACE FUNCTION refresh_customer_stats()
RETURNS void AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY customer_stats;
END;
$$ LANGUAGE plpgsql;

-- Schedule refresh (using pg_cron extension)
SELECT cron.schedule('refresh-stats', '0 */6 * * *', 'SELECT refresh_customer_stats();');
```

### 2.2 Connection Pooling and Caching

**Connection Pool Configuration:**
```python
# Database connection pooling with pgbouncer
# pgbouncer.ini configuration
[databases]
customer_db = host=localhost port=5432 dbname=customer_db user=app_user

[pgbouncer]
pool_mode = transaction
listen_port = 6432
listen_addr = 127.0.0.1
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
logfile = /var/log/pgbouncer/pgbouncer.log
pidfile = /var/run/pgbouncer/pgbouncer.pid
admin_users = admin
stats_users = stats, admin

# Connection pool settings
max_client_conn = 100
default_pool_size = 20
min_pool_size = 5
reserve_pool_size = 5
reserve_pool_timeout = 5
max_db_connections = 50
max_user_connections = 50

# Performance settings
server_reset_query = DISCARD ALL
server_check_query = SELECT 1
server_check_delay = 30
server_lifetime = 3600
server_idle_timeout = 600

# Django settings for connection pooling
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customer_db',
        'USER': 'app_user',
        'PASSWORD': 'secure_password',
        'HOST': '127.0.0.1',
        'PORT': '6432',  # pgbouncer port
        'CONN_MAX_AGE': 0,  # Let pgbouncer handle connections
        'OPTIONS': {
            'MAX_CONNS': 20,
            'MIN_CONNS': 5,
        }
    }
}
```

**Redis Caching Strategy:**
```python
# Advanced caching strategies
import redis
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
import pickle
import json

class AdvancedCacheManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True,
            max_connections=20
        )
        self.default_timeout = 300  # 5 minutes
    
    def get_or_set_complex(self, key, callable_func, timeout=None):
        """Get from cache or set with complex data."""
        timeout = timeout or self.default_timeout
        
        # Try to get from cache
        cached_data = cache.get(key)
        if cached_data is not None:
            return cached_data
        
        # Generate data and cache it
        data = callable_func()
        cache.set(key, data, timeout)
        return data
    
    def cache_customer_data(self, customer_id):
        """Cache customer data with related information."""
        cache_key = f"customer:{customer_id}:full"
        
        def get_customer_data():
            customer = Customer.objects.select_related('company').get(id=customer_id)
            return {
                'customer': CustomerSerializer(customer).data,
                'orders': OrderSerializer(customer.orders.all()[:10], many=True).data,
                'last_activity': customer.last_activity.isoformat() if customer.last_activity else None
            }
        
        return self.get_or_set_complex(cache_key, get_customer_data, timeout=600)
    
    def invalidate_customer_cache(self, customer_id):
        """Invalidate all customer-related cache entries."""
        patterns = [
            f"customer:{customer_id}:*",
            f"customer_list:*",
            f"customer_stats:*"
        ]
        
        for pattern in patterns:
            keys = self.redis_client.keys(pattern)
            if keys:
                self.redis_client.delete(*keys)
    
    def cache_with_tags(self, key, data, tags, timeout=None):
        """Cache data with tags for group invalidation."""
        timeout = timeout or self.default_timeout
        
        # Store the data
        cache.set(key, data, timeout)
        
        # Store tag associations
        for tag in tags:
            tag_key = f"tag:{tag}"
            tagged_keys = cache.get(tag_key, set())
            tagged_keys.add(key)
            cache.set(tag_key, tagged_keys, timeout)
    
    def invalidate_by_tag(self, tag):
        """Invalidate all cache entries with a specific tag."""
        tag_key = f"tag:{tag}"
        tagged_keys = cache.get(tag_key, set())
        
        if tagged_keys:
            cache.delete_many(list(tagged_keys))
            cache.delete(tag_key)

# Usage in views
cache_manager = AdvancedCacheManager()

class CustomerViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, pk=None):
        # Use advanced caching
        customer_data = cache_manager.cache_customer_data(pk)
        return Response(customer_data)
    
    def update(self, request, pk=None):
        response = super().update(request, pk)
        # Invalidate cache after update
        cache_manager.invalidate_customer_cache(pk)
        return response
```

## 3. Infrastructure Performance Optimization

### 3.1 Container and Orchestration Optimization

**Docker Performance Optimization:**
```dockerfile
# Multi-stage optimized Dockerfile
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production --no-audit --no-fund && \
    npm cache clean --force

FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --no-audit --no-fund
COPY . .
RUN npm run build

FROM node:18-alpine AS runtime
# Install dumb-init for proper signal handling
RUN apk add --no-cache dumb-init

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

WORKDIR /app

# Copy built application
COPY --from=builder --chown=nextjs:nodejs /app/dist ./dist
COPY --from=dependencies --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs package*.json ./

USER nextjs

EXPOSE 3000

# Use dumb-init for proper signal handling
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/server.js"]

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

**Kubernetes Resource Optimization:**
```yaml
# Optimized Kubernetes deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customer-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: customer-app
  template:
    metadata:
      labels:
        app: customer-app
    spec:
      containers:
      - name: app
        image: customer-app:latest
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url

---
# Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: customer-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: customer-app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

### 3.2 Load Balancing and CDN

**Nginx Load Balancer Configuration:**
```nginx
# High-performance Nginx configuration
upstream backend {
    least_conn;
    server app1:3000 max_fails=3 fail_timeout=30s;
    server app2:3000 max_fails=3 fail_timeout=30s;
    server app3:3000 max_fails=3 fail_timeout=30s;
    keepalive 32;
}

server {
    listen 80;
    listen 443 ssl http2;
    server_name customer-app.com;

    # SSL configuration
    ssl_certificate /etc/ssl/certs/customer-app.crt;
    ssl_certificate_key /etc/ssl/private/customer-app.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # Performance optimizations
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/json
        application/javascript
        application/xml+rss
        application/atom+xml
        image/svg+xml;

    # Caching
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        add_header Vary Accept-Encoding;
    }

    # API proxy
    location /api/ {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        
        # Timeouts
        proxy_connect_timeout 5s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
        
        # Buffer settings
        proxy_buffering on;
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
    }

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;

    location /api/auth/login {
        limit_req zone=login burst=3 nodelay;
        proxy_pass http://backend;
    }

    location /api/ {
        limit_req zone=api burst=20 nodelay;
        proxy_pass http://backend;
    }
}
```

## 4. Monitoring and Performance Analytics

### 4.1 Application Performance Monitoring

**Performance Monitoring System:**
```python
# Comprehensive performance monitoring
import time
import psutil
import logging
from functools import wraps
from django.db import connection
from django.core.cache import cache
import threading
from collections import defaultdict

class PerformanceMonitor:
    def __init__(self):
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
        self.logger = logging.getLogger('performance')
    
    def track_execution_time(self, func_name=None):
        """Decorator to track function execution time."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    execution_time = time.time() - start_time
                    name = func_name or f"{func.__module__}.{func.__name__}"
                    self.record_metric('execution_time', name, execution_time)
                    
                    # Log slow operations
                    if execution_time > 1.0:  # 1 second threshold
                        self.logger.warning(f"Slow operation: {name} took {execution_time:.2f}s")
            
            return wrapper
        return decorator
    
    def track_database_queries(self):
        """Context manager to track database query performance."""
        class DatabaseTracker:
            def __init__(self, monitor):
                self.monitor = monitor
                self.initial_queries = 0
            
            def __enter__(self):
                self.initial_queries = len(connection.queries)
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                query_count = len(connection.queries) - self.initial_queries
                total_time = sum(float(q['time']) for q in connection.queries[self.initial_queries:])
                
                self.monitor.record_metric('db_queries', 'count', query_count)
                self.monitor.record_metric('db_queries', 'time', total_time)
                
                # Log excessive queries
                if query_count > 10:
                    self.monitor.logger.warning(f"High query count: {query_count} queries")
        
        return DatabaseTracker(self)
    
    def record_metric(self, category, name, value):
        """Record a performance metric."""
        with self.lock:
            self.metrics[f"{category}.{name}"].append({
                'value': value,
                'timestamp': time.time()
            })
    
    def get_system_metrics(self):
        """Get current system performance metrics."""
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'network_io': psutil.net_io_counters()._asdict(),
            'process_count': len(psutil.pids())
        }
    
    def generate_performance_report(self):
        """Generate comprehensive performance report."""
        with self.lock:
            report = {
                'system_metrics': self.get_system_metrics(),
                'application_metrics': {},
                'recommendations': []
            }
            
            # Analyze application metrics
            for metric_name, values in self.metrics.items():
                if values:
                    recent_values = [v['value'] for v in values[-100:]]  # Last 100 values
                    report['application_metrics'][metric_name] = {
                        'avg': sum(recent_values) / len(recent_values),
                        'max': max(recent_values),
                        'min': min(recent_values),
                        'count': len(recent_values)
                    }
            
            # Generate recommendations
            report['recommendations'] = self.generate_recommendations(report)
            
            return report
    
    def generate_recommendations(self, report):
        """Generate performance optimization recommendations."""
        recommendations = []
        
        # CPU recommendations
        if report['system_metrics']['cpu_percent'] > 80:
            recommendations.append({
                'type': 'cpu',
                'severity': 'high',
                'message': 'High CPU usage detected. Consider scaling horizontally or optimizing CPU-intensive operations.'
            })
        
        # Memory recommendations
        if report['system_metrics']['memory_percent'] > 85:
            recommendations.append({
                'type': 'memory',
                'severity': 'high',
                'message': 'High memory usage detected. Check for memory leaks or consider increasing available memory.'
            })
        
        # Database recommendations
        db_metrics = report['application_metrics'].get('db_queries.count', {})
        if db_metrics.get('avg', 0) > 20:
            recommendations.append({
                'type': 'database',
                'severity': 'medium',
                'message': 'High database query count. Consider query optimization or caching strategies.'
            })
        
        return recommendations

# Usage in Django views
performance_monitor = PerformanceMonitor()

class OptimizedCustomerViewSet(viewsets.ModelViewSet):
    
    @performance_monitor.track_execution_time('customer_list')
    def list(self, request, *args, **kwargs):
        with performance_monitor.track_database_queries():
            return super().list(request, *args, **kwargs)
    
    @performance_monitor.track_execution_time('customer_create')
    def create(self, request, *args, **kwargs):
        with performance_monitor.track_database_queries():
            return super().create(request, *args, **kwargs)
```

### 4.2 Real-time Performance Dashboard

**Performance Dashboard Implementation:**
```python
# Real-time performance dashboard
from django.http import JsonResponse
from django.views import View
import json
from datetime import datetime, timedelta

class PerformanceDashboardView(View):
    def get(self, request):
        """Return real-time performance metrics."""
        
        # Get current performance data
        performance_data = {
            'timestamp': datetime.now().isoformat(),
            'system_metrics': performance_monitor.get_system_metrics(),
            'application_metrics': self.get_application_metrics(),
            'database_metrics': self.get_database_metrics(),
            'cache_metrics': self.get_cache_metrics(),
            'alerts': self.get_performance_alerts()
        }
        
        return JsonResponse(performance_data)
    
    def get_application_metrics(self):
        """Get application-specific performance metrics."""
        return {
            'active_users': self.get_active_user_count(),
            'request_rate': self.get_request_rate(),
            'response_times': self.get_response_time_percentiles(),
            'error_rate': self.get_error_rate()
        }
    
    def get_database_metrics(self):
        """Get database performance metrics."""
        from django.db import connection
        
        with connection.cursor() as cursor:
            # Get active connections
            cursor.execute("""
                SELECT count(*) as active_connections
                FROM pg_stat_activity 
                WHERE state = 'active'
            """)
            active_connections = cursor.fetchone()[0]
            
            # Get slow queries
            cursor.execute("""
                SELECT query, mean_time, calls
                FROM pg_stat_statements
                WHERE mean_time > 1000
                ORDER BY mean_time DESC
                LIMIT 5
            """)
            slow_queries = cursor.fetchall()
        
        return {
            'active_connections': active_connections,
            'slow_queries': [
                {
                    'query': query[:100] + '...' if len(query) > 100 else query,
                    'mean_time': mean_time,
                    'calls': calls
                }
                for query, mean_time, calls in slow_queries
            ]
        }
    
    def get_cache_metrics(self):
        """Get cache performance metrics."""
        try:
            from django_redis import get_redis_connection
            redis_conn = get_redis_connection("default")
            
            info = redis_conn.info()
            return {
                'hit_rate': info.get('keyspace_hits', 0) / max(info.get('keyspace_hits', 0) + info.get('keyspace_misses', 0), 1),
                'memory_usage': info.get('used_memory_human', '0B'),
                'connected_clients': info.get('connected_clients', 0),
                'operations_per_sec': info.get('instantaneous_ops_per_sec', 0)
            }
        except Exception:
            return {'error': 'Cache metrics unavailable'}
    
    def get_performance_alerts(self):
        """Get current performance alerts."""
        alerts = []
        
        system_metrics = performance_monitor.get_system_metrics()
        
        # CPU alert
        if system_metrics['cpu_percent'] > 80:
            alerts.append({
                'type': 'cpu',
                'severity': 'warning' if system_metrics['cpu_percent'] < 90 else 'critical',
                'message': f"High CPU usage: {system_metrics['cpu_percent']:.1f}%",
                'timestamp': datetime.now().isoformat()
            })
        
        # Memory alert
        if system_metrics['memory_percent'] > 85:
            alerts.append({
                'type': 'memory',
                'severity': 'warning' if system_metrics['memory_percent'] < 95 else 'critical',
                'message': f"High memory usage: {system_metrics['memory_percent']:.1f}%",
                'timestamp': datetime.now().isoformat()
            })
        
        return alerts

# WebSocket for real-time updates
import asyncio
import websockets
import json

class PerformanceWebSocketHandler:
    def __init__(self):
        self.clients = set()
    
    async def register_client(self, websocket):
        """Register a new WebSocket client."""
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)
    
    async def broadcast_metrics(self):
        """Broadcast performance metrics to all connected clients."""
        while True:
            if self.clients:
                # Get current metrics
                metrics = {
                    'timestamp': datetime.now().isoformat(),
                    'system': performance_monitor.get_system_metrics(),
                    'alerts': self.get_current_alerts()
                }
                
                # Send to all clients
                disconnected = set()
                for client in self.clients:
                    try:
                        await client.send(json.dumps(metrics))
                    except websockets.exceptions.ConnectionClosed:
                        disconnected.add(client)
                
                # Remove disconnected clients
                self.clients -= disconnected
            
            await asyncio.sleep(5)  # Update every 5 seconds
```

## 5. Performance Testing and Optimization

### 5.1 Load Testing Framework

**Automated Load Testing:**
```python
# Load testing with locust
from locust import HttpUser, task, between
import random
import json

class CustomerManagementUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Login user before starting tasks."""
        response = self.client.post("/api/auth/login", json={
            "username": "testuser",
            "password": "testpass"
        })
        
        if response.status_code == 200:
            self.token = response.json().get("token")
            self.client.headers.update({"Authorization": f"Bearer {self.token}"})
    
    @task(3)
    def list_customers(self):
        """Test customer list endpoint."""
        self.client.get("/api/customers/")
    
    @task(2)
    def get_customer_detail(self):
        """Test customer detail endpoint."""
        customer_id = random.randint(1, 100)
        self.client.get(f"/api/customers/{customer_id}/")
    
    @task(1)
    def create_customer(self):
        """Test customer creation."""
        customer_data = {
            "first_name": f"Test{random.randint(1, 1000)}",
            "last_name": f"User{random.randint(1, 1000)}",
            "email": f"test{random.randint(1, 1000)}@example.com",
            "phone": f"+1555{random.randint(1000000, 9999999)}"
        }
        
        response = self.client.post("/api/customers/", json=customer_data)
        
        if response.status_code == 201:
            # Test updating the created customer
            customer_id = response.json().get("id")
            if customer_id:
                self.client.put(f"/api/customers/{customer_id}/", json={
                    **customer_data,
                    "first_name": f"Updated{customer_data['first_name']}"
                })
    
    @task(1)
    def search_customers(self):
        """Test customer search functionality."""
        search_terms = ["john", "smith", "test", "user", "example"]
        search_term = random.choice(search_terms)
        self.client.get(f"/api/customers/?search={search_term}")
    
    @task(1)
    def get_dashboard_stats(self):
        """Test dashboard statistics endpoint."""
        self.client.get("/api/customers/stats/")

# Performance test runner
class PerformanceTestRunner:
    def __init__(self):
        self.results = {}
    
    def run_load_test(self, users=10, spawn_rate=2, duration=60):
        """Run load test with specified parameters."""
        import subprocess
        import tempfile
        import os
        
        # Create temporary locust file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(self.get_locust_script())
            locust_file = f.name
        
        try:
            # Run locust test
            cmd = [
                'locust',
                '-f', locust_file,
                '--headless',
                '--users', str(users),
                '--spawn-rate', str(spawn_rate),
                '--run-time', f'{duration}s',
                '--host', 'http://localhost:8000',
                '--csv', 'performance_results'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Parse results
            self.results = self.parse_locust_results('performance_results_stats.csv')
            
            return self.results
            
        finally:
            # Cleanup
            os.unlink(locust_file)
    
    def parse_locust_results(self, csv_file):
        """Parse locust CSV results."""
        import csv
        
        results = {}
        try:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    results[row['Name']] = {
                        'requests': int(row['Request Count']),
                        'failures': int(row['Failure Count']),
                        'avg_response_time': float(row['Average Response Time']),
                        'min_response_time': float(row['Min Response Time']),
                        'max_response_time': float(row['Max Response Time']),
                        'requests_per_sec': float(row['Requests/s'])
                    }
        except FileNotFoundError:
            pass
        
        return results
    
    def generate_performance_report(self):
        """Generate comprehensive performance report."""
        if not self.results:
            return "No performance test results available"
        
        report = {
            'summary': {
                'total_requests': sum(r['requests'] for r in self.results.values()),
                'total_failures': sum(r['failures'] for r in self.results.values()),
                'avg_response_time': sum(r['avg_response_time'] for r in self.results.values()) / len(self.results),
                'total_rps': sum(r['requests_per_sec'] for r in self.results.values())
            },
            'endpoint_details': self.results,
            'recommendations': self.generate_performance_recommendations()
        }
        
        return report
    
    def generate_performance_recommendations(self):
        """Generate performance optimization recommendations."""
        recommendations = []
        
        for endpoint, metrics in self.results.items():
            # Check response time
            if metrics['avg_response_time'] > 1000:  # 1 second
                recommendations.append({
                    'endpoint': endpoint,
                    'issue': 'High response time',
                    'current': f"{metrics['avg_response_time']:.0f}ms",
                    'recommendation': 'Optimize database queries, add caching, or improve algorithm efficiency'
                })
            
            # Check failure rate
            failure_rate = metrics['failures'] / max(metrics['requests'], 1) * 100
            if failure_rate > 1:  # 1% failure rate
                recommendations.append({
                    'endpoint': endpoint,
                    'issue': 'High failure rate',
                    'current': f"{failure_rate:.1f}%",
                    'recommendation': 'Investigate error causes, improve error handling, or increase resource allocation'
                })
        
        return recommendations
```

---

**Document Version**: 1.0  
**Last Updated**: Current Date  
**Review Cycle**: Quarterly  
**Owner**: IT Operations Team  
**Approval**: CTO