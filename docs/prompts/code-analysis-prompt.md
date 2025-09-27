# Code Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable code analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Code Quality Business Impact
```
Analyze the highlighted code section and provide business-focused assessment:

BUSINESS IMPACT ANALYSIS:
- How does this code affect system reliability and availability?
- What are the maintenance costs and technical debt implications?
- Performance impact on user experience and system scalability
- Compliance and regulatory implications of current implementation

STRATEGIC CONSIDERATIONS:
- Does this code support or hinder business objectives?
- Integration complexity with other business systems
- Skills and resource requirements for maintenance and enhancement
- Technology lifecycle and vendor dependency risks

FINANCIAL IMPLICATIONS:
- Development and maintenance cost analysis
- Performance optimization ROI potential
- Risk cost if code quality issues cause system failures
- Training and knowledge transfer costs for this code complexity

Save business impact analysis to: doc/code-analysis/business-impact-analysis.md
```

## General Level: Code Understanding and Context
```
Provide comprehensive code analysis with balanced technical and business context:

CODE ARCHITECTURE OVERVIEW:
- System design philosophy and architectural patterns used
- Code organization and structure with maintainability assessment
- Technology stack evaluation and framework utilization
- Integration points and external dependencies analysis

CODE QUALITY ASSESSMENT:
- Maintainability score with specific improvement recommendations
- Security implementation review with vulnerability assessment
- Performance optimization opportunities with impact analysis
- Technical debt identification with remediation priorities

PRACTICAL IMPLEMENTATION CONTEXT:
- Development workflow integration and developer experience
- Deployment considerations and operational complexity
- Testing strategy and coverage assessment
- Documentation quality and knowledge transfer requirements

IMPROVEMENT ROADMAP:
- Immediate improvements with quick wins and low effort
- Short-term enhancements with moderate impact and effort
- Long-term strategic improvements with high impact
- Success metrics and progress tracking framework

Save code understanding analysis to: doc/code-analysis/code-understanding-context.md
```

## Technical Level: Detailed Technical Code Analysis
```
Conduct in-depth technical code analysis covering:

TECHNICAL ARCHITECTURE DEEP DIVE:
- Component-level technical analysis with code quality scoring
- Database schema optimization and query performance analysis
- API layer architecture with security and performance assessment
- Configuration management and deployment architecture review

CODE IMPLEMENTATION SPECIFICATIONS:
- Security implementation with validation framework analysis
- Performance optimization with benchmarking and caching strategies
- Testing specifications with unit, integration, and performance tests
- Error handling and logging implementation review

TECHNICAL DEBT AND OPTIMIZATION:
- Current technical debt assessment with remediation priorities
- Refactoring recommendations with effort and impact analysis
- Performance bottleneck identification with optimization solutions
- Scalability assessment with architecture improvement recommendations

IMPLEMENTATION ROADMAP:
- Immediate technical improvements with code examples
- Medium-term technical enhancements with architecture changes
- Long-term technical architecture with scalability considerations
- Technical success metrics and monitoring specifications

Save detailed technical analysis to: doc/code-analysis/detailed-technical-analysis.md
Include code examples in: doc/code-analysis/technical-examples/
```

## Code Analysis Best Practices

### 1. **Context-Aware Analysis**
- Understand business requirements and constraints
- Consider system architecture and integration points
- Assess code within broader application ecosystem

### 2. **Multi-Dimensional Quality Assessment**
- Evaluate maintainability, security, performance, and scalability
- Consider technical debt and long-term sustainability
- Assess testing coverage and documentation quality

### 3. **Actionable Recommendations**
- Provide specific, implementable improvement suggestions
- Prioritize recommendations by impact and effort
- Include code examples and implementation guidance

### 4. **Business Value Alignment**
- Connect technical improvements to business outcomes
- Quantify costs and benefits where possible
- Consider resource constraints and timeline implications