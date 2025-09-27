# IT Architectural Design Principles and Operational Excellence

## Executive Summary

This document establishes comprehensive architectural design principles for building scalable, maintainable, and resilient IT systems. These principles guide system design decisions, technology choices, and implementation strategies to ensure long-term operational excellence and business value delivery.

## 1. Core Architectural Principles

### 1.1 Scalability and Performance

**Horizontal Scaling Design:**
```python
# Microservices architecture pattern
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import asyncio
import aiohttp
from dataclasses import dataclass

@dataclass
class ServiceEndpoint:
    name: str
    host: str
    port: int
    health_check_path: str
    weight: int = 1
    max_connections: int = 100

class LoadBalancer:
    def __init__(self):
        self.services = {}
        self.health_status = {}
        self.connection_pools = {}
    
    def register_service(self, service_type: str, endpoint: ServiceEndpoint):
        """Register a service endpoint for load balancing."""
        if service_type not in self.services:
            self.services[service_type] = []
        
        self.services[service_type].append(endpoint)
        self.health_status[f"{endpoint.host}:{endpoint.port}"] = True
        
        # Initialize connection pool
        connector = aiohttp.TCPConnector(
            limit=endpoint.max_connections,
            limit_per_host=endpoint.max_connections
        )
        self.connection_pools[f"{endpoint.host}:{endpoint.port}"] = aiohttp.ClientSession(
            connector=connector
        )
    
    async def get_healthy_endpoint(self, service_type: str) -> Optional[ServiceEndpoint]:
        """Get a healthy endpoint using weighted round-robin."""
        if service_type not in self.services:
            return None
        
        healthy_endpoints = [
            endpoint for endpoint in self.services[service_type]
            if self.health_status.get(f"{endpoint.host}:{endpoint.port}", False)
        ]
        
        if not healthy_endpoints:
            return None
        
        # Weighted selection based on current load
        return self.select_endpoint_by_weight(healthy_endpoints)
    
    async def make_request(self, service_type: str, path: str, method: str = 'GET', **kwargs):
        """Make load-balanced request to service."""
        endpoint = await self.get_healthy_endpoint(service_type)
        
        if not endpoint:
            raise Exception(f"No healthy endpoints available for {service_type}")
        
        session = self.connection_pools[f"{endpoint.host}:{endpoint.port}"]
        url = f"http://{endpoint.host}:{endpoint.port}{path}"
        
        try:
            async with session.request(method, url, **kwargs) as response:
                return await response.json()
        except Exception as e:
            # Mark endpoint as unhealthy and retry
            self.health_status[f"{endpoint.host}:{endpoint.port}"] = False
            await self.schedule_health_check(endpoint)
            raise

class ServiceMesh:
    """Service mesh implementation for microservices communication."""
    
    def __init__(self):
        self.load_balancer = LoadBalancer()
        self.circuit_breakers = {}
        self.retry_policies = {}
        self.timeout_policies = {}
    
    def configure_circuit_breaker(self, service: str, failure_threshold: int = 5, 
                                 recovery_timeout: int = 60):
        """Configure circuit breaker for service."""
        self.circuit_breakers[service] = {
            'failure_count': 0,
            'failure_threshold': failure_threshold,
            'state': 'closed',  # closed, open, half-open
            'last_failure_time': None,
            'recovery_timeout': recovery_timeout
        }
    
    def configure_retry_policy(self, service: str, max_retries: int = 3, 
                              backoff_multiplier: float = 2.0):
        """Configure retry policy for service."""
        self.retry_policies[service] = {
            'max_retries': max_retries,
            'backoff_multiplier': backoff_multiplier,
            'initial_delay': 1.0
        }
    
    async def call_service(self, service: str, path: str, method: str = 'GET', **kwargs):
        """Make resilient service call with circuit breaker and retries."""
        # Check circuit breaker
        if not self.is_circuit_closed(service):
            raise Exception(f"Circuit breaker open for {service}")
        
        # Apply retry policy
        retry_policy = self.retry_policies.get(service, {'max_retries': 0})
        
        for attempt in range(retry_policy['max_retries'] + 1):
            try:
                result = await self.load_balancer.make_request(service, path, method, **kwargs)
                
                # Reset circuit breaker on success
                if service in self.circuit_breakers:
                    self.circuit_breakers[service]['failure_count'] = 0
                
                return result
                
            except Exception as e:
                # Update circuit breaker
                self.record_failure(service)
                
                if attempt < retry_policy['max_retries']:
                    delay = retry_policy.get('initial_delay', 1.0) * (
                        retry_policy.get('backoff_multiplier', 2.0) ** attempt
                    )
                    await asyncio.sleep(delay)
                else:
                    raise

# Database sharding strategy
class DatabaseShardManager:
    def __init__(self):
        self.shards = {}
        self.shard_mapping = {}
        self.replication_config = {}
    
    def add_shard(self, shard_id: str, connection_config: Dict):
        """Add a database shard."""
        self.shards[shard_id] = connection_config
    
    def get_shard_for_key(self, key: str) -> str:
        """Determine which shard to use for a given key."""
        # Consistent hashing for shard selection
        import hashlib
        
        hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
        shard_count = len(self.shards)
        shard_index = hash_value % shard_count
        
        return list(self.shards.keys())[shard_index]
    
    def execute_query(self, key: str, query: str, params: List = None):
        """Execute query on appropriate shard."""
        shard_id = self.get_shard_for_key(key)
        connection_config = self.shards[shard_id]
        
        # Execute query on selected shard
        return self.execute_on_shard(shard_id, query, params)
    
    def execute_cross_shard_query(self, query: str, params: List = None):
        """Execute query across all shards and aggregate results."""
        results = []
        
        for shard_id in self.shards:
            shard_result = self.execute_on_shard(shard_id, query, params)
            results.extend(shard_result)
        
        return results
```

### 1.2 Resilience and Fault Tolerance

**Resilience Patterns Implementation:**
```python
# Comprehensive resilience patterns
import asyncio
import time
import random
from typing import Callable, Any, Optional
from functools import wraps
from enum import Enum

class CircuitBreakerState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60, 
                 expected_exception: type = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitBreakerState.CLOSED
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if self.state == CircuitBreakerState.OPEN:
                if self._should_attempt_reset():
                    self.state = CircuitBreakerState.HALF_OPEN
                else:
                    raise Exception("Circuit breaker is OPEN")
            
            try:
                result = await func(*args, **kwargs)
                self._on_success()
                return result
            except self.expected_exception as e:
                self._on_failure()
                raise
        
        return wrapper
    
    def _should_attempt_reset(self) -> bool:
        return (time.time() - self.last_failure_time) >= self.recovery_timeout
    
    def _on_success(self):
        self.failure_count = 0
        self.state = CircuitBreakerState.CLOSED
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitBreakerState.OPEN

class RetryPolicy:
    def __init__(self, max_attempts: int = 3, base_delay: float = 1.0, 
                 max_delay: float = 60.0, exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(self.max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    
                    if attempt < self.max_attempts - 1:
                        delay = self._calculate_delay(attempt)
                        await asyncio.sleep(delay)
                    else:
                        raise last_exception
        
        return wrapper
    
    def _calculate_delay(self, attempt: int) -> float:
        delay = self.base_delay * (self.exponential_base ** attempt)
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            delay *= (0.5 + random.random() * 0.5)  # Add 0-50% jitter
        
        return delay

class BulkheadPattern:
    """Isolate resources to prevent cascade failures."""
    
    def __init__(self):
        self.resource_pools = {}
        self.pool_limits = {}
        self.active_requests = {}
    
    def create_resource_pool(self, pool_name: str, max_concurrent: int):
        """Create a resource pool with concurrency limits."""
        self.resource_pools[pool_name] = asyncio.Semaphore(max_concurrent)
        self.pool_limits[pool_name] = max_concurrent
        self.active_requests[pool_name] = 0
    
    def isolate_resource(self, pool_name: str):
        """Decorator to isolate resource usage."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                if pool_name not in self.resource_pools:
                    raise ValueError(f"Resource pool {pool_name} not found")
                
                semaphore = self.resource_pools[pool_name]
                
                async with semaphore:
                    self.active_requests[pool_name] += 1
                    try:
                        return await func(*args, **kwargs)
                    finally:
                        self.active_requests[pool_name] -= 1
            
            return wrapper
        return decorator
    
    def get_pool_status(self, pool_name: str) -> Dict:
        """Get current status of resource pool."""
        if pool_name not in self.resource_pools:
            return {"error": "Pool not found"}
        
        semaphore = self.resource_pools[pool_name]
        return {
            "pool_name": pool_name,
            "max_concurrent": self.pool_limits[pool_name],
            "available_slots": semaphore._value,
            "active_requests": self.active_requests[pool_name],
            "utilization": (self.active_requests[pool_name] / self.pool_limits[pool_name]) * 100
        }

# Usage example
bulkhead = BulkheadPattern()
bulkhead.create_resource_pool("database", 10)
bulkhead.create_resource_pool("external_api", 5)
bulkhead.create_resource_pool("file_processing", 3)

@CircuitBreaker(failure_threshold=3, recovery_timeout=30)
@RetryPolicy(max_attempts=3, base_delay=1.0)
@bulkhead.isolate_resource("database")
async def database_operation():
    """Example database operation with resilience patterns."""
    # Simulate database operation
    if random.random() < 0.1:  # 10% failure rate
        raise Exception("Database connection failed")
    
    await asyncio.sleep(0.1)  # Simulate processing time
    return {"status": "success", "data": "result"}

@CircuitBreaker(failure_threshold=5, recovery_timeout=60)
@RetryPolicy(max_attempts=2, base_delay=2.0)
@bulkhead.isolate_resource("external_api")
async def external_api_call():
    """Example external API call with resilience patterns."""
    # Simulate external API call
    if random.random() < 0.2:  # 20% failure rate
        raise Exception("External API unavailable")
    
    await asyncio.sleep(0.5)  # Simulate network latency
    return {"status": "success", "data": "api_result"}
```

### 1.3 Security by Design

**Security Architecture Patterns:**
```python
# Security-first architectural patterns
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import jwt
import secrets
import hashlib
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import base64

class SecureDataLayer:
    """Secure data access layer with encryption and access control."""
    
    def __init__(self, encryption_key: bytes):
        self.cipher_suite = Fernet(encryption_key)
        self.access_policies = {}
        self.audit_logger = SecurityAuditLogger()
    
    def encrypt_sensitive_field(self, data: str) -> str:
        """Encrypt sensitive data fields."""
        if not data:
            return data
        
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()
    
    def decrypt_sensitive_field(self, encrypted_data: str) -> str:
        """Decrypt sensitive data fields."""
        if not encrypted_data:
            return encrypted_data
        
        try:
            decoded_data = base64.b64decode(encrypted_data.encode())
            decrypted_data = self.cipher_suite.decrypt(decoded_data)
            return decrypted_data.decode()
        except Exception:
            # Return empty string if decryption fails
            return ""
    
    def define_access_policy(self, resource: str, policy: Dict):
        """Define access control policy for a resource."""
        self.access_policies[resource] = policy
    
    def check_access(self, user: Dict, resource: str, action: str) -> bool:
        """Check if user has access to perform action on resource."""
        policy = self.access_policies.get(resource, {})
        
        # Check role-based access
        required_roles = policy.get(action, [])
        user_roles = user.get('roles', [])
        
        has_role_access = any(role in user_roles for role in required_roles)
        
        # Check attribute-based access
        conditions = policy.get('conditions', {})
        meets_conditions = self.evaluate_conditions(user, conditions)
        
        # Log access attempt
        self.audit_logger.log_access_attempt(
            user['id'], resource, action, has_role_access and meets_conditions
        )
        
        return has_role_access and meets_conditions
    
    def evaluate_conditions(self, user: Dict, conditions: Dict) -> bool:
        """Evaluate attribute-based access conditions."""
        for condition_type, condition_value in conditions.items():
            if condition_type == 'department':
                if user.get('department') != condition_value:
                    return False
            elif condition_type == 'clearance_level':
                if user.get('clearance_level', 0) < condition_value:
                    return False
            elif condition_type == 'time_restriction':
                current_hour = datetime.now().hour
                if not (condition_value['start'] <= current_hour <= condition_value['end']):
                    return False
        
        return True

class ZeroTrustArchitecture:
    """Zero Trust security architecture implementation."""
    
    def __init__(self):
        self.identity_verifier = IdentityVerifier()
        self.device_trust_manager = DeviceTrustManager()
        self.network_segmentation = NetworkSegmentation()
        self.continuous_monitoring = ContinuousMonitoring()
    
    def verify_request(self, request: Dict) -> Dict:
        """Verify request using Zero Trust principles."""
        verification_result = {
            'allowed': False,
            'trust_score': 0.0,
            'verification_details': {}
        }
        
        # 1. Verify identity
        identity_result = self.identity_verifier.verify(request['user'])
        verification_result['verification_details']['identity'] = identity_result
        
        # 2. Verify device trust
        device_result = self.device_trust_manager.verify(request['device'])
        verification_result['verification_details']['device'] = device_result
        
        # 3. Check network context
        network_result = self.network_segmentation.verify(request['network_context'])
        verification_result['verification_details']['network'] = network_result
        
        # 4. Evaluate resource access
        resource_result = self.evaluate_resource_access(request)
        verification_result['verification_details']['resource'] = resource_result
        
        # Calculate overall trust score
        trust_score = self.calculate_trust_score([
            identity_result, device_result, network_result, resource_result
        ])
        
        verification_result['trust_score'] = trust_score
        verification_result['allowed'] = trust_score >= 0.7  # 70% trust threshold
        
        # Log verification attempt
        self.continuous_monitoring.log_verification(request, verification_result)
        
        return verification_result
    
    def calculate_trust_score(self, verification_results: List[Dict]) -> float:
        """Calculate overall trust score from individual verifications."""
        weights = {
            'identity': 0.3,
            'device': 0.25,
            'network': 0.2,
            'resource': 0.25
        }
        
        total_score = 0.0
        for i, result in enumerate(verification_results):
            weight = list(weights.values())[i]
            score = result.get('trust_score', 0.0)
            total_score += score * weight
        
        return min(1.0, max(0.0, total_score))

class SecurityAuditLogger:
    """Comprehensive security audit logging."""
    
    def __init__(self):
        self.audit_events = []
        self.alert_thresholds = {
            'failed_access_attempts': 5,
            'privilege_escalation': 1,
            'data_access_anomaly': 10
        }
    
    def log_access_attempt(self, user_id: str, resource: str, action: str, allowed: bool):
        """Log access attempt with security context."""
        event = {
            'event_type': 'access_attempt',
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'allowed': allowed,
            'ip_address': self.get_client_ip(),
            'user_agent': self.get_user_agent(),
            'session_id': self.get_session_id()
        }
        
        self.audit_events.append(event)
        
        # Check for security alerts
        if not allowed:
            self.check_failed_access_pattern(user_id)
    
    def log_data_access(self, user_id: str, data_type: str, record_count: int):
        """Log data access for anomaly detection."""
        event = {
            'event_type': 'data_access',
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'data_type': data_type,
            'record_count': record_count,
            'ip_address': self.get_client_ip()
        }
        
        self.audit_events.append(event)
        
        # Check for data access anomalies
        self.check_data_access_anomaly(user_id, data_type, record_count)
    
    def check_failed_access_pattern(self, user_id: str):
        """Check for suspicious failed access patterns."""
        recent_failures = [
            event for event in self.audit_events[-100:]  # Last 100 events
            if (event['user_id'] == user_id and 
                event['event_type'] == 'access_attempt' and 
                not event['allowed'] and
                datetime.fromisoformat(event['timestamp']) > datetime.now() - timedelta(minutes=15))
        ]
        
        if len(recent_failures) >= self.alert_thresholds['failed_access_attempts']:
            self.trigger_security_alert('multiple_failed_access', {
                'user_id': user_id,
                'failure_count': len(recent_failures),
                'time_window': '15 minutes'
            })
    
    def generate_security_report(self, days: int = 7) -> Dict:
        """Generate comprehensive security audit report."""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        recent_events = [
            event for event in self.audit_events
            if datetime.fromisoformat(event['timestamp']) > cutoff_date
        ]
        
        return {
            'report_period_days': days,
            'total_events': len(recent_events),
            'access_attempts': len([e for e in recent_events if e['event_type'] == 'access_attempt']),
            'failed_access_attempts': len([e for e in recent_events if e['event_type'] == 'access_attempt' and not e['allowed']]),
            'data_access_events': len([e for e in recent_events if e['event_type'] == 'data_access']),
            'unique_users': len(set(e['user_id'] for e in recent_events)),
            'top_accessed_resources': self.get_top_resources(recent_events),
            'security_alerts': self.get_security_alerts(recent_events)
        }
```

## 2. Microservices Architecture

### 2.1 Service Design Patterns

**Domain-Driven Design Implementation:**
```python
# Domain-driven microservices architecture
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import uuid
from datetime import datetime

# Domain Events
class DomainEvent(ABC):
    def __init__(self):
        self.event_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.version = 1

class CustomerCreated(DomainEvent):
    def __init__(self, customer_id: str, customer_data: Dict):
        super().__init__()
        self.customer_id = customer_id
        self.customer_data = customer_data

class CustomerUpdated(DomainEvent):
    def __init__(self, customer_id: str, changes: Dict):
        super().__init__()
        self.customer_id = customer_id
        self.changes = changes

# Aggregate Root
class AggregateRoot(ABC):
    def __init__(self):
        self.domain_events: List[DomainEvent] = []
        self.version = 0
    
    def add_domain_event(self, event: DomainEvent):
        self.domain_events.append(event)
    
    def clear_domain_events(self):
        self.domain_events.clear()
    
    def get_uncommitted_events(self) -> List[DomainEvent]:
        return self.domain_events.copy()

# Customer Aggregate
class Customer(AggregateRoot):
    def __init__(self, customer_id: str, first_name: str, last_name: str, email: str):
        super().__init__()
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_active = True
        self.created_at = datetime.now()
        
        # Raise domain event
        self.add_domain_event(CustomerCreated(
            customer_id=self.customer_id,
            customer_data={
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
            }
        ))
    
    def update_contact_info(self, email: str = None, phone: str = None):
        changes = {}
        
        if email and email != self.email:
            changes['email'] = {'old': self.email, 'new': email}
            self.email = email
        
        if phone and hasattr(self, 'phone') and phone != self.phone:
            changes['phone'] = {'old': getattr(self, 'phone', None), 'new': phone}
            self.phone = phone
        
        if changes:
            self.version += 1
            self.add_domain_event(CustomerUpdated(
                customer_id=self.customer_id,
                changes=changes
            ))
    
    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.version += 1
            self.add_domain_event(CustomerUpdated(
                customer_id=self.customer_id,
                changes={'is_active': {'old': True, 'new': False}}
            ))

# Repository Pattern
class CustomerRepository(ABC):
    @abstractmethod
    async def get_by_id(self, customer_id: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    async def save(self, customer: Customer) -> None:
        pass
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[Customer]:
        pass

class PostgreSQLCustomerRepository(CustomerRepository):
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.event_store = EventStore(connection_pool)
    
    async def get_by_id(self, customer_id: str) -> Optional[Customer]:
        async with self.connection_pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM customers WHERE customer_id = $1",
                customer_id
            )
            
            if row:
                customer = Customer(
                    customer_id=row['customer_id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email']
                )
                customer.is_active = row['is_active']
                customer.created_at = row['created_at']
                customer.version = row['version']
                customer.clear_domain_events()  # Clear events for existing entity
                
                return customer
            
            return None
    
    async def save(self, customer: Customer) -> None:
        async with self.connection_pool.acquire() as conn:
            async with conn.transaction():
                # Save customer data
                await conn.execute("""
                    INSERT INTO customers (customer_id, first_name, last_name, email, is_active, created_at, version)
                    VALUES ($1, $2, $3, $4, $5, $6, $7)
                    ON CONFLICT (customer_id) DO UPDATE SET
                        first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name,
                        email = EXCLUDED.email,
                        is_active = EXCLUDED.is_active,
                        version = EXCLUDED.version
                """, customer.customer_id, customer.first_name, customer.last_name,
                    customer.email, customer.is_active, customer.created_at, customer.version)
                
                # Save domain events
                for event in customer.get_uncommitted_events():
                    await self.event_store.save_event(event)
                
                customer.clear_domain_events()

# Event Store
class EventStore:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
    
    async def save_event(self, event: DomainEvent):
        async with self.connection_pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO domain_events (event_id, event_type, event_data, timestamp, version)
                VALUES ($1, $2, $3, $4, $5)
            """, event.event_id, event.__class__.__name__, 
                self.serialize_event(event), event.timestamp, event.version)
    
    def serialize_event(self, event: DomainEvent) -> str:
        import json
        
        event_data = {
            'event_id': event.event_id,
            'timestamp': event.timestamp.isoformat(),
            'version': event.version
        }
        
        # Add event-specific data
        if isinstance(event, CustomerCreated):
            event_data.update({
                'customer_id': event.customer_id,
                'customer_data': event.customer_data
            })
        elif isinstance(event, CustomerUpdated):
            event_data.update({
                'customer_id': event.customer_id,
                'changes': event.changes
            })
        
        return json.dumps(event_data)

# Application Service
class CustomerApplicationService:
    def __init__(self, customer_repository: CustomerRepository, event_publisher):
        self.customer_repository = customer_repository
        self.event_publisher = event_publisher
    
    async def create_customer(self, command: Dict) -> str:
        # Validate command
        self.validate_create_customer_command(command)
        
        # Check if customer already exists
        existing_customer = await self.customer_repository.find_by_email(command['email'])
        if existing_customer:
            raise ValueError("Customer with this email already exists")
        
        # Create customer aggregate
        customer_id = str(uuid.uuid4())
        customer = Customer(
            customer_id=customer_id,
            first_name=command['first_name'],
            last_name=command['last_name'],
            email=command['email']
        )
        
        # Save customer
        await self.customer_repository.save(customer)
        
        # Publish domain events
        for event in customer.get_uncommitted_events():
            await self.event_publisher.publish(event)
        
        return customer_id
    
    async def update_customer_contact(self, customer_id: str, command: Dict):
        # Load customer
        customer = await self.customer_repository.get_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        # Update contact information
        customer.update_contact_info(
            email=command.get('email'),
            phone=command.get('phone')
        )
        
        # Save changes
        await self.customer_repository.save(customer)
        
        # Publish domain events
        for event in customer.get_uncommitted_events():
            await self.event_publisher.publish(event)
    
    def validate_create_customer_command(self, command: Dict):
        required_fields = ['first_name', 'last_name', 'email']
        
        for field in required_fields:
            if field not in command or not command[field]:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate email format
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, command['email']):
            raise ValueError("Invalid email format")
```

### 2.2 API Gateway and Service Communication

**API Gateway Implementation:**
```python
# Comprehensive API Gateway
import asyncio
import aiohttp
from aiohttp import web
import jwt
import time
from typing import Dict, List, Optional, Callable
import json
import logging
from dataclasses import dataclass

@dataclass
class RouteConfig:
    path: str
    method: str
    service_name: str
    service_path: str
    auth_required: bool = True
    rate_limit: Optional[int] = None
    timeout: int = 30
    retry_count: int = 0

class APIGateway:
    def __init__(self):
        self.routes = {}
        self.services = {}
        self.middleware_stack = []
        self.rate_limiters = {}
        self.circuit_breakers = {}
        self.logger = logging.getLogger('api_gateway')
    
    def register_service(self, name: str, base_url: str, health_check_path: str = '/health'):
        """Register a backend service."""
        self.services[name] = {
            'base_url': base_url,
            'health_check_path': health_check_path,
            'healthy': True,
            'last_health_check': None
        }
    
    def add_route(self, config: RouteConfig):
        """Add a route configuration."""
        route_key = f"{config.method}:{config.path}"
        self.routes[route_key] = config
        
        # Initialize rate limiter if specified
        if config.rate_limit:
            self.rate_limiters[route_key] = RateLimiter(
                max_requests=config.rate_limit,
                window_seconds=60
            )
    
    def add_middleware(self, middleware: Callable):
        """Add middleware to the processing stack."""
        self.middleware_stack.append(middleware)
    
    async def handle_request(self, request: web.Request) -> web.Response:
        """Main request handler."""
        start_time = time.time()
        
        try:
            # Find matching route
            route_config = self.find_route(request.method, request.path)
            if not route_config:
                return web.json_response(
                    {'error': 'Route not found'}, 
                    status=404
                )
            
            # Process middleware stack
            context = {'request': request, 'route_config': route_config}
            
            for middleware in self.middleware_stack:
                result = await middleware(context)
                if isinstance(result, web.Response):
                    return result
            
            # Forward request to backend service
            response = await self.forward_request(request, route_config)
            
            # Log request
            self.log_request(request, response, time.time() - start_time)
            
            return response
            
        except Exception as e:
            self.logger.error(f"Request handling failed: {str(e)}")
            return web.json_response(
                {'error': 'Internal server error'}, 
                status=500
            )
    
    def find_route(self, method: str, path: str) -> Optional[RouteConfig]:
        """Find matching route configuration."""
        route_key = f"{method}:{path}"
        
        # Exact match first
        if route_key in self.routes:
            return self.routes[route_key]
        
        # Pattern matching for parameterized routes
        for registered_route, config in self.routes.items():
            if self.match_route_pattern(registered_route, route_key):
                return config
        
        return None
    
    async def forward_request(self, request: web.Request, config: RouteConfig) -> web.Response:
        """Forward request to backend service."""
        service = self.services.get(config.service_name)
        if not service:
            return web.json_response(
                {'error': 'Service not available'}, 
                status=503
            )
        
        # Check service health
        if not service['healthy']:
            return web.json_response(
                {'error': 'Service unhealthy'}, 
                status=503
            )
        
        # Build target URL
        target_url = f"{service['base_url']}{config.service_path}"
        
        # Prepare request data
        headers = dict(request.headers)
        headers.pop('Host', None)  # Remove original host header
        
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=config.timeout)) as session:
                # Forward request with retry logic
                for attempt in range(config.retry_count + 1):
                    try:
                        async with session.request(
                            method=request.method,
                            url=target_url,
                            headers=headers,
                            data=await request.read(),
                            params=request.query
                        ) as response:
                            
                            # Read response
                            response_data = await response.read()
                            
                            # Create response
                            return web.Response(
                                body=response_data,
                                status=response.status,
                                headers=response.headers
                            )
                    
                    except asyncio.TimeoutError:
                        if attempt < config.retry_count:
                            await asyncio.sleep(2 ** attempt)  # Exponential backoff
                            continue
                        else:
                            return web.json_response(
                                {'error': 'Service timeout'}, 
                                status=504
                            )
                    
                    except Exception as e:
                        if attempt < config.retry_count:
                            await asyncio.sleep(2 ** attempt)
                            continue
                        else:
                            self.logger.error(f"Service request failed: {str(e)}")
                            return web.json_response(
                                {'error': 'Service error'}, 
                                status=502
                            )
        
        except Exception as e:
            self.logger.error(f"Request forwarding failed: {str(e)}")
            return web.json_response(
                {'error': 'Gateway error'}, 
                status=500
            )

# Middleware implementations
class AuthenticationMiddleware:
    def __init__(self, jwt_secret: str):
        self.jwt_secret = jwt_secret
    
    async def __call__(self, context: Dict) -> Optional[web.Response]:
        request = context['request']
        route_config = context['route_config']
        
        if not route_config.auth_required:
            return None
        
        # Extract JWT token
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return web.json_response(
                {'error': 'Missing or invalid authorization header'}, 
                status=401
            )
        
        token = auth_header[7:]  # Remove 'Bearer ' prefix
        
        try:
            # Verify JWT token
            payload = jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
            
            # Add user context to request
            context['user'] = payload
            
            return None  # Continue processing
            
        except jwt.ExpiredSignatureError:
            return web.json_response(
                {'error': 'Token expired'}, 
                status=401
            )
        except jwt.InvalidTokenError:
            return web.json_response(
                {'error': 'Invalid token'}, 
                status=401
            )

class RateLimitingMiddleware:
    def __init__(self, gateway: APIGateway):
        self.gateway = gateway
    
    async def __call__(self, context: Dict) -> Optional[web.Response]:
        request = context['request']
        route_config = context['route_config']
        
        route_key = f"{route_config.method}:{route_config.path}"
        rate_limiter = self.gateway.rate_limiters.get(route_key)
        
        if rate_limiter:
            client_id = self.get_client_identifier(request)
            
            if not rate_limiter.allow_request(client_id):
                return web.json_response(
                    {'error': 'Rate limit exceeded'}, 
                    status=429,
                    headers={'Retry-After': '60'}
                )
        
        return None
    
    def get_client_identifier(self, request: web.Request) -> str:
        # Use user ID if authenticated, otherwise use IP address
        user = getattr(request, 'user', None)
        if user:
            return user.get('user_id', request.remote)
        return request.remote

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}  # client_id -> list of timestamps
    
    def allow_request(self, client_id: str) -> bool:
        now = time.time()
        
        # Clean old requests
        if client_id in self.requests:
            self.requests[client_id] = [
                timestamp for timestamp in self.requests[client_id]
                if now - timestamp < self.window_seconds
            ]
        else:
            self.requests[client_id] = []
        
        # Check rate limit
        if len(self.requests[client_id]) >= self.max_requests:
            return False
        
        # Record request
        self.requests[client_id].append(now)
        return True

# Gateway setup
async def create_api_gateway():
    gateway = APIGateway()
    
    # Register services
    gateway.register_service('customer-service', 'http://customer-service:8001')
    gateway.register_service('order-service', 'http://order-service:8002')
    gateway.register_service('notification-service', 'http://notification-service:8003')
    
    # Add middleware
    gateway.add_middleware(AuthenticationMiddleware('your-jwt-secret'))
    gateway.add_middleware(RateLimitingMiddleware(gateway))
    
    # Configure routes
    gateway.add_route(RouteConfig(
        path='/api/customers',
        method='GET',
        service_name='customer-service',
        service_path='/customers',
        rate_limit=100
    ))
    
    gateway.add_route(RouteConfig(
        path='/api/customers',
        method='POST',
        service_name='customer-service',
        service_path='/customers',
        rate_limit=20
    ))
    
    # Create web application
    app = web.Application()
    app.router.add_route('*', '/{path:.*}', gateway.handle_request)
    
    return app
```

---

**Document Version**: 1.0  
**Last Updated**: Current Date  
**Review Cycle**: Quarterly  
**Owner**: Architecture Team  
**Approval**: CTO