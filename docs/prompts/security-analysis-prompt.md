# Security Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable security analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Strategic Security Assessment
```
Perform a comprehensive security analysis of this codebase with executive-level reporting. Provide:

BUSINESS IMPACT ANALYSIS:
- Quantified risk levels (High/Medium/Low) with potential financial impact
- Regulatory compliance gaps and associated penalties/fines
- Competitive disadvantage or reputational risk from security breaches
- Timeline and budget estimates for critical security fixes

EXECUTIVE SUMMARY:
- Top 3 most critical security risks that could impact business operations
- Recommended immediate actions (next 30 days) and their costs
- Strategic security investments needed over 6-12 months
- ROI analysis for proposed security improvements

OUTPUT FORMAT:
- Executive dashboard with key metrics and risk scores
- 1-page executive summary suitable for board presentation
- Cost-benefit analysis with clear financial justification
- Implementation roadmap with milestones and resource requirements

Save comprehensive analysis to: doc/security/executive-security-assessment.md
```

## General Level: Security Overview Assessment  
```
Conduct a security analysis that balances technical detail with business context. Include:

SECURITY OVERVIEW:
- Clear explanation of each security issue and why it matters
- Real-world examples of how vulnerabilities could be exploited
- Impact on system functionality and user experience
- Dependencies between security issues and other system components

PRACTICAL IMPLICATIONS:
- Which security issues should be prioritized and why
- How fixes would affect current development timeline
- Resource requirements (people, time, tools) for implementation
- Testing and validation approaches for security improvements

COMMUNICATION FORMAT:
- Use business-friendly language with technical context
- Include both immediate risks and long-term security strategy
- Provide clear next steps and decision points
- Visual risk matrix showing priority vs complexity

Save analysis to: doc/security/security-overview-analysis.md
```

## Technical Level: Detailed Security Analysis
```
Perform an in-depth technical security analysis covering:

TECHNICAL VULNERABILITY ASSESSMENT:
- Code-level security flaws with line numbers and file references
- Attack vectors and exploitation scenarios with proof-of-concept examples
- Security design pattern violations and architectural weaknesses  
- Dependency vulnerabilities with version-specific CVE details

DETAILED TECHNICAL RECOMMENDATIONS:
- Specific code changes required with before/after examples
- Security libraries, frameworks, and tools to implement
- Configuration changes and environment hardening steps
- Unit test and integration test requirements for security features

IMPLEMENTATION SPECIFICATIONS:
- Technical architecture for security improvements
- API security requirements and authentication mechanisms
- Data encryption, validation, and sanitization specifications
- Monitoring, logging, and incident response technical requirements

COMPLIANCE TECHNICAL DETAILS:
- Technical implementation requirements for regulatory compliance
- Code review checklist for ongoing security validation
- Automated security testing and CI/CD integration requirements

Save detailed analysis to: doc/security/technical-security-analysis.md
Include code examples in: doc/security/security-code-examples/
```

## Best Practices for Security Analysis

### 1. **Comprehensive Security Scan**
- Request analysis of best practices and security issues
- Specify output format and location
- Ask for impact assessment and resolution methods

### 2. **Risk Assessment**
- Compare different types of risks (security vs operational)
- Request quantitative analysis where possible
- Ask for prioritization based on impact

### 3. **Implementation Planning**
- Request step-by-step resolution without implementation
- Ask for prioritized approaches
- Consider different implementation phases

### 4. **Business Case Development**
- Request cost analysis for implementation
- Ask for ROI and cost-benefit calculations
- Consider different investment levels