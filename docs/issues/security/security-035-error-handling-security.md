# Security Issue #35: Error Handling Security Improvements

## Dependencies
- **Blocks**: Production deployment, security compliance validation
- **Depends On**: Issue #38 (backend database connection for comprehensive error testing)
- **Related**: Issue #32 (XSS vulnerabilities - resolved), Issue #33 (log injection - resolved)

## Problem Classification
- **Type**: Security
- **Category**: Security/Error Handling
- **Impact**: High (Security vulnerability)
- **Urgency**: High (Security risk)
- **Severity**: Major
- **CVSS Score**: 6.5 (Medium-High)
- **CWE**: CWE-209 (Information Exposure Through Error Messages)

## Executive Summary

**Business Impact**: Inadequate error handling may expose sensitive system information to attackers, fail silently creating operational blind spots, and create security vulnerabilities that could lead to data breaches, system compromise, compliance violations, and complete loss of customer trust. This represents a critical security gap in the application's defense mechanisms.

**Financial Impact**: Potential $10,000-50,000 impact from security incidents, regulatory fines (GDPR, CCPA), data breach costs, legal liability, and reputation damage. Risk of customer churn due to security concerns, potential class-action lawsuits, and loss of business partnerships due to security compliance failures.

**Strategic Risk**: Security vulnerabilities undermine system integrity and could result in regulatory compliance failures, especially critical for customer data management systems. Poor error handling can create attack vectors, enable reconnaissance attacks, and compromise the entire security posture of the organization.

## General Summary

**Problem Overview**: The error handling system has critical security weaknesses including limited error type acceptance, potential information disclosure through error messages, inadequate error checking in shell scripts, and missing security-focused logging. These issues could be exploited by attackers for reconnaissance, privilege escalation, or system compromise.

**User Impact**: 
- Users may receive error messages that expose sensitive system information
- System failures may go undetected due to silent errors, creating security blind spots
- Sensitive information could be exposed in error responses to unauthorized users
- Security incidents may not be properly logged, detected, or responded to
- Poor error handling reduces system reliability and creates attack opportunities
- Compliance violations due to inadequate data protection in error scenarios

**Business Context**: Secure error handling is critical for maintaining system security, regulatory compliance, and operational reliability. Poor error handling can create attack vectors, expose sensitive data, enable system reconnaissance, and undermine the security posture of customer data management systems, potentially violating privacy regulations.

## Technical Summary

### Root Cause Analysis

**Primary Cause**: Error handling system has multiple critical security weaknesses including type limitations, information disclosure risks, inadequate error checking, and missing security-focused monitoring and response capabilities.

**Technical Details**:
```typescript
// Current problematic implementation in useErrorHandler.ts
const useErrorHandler = (error: Error) => {  // Only accepts Error type
  // Limited error handling capability
  // Potential information disclosure in error messages
  // No security context or sanitization
  console.error(error) // Logs full error details including sensitive data
}

// Shell script issues in tests/run-tests.sh
cd some/directory  # No error checking
# Commands continue even if cd fails, creating security blind spots
```

**Contributing Factors**:
1. Type-limited error handler restricting security-focused error processing
2. Shell scripts lacking proper error checking and security validation
3. Potential information disclosure in error messages and stack traces
4. Missing security-focused error logging and monitoring systems
5. Inadequate error sanitization for user-facing messages
6. No correlation between errors and potential security incidents
7. Lack of security context in error handling and response

**Security Vulnerabilities**:
1. **Information Disclosure (CWE-209)**: Stack traces, file paths, database schemas, and system configuration exposed in error messages
2. **Silent Failures (CWE-754)**: Shell commands and critical operations failing without detection, creating security blind spots
3. **Type Coercion Issues (CWE-843)**: Unexpected error types causing runtime failures and potential security bypasses
4. **Insufficient Logging (CWE-778)**: Security-relevant errors not properly tracked, hindering incident response
5. **Error-based Enumeration**: Attackers using error messages to enumerate system resources and vulnerabilities

**Attack Scenarios**:
```typescript
// Information disclosure through error messages
try {
  await database.query('SELECT * FROM users WHERE id = ?', [userId])
} catch (error) {
  // Exposes database schema and connection details
  return res.status(500).json({ error: error.message })
  // "Table 'production_db.users' doesn't exist at connection 'mysql://admin:password@db.internal:3306/production_db'"
}

// Path traversal information disclosure
try {
  const file = fs.readFileSync(`/app/uploads/${filename}`)
} catch (error) {
  // Exposes internal file system structure
  console.error(error) // "ENOENT: no such file or directory, open '/app/uploads/../../../etc/passwd'"
}
```

### Suggested Resolution

**Immediate Security Fix (1-2 days)**:
```typescript
// Enhanced secure error handler with comprehensive security controls
interface SecureErrorHandler {
  handleError: (error: unknown, context?: SecurityContext) => void
  sanitizeError: (error: unknown) => SafeErrorMessage
  logSecurityEvent: (error: unknown, context: SecurityContext) => void
}

interface SecurityContext {
  userId?: string
  sessionId?: string
  ipAddress?: string
  userAgent?: string
  endpoint?: string
  operation?: string
  sensitivityLevel?: 'low' | 'medium' | 'high' | 'critical'
}

interface SafeErrorMessage {
  userMessage: string
  errorCode: string
  timestamp: string
  correlationId: string
  supportReference?: string
}

const useSecureErrorHandler = (): SecureErrorHandler => {
  const securityLogger = useSecurityLogger()
  const errorClassifier = useErrorClassifier()
  
  const handleError = (error: unknown, context?: SecurityContext) => {
    const sanitizedError = sanitizeError(error)
    const securityContext = context || getDefaultSecurityContext()
    
    // Classify error for security analysis
    const classification = errorClassifier.classify(error, securityContext)
    
    // Log security event with full context (server-side only)
    logSecurityEvent(error, securityContext, classification)
    
    // Send sanitized error to monitoring with security correlation
    errorTracker.captureException(sanitizedError, {
      context: securityContext,
      classification: classification,
      correlationId: sanitizedError.correlationId
    })
    
    // Show user-friendly message (never expose sensitive data)
    toast.error(sanitizedError.userMessage)
    
    // Trigger security response if needed
    if (classification.threatLevel === 'high') {
      triggerSecurityResponse(error, securityContext, classification)
    }
  }

  const sanitizeError = (error: unknown): SafeErrorMessage => {
    const correlationId = generateCorrelationId()
    
    // Comprehensive error sanitization with security focus
    if (error instanceof Error) {
      return {
        userMessage: getSecureErrorMessage(error.message, error.name),
        errorCode: generateSecureErrorCode(error),
        timestamp: new Date().toISOString(),
        correlationId: correlationId,
        supportReference: generateSupportReference(correlationId)
      }
    }
    
    if (typeof error === 'string') {
      return {
        userMessage: 'An error occurred. Please try again.',
        errorCode: 'GENERIC_ERROR',
        timestamp: new Date().toISOString(),
        correlationId: correlationId
      }
    }
    
    // Handle API errors with security sanitization
    if (isApiError(error)) {
      return {
        userMessage: sanitizeApiError(error),
        errorCode: generateApiErrorCode(error),
        timestamp: new Date().toISOString(),
        correlationId: correlationId,
        supportReference: generateSupportReference(correlationId)
      }
    }
    
    // Default ultra-safe error response
    return {
      userMessage: 'An unexpected error occurred. Please contact support if the issue persists.',
      errorCode: 'UNKNOWN_ERROR',
      timestamp: new Date().toISOString(),
      correlationId: correlationId,
      supportReference: generateSupportReference(correlationId)
    }
  }

  const logSecurityEvent = (error: unknown, context: SecurityContext, classification: any) => {
    const securityEvent = {
      timestamp: new Date().toISOString(),
      eventType: 'error_security_event',
      errorType: error instanceof Error ? error.name : typeof error,
      threatLevel: classification.threatLevel,
      sensitivityLevel: context.sensitivityLevel || 'medium',
      userId: context.userId,
      sessionId: context.sessionId,
      ipAddress: hashPII(context.ipAddress), // Hash PII for privacy
      userAgent: sanitizeUserAgent(context.userAgent),
      endpoint: context.endpoint,
      operation: context.operation,
      errorFingerprint: generateErrorFingerprint(error),
      potentialAttack: classification.potentialAttack,
      correlationId: generateCorrelationId(),
      // Full error details (server-side only, never sent to client)
      fullError: process.env.NODE_ENV === 'development' ? error : '[REDACTED]'
    }
    
    // Log to secure audit trail
    securityLogger.logSecurityEvent(securityEvent)
    
    // Real-time threat detection
    if (classification.potentialAttack) {
      securityLogger.logThreatEvent({
        ...securityEvent,
        threatType: classification.threatType,
        confidence: classification.confidence,
        recommendedAction: classification.recommendedAction
      })
    }
  }

  return { handleError, sanitizeError, logSecurityEvent }
}

// Secure error message mapping with comprehensive sanitization
const getSecureErrorMessage = (errorMessage: string, errorName: string): string => {
  // Remove all potentially sensitive information
  const sanitizedMessage = errorMessage
    .replace(/\/[^\s]+/g, '[PATH]')  // Remove file paths
    .replace(/\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/g, '[IP]')  // Remove IP addresses
    .replace(/password|token|key|secret|api[_-]?key/gi, '[CREDENTIAL]')  // Remove credentials
    .replace(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g, '[EMAIL]')  // Remove emails
    .replace(/\b[A-Za-z0-9+/]{20,}={0,2}\b/g, '[TOKEN]')  // Remove base64 tokens
    .replace(/at\s+[^\s]+/g, '[STACK]')  // Remove stack traces
    .replace(/line\s+\d+/g, '[LINE]')  // Remove line numbers
    .replace(/column\s+\d+/g, '[COLUMN]')  // Remove column numbers
  
  // Map to safe, user-friendly messages
  const safeMessages: Record<string, string> = {
    'NetworkError': 'Unable to connect to the server. Please check your internet connection and try again.',
    'TimeoutError': 'The request took too long to complete. Please try again.',
    'UnauthorizedError': 'You are not authorized to perform this action. Please log in and try again.',
    'ForbiddenError': 'Access denied. Please contact your administrator if you believe this is an error.',
    'NotFoundError': 'The requested resource was not found. Please verify the information and try again.',
    'ValidationError': 'The provided information is invalid. Please check your input and try again.',
    'InternalServerError': 'A server error occurred. Our team has been notified and is working to resolve the issue.',
    'DatabaseError': 'A database error occurred. Please try again later.',
    'AuthenticationError': 'Authentication failed. Please log in again.',
    'RateLimitError': 'Too many requests. Please wait a moment before trying again.'
  }
  
  // Return safe message based on error type or generic fallback
  return safeMessages[errorName] || 
         safeMessages[Object.keys(safeMessages).find(key => 
           sanitizedMessage.toLowerCase().includes(key.toLowerCase().replace('error', ''))
         ) || ''] ||
         'An error occurred while processing your request. Please try again or contact support if the issue persists.'
}

// Advanced error classification for security analysis
class ErrorClassifier {
  classify(error: unknown, context: SecurityContext) {
    const classification = {
      threatLevel: 'low' as 'low' | 'medium' | 'high' | 'critical',
      potentialAttack: false,
      threatType: null as string | null,
      confidence: 0,
      recommendedAction: 'monitor' as 'monitor' | 'alert' | 'block' | 'investigate'
    }
    
    if (error instanceof Error) {
      // Analyze error patterns for potential attacks
      const errorString = error.message + error.stack
      
      // SQL Injection indicators
      if (/sql|database|query|table|column/i.test(errorString)) {
        classification.threatLevel = 'high'
        classification.potentialAttack = true
        classification.threatType = 'sql_injection_attempt'
        classification.confidence = 0.7
        classification.recommendedAction = 'investigate'
      }
      
      // Path traversal indicators
      if (/\.\.\/|\.\.\\|\/etc\/|\/proc\/|\/sys\//i.test(errorString)) {
        classification.threatLevel = 'high'
        classification.potentialAttack = true
        classification.threatType = 'path_traversal_attempt'
        classification.confidence = 0.8
        classification.recommendedAction = 'block'
      }
      
      // Command injection indicators
      if (/sh|bash|cmd|powershell|exec|eval/i.test(errorString)) {
        classification.threatLevel = 'critical'
        classification.potentialAttack = true
        classification.threatType = 'command_injection_attempt'
        classification.confidence = 0.9
        classification.recommendedAction = 'block'
      }
      
      // Authentication bypass attempts
      if (/auth|login|session|token|jwt/i.test(errorString) && context.endpoint?.includes('auth')) {
        classification.threatLevel = 'high'
        classification.potentialAttack = true
        classification.threatType = 'authentication_bypass_attempt'
        classification.confidence = 0.6
        classification.recommendedAction = 'investigate'
      }
    }
    
    return classification
  }
}

// Secure shell script implementation
const createSecureShellScript = () => `
#!/bin/bash
# Enhanced run-tests.sh with comprehensive security and error handling

set -euo pipefail  # Exit on error, undefined vars, pipe failures
IFS=$'\\n\\t'      # Secure Internal Field Separator

# Security logging function
log_security_event() {
    local event_type="$1"
    local message="$2"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    echo "{\\"timestamp\\": \\"$timestamp\\", \\"event_type\\": \\"$event_type\\", \\"message\\": \\"$message\\", \\"script\\": \\"$0\\", \\"user\\": \\"$(whoami)\\", \\"pwd\\": \\"$(pwd)\\"}" >> /var/log/security/script-execution.log
}

# Function for secure directory changes with validation
secure_cd() {
    local target_dir="$1"
    local max_depth=10
    local current_depth=0
    
    # Validate directory path for security
    if [[ "$target_dir" =~ \\.\\. ]] || [[ "$target_dir" =~ ^/ ]] || [[ "$target_dir" =~ \\$ ]]; then
        log_security_event "security_violation" "Potentially malicious directory path rejected: $target_dir"
        echo "ERROR: Invalid directory path detected - potential security risk" >&2
        exit 1
    fi
    
    # Check if directory exists and is accessible
    if [[ ! -d "$target_dir" ]]; then
        log_security_event "error" "Directory does not exist: $target_dir"
        echo "ERROR: Directory does not exist: $target_dir" >&2
        exit 1
    fi
    
    # Attempt directory change with error handling
    if ! cd "$target_dir" 2>/dev/null; then
        log_security_event "error" "Failed to change to directory: $target_dir"
        echo "ERROR: Failed to change to directory: $target_dir" >&2
        exit 1
    fi
    
    log_security_event "directory_change" "Successfully changed to directory: $(pwd)"
    echo "INFO: Changed to directory: $(pwd)"
}

# Function for secure command execution with comprehensive validation
secure_execute() {
    local command="$1"
    local description="$2"
    local timeout="${3:-300}"  # Default 5 minute timeout
    
    # Validate command for security
    if [[ "$command" =~ [;&|`$] ]] || [[ "$command" =~ rm.*-rf ]] || [[ "$command" =~ sudo ]]; then
        log_security_event "security_violation" "Potentially dangerous command rejected: $command"
        echo "ERROR: Potentially dangerous command detected - execution blocked" >&2
        exit 1
    fi
    
    log_security_event "command_execution" "Executing: $description - Command: $command"
    echo "INFO: Executing: $description"
    
    # Execute with timeout and comprehensive error handling
    if timeout "$timeout" bash -c "$command"; then
        log_security_event "command_success" "Successfully completed: $description"
        echo "SUCCESS: $description completed successfully"
    else
        local exit_code=$?
        log_security_event "command_failure" "Failed to execute: $description - Exit code: $exit_code"
        echo "ERROR: Failed to execute: $description (Exit code: $exit_code)" >&2
        exit $exit_code
    fi
}

# Security validation function
validate_environment() {
    # Check for required security tools
    local required_tools=("timeout" "whoami" "pwd")
    
    for tool in "\${required_tools[@]}"; do
        if ! command -v "$tool" >/dev/null 2>&1; then
            log_security_event "security_error" "Required security tool not found: $tool"
            echo "ERROR: Required security tool not found: $tool" >&2
            exit 1
        fi
    done
    
    # Validate current user (should not be root for security)
    if [[ "$(whoami)" == "root" ]]; then
        log_security_event "security_warning" "Script running as root - potential security risk"
        echo "WARNING: Running as root - consider using a less privileged user" >&2
    fi
    
    log_security_event "environment_validation" "Environment validation completed successfully"
}

# Main execution with comprehensive security and error handling
main() {
    local start_time=$(date +%s)
    
    log_security_event "script_start" "Test execution script started"
    echo "INFO: Starting secure test execution..."
    
    # Validate environment security
    validate_environment
    
    # Get script directory securely
    local script_dir
    script_dir="$(cd "$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
    
    # Navigate to project root securely
    secure_cd "$script_dir"
    secure_cd "../backend"
    
    # Execute backend tests with security controls
    secure_execute "python manage.py test --verbosity=2" "Backend tests" 600
    
    # Navigate to frontend securely
    secure_cd "../frontend"
    
    # Execute frontend tests with security controls
    secure_execute "npm test -- --watchAll=false --coverage" "Frontend tests" 600
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    log_security_event "script_completion" "All tests completed successfully in $duration seconds"
    echo "SUCCESS: All tests completed successfully in $duration seconds"
}

# Comprehensive error handling and cleanup
cleanup() {
    local exit_code=$?
    log_security_event "script_cleanup" "Script cleanup initiated with exit code: $exit_code"
    
    # Perform any necessary cleanup
    # Remove temporary files, reset permissions, etc.
    
    if [[ $exit_code -ne 0 ]]; then
        log_security_event "script_failure" "Script failed with exit code: $exit_code"
        echo "ERROR: Script failed with exit code: $exit_code" >&2
    fi
    
    exit $exit_code
}

# Set up comprehensive error trapping
trap 'log_security_event "script_error" "Script failed at line $LINENO with command: $BASH_COMMAND"; cleanup' ERR
trap 'log_security_event "script_interrupt" "Script interrupted by user"; cleanup' INT TERM

# Execute main function with all arguments
main "$@"
`
```

**Long-term Solution (3-4 days)**:
1. **Comprehensive Error Classification System**: AI-powered error analysis and threat detection
2. **Advanced Security Monitoring**: Real-time threat correlation and incident response
3. **Automated Security Response**: Automated blocking and mitigation of detected threats
4. **Compliance Integration**: GDPR, CCPA, and other privacy regulation compliance
5. **Security Audit Trail**: Complete audit trail for security and compliance requirements

**Alternative Approaches**:
- **Option 1**: Centralized error handling service with advanced security analytics
- **Option 2**: Error handling middleware with built-in threat detection and response
- **Option 3**: AI-powered error analysis and automated threat response system

### Monitoring and Alerting

**Security Event Monitoring**:
```typescript
// Comprehensive security monitoring for error handling
class SecurityErrorMonitor {
  private threatDetector: ThreatDetector
  private incidentResponder: IncidentResponder
  private complianceLogger: ComplianceLogger
  
  constructor() {
    this.threatDetector = new ThreatDetector()
    this.incidentResponder = new IncidentResponder()
    this.complianceLogger = new ComplianceLogger()
  }
  
  trackSecurityError(error: unknown, severity: 'low' | 'medium' | 'high' | 'critical', 
                    context: SecurityContext) {
    const securityEvent = {
      id: generateSecurityEventId(),
      timestamp: new Date().toISOString(),
      type: 'security_error',
      severity,
      error: this.sanitizeErrorForLogging(error),
      context: this.sanitizeContext(context),
      threatAnalysis: this.threatDetector.analyze(error, context),
      complianceImpact: this.assessComplianceImpact(error, context)
    }
    
    // Log to secure audit trail
    this.complianceLogger.logSecurityEvent(securityEvent)
    
    // Real-time threat analysis
    if (securityEvent.threatAnalysis.threatLevel >= 'high') {
      this.handleHighThreatEvent(securityEvent)
    }
    
    // Compliance monitoring
    if (securityEvent.complianceImpact.violations.length > 0) {
      this.handleComplianceViolation(securityEvent)
    }
  }
  
  private handleHighThreatEvent(event: SecurityEvent) {
    // Immediate security response
    this.incidentResponder.initiateResponse({
      eventId: event.id,
      threatLevel: event.threatAnalysis.threatLevel,
      recommendedActions: event.threatAnalysis.recommendedActions,
      affectedSystems: event.context.affectedSystems,
      potentialImpact: event.threatAnalysis.potentialImpact
    })
    
    // Alert security team
    this.alertSecurityTeam(event)
    
    // Automated mitigation if configured
    if (event.threatAnalysis.autoMitigate) {
      this.incidentResponder.executeMitigation(event)
    }
  }
}
```

**Error Tracking**:
- Error rate monitoring by type, severity, and security classification
- Information disclosure attempt detection and correlation
- Suspicious error pattern analysis and threat intelligence integration
- Security incident correlation and automated response

**Health Checks**:
- Error handling system security posture monitoring
- Security policy compliance verification and reporting
- Error sanitization effectiveness tracking and validation
- Threat detection system performance and accuracy monitoring

### Testing Strategy

**Unit Tests**:
```typescript
describe('Secure Error Handling', () => {
  it('sanitizes all sensitive information from errors', () => {
    const sensitiveError = new Error('Database connection failed: mysql://admin:password123@db.internal:3306/production_db - Table users not found at /app/src/models/user.js:45')
    const handler = useSecureErrorHandler()
    
    const sanitized = handler.sanitizeError(sensitiveError)
    
    // Verify all sensitive data is removed
    expect(sanitized.userMessage).not.toContain('password123')
    expect(sanitized.userMessage).not.toContain('admin')
    expect(sanitized.userMessage).not.toContain('db.internal')
    expect(sanitized.userMessage).not.toContain('/app/src/models')
    expect(sanitized.userMessage).not.toContain('3306')
    expect(sanitized.userMessage).toBe('A database error occurred. Please try again later.')
  })

  it('detects and classifies potential security threats', () => {
    const sqlInjectionError = new Error("SQL syntax error: You have an error in your SQL syntax near 'UNION SELECT * FROM users'")
    const handler = useSecureErrorHandler()
    const classifier = new ErrorClassifier()
    
    const classification = classifier.classify(sqlInjectionError, {
      endpoint: '/api/users',
      operation: 'search'
    })
    
    expect(classification.potentialAttack).toBe(true)
    expect(classification.threatType).toBe('sql_injection_attempt')
    expect(classification.threatLevel).toBe('high')
    expect(classification.recommendedAction).toBe('investigate')
  })

  it('prevents information disclosure in API errors', () => {
    const apiError = {
      response: {
        data: { 
          message: 'Internal server error: /etc/passwd not found',
          stack: 'Error at /app/src/controllers/user.js:123:45',
          config: { baseURL: 'https://internal-api.company.com' }
        }
      }
    }
    
    const handler = useSecureErrorHandler()
    const sanitized = handler.sanitizeError(apiError)
    
    expect(sanitized.userMessage).not.toContain('/etc/passwd')
    expect(sanitized.userMessage).not.toContain('/app/src/controllers')
    expect(sanitized.userMessage).not.toContain('internal-api.company.com')
    expect(sanitized.correlationId).toBeDefined()
    expect(sanitized.supportReference).toBeDefined()
  })
})
```

**Security Testing**:
```typescript
describe('Error Handling Security Tests', () => {
  it('prevents all forms of information disclosure', () => {
    const sensitiveErrors = [
      new Error('API key: sk_live_123456789abcdef'),
      new Error('Password: mySecretPassword123!'),
      new Error('JWT Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
      new Error('Database: postgresql://user:pass@localhost:5432/db'),
      new Error('File path: /home/user/.ssh/id_rsa'),
      new Error('IP Address: 192.168.1.100'),
      new Error('Email: admin@company.com')
    ]
    
    const handler = useSecureErrorHandler()
    
    sensitiveErrors.forEach(error => {
      const sanitized = handler.sanitizeError(error)
      
      // Verify no sensitive patterns remain
      expect(sanitized.userMessage).not.toMatch(/sk_live_/i)
      expect(sanitized.userMessage).not.toMatch(/password/i)
      expect(sanitized.userMessage).not.toMatch(/jwt|token/i)
      expect(sanitized.userMessage).not.toMatch(/postgresql:\/\//i)
      expect(sanitized.userMessage).not.toMatch(/\/home\/|\/etc\/|\/var\//i)
      expect(sanitized.userMessage).not.toMatch(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/)
      expect(sanitized.userMessage).not.toMatch(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/)
    })
  })

  it('detects and responds to attack patterns', () => {
    const attackPatterns = [
      new Error("SQL error: UNION SELECT password FROM admin_users"),
      new Error("Path traversal: ../../../../etc/passwd"),
      new Error("Command injection: ; rm -rf / ;"),
      new Error("XSS attempt: <script>alert('xss')</script>"),
      new Error("LDAP injection: *)(uid=*))(|(uid=*")
    ]
    
    const handler = useSecureErrorHandler()
    const monitor = new SecurityErrorMonitor()
    
    attackPatterns.forEach(error => {
      const context = { endpoint: '/api/test', userId: 'test-user' }
      
      // Should trigger security alerts
      expect(() => {
        handler.handleError(error, context)
      }).not.toThrow()
      
      // Verify security event was logged
      expect(monitor.getSecurityEvents()).toContainEqual(
        expect.objectContaining({
          type: 'security_error',
          threatAnalysis: expect.objectContaining({
            potentialAttack: true,
            threatLevel: expect.stringMatching(/high|critical/)
          })
        })
      )
    })
  })
})
```

### Implementation Timeline

**Phase 1 (Day 1)**: Emergency security fixes - Implement secure error handler, sanitization, and shell script security
**Phase 2 (Day 2)**: Add comprehensive security monitoring, threat detection, and incident response capabilities
**Phase 3 (Day 3)**: Implement compliance logging, automated security testing, and advanced threat correlation
**Phase 4 (Day 4)**: Security review, penetration testing, compliance validation, and comprehensive team security training

### Success Criteria

**Technical Metrics**:
- [ ] Error handler accepts unknown error types safely with comprehensive security validation
- [ ] Sensitive information never exposed in error messages (0% information disclosure rate)
- [ ] Shell scripts fail safely with proper error checking and security validation
- [ ] Security monitoring detects 100% of suspicious error patterns and potential attacks
- [ ] Error sanitization removes 100% of sensitive data with comprehensive pattern matching
- [ ] Error handling performance impact <5ms per error with security controls

**Business Metrics**:
- [ ] Zero information disclosure incidents or security breaches
- [ ] Security compliance requirements met (GDPR, CCPA, SOC 2, ISO 27001)
- [ ] User experience improved through better error messages and faster resolution
- [ ] Operational reliability increased through proper error detection and response
- [ ] Regulatory audit findings resolved with comprehensive documentation

**Quality Metrics**:
- [ ] All security tests pass with 100% coverage of attack vectors and edge cases
- [ ] Error handling reliability >99.9% with comprehensive monitoring and alerting
- [ ] Security incident response time <15 minutes with automated threat detection
- [ ] Developer security training completed with 100% participation and certification
- [ ] Compliance documentation complete with regular security audits and reviews

---

**Priority**: High - Critical security vulnerability requiring immediate attention to prevent information disclosure, enable proper threat detection, and maintain regulatory compliance for customer data protection.