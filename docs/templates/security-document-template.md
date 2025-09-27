# Security Issue #[ID]: [Brief Descriptive Title]

## Dependencies
- **Blocks**: [List of security features, compliance requirements, or processes that cannot proceed until this security issue is resolved]
- **Depends On**: [List of infrastructure, authentication systems, or other security measures that must be in place before addressing this issue]
- **Related**: [List of related security issues, vulnerabilities, or compliance requirements that share context or impact]

## Problem Classification
- **Type**: Security
- **Category**: [Security/Application Security/Infrastructure Security/Development Tools/Data Protection]
- **Impact**: [Critical/High/Medium/Low] ([Brief impact description])
- **Urgency**: [Critical/High/Medium/Low] ([Brief urgency description])
- **Severity**: [Blocker/Major/Minor/Trivial]
- **CVSS Score**: [0.0-10.0] ([None/Low/Medium/High/Critical])
- **CWE**: [CWE-XXX] ([Common Weakness Enumeration classification])

## Executive Summary

**Business Impact**: [Describe how this security vulnerability affects business operations, reputation, customer trust, and strategic objectives. Include specific business processes, compliance requirements, or regulatory implications that are impacted.]

**Financial Impact**: [Quantify the financial impact with specific dollar amounts or ranges. Include potential costs from security incidents, regulatory fines, legal liability, reputation damage, customer churn, or business disruption. Consider both immediate and long-term financial consequences.]

**Strategic Risk**: [Explain the broader strategic implications, competitive disadvantage, compliance risks, regulatory violations, or long-term consequences if not addressed. Include potential impact on customer trust, market position, and business continuity.]

## General Summary

**Problem Overview**: [Provide a clear, non-technical description of the security vulnerability that stakeholders can understand. Explain what is vulnerable, how it could be exploited, and what the potential consequences are.]

**User Impact**: 
- [List specific ways users could be affected by this security vulnerability]
- [Include potential data exposure, service disruption, or privacy violations]
- [Note any compliance or regulatory implications for users]
- [Describe impact on user trust and confidence in the system]
- [Include potential legal or financial liability for users]

**Business Context**: [Explain why this security vulnerability matters to the business, how it relates to compliance requirements, regulatory obligations, and the importance of maintaining security posture for business operations.]

## Technical Summary

### Root Cause Analysis

**Primary Cause**: [Identify the main technical reason for the security vulnerability]

**Technical Details**:
```[language]
// Current vulnerable implementation or security flaw
[Include relevant code snippets, configuration issues, or system vulnerabilities]
```

**Contributing Factors**:
1. [List secondary causes or conditions that contribute to the vulnerability]
2. [Include environmental factors, dependencies, or architectural issues]
3. [Note any security controls that are missing or inadequate]
4. [Include process or procedural gaps that enabled the vulnerability]

**Attack Vectors**:
1. **[Attack Vector 1]**: [Description of how this attack could be executed]
2. **[Attack Vector 2]**: [Description of alternative attack methods]
3. **[Attack Vector 3]**: [Description of advanced or chained attacks]

**Example Exploitation Scenarios**:
```[language]
// Example of how an attacker might exploit this vulnerability
[Include specific attack payloads, malicious inputs, or exploitation techniques]
```

**Security Impact Assessment**:
- **Confidentiality**: [HIGH/MEDIUM/LOW] - [Description of data exposure risk]
- **Integrity**: [HIGH/MEDIUM/LOW] - [Description of data modification risk]
- **Availability**: [HIGH/MEDIUM/LOW] - [Description of service disruption risk]

### Suggested Resolution

**Immediate Security Fix ([timeframe])**:
```[language]
// Secure implementation with comprehensive security controls
[Include specific secure coding examples, configuration changes, or security controls]
```

**Long-term Solution ([timeframe])**:
[Describe comprehensive security solution approach including:]
1. **[Security Control 1]**: [Description and implementation approach]
2. **[Security Control 2]**: [Description and implementation approach]
3. **[Security Control 3]**: [Description and implementation approach]

**Alternative Approaches**:
- **Option 1**: [Brief description with security pros/cons]
- **Option 2**: [Brief description with security pros/cons]
- **Option 3**: [Brief description with security pros/cons]

### Monitoring and Alerting

**Security Event Monitoring**:
```[language]
// Security monitoring implementation
[Include code for tracking security events, threat detection, or incident response]
```

**Threat Detection**:
- [Specify what threats to monitor for]
- [Define alerting thresholds and escalation procedures]
- [Include automated response capabilities]

**Security Metrics**:
- [Define security health indicators and KPIs]
- [Specify monitoring intervals and reporting requirements]
- [Include compliance and audit trail requirements]

### Testing Strategy

**Security Testing**:
```[language]
describe('[Security Feature] Testing', () => {
  it('[security test description]', () => {
    // Security test implementation
  })
  
  it('[penetration test description]', () => {
    // Attack simulation test
  })
})
```

**Vulnerability Assessment**:
- [Describe vulnerability scanning requirements]
- [Include penetration testing needs]
- [Specify security code review requirements]

**Compliance Testing**:
- [Define regulatory compliance test requirements]
- [Include privacy and data protection testing]
- [Specify audit and certification requirements]

**Threat Modeling**:
- [Define threat modeling requirements]
- [Include attack surface analysis]
- [Specify risk assessment and mitigation validation]

### Implementation Timeline

**Phase 1 ([timeframe])**: [Description of immediate security fixes and emergency patches]
**Phase 2 ([timeframe])**: [Description of core security implementation and controls]
**Phase 3 ([timeframe])**: [Description of security testing, validation, and monitoring]
**Phase 4 ([timeframe])**: [Description of compliance validation, documentation, and training]

### Success Criteria

**Technical Security Metrics**:
- [ ] [Specific security requirement or vulnerability remediation target]
- [ ] [Security control effectiveness or coverage target]
- [ ] [Threat detection and response time target]
- [ ] [Security test coverage or penetration test success criteria]

**Business Security Metrics**:
- [ ] [Compliance requirement achievement or certification target]
- [ ] [Risk reduction or security posture improvement target]
- [ ] [Incident response capability or recovery time target]
- [ ] [Customer trust or security confidence improvement]

**Quality Security Metrics**:
- [ ] [Security code quality or vulnerability density improvement]
- [ ] [Security awareness training completion or competency target]
- [ ] [Security documentation completeness or audit readiness target]
- [ ] [Security process maturity or governance improvement]

---

**Priority**: [Critical/High/Medium/Low] - [Brief justification for priority level based on risk assessment, business impact, and regulatory requirements]

---

## Security Template Usage Instructions

### When to Use This Template
- Documenting security vulnerabilities, threats, or weaknesses
- Creating security incident reports or post-mortem analyses
- Planning security improvements or hardening initiatives
- Communicating security risks to business stakeholders and executives

### How to Fill Out Each Section

1. **Problem Classification**: Use consistent security categories and include CVSS scores and CWE classifications
2. **Executive Summary**: Focus on business language, regulatory implications, and quantifiable security risks
3. **General Summary**: Write for non-technical stakeholders who need to understand security implications
4. **Technical Summary**: Include detailed security analysis, attack vectors, and technical remediation for security teams
5. **Success Criteria**: Make security criteria specific, measurable, and aligned with compliance requirements

### Security-Specific Guidelines

- **CVSS Scoring**: Use CVSS v3.1 calculator for consistent vulnerability scoring
- **CWE Classification**: Reference MITRE CWE database for vulnerability categorization
- **Compliance Mapping**: Include relevant regulatory frameworks (GDPR, CCPA, SOC 2, ISO 27001)
- **Threat Intelligence**: Incorporate threat intelligence and attack pattern analysis
- **Risk Assessment**: Include quantitative risk analysis and business impact assessment

### Quality Checklist

Before finalizing a security document, ensure:
- [ ] CVSS score accurately reflects vulnerability severity and exploitability
- [ ] CWE classification correctly categorizes the security weakness
- [ ] Attack vectors are comprehensively documented with exploitation examples
- [ ] Security controls address root causes and provide defense in depth
- [ ] Compliance implications are identified and addressed
- [ ] Incident response and escalation procedures are defined
- [ ] Security testing validates effectiveness of implemented controls
- [ ] Document is reviewed by security team and relevant stakeholders