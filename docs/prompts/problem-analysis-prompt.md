# Problem Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable problem analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Strategic Problem Assessment
```
Analyze identified issues and provide executive-level problem assessment including:

BUSINESS PROBLEM QUANTIFICATION:
- Financial impact of each problem (revenue loss, cost increase, opportunity cost)
- Customer satisfaction and retention impact from unresolved issues
- Competitive disadvantage and market position risks
- Regulatory compliance violations and associated penalties

STRATEGIC PROBLEM PRIORITIZATION:
- Problem severity matrix with business impact vs resolution complexity
- Critical path analysis showing problem dependencies and cascading effects
- Timeline sensitivity - which problems worsen without immediate action
- Resource allocation strategy based on problem ROI and business value

EXECUTIVE DECISION FRAMEWORK:
- Go/no-go decisions for problem resolution investments
- Budget requirements and approval thresholds for each problem category
- Stakeholder communication plan for high-impact problems
- Success metrics and KPIs for problem resolution tracking

OUTPUT REQUIREMENTS:
- Executive problem dashboard with key indicators and trends
- Board-level problem summary with clear action recommendations
- Investment justification with ROI analysis for problem resolution
- Risk mitigation timeline with business continuity considerations

Save executive problem assessment to: docs/analysis/executive/problem-analysis/strategic-problem-assessment.md
```

## General Level: Problem Context and Impact Analysis
```
Provide comprehensive problem analysis with balanced technical and business context:

PROBLEM IDENTIFICATION AND CONTEXT:
- Root cause analysis with clear explanation of how problems originated
- Problem interdependencies and how issues compound each other
- User experience impact and customer-facing consequences
- System reliability and operational efficiency implications

PRACTICAL PROBLEM RESOLUTION:
- Problem prioritization based on impact, effort, and business value
- Resource requirements (team, time, budget) for each problem resolution
- Implementation timeline with realistic milestones and dependencies
- Testing and validation strategy to ensure problems are fully resolved

STAKEHOLDER COMMUNICATION:
- Problem explanations suitable for non-technical stakeholders
- Impact assessment in business terms (revenue, customers, operations)
- Decision points requiring management approval or resource allocation
- Progress tracking and reporting framework for problem resolution

ALTERNATIVE SOLUTIONS:
- Multiple resolution approaches with pros/cons analysis
- Workaround strategies for immediate problem mitigation
- Long-term vs short-term solution trade-offs
- Cost-benefit analysis for different resolution approaches

Save problem context analysis to: docs/analysis/general/problem-analysis/problem-context-impact-analysis.md
```

## Technical Level: Detailed Problem Root Cause Analysis
```
Conduct in-depth technical problem analysis covering:

TECHNICAL ROOT CAUSE ANALYSIS:
- Detailed failure mode analysis with system interaction diagrams
- Code-level issues with specific file references and line numbers
- Architecture and design pattern violations contributing to problems
- Performance bottlenecks and scalability limitations causing issues

PROBLEM REPRODUCTION AND DEBUGGING:
- Step-by-step problem reproduction scenarios with test cases
- Debugging methodology and tools for problem investigation
- Log analysis and monitoring data interpretation
- Environment-specific factors contributing to problem manifestation

TECHNICAL SOLUTION SPECIFICATIONS:
- Detailed implementation plans with code examples and architecture changes
- Database schema modifications and migration strategies
- API changes and backward compatibility considerations
- Testing framework requirements for problem validation

PREVENTION AND MONITORING:
- Code review checklist to prevent similar problems
- Automated testing strategies to catch problems early
- Monitoring and alerting improvements to detect problems faster
- Technical debt reduction plan to address underlying problem causes

IMPLEMENTATION ROADMAP:
- Technical task breakdown with effort estimates and dependencies
- Development environment setup for problem resolution
- Deployment strategy and rollback procedures
- Performance benchmarks and success criteria

Save technical problem analysis to: docs/analysis/technical/problem-analysis/detailed-root-cause-analysis.md
Include technical diagrams in: docs/analysis/technical/problem-analysis/technical-diagrams/
Include code examples in: docs/analysis/technical/problem-analysis/solution-examples/
```

## Specialized Problem Analysis Prompts

### Performance Problem Analysis
```
Analyze performance issues with focus on business impact and strategic implications:

BUSINESS PERFORMANCE IMPACT:
- Revenue impact from slow response times and system unavailability
- Customer churn risk and satisfaction scores related to performance
- Operational cost increase from performance-related support and infrastructure
- Competitive disadvantage from poor user experience vs competitors

STRATEGIC PERFORMANCE INVESTMENT:
- Performance optimization ROI with quantified business benefits
- Infrastructure scaling costs vs performance improvement benefits
- Technology modernization investment requirements and timeline
- Market opportunity cost from performance limitations

EXECUTIVE PERFORMANCE METRICS:
- Key performance indicators aligned with business objectives
- Performance SLA requirements for customer contracts and agreements
- Performance benchmarking against industry standards and competitors
- Performance-related risk assessment and mitigation strategies

Save performance business assessment to: docs/analysis/executive/problem-analysis/performance-impact-assessment.md
```

### Integration Problem Analysis
```
Analyze integration issues with focus on system interoperability and business impact:

INTEGRATION PROBLEM IDENTIFICATION:
- API compatibility issues and version conflicts
- Data synchronization problems and consistency issues
- Authentication and authorization integration failures
- Third-party service dependencies and reliability problems

BUSINESS INTEGRATION IMPACT:
- Workflow disruption and operational efficiency impact
- Data integrity risks and compliance implications
- Customer experience degradation from integration failures
- Partner relationship impact from integration reliability issues

INTEGRATION SOLUTION STRATEGY:
- Integration architecture improvements and standardization
- API versioning and backward compatibility strategies
- Error handling and retry mechanisms for robust integrations
- Monitoring and alerting for integration health and performance

Save integration problem analysis to: docs/analysis/general/problem-analysis/integration-problem-assessment.md
```

### User Experience Problem Analysis
```
Analyze user experience issues with focus on customer impact and business consequences:

USER EXPERIENCE PROBLEM ASSESSMENT:
- User journey analysis with pain point identification
- Accessibility issues and compliance gap analysis
- Mobile responsiveness and cross-platform compatibility problems
- User interface usability issues and design inconsistencies

CUSTOMER IMPACT QUANTIFICATION:
- User satisfaction scores and feedback analysis related to UX problems
- Task completion rates and user efficiency metrics
- Customer support ticket analysis for UX-related issues
- User retention and churn correlation with UX problem areas

UX IMPROVEMENT STRATEGY:
- User experience optimization roadmap with priority ranking
- Design system implementation for consistency and maintainability
- Accessibility compliance plan with WCAG guidelines adherence
- User testing and feedback integration process for continuous improvement

Save UX problem analysis to: docs/analysis/general/problem-analysis/ux-problem-impact-analysis.md
```

## Problem Analysis Best Practices

### 1. **Root Cause Focus**
- Dig deep to identify underlying causes, not just symptoms
- Consider system-wide impacts and interdependencies
- Analyze both technical and process-related factors

### 2. **Impact Quantification**
- Measure business impact in concrete terms (revenue, users, time)
- Assess both immediate and long-term consequences
- Consider cascading effects and compound problems

### 3. **Solution-Oriented Analysis**
- Provide multiple resolution approaches with trade-offs
- Consider both quick fixes and long-term solutions
- Include prevention strategies to avoid recurrence

### 4. **Stakeholder Communication**
- Tailor analysis depth and language to audience needs
- Provide clear decision points and approval requirements
- Include progress tracking and success metrics