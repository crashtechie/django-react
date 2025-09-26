# Comprehensive Analysis Prompts for Multi-Audience Code Review

This document provides structured prompts designed to generate detailed, actionable results for **Executive**, **General**, and **Technical** audiences. Each prompt includes specific requirements for context, format, and depth of analysis.

## How to Use This Document

### Executive Prompts
- Focus on **business impact**, ROI, risk levels, and strategic decisions
- Request quantified metrics, timelines, and budget implications
- Emphasize compliance, liability, and competitive advantage

### General Prompts  
- Provide **balanced technical and business context**
- Include clear explanations of technical concepts
- Focus on practical implications and next steps

### Technical Prompts
- Request **detailed technical analysis** with code examples
- Include specific implementation recommendations
- Provide comprehensive technical specifications and requirements

---

## Security Analysis Prompts

### Executive Level: Strategic Security Assessment
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

### General Level: Security Overview Assessment  
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

### Technical Level: Detailed Security Analysis
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

---

## Risk Assessment Analysis Prompts

### Executive Level: Strategic Risk Assessment
```
Analyze this issues document and provide executive-level risk assessment including:

RISK QUANTIFICATION:
- Business impact scoring (1-10) for each identified issue
- Probability of occurrence and potential financial losses
- Regulatory compliance risks and associated penalties
- Competitive and reputational risk assessment

STRATEGIC RISK MATRIX:
- Risk vs Impact matrix with clear prioritization
- Critical path analysis showing which risks could cascade
- Timeline sensitivity - which risks become worse if not addressed
- Resource allocation recommendations based on risk levels

BUSINESS CONTINUITY ANALYSIS:
- Operational failure scenarios and business impact
- Recovery time objectives and acceptable risk levels
- Insurance and liability considerations
- Stakeholder communication requirements for each risk level

OUTPUT REQUIREMENTS:
- Executive risk dashboard with key risk indicators
- Board-level risk summary with clear recommendations
- Budget requirements for risk mitigation by priority level
- Risk monitoring and reporting schedule

Save executive risk assessment to: doc/risk/executive-risk-analysis.md
```

### General Level: Comprehensive Risk Overview
```
Provide a balanced risk analysis that includes both technical and business perspectives:

MULTI-DIMENSIONAL RISK ANALYSIS:
- Security risk vs operational failure risk comparison
- Short-term vs long-term risk implications
- Individual risk assessment and interconnected risk scenarios
- Risk tolerance recommendations based on business context

PRACTICAL RISK MANAGEMENT:
- Which risks should be addressed immediately vs planned remediation
- Risk mitigation strategies with cost-benefit analysis
- Alternative approaches and their risk trade-offs
- Monitoring and early warning indicators for each risk category

STAKEHOLDER COMMUNICATION:
- Risk explanations suitable for non-technical stakeholders
- Decision points and approval requirements
- Implementation timeline with risk reduction milestones
- Success metrics and validation approaches

Save comprehensive risk analysis to: doc/risk/comprehensive-risk-analysis.md
```

### Technical Level: Detailed Technical Risk Analysis
```
Conduct detailed technical risk assessment covering:

TECHNICAL FAILURE ANALYSIS:
- Specific failure modes and root cause analysis
- System dependencies that could amplify risks
- Performance degradation scenarios and thresholds
- Data integrity and consistency risk factors

SECURITY RISK DEEP DIVE:
- Attack surface analysis with technical specifications
- Vulnerability exploit chains and technical impact
- Security control effectiveness assessment
- Threat modeling with technical attack scenarios

OPERATIONAL RISK ASSESSMENT:
- Infrastructure dependencies and single points of failure
- Deployment and configuration risks
- Monitoring and alerting gaps that could mask issues
- Recovery procedures and technical requirements

RISK INTERCONNECTION ANALYSIS:
- Technical dependencies between risk factors
- Cascading failure scenarios with technical details
- Priority ordering based on technical complexity and impact
- Technical debt that amplifies other risks

Save technical risk analysis to: doc/risk/technical-risk-analysis.md
Include technical diagrams in: doc/risk/technical-diagrams/
```

---

## Code Analysis Prompts

### Executive Level: Code Quality Business Impact
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

### General Level: Code Understanding and Context
```
Provide comprehensive code analysis that bridges technical and business understanding:

FUNCTIONAL ANALYSIS:
- What does this code accomplish and why is it important?
- How does it fit into the overall system architecture?
- What business processes or user workflows does it support?
- What would happen if this code failed or performed poorly?

DEPENDENCY AND INTEGRATION ANALYSIS:
- Which other system components depend on this code?
- What external systems, databases, or services does this code require?
- How tightly coupled is this code to other system components?
- What would be the impact of changing or replacing this code?

QUALITY AND MAINTAINABILITY ASSESSMENT:
- Is this code easy to understand and modify?
- Are there potential reliability or performance concerns?
- How well does this code handle error conditions?
- What testing and validation exists for this code?

Save code analysis to: doc/code-analysis/code-context-analysis.md
```

### Technical Level: Detailed Code Analysis
```
Perform comprehensive technical analysis of the highlighted code:

TECHNICAL FUNCTIONALITY ANALYSIS:
- Line-by-line code explanation with algorithm analysis
- Data structures and memory usage patterns
- Control flow analysis and execution paths
- Performance characteristics and complexity analysis

DEPENDENCY MAPPING:
- Detailed dependency graph with specific method/function calls
- Database schema dependencies and query analysis
- External API dependencies and integration points
- Configuration and environment dependencies

TECHNICAL QUALITY ASSESSMENT:
- Code smell identification with specific examples
- Design pattern usage and implementation quality
- Error handling and exception management analysis  
- Thread safety and concurrency considerations

TECHNICAL IMPROVEMENT RECOMMENDATIONS:
- Specific refactoring opportunities with code examples
- Performance optimization possibilities with benchmarks
- Security considerations and hardening recommendations
- Testing requirements and test case specifications

ARCHITECTURAL ANALYSIS:
- How this code fits into overall system architecture
- Adherence to SOLID principles and best practices
- Coupling and cohesion analysis with improvement suggestions
- Scalability and extensibility assessment

Save detailed technical analysis to: doc/code-analysis/detailed-technical-analysis.md
Include code examples and diagrams in: doc/code-analysis/technical-examples/
```

---

## Solution Planning Prompts

### Executive Level: Strategic Solution Planning
```
Develop strategic solution plan with executive-level focus:

BUSINESS-ALIGNED SOLUTION STRATEGY:
- Solution options ranked by business value and strategic alignment
- Investment requirements and expected ROI for each option
- Timeline and resource allocation for implementation
- Risk mitigation strategies for each solution approach

ORGANIZATIONAL IMPACT ASSESSMENT:  
- Staffing and skills requirements for solution implementation
- Change management and training needs
- Stakeholder communication and approval requirements
- Success metrics and business outcome measurements

STRATEGIC DECISION FRAMEWORK:
- Build vs buy vs outsource analysis with total cost of ownership
- Technology platform decisions and long-term implications
- Vendor evaluation criteria and risk assessment
- Implementation phases with business milestone achievements

Save strategic solution plan to: doc/solutions/strategic-solution-plan.md
```

### General Level: Comprehensive Solution Planning
```
Create balanced solution plan addressing both technical and business needs:

SOLUTION OPTIONS ANALYSIS:
- Multiple solution approaches with pros/cons analysis
- Implementation complexity and timeline for each option
- Resource requirements and skill dependencies
- Risk assessment and mitigation strategies for each approach

PRACTICAL IMPLEMENTATION PLANNING:
- Phase-by-phase implementation roadmap
- Dependencies between solution components
- Testing and validation requirements
- Rollback and contingency planning

STAKEHOLDER CONSIDERATIONS:
- Impact on different user groups and business processes
- Training and change management requirements
- Communication plan and status reporting approach
- Success criteria and validation methods

Save comprehensive solution plan to: doc/solutions/comprehensive-solution-plan.md
```

### Technical Level: Detailed Technical Solution Plan
```
Develop comprehensive technical solution plan including:

TECHNICAL ARCHITECTURE PLANNING:
- Detailed technical design with architecture diagrams
- Technology stack selection with technical justification
- Database schema changes and data migration requirements
- API design and integration specifications

IMPLEMENTATION SPECIFICATIONS:
- Step-by-step technical implementation roadmap
- Code structure and module organization plan
- Configuration and deployment requirements
- Security implementation and testing specifications

TECHNICAL VALIDATION PLAN:
- Unit testing strategy and test case specifications
- Integration testing requirements and scenarios
- Performance testing benchmarks and success criteria
- Security testing and penetration testing requirements

DEPLOYMENT AND OPERATIONS PLAN:
- Environment setup and configuration management
- Deployment pipeline and CI/CD integration
- Monitoring and alerting implementation
- Backup, recovery, and maintenance procedures

Save detailed technical solution plan to: doc/solutions/technical-solution-plan.md
Include technical diagrams in: doc/solutions/technical-diagrams/
Include code templates in: doc/solutions/code-templates/
```

---

## Cost Analysis Prompts

### Executive Level: Strategic Financial Analysis
```
Perform comprehensive financial analysis for executive decision-making:

STRATEGIC INVESTMENT ANALYSIS:
- Total Cost of Ownership (TCO) over 3-5 year investment horizon
- Capital expenditure vs operational expenditure breakdown
- ROI analysis with sensitivity analysis for different scenarios
- Budget impact and financing requirements with quarterly cash flow projections

BUSINESS CASE DEVELOPMENT:
- Net Present Value (NPV) calculation with appropriate discount rates
- Break-even analysis and payback period calculations
- Risk-adjusted return calculations including probability-weighted outcomes
- Competitive advantage and market positioning value quantification

FINANCIAL RISK ASSESSMENT:
- Cost overrun probability and budget contingency recommendations
- Revenue impact analysis from system improvements or failures
- Regulatory compliance cost avoidance and penalty prevention value
- Insurance and liability cost implications

STRATEGIC PORTFOLIO ANALYSIS:
- Investment priority ranking across all technology initiatives
- Resource allocation optimization across competing priorities
- Strategic value alignment scoring with business objectives
- Long-term technology platform investment implications

OUTPUT REQUIREMENTS:
- Executive financial dashboard with key cost metrics
- Board presentation slides with financial justification
- Budget request documentation with approval workflow
- Financial milestone tracking and reporting framework

Save executive financial analysis to: doc/cost-analysis/executive-financial-analysis.md
Include financial models in: doc/cost-analysis/financial-models/
```

### General Level: Comprehensive Cost-Benefit Analysis
```
Provide balanced cost-benefit analysis addressing both financial and operational considerations:

IMPLEMENTATION COST ANALYSIS:
- Development costs including personnel, tools, and infrastructure
- Project management and coordination costs
- Training and knowledge transfer expenses
- Testing, validation, and quality assurance costs

OPERATIONAL IMPACT ASSESSMENT:
- Ongoing maintenance and support cost implications
- Performance improvements and efficiency gains
- User productivity impact and business process improvements
- System reliability and availability cost benefits

RISK COST EVALUATION:
- Cost of NOT implementing proposed solutions
- Downtime and business disruption cost analysis
- Security breach and data loss potential costs
- Compliance violation and regulatory penalty risks

DECISION SUPPORT FRAMEWORK:
- Cost-benefit comparison matrix for different solution options
- Implementation timeline with cost distribution over time
- Resource requirement planning with skill and availability analysis
- Success metrics and cost validation approaches

PRACTICAL FINANCIAL PLANNING:
- Budget planning with quarterly expense distribution
- Contingency planning and cost control measures
- Vendor and procurement cost optimization strategies
- Cost monitoring and reporting recommendations

Save comprehensive cost analysis to: doc/cost-analysis/comprehensive-cost-analysis.md
```

### Technical Level: Detailed Technical Cost Analysis
```
Conduct detailed technical cost analysis covering all implementation aspects:

TECHNICAL DEVELOPMENT COSTS:
- Line-by-line effort estimation for code changes
- Architecture and design cost breakdown by component
- Database migration and data transformation costs
- API development and integration technical costs

INFRASTRUCTURE AND PLATFORM COSTS:
- Hardware and cloud infrastructure cost projections
- Software licensing and subscription cost analysis
- Development and testing environment costs
- Deployment and monitoring tool costs

TECHNICAL RESOURCE ANALYSIS:
- Skill-specific hourly rates and availability analysis
- Technical training and certification costs
- External consultant and contractor rate analysis
- Technical tool and platform learning curve costs

PERFORMANCE AND SCALABILITY COSTS:
- Performance optimization development costs
- Load testing and capacity planning expenses
- Scalability architecture implementation costs
- Monitoring and alerting system implementation costs

MAINTENANCE AND OPERATIONS COSTS:
- Code maintenance complexity and ongoing costs
- System administration and operations costs
- Technical debt accumulation and future remediation costs
- Version upgrades and technology refresh costs

TECHNICAL RISK COST ANALYSIS:
- Implementation risk mitigation costs
- Technical failure recovery and rollback costs
- Security vulnerability remediation costs
- Performance degradation business impact costs

OUTPUT SPECIFICATIONS:
- Detailed technical cost breakdown with work breakdown structure
- Resource loading and timeline with critical path analysis
- Technical risk register with cost impact analysis
- Cost validation and tracking methodology

Save detailed technical cost analysis to: doc/cost-analysis/technical-cost-analysis.md
Include technical cost models in: doc/cost-analysis/technical-cost-models/
Include resource planning spreadsheets in: doc/cost-analysis/resource-planning/
```

```
what are the infrastructure and tooling costs associated with implementing continuous security and quality monitoring?
```

```
calculate the training and knowledge transfer costs for implementing these architectural improvements.
```

### Cost Optimization Prompts
```
identify cost-effective alternatives to the proposed solutions that achieve 80% of the benefits at 50% of the cost.
```

```
what are the quick wins that provide immediate cost savings with minimal investment?
```

```
analyze the cost-benefit trade-offs between automated vs manual approaches to addressing these issues.
```

### Documentation and Consolidation
```
can you put all this in a single document in the doc/ folder?
```

```
could you convert the following file to a well formatted pdf document?
```

```
could you add prompts I used in this session to the ExamplePrompts.md file?
```

## Best Practices for Security Analysis Prompts

### 1. **Comprehensive Security Scan**
- Request analysis of best practices and security issues
- Specify output format and location
- Ask for impact assessment and resolution methods

### 2. **Risk Assessment**
- Compare different types of risks (security vs operational)
- Request quantitative analysis where possible
- Ask for prioritization based on impact

### 3. **Code Understanding**
- Ask for specific functionality explanations
- Request dependency analysis (both incoming and outgoing)
- Understand the broader system impact

### 4. **Solution Planning**
- Request step-by-step resolution without implementation
- Ask for prioritized approaches
- Consider different implementation phases

### 5. **Business Case Development**
- Request cost analysis for implementation
- Ask for ROI and cost-benefit calculations
- Consider different investment levels

### 6. **Documentation**
- Request consolidation of analysis into single documents
- Ask for different output formats (PDF, HTML, etc.)
- Maintain prompt history for reference

## Tips for Effective Security Analysis Prompts

### **Be Specific**
- Target specific files, functions, or code sections
- Request particular types of analysis (security, performance, maintainability)
- Specify desired output format and location

### **Ask for Context**
- Request dependency analysis
- Ask about broader system impact
- Understand the business implications

### **Request Actionable Output**
- Ask for specific steps to resolve issues
- Request prioritized recommendations
- Ask for cost-benefit analysis

### **Document Everything**
- Request comprehensive documentation
- Ask for different output formats
- Maintain traceability of analysis and decisions

## Sample Workflow Using These Prompts

1. **Initial Assessment**: Start with comprehensive security scan
2. **Risk Analysis**: Analyze and prioritize identified issues
3. **Code Understanding**: Deep dive into specific problematic areas
4. **Solution Planning**: Develop step-by-step resolution approach
5. **Business Case**: Calculate costs and benefits
6. **Documentation**: Consolidate findings into actionable documents
7. **Format for Stakeholders**: Convert to presentation-ready formats

## Advanced Analysis Prompts

### **Dependency Analysis**
```
what sections of code depend on this code?
what are the dependencies of this code?
```

### **Impact Assessment**
```
what would be the failure risk vs the security risk levels?
what would be the cost savings of implementing these solutions?
```

### **Implementation Planning**
```
what would be the steps to resolve this? do not make any code changes.
what is the agile sprint cost of this resolution with one engineer?
```

---

# AUTOMATION OF ANALYSIS EVALUATIONS

## Overview: Automating Code Analysis with AI

Yes, these evaluations can be automated! Here are several approaches to automate the analysis prompts in this document:

## Automation Approach 1: GitHub Actions + AI API Integration

### Implementation Strategy
Create GitHub Actions workflows that trigger automated analysis on code commits, pull requests, or scheduled intervals.

### Required Components:
```yaml
# .github/workflows/automated-analysis.yml
name: Automated Code Analysis
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'  # Weekly analysis

jobs:
  executive-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Executive Analysis
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python automation/executive_analysis.py
          
  technical-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Technical Analysis
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python automation/technical_analysis.py
```

### Python Automation Script Example:
```python
# automation/automated_analyzer.py
import openai
import os
import json
from pathlib import Path

class AutomatedAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.prompts = self.load_prompts()
    
    def load_prompts(self):
        # Load prompts from ExamplePrompts.md
        with open('ExamplePrompts.md', 'r') as f:
            content = f.read()
        return self.parse_prompts(content)
    
    def analyze_codebase(self, audience_level="executive"):
        results = {}
        for analysis_type, prompt in self.prompts[audience_level].items():
            # Get relevant code files
            code_context = self.get_code_context(analysis_type)
            
            # Run AI analysis
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert code analyst."},
                    {"role": "user", "content": f"{prompt}\n\nCode to analyze:\n{code_context}"}
                ]
            )
            
            results[analysis_type] = response.choices[0].message.content
            
        return results
    
    def generate_reports(self, results, audience_level):
        # Generate formatted reports for each audience
        report_dir = Path(f"doc/{audience_level}-reports")
        report_dir.mkdir(exist_ok=True)
        
        for analysis_type, content in results.items():
            report_path = report_dir / f"{analysis_type}-analysis.md"
            with open(report_path, 'w') as f:
                f.write(content)
```

## Automation Approach 2: Pre-commit Hooks Integration

### Setup Pre-commit Configuration:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: automated-security-analysis
        name: Automated Security Analysis
        entry: python automation/security_analysis.py
        language: python
        files: \.(py|js|ts|java)$
        
      - id: automated-performance-analysis
        name: Automated Performance Analysis
        entry: python automation/performance_analysis.py
        language: python
        files: \.(py|js|ts|java)$
```

## Automation Approach 3: IDE Integration with VS Code Extension

### VS Code Extension Configuration:
```json
{
  "contributes": {
    "commands": [
      {
        "command": "automated-analysis.runExecutiveAnalysis",
        "title": "Run Executive Analysis",
        "category": "Automated Analysis"
      },
      {
        "command": "automated-analysis.runTechnicalAnalysis", 
        "title": "Run Technical Analysis",
        "category": "Automated Analysis"
      }
    ],
    "keybindings": [
      {
        "command": "automated-analysis.runExecutiveAnalysis",
        "key": "ctrl+shift+e",
        "when": "editorFocus"
      }
    ]
  }
}
```

## Automation Approach 4: Docker-based Analysis Pipeline

### Dockerfile for Analysis Environment:
```dockerfile
FROM python:3.11-slim

WORKDIR /analysis

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY automation/ ./automation/
COPY ExamplePrompts.md .

ENTRYPOINT ["python", "automation/run_analysis.py"]
```

### Docker Compose for Multi-stage Analysis:
```yaml
version: '3.8'
services:
  executive-analysis:
    build: .
    environment:
      - ANALYSIS_LEVEL=executive
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./src:/analysis/src:ro
      - ./doc:/analysis/doc
    command: ["--audience", "executive"]
    
  technical-analysis:
    build: .
    environment:
      - ANALYSIS_LEVEL=technical
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./src:/analysis/src:ro
      - ./doc:/analysis/doc
    command: ["--audience", "technical"]
```

## Automation Approach 5: Scheduled Analysis with Azure Functions/AWS Lambda

### Azure Function Example:
```python
import azure.functions as func
import openai
import logging

def main(timer: func.TimerRequest) -> None:
    logging.info('Automated analysis function started')
    
    # Initialize analyzer
    analyzer = AutomatedAnalyzer(os.environ['OPENAI_API_KEY'])
    
    # Run analysis for each audience
    for audience in ['executive', 'general', 'technical']:
        results = analyzer.analyze_codebase(audience)
        analyzer.generate_reports(results, audience)
        
        # Send notifications
        send_analysis_notification(audience, results)
    
    logging.info('Automated analysis completed')
```

## Implementation Recommendations

### Phase 1: Basic Automation (Week 1-2)
1. **Set up GitHub Actions workflow** for automated analysis
2. **Create Python scripts** that use the prompts from this document
3. **Implement basic report generation** for each audience level
4. **Set up notification system** for analysis completion

### Phase 2: Enhanced Integration (Week 3-4)
1. **Add pre-commit hooks** for real-time analysis
2. **Integrate with issue tracking** (GitHub Issues, Jira)
3. **Implement cost tracking** and ROI calculation automation
4. **Create dashboard** for analysis results visualization

### Phase 3: Advanced Automation (Week 5-8)
1. **Develop VS Code extension** for in-editor analysis
2. **Implement machine learning** for pattern recognition
3. **Create automated remediation suggestions**
4. **Add compliance and regulatory checking**

### Required Tools and Services:
- **AI/LLM API**: OpenAI GPT-4, Anthropic Claude, or Azure OpenAI
- **CI/CD Platform**: GitHub Actions, Azure DevOps, or Jenkins
- **Cloud Platform**: Azure Functions, AWS Lambda, or Google Cloud Functions
- **Database**: For storing analysis history and metrics
- **Notification System**: Slack, Microsoft Teams, or email integration

### Cost Considerations for Automation:
- **API Costs**: $20-200/month depending on analysis frequency
- **Cloud Infrastructure**: $10-50/month for basic automation
- **Development Time**: 40-80 hours for full implementation
- **Maintenance**: 2-4 hours/month for updates and monitoring

## Configuration Files for Automation

### Create automation configuration file:
```yaml
# automation-config.yml
analysis:
  schedules:
    executive: "weekly"
    general: "bi-weekly" 
    technical: "daily"
    
  triggers:
    - push_to_main
    - pull_request
    - manual_trigger
    
  outputs:
    formats: [markdown, html, pdf]
    locations:
      executive: "doc/executive-reports/"
      general: "doc/general-reports/"
      technical: "doc/technical-reports/"
      
  notifications:
    executive: ["ceo@company.com", "cto@company.com"]
    general: ["dev-team@company.com"]
    technical: ["tech-leads@company.com"]
    
  ai_settings:
    model: "gpt-4"
    temperature: 0.3
    max_tokens: 4000
```

### Sample automation script:
```python
# automation/analysis_runner.py
#!/usr/bin/env python3

import yaml
import argparse
from automated_analyzer import AutomatedAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Run automated code analysis')
    parser.add_argument('--audience', choices=['executive', 'general', 'technical'], 
                       required=True, help='Target audience for analysis')
    parser.add_argument('--config', default='automation-config.yml',
                       help='Configuration file path')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Initialize and run analyzer
    analyzer = AutomatedAnalyzer(config)
    results = analyzer.analyze_codebase(args.audience)
    
    # Generate reports and notifications
    analyzer.generate_reports(results, args.audience)
    analyzer.send_notifications(results, args.audience)

if __name__ == "__main__":
    main()
```

## Benefits of Automation:
1. **Consistency**: Same analysis quality every time
2. **Frequency**: Regular analysis without manual effort
3. **Scalability**: Analyze multiple projects simultaneously
4. **Historical Tracking**: Monitor improvement trends over time
5. **Cost Efficiency**: Reduce manual analysis time by 80-90%
6. **Early Detection**: Catch issues before they become critical

The automation approaches above can significantly reduce manual effort while providing consistent, comprehensive analysis results for all three audience levels.

---

## Performance Analysis Prompts

### Executive Level: Performance Business Impact Assessment
```
Analyze system performance with focus on business impact and strategic implications:

PERFORMANCE BUSINESS IMPACT:
- User experience impact and customer satisfaction implications
- Revenue impact from performance-related user abandonment or dissatisfaction
- Competitive disadvantage from slower system response compared to competitors
- Scalability limitations that could constrain business growth

PERFORMANCE COST ANALYSIS:
- Infrastructure cost implications of current performance levels
- Cost savings potential from performance optimizations
- Resource efficiency improvements and operational cost reductions
- Performance-related support and maintenance cost analysis

STRATEGIC PERFORMANCE PLANNING:
- Performance requirements to support projected business growth
- Investment priorities for performance infrastructure improvements
- Performance monitoring and SLA requirements for business continuity
- Performance-related risk assessment and mitigation strategies

PERFORMANCE ROI ANALYSIS:
- Business value of performance improvements vs investment costs
- Customer retention and acquisition benefits from better performance
- Operational efficiency gains from performance optimizations
- Long-term scalability investment requirements and timeline

Save executive performance analysis to: doc/performance/executive-performance-analysis.md
```

### General Level: Comprehensive Performance Assessment
```
Provide balanced performance analysis covering technical and business considerations:

PERFORMANCE OVERVIEW:
- Current system performance baseline with key metrics
- Performance bottlenecks and their practical impact on users
- Scalability analysis with realistic growth projections
- Performance comparison with industry standards and competitors

PRACTICAL PERFORMANCE IMPLICATIONS:
- How performance issues affect daily operations and user workflows
- Resource utilization patterns and optimization opportunities
- Performance monitoring and alerting requirements
- Performance testing and validation approaches

PERFORMANCE IMPROVEMENT PLANNING:
- Performance optimization priorities ranked by impact and effort
- Resource requirements for performance improvements
- Timeline and milestone planning for performance enhancements
- Performance success metrics and validation criteria

STAKEHOLDER IMPACT ANALYSIS:
- User experience impact and satisfaction implications
- Business process efficiency and productivity effects
- Support team workload and customer service implications
- Training and communication requirements for performance changes

Save comprehensive performance analysis to: doc/performance/comprehensive-performance-analysis.md
```

### Technical Level: Detailed Performance Technical Analysis
```
Conduct comprehensive technical performance analysis including:

TECHNICAL PERFORMANCE PROFILING:
- CPU, memory, I/O, and network utilization analysis with specific metrics
- Algorithm complexity analysis (Big O notation) for critical code paths
- Database query performance analysis with execution plans
- Concurrency and threading performance characteristics

PERFORMANCE BOTTLENECK IDENTIFICATION:
- Specific code sections causing performance degradation with line numbers
- Memory allocation patterns and potential memory leaks
- I/O operations and blocking calls that impact responsiveness
- Database schema and indexing performance issues

SCALABILITY TECHNICAL ANALYSIS:
- Load testing results with specific performance thresholds
- Horizontal and vertical scaling characteristics and limitations
- Caching strategy effectiveness and optimization opportunities
- Resource consumption patterns under various load conditions

TECHNICAL OPTIMIZATION RECOMMENDATIONS:
- Specific code optimizations with before/after performance comparisons
- Algorithm and data structure improvements with performance impact analysis
- Database optimization strategies including indexing and query optimization
- Infrastructure and architecture improvements for better performance

PERFORMANCE MONITORING TECHNICAL REQUIREMENTS:
- Application Performance Monitoring (APM) tool implementation requirements
- Custom metrics and alerting specifications
- Performance testing automation and CI/CD integration
- Performance regression detection and prevention strategies

Save detailed technical performance analysis to: doc/performance/technical-performance-analysis.md
Include performance benchmarks in: doc/performance/benchmarks/
Include profiling results in: doc/performance/profiling-data/
```

---

## Architecture Analysis Prompts

### Executive Level: Strategic Architecture Assessment
```
Analyze system architecture from strategic business perspective:

STRATEGIC ARCHITECTURE ALIGNMENT:
- How well does current architecture support business objectives and strategy?
- Architecture scalability to support projected business growth over 3-5 years
- Technology platform decisions and their long-term business implications
- Architecture flexibility to adapt to changing market requirements

ARCHITECTURE BUSINESS RISK ASSESSMENT:
- Single points of failure that could impact business operations
- Vendor dependencies and technology lock-in risks
- Architecture complexity and its impact on time-to-market for new features
- Compliance and regulatory architecture requirements

ARCHITECTURE INVESTMENT ANALYSIS:
- Architecture modernization costs vs business value and competitive advantage
- Technology debt and its impact on development velocity and costs
- Architecture decisions that enable or constrain future business opportunities
- ROI analysis for proposed architecture improvements

STRATEGIC TECHNOLOGY PLANNING:
- Architecture roadmap alignment with business strategic initiatives
- Technology platform consolidation and standardization opportunities
- Architecture skills and talent requirements for long-term sustainability
- Architecture governance and decision-making framework requirements

Save strategic architecture analysis to: doc/architecture/strategic-architecture-analysis.md
```

### General Level: Comprehensive Architecture Assessment
```
Provide balanced architecture analysis addressing both technical and business needs:

ARCHITECTURE OVERVIEW:
- Current architecture strengths and areas for improvement
- Component relationships and system integration patterns
- Architecture patterns in use and their appropriateness for current needs
- System boundaries and external dependencies

ARCHITECTURE QUALITY ASSESSMENT:
- Maintainability and extensibility of current architecture
- Scalability characteristics and growth accommodation
- Reliability and fault tolerance architecture patterns
- Security architecture and data protection measures

PRACTICAL ARCHITECTURE IMPLICATIONS:
- Impact of architecture decisions on development team productivity
- Architecture complexity and its effect on system troubleshooting
- Integration challenges and dependencies that affect project delivery
- Architecture documentation and knowledge transfer requirements

ARCHITECTURE IMPROVEMENT PLANNING:
- Architecture refactoring priorities based on business value and risk
- Migration strategies for architecture improvements
- Resource requirements and timeline for architecture changes
- Architecture validation and testing approaches

Save comprehensive architecture analysis to: doc/architecture/comprehensive-architecture-analysis.md
```

### Technical Level: Detailed Technical Architecture Analysis
```
Conduct comprehensive technical architecture analysis including:

TECHNICAL ARCHITECTURE DEEP DIVE:
- Detailed component architecture with interaction diagrams
- Design pattern implementation analysis and adherence to best practices
- SOLID principles compliance assessment with specific examples
- Service architecture analysis (microservices, monolith, modular monolith)

ARCHITECTURE QUALITY ATTRIBUTES:
- Scalability analysis with specific bottleneck identification
- Performance architecture characteristics and optimization opportunities
- Fault tolerance and resilience patterns implementation
- Security architecture analysis including threat modeling

TECHNICAL ARCHITECTURE STANDARDS:
- Code organization and layer separation analysis
- API design consistency and RESTful/GraphQL implementation quality
- Database architecture and data modeling assessment
- Configuration management and environment architecture

ARCHITECTURE TECHNICAL DEBT:
- Architectural anti-patterns and code smells identification
- Component coupling analysis with dependency graphs
- Architecture violation detection and remediation recommendations
- Technical architecture refactoring roadmap with specific improvements

INTEGRATION ARCHITECTURE:
- External system integration patterns and protocols analysis
- Message queuing and event-driven architecture assessment
- Data synchronization and consistency patterns
- API versioning and backward compatibility strategies

DEPLOYMENT AND OPERATIONS ARCHITECTURE:
- Infrastructure as Code and deployment architecture analysis
- Monitoring, logging, and observability architecture
- Disaster recovery and backup architecture assessment
- DevOps and CI/CD pipeline architecture evaluation

Save detailed technical architecture analysis to: doc/architecture/technical-architecture-analysis.md
Include architecture diagrams in: doc/architecture/diagrams/
Include component specifications in: doc/architecture/component-specs/
```

---

## Data Quality Analysis Prompts

### Executive Level: Data Quality Business Impact Assessment
```
Analyze data quality from business impact and strategic perspective:

DATA QUALITY BUSINESS IMPACT:
- Revenue impact from data quality issues (lost sales, customer dissatisfaction)
- Regulatory compliance risks and potential penalties from data quality failures
- Decision-making impact from inaccurate or incomplete data
- Brand reputation and customer trust implications of data quality issues

DATA QUALITY STRATEGIC ANALYSIS:
- Data quality requirements to support business objectives and KPIs
- Data governance maturity assessment and strategic improvement roadmap
- Data quality investment priorities and expected business value
- Competitive advantage opportunities from superior data quality

DATA QUALITY RISK ASSESSMENT:
- Business continuity risks from data corruption or loss scenarios
- Legal and regulatory exposure from data quality and privacy violations
- Customer retention and acquisition impact from data quality issues
- Financial reporting and audit risk from data accuracy problems

DATA QUALITY ROI ANALYSIS:
- Cost-benefit analysis of data quality improvement initiatives
- Productivity gains from better data quality and reduced manual data cleaning
- Customer lifetime value improvements from better data-driven decisions
- Operational efficiency gains from automated data quality processes

Save executive data quality analysis to: doc/data-quality/executive-data-quality-analysis.md
```

### General Level: Comprehensive Data Quality Assessment
```
Provide balanced data quality analysis covering technical and business considerations:

DATA QUALITY OVERVIEW:
- Current data quality baseline with key metrics and quality scores
- Data quality issues impact on business processes and user experience
- Data validation and cleansing processes effectiveness assessment
- Data quality monitoring and alerting current capabilities

DATA QUALITY PRACTICAL IMPLICATIONS:
- How data quality issues affect daily operations and reporting accuracy
- User workflow impact from data quality problems and error handling
- Data integration challenges and quality inconsistencies across systems
- Support team burden from data quality-related user issues

DATA QUALITY IMPROVEMENT PLANNING:
- Data quality improvement priorities ranked by business impact
- Resource requirements for data quality initiatives and tool implementation
- Timeline and milestone planning for data quality enhancements
- Data quality success metrics and validation approaches

STAKEHOLDER DATA IMPACT:
- Business user impact from data quality improvements
- Reporting and analytics accuracy improvements expected
- Customer-facing data quality improvements and their value
- Compliance and audit preparation benefits from better data quality

Save comprehensive data quality analysis to: doc/data-quality/comprehensive-data-quality-analysis.md
```

### Technical Level: Detailed Data Quality Technical Analysis
```
Conduct comprehensive technical data quality analysis including:

DATA VALIDATION TECHNICAL ANALYSIS:
- Input validation mechanisms with specific validation rule analysis
- Data type validation and constraint enforcement assessment
- Business rule validation implementation and gap analysis
- Real-time vs batch data validation architecture evaluation

DATA INTEGRITY TECHNICAL ASSESSMENT:
- Database constraint and referential integrity analysis
- Data consistency patterns across distributed systems
- Transaction management and ACID compliance evaluation
- Data versioning and change tracking technical implementation

DATA PROCESSING RELIABILITY:
- Error handling and exception management in data pipelines
- Data transformation accuracy and loss prevention mechanisms
- Idempotency and reprocessing capabilities for failed data operations
- Data recovery and rollback mechanisms for corrupted data scenarios

DATA QUALITY MONITORING TECHNICAL REQUIREMENTS:
- Data quality metrics collection and monitoring implementation
- Automated data quality testing and validation frameworks
- Data profiling and anomaly detection technical specifications
- Data quality dashboard and alerting system requirements

DATA LINEAGE AND AUDIT TECHNICAL ANALYSIS:
- Data lineage tracking implementation and metadata management
- Audit trail and change logging technical architecture
- Data provenance and transformation history tracking
- Compliance reporting and data governance technical capabilities

DATA PRIVACY AND SECURITY TECHNICAL ASSESSMENT:
- Data encryption and anonymization technical implementation
- PII detection and handling mechanisms
- Data retention and deletion technical processes
- GDPR/CCPA compliance technical requirements and gaps

Save detailed technical data quality analysis to: doc/data-quality/technical-data-quality-analysis.md
Include data quality metrics in: doc/data-quality/metrics/
Include validation specifications in: doc/data-quality/validation-specs/
```

---

## Best Practices for Using These Improved Prompts

### 1. **Context Preparation**
Before using any prompt, ensure you have:
- Specific code files or components to analyze
- Clear business context and objectives
- Relevant stakeholder information and requirements
- Current system documentation and architecture diagrams

### 2. **Audience-Appropriate Execution**
- **Executive**: Focus on business outcomes, ROI, and strategic alignment
- **General**: Balance technical detail with business context
- **Technical**: Provide comprehensive technical specifications and implementation details

### 3. **Output Quality Enhancement**
- Always specify exact output file paths and formats
- Request specific metrics, timelines, and quantifiable results  
- Include success criteria and validation requirements
- Ask for prioritized recommendations with effort/impact analysis

### 4. **Follow-up and Validation**
- Review generated reports for completeness and accuracy
- Validate recommendations with subject matter experts
- Update prompts based on feedback and improved requirements
- Maintain version control of prompt improvements and results

### 5. **Integration with Development Workflow**
- Incorporate analysis results into sprint planning and roadmap discussions
- Use analysis outputs for technical debt prioritization
- Include security and performance requirements in user stories
- Track implementation of recommendations and measure improvements

## Technical Debt Analysis Prompts

### **Code Quality Assessment**
```
identify technical debt in this codebase. What shortcuts or quick fixes have accumulated over time?
```

```
analyze code complexity and maintainability. Which areas would be most difficult for new developers to understand?
```

### **Maintenance Burden Analysis**
```
what parts of this code would be most expensive to maintain or modify? Why?
```

```
identify areas where small changes could require extensive modifications throughout the codebase.
```

### **Refactoring Priorities**
```
prioritize technical debt items by business impact and effort required to resolve. What should be addressed first?
```

```
identify refactoring opportunities that would provide the biggest improvement in code maintainability.
```

### **Future-Proofing Assessment**
```
analyze this code for obsolete patterns, deprecated dependencies, or technologies nearing end-of-life.
```

```
what technical debt items pose the highest risk to future development velocity or system stability?
```

## Comprehensive Analysis Workflows

### **Performance Review Workflow**
1. **Initial Assessment**: Identify bottlenecks and resource issues
2. **Scalability Analysis**: Test limits and breaking points
3. **Optimization Planning**: Prioritize improvements by impact
4. **Resource Management**: Evaluate cleanup and efficiency
5. **Monitoring Strategy**: Define performance metrics and alerts

### **Architecture Review Workflow**
1. **Current State Analysis**: Document existing architecture
2. **Design Pattern Review**: Evaluate implementation patterns
3. **Coupling Analysis**: Assess component dependencies
4. **Scalability Assessment**: Plan for future growth
5. **Improvement Roadmap**: Prioritize architectural changes

### **Data Quality Review Workflow**
1. **Validation Analysis**: Review data validation mechanisms
2. **Error Handling Review**: Assess data error scenarios
3. **Consistency Checks**: Evaluate data integrity measures
4. **Compliance Assessment**: Check regulatory requirements
5. **Quality Metrics**: Define data quality monitoring

### **Technical Debt Review Workflow**
1. **Debt Identification**: Catalog existing technical debt
2. **Impact Assessment**: Evaluate business impact of debt items
3. **Effort Estimation**: Calculate cost to resolve each item
4. **Priority Matrix**: Rank by impact vs effort
5. **Remediation Plan**: Create staged debt reduction strategy

## Combined Analysis Prompts

### **Holistic Code Review**
```
perform a comprehensive analysis of this code covering security, performance, architecture, data quality, and technical debt. Provide a prioritized action plan.
```

### **Risk Assessment Across Domains**
```
identify the highest risk areas considering security vulnerabilities, performance bottlenecks, architectural weaknesses, data quality issues, and technical debt.
```

### **Cost-Benefit Analysis for Improvements**
```
calculate the cost and benefit of addressing the identified issues across performance, architecture, data quality, and technical debt. What provides the best ROI?
```

### **Comprehensive Cost Analysis**
```
perform a detailed cost analysis including development effort, operational impact, risk mitigation value, and long-term ROI for all identified improvements.
```

### **Budget-Constrained Planning**
```
given a budget constraint of $X, prioritize and plan the most impactful improvements across security, performance, architecture, data quality, and technical debt.
```

### **Implementation Roadmap**
```
create a phased implementation plan that addresses security, performance, architecture, data quality, and technical debt issues in the most effective order.
```

## Domain-Specific Best Practices

### **Performance Analysis Tips**
- Focus on actual bottlenecks, not theoretical optimizations
- Consider both time and space complexity
- Evaluate performance under realistic load conditions
- Include monitoring and alerting in recommendations

### **Architecture Analysis Tips**
- Look for SOLID principles violations
- Assess testability and maintainability
- Consider future evolution and extension points
- Evaluate technology choices and their long-term viability

### **Data Quality Analysis Tips**
- Test with real-world data scenarios
- Consider data volume, velocity, and variety
- Evaluate both input validation and output verification
- Include data lineage and auditability requirements

### **Technical Debt Analysis Tips**
- Quantify the impact on development velocity
- Consider both short-term fixes and long-term solutions
- Assess the risk of leaving debt unaddressed
- Balance debt reduction with feature development


is  there a way to automate these evaluations based on the prompts in this document?
