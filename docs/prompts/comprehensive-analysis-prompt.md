# Comprehensive Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable analysis results for **Executive**, **General**, and **Technical** audiences across all analysis domains.

## Executive Level: Strategic Analysis Assessment
```
Perform comprehensive analysis with executive-level strategic focus:

BUSINESS IMPACT ANALYSIS:
- Financial impact quantification (revenue, costs, opportunity cost)
- Strategic alignment with business objectives and competitive advantage
- Risk assessment with regulatory compliance and market position implications
- ROI analysis with investment requirements and expected returns

STRATEGIC DECISION FRAMEWORK:
- Priority matrix with business value vs implementation complexity
- Resource allocation strategy and budget requirements
- Timeline sensitivity and critical path dependencies
- Success metrics and KPIs for tracking progress

EXECUTIVE RECOMMENDATIONS:
- Go/no-go decisions with clear justification
- Investment approval thresholds and governance requirements
- Stakeholder communication plan and reporting framework
- Risk mitigation strategies and contingency planning

Save executive analysis to: docs/analysis/executive/comprehensive-strategic-analysis.md
```

## General Level: Balanced Analysis Assessment
```
Provide comprehensive analysis with balanced technical and business context:

ANALYSIS OVERVIEW:
- Current state assessment with strengths and improvement areas
- Problem identification with root cause analysis
- Impact assessment on users, operations, and business processes
- Integration and dependency analysis across system components

PRACTICAL IMPLEMENTATION:
- Solution prioritization based on impact, effort, and business value
- Resource requirements (team, time, budget, tools)
- Implementation timeline with realistic milestones
- Testing and validation strategy

STAKEHOLDER CONSIDERATIONS:
- Communication plan for technical and non-technical audiences
- Change management and training requirements
- Progress tracking and reporting approach
- Success criteria and validation methods

Save general analysis to: docs/analysis/general/comprehensive-balanced-analysis.md
```

## Technical Level: Detailed Technical Analysis
```
Conduct in-depth technical analysis covering:

TECHNICAL ASSESSMENT:
- Architecture analysis with component interaction diagrams
- Code-level analysis with specific file references and line numbers
- Performance profiling with bottleneck identification
- Security vulnerability assessment with exploitation scenarios

TECHNICAL SPECIFICATIONS:
- Implementation plans with code examples and architecture changes
- Database schema modifications and migration strategies
- API design and integration specifications
- Configuration and deployment requirements

QUALITY ASSURANCE:
- Testing framework requirements and test case specifications
- Monitoring and alerting implementation
- Error handling and recovery procedures
- Performance benchmarks and success criteria

IMPLEMENTATION ROADMAP:
- Technical task breakdown with effort estimates
- Development environment setup requirements
- Deployment strategy and rollback procedures
- Maintenance and operational considerations

Save technical analysis to: docs/analysis/technical/comprehensive-technical-analysis.md
Include technical diagrams in: docs/analysis/technical/diagrams/
Include code examples in: docs/analysis/technical/code-examples/
```## Specialized Analysis Prompts

### Security Analysis
```
Analyze security risks with focus on business impact and technical implementation:

SECURITY RISK ASSESSMENT:
- Vulnerability identification with CVSS scoring and business impact
- Compliance gaps and regulatory penalty risks
- Attack vector analysis with exploitation scenarios
- Security control effectiveness assessment

SECURITY IMPLEMENTATION STRATEGY:
- Security architecture improvements and hardening measures
- Authentication and authorization enhancement requirements
- Data protection and encryption implementation
- Security monitoring and incident response procedures

Save security analysis to: docs/analysis/security/comprehensive-security-analysis.md
```

### Performance Analysis
```
Analyze performance issues with focus on optimization and scalability:

PERFORMANCE ASSESSMENT:
- Performance bottleneck identification with profiling data
- Scalability analysis with load testing results
- Resource utilization patterns and optimization opportunities
- Performance impact on user experience and business operations

PERFORMANCE OPTIMIZATION STRATEGY:
- Caching strategy implementation and database optimization
- Code-level optimizations with before/after comparisons
- Infrastructure scaling recommendations
- Performance monitoring and alerting implementation

Save performance analysis to: docs/analysis/performance/comprehensive-performance-analysis.md
```

### Cost Analysis
```
Analyze implementation costs and return on investment:

COST ASSESSMENT:
- Total cost of ownership with 3-5 year projection
- Implementation costs including development, infrastructure, and training
- Operational costs and maintenance implications
- Risk costs and cost of inaction analysis

COST OPTIMIZATION STRATEGY:
- Cost-benefit analysis for different solution approaches
- Resource optimization and efficiency improvements
- Vendor negotiation and procurement optimization
- Cost monitoring and control mechanisms

Save cost analysis to: docs/analysis/cost/comprehensive-cost-analysis.md
```

## Analysis Best Practices

### 1. **Comprehensive Assessment**
- Analyze all relevant domains (security, performance, architecture, cost)
- Consider both immediate and long-term implications
- Include stakeholder impact and change management considerations

### 2. **Data-Driven Analysis**
- Use quantitative metrics and measurable outcomes
- Provide specific examples and evidence
- Include benchmarking against industry standards

### 3. **Actionable Recommendations**
- Prioritize recommendations by impact and feasibility
- Provide clear implementation roadmaps
- Include success criteria and validation approaches

### 4. **Stakeholder Communication**
- Tailor analysis depth and language to audience needs
- Provide clear decision points and approval requirements
- Include progress tracking and reporting frameworksrstanding**
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


*For detailed automation implementation guidance, see [AutomationGuide.md](./AutomationGuide.md)*

---

## AWS Services Analysis Prompts

### Executive Level: AWS Strategic Assessment
```
Analyze AWS service utilization and provide executive-level strategic assessment:

AWS COST OPTIMIZATION ANALYSIS:
- Current AWS spending analysis with cost breakdown by service category
- Reserved Instance and Savings Plan optimization opportunities with ROI calculations
- Right-sizing recommendations with potential cost savings quantification
- Multi-account strategy cost implications and governance requirements

AWS STRATEGIC ALIGNMENT:
- AWS service selection alignment with business objectives and growth strategy
- Cloud-first strategy implementation progress and competitive advantages
- AWS Well-Architected Framework compliance and business risk mitigation
- Digital transformation acceleration through AWS service adoption

AWS BUSINESS CONTINUITY:
- Disaster recovery and business continuity AWS architecture assessment
- Multi-region strategy for high availability and compliance requirements
- AWS security and compliance posture for regulatory requirements
- Vendor lock-in risk assessment and multi-cloud strategy considerations

AWS INVESTMENT ROADMAP:
- AWS service adoption roadmap aligned with business priorities
- Skills and training investment requirements for AWS capabilities
- AWS partnership and support level optimization for business needs
- Innovation opportunities through emerging AWS services and AI/ML capabilities

Save executive AWS analysis to: docs/analysis/executive/aws/aws-strategic-assessment.md
```

### General Level: AWS Implementation Assessment
```
Provide comprehensive AWS analysis with balanced technical and business context:

AWS SERVICE UTILIZATION REVIEW:
- Current AWS services usage patterns and optimization opportunities
- Service integration effectiveness and architectural coherence
- AWS best practices compliance and improvement recommendations
- Cost efficiency analysis with practical optimization strategies

AWS OPERATIONAL EXCELLENCE:
- AWS monitoring and alerting setup effectiveness
- Backup and disaster recovery implementation assessment
- Security group and IAM policy review for least privilege access
- AWS CloudFormation/CDK infrastructure as code maturity

AWS PERFORMANCE OPTIMIZATION:
- EC2 instance types and sizing optimization for workload requirements
- RDS performance tuning and read replica strategy assessment
- CloudFront CDN configuration and caching strategy effectiveness
- Auto Scaling configuration and cost-performance balance

AWS SECURITY AND COMPLIANCE:
- AWS security services implementation (GuardDuty, Security Hub, Config)
- Data encryption at rest and in transit implementation review
- VPC security architecture and network segmentation assessment
- Compliance framework alignment (SOC2, HIPAA, PCI-DSS) with AWS services

Save comprehensive AWS analysis to: docs/analysis/general/aws/aws-implementation-assessment.md
```

### Technical Level: Detailed AWS Architecture Analysis
```
Conduct in-depth technical AWS analysis covering:

AWS INFRASTRUCTURE ARCHITECTURE:
- VPC design with subnet strategy, routing tables, and security group configuration
- EC2 instance selection criteria with performance and cost optimization analysis
- Load balancer configuration (ALB/NLB) with health check and routing optimization
- Auto Scaling policies and CloudWatch metrics integration for dynamic scaling

AWS DATABASE AND STORAGE OPTIMIZATION:
- RDS configuration with Multi-AZ, read replicas, and backup strategy
- S3 bucket policies, lifecycle management, and storage class optimization
- ElastiCache implementation for session management and database query caching
- Database migration strategies and performance optimization techniques

AWS SERVERLESS AND CONTAINER SERVICES:
- Lambda function optimization with memory allocation and execution time analysis
- API Gateway configuration with throttling, caching, and security implementation
- ECS/EKS cluster configuration with service mesh and container optimization
- Step Functions workflow design for complex business process automation

AWS SECURITY TECHNICAL IMPLEMENTATION:
- IAM roles and policies with least privilege access implementation
- AWS KMS key management and encryption strategy technical specifications
- AWS WAF rules configuration and DDoS protection implementation
- VPC Flow Logs and CloudTrail configuration for security monitoring

AWS MONITORING AND OBSERVABILITY:
- CloudWatch custom metrics and dashboard configuration
- X-Ray distributed tracing implementation for microservices
- AWS Config rules for compliance monitoring and automated remediation
- CloudFormation drift detection and infrastructure state management

AWS COST OPTIMIZATION TECHNICAL STRATEGIES:
- Spot Instance integration strategies for cost-effective compute
- S3 Intelligent Tiering and lifecycle policy technical implementation
- Reserved Instance and Savings Plan technical optimization strategies
- AWS Cost Explorer and Budgets API integration for automated cost management

Save detailed technical AWS analysis to: docs/analysis/technical/aws/technical-aws-architecture.md
Include AWS architecture diagrams in: docs/analysis/technical/aws/architecture-diagrams/
Include CloudFormation templates in: docs/analysis/technical/aws/cloudformation-templates/
```

---

## AWS Service-Specific Analysis Prompts

### Compute Services Analysis
```
Analyze AWS compute services optimization opportunities:

EC2 OPTIMIZATION ANALYSIS:
- Instance type recommendations based on CPU, memory, and network requirements
- Spot Instance integration opportunities with fault-tolerant architecture
- Placement groups and enhanced networking configuration for performance
- EC2 Image Builder automation for consistent AMI management

CONTAINER SERVICES ASSESSMENT:
- ECS vs EKS decision criteria based on workload characteristics
- Fargate vs EC2 launch type cost-benefit analysis
- Container image optimization and security scanning implementation
- Service mesh implementation (App Mesh) for microservices communication

SERVERLESS COMPUTE OPTIMIZATION:
- Lambda function performance tuning and cold start optimization
- Lambda Layer strategy for code reuse and deployment optimization
- EventBridge integration for event-driven architecture implementation
- Step Functions vs Lambda orchestration decision framework

Save compute services analysis to: docs/analysis/aws/compute-services-analysis.md
```

### Database Services Analysis
```
Analyze AWS database services for optimal performance and cost:

RDS OPTIMIZATION STRATEGIES:
- Database engine selection criteria (PostgreSQL, MySQL, Aurora)
- Read replica configuration for read-heavy workloads
- Aurora Serverless vs provisioned capacity cost-benefit analysis
- Database parameter group optimization for specific workload patterns

NOSQL DATABASE ASSESSMENT:
- DynamoDB table design and partition key optimization
- DynamoDB Global Tables for multi-region data replication
- DocumentDB vs DynamoDB decision criteria for document storage
- ElastiCache Redis vs Memcached selection for caching strategies

DATABASE MIGRATION AND MODERNIZATION:
- AWS DMS migration strategy with minimal downtime approach
- Database schema optimization for cloud-native performance
- Backup and point-in-time recovery strategy implementation
- Database monitoring with Performance Insights and CloudWatch

Save database services analysis to: docs/analysis/aws/database-services-analysis.md
```

### Storage Services Analysis
```
Analyze AWS storage services for cost optimization and performance:

S3 STORAGE OPTIMIZATION:
- Storage class selection strategy (Standard, IA, Glacier, Deep Archive)
- S3 Transfer Acceleration and CloudFront integration for global performance
- S3 Event Notifications integration with Lambda for automated processing
- Cross-Region Replication and versioning strategy for data protection

BLOCK STORAGE OPTIMIZATION:
- EBS volume type selection (gp3, io2, st1) based on IOPS and throughput requirements
- EBS snapshot lifecycle management and cost optimization
- EFS vs FSx selection criteria for shared file system requirements
- Storage Gateway integration for hybrid cloud storage strategies

DATA ARCHIVAL AND BACKUP:
- AWS Backup centralized backup strategy across multiple services
- Glacier and Deep Archive lifecycle policies for long-term retention
- Cross-account backup strategies for disaster recovery
- Data lifecycle management automation with S3 Intelligent Tiering

Save storage services analysis to: docs/analysis/aws/storage-services-analysis.md
```

### Networking Services Analysis
```
Analyze AWS networking services for security and performance optimization:

VPC ARCHITECTURE OPTIMIZATION:
- Multi-AZ subnet design with public/private subnet strategy
- NAT Gateway vs NAT Instance cost-benefit analysis
- VPC Peering vs Transit Gateway for multi-VPC connectivity
- VPC Endpoints implementation for secure service access

CONTENT DELIVERY AND LOAD BALANCING:
- CloudFront distribution configuration with origin optimization
- Application Load Balancer vs Network Load Balancer selection criteria
- Global Accelerator implementation for improved global performance
- Route 53 DNS optimization with health checks and failover routing

NETWORK SECURITY IMPLEMENTATION:
- Security Group vs NACL usage patterns and best practices
- AWS WAF rule configuration for application-layer protection
- Shield Advanced implementation for DDoS protection
- Network monitoring with VPC Flow Logs and Traffic Mirroring

Save networking services analysis to: docs/analysis/aws/networking-services-analysis.md
```

### Security Services Analysis
```
Analyze AWS security services implementation and optimization:

IDENTITY AND ACCESS MANAGEMENT:
- IAM policy optimization with least privilege access principles
- AWS SSO implementation for centralized identity management
- Cross-account access strategy with assume role patterns
- Service-linked roles and resource-based policies optimization

SECURITY MONITORING AND COMPLIANCE:
- GuardDuty threat detection configuration and response automation
- Security Hub centralized security findings management
- Config rules implementation for compliance monitoring
- CloudTrail logging strategy with log integrity validation

DATA PROTECTION AND ENCRYPTION:
- KMS key management strategy with key rotation policies
- Secrets Manager integration for credential management
- Certificate Manager automation for SSL/TLS certificate lifecycle
- Macie implementation for sensitive data discovery and protection

Save security services analysis to: docs/analysis/aws/security-services-analysis.md
```

### DevOps and Management Services Analysis
```
Analyze AWS DevOps and management services for operational excellence:

CI/CD PIPELINE OPTIMIZATION:
- CodePipeline vs third-party CI/CD tools comparison
- CodeBuild optimization with custom build environments
- CodeDeploy blue-green deployment strategy implementation
- CodeCommit vs external Git repository integration strategies

INFRASTRUCTURE AS CODE:
- CloudFormation vs CDK vs Terraform decision framework
- CloudFormation StackSets for multi-account deployments
- Systems Manager Parameter Store vs Secrets Manager usage patterns
- AWS Config remediation actions for automated compliance

MONITORING AND OBSERVABILITY:
- CloudWatch custom metrics and composite alarms configuration
- X-Ray distributed tracing for microservices debugging
- AWS Distro for OpenTelemetry implementation strategy
- CloudWatch Insights log analysis and alerting automation

Save DevOps services analysis to: docs/analysis/aws/devops-services-analysis.md
```

### AI/ML Services Analysis
```
Analyze AWS AI/ML services for business value and implementation:

MANAGED AI SERVICES ASSESSMENT:
- Amazon Rekognition for image and video analysis use cases
- Amazon Comprehend for natural language processing implementation
- Amazon Textract for document processing automation
- Amazon Polly and Transcribe for voice processing workflows

MACHINE LEARNING PLATFORM EVALUATION:
- SageMaker vs self-managed ML infrastructure cost-benefit analysis
- SageMaker Studio implementation for data science workflows
- SageMaker Pipelines for MLOps and model deployment automation
- SageMaker Model Registry for model versioning and governance

DATA ANALYTICS AND PROCESSING:
- Amazon Redshift vs Athena for data warehousing requirements
- Kinesis Data Streams vs Kinesis Data Firehose for real-time processing
- EMR cluster optimization for big data processing workloads
- QuickSight implementation for business intelligence and dashboards

Save AI/ML services analysis to: docs/analysis/aws/aiml-services-analysis.md
```

---

## AWS Cost Optimization Prompts

### Executive Level: AWS Cost Strategy
```
Analyze AWS costs from strategic business perspective:

AWS COST STRATEGIC ANALYSIS:
- Total Cost of Ownership (TCO) analysis comparing AWS vs on-premises
- AWS spending trend analysis with business growth correlation
- Cost allocation strategy across business units and projects
- AWS cost as percentage of revenue and industry benchmark comparison

AWS COST OPTIMIZATION ROI:
- Reserved Instance and Savings Plan investment ROI calculations
- Right-sizing initiative cost savings potential with implementation timeline
- Automated cost optimization tools ROI (AWS Cost Optimizer, third-party tools)
- Cloud financial management maturity assessment and improvement roadmap

AWS BUDGET AND GOVERNANCE:
- AWS budget allocation strategy aligned with business priorities
- Cost governance framework with approval workflows and spending limits
- Chargeback and showback implementation for cost accountability
- AWS cost anomaly detection and automated response procedures

Save executive AWS cost analysis to: docs/analysis/executive/aws/aws-cost-strategy.md
```

### Technical Level: AWS Cost Optimization Implementation
```
Conduct detailed technical AWS cost optimization analysis:

COMPUTE COST OPTIMIZATION:
- EC2 instance right-sizing analysis with performance impact assessment
- Spot Instance integration patterns with fault-tolerant architecture design
- Lambda function cost optimization with memory and timeout tuning
- Container cost optimization with Fargate vs EC2 analysis

STORAGE COST OPTIMIZATION:
- S3 storage class optimization with lifecycle policy automation
- EBS volume optimization with gp3 migration and snapshot management
- Data transfer cost optimization with CloudFront and VPC Endpoints
- Backup cost optimization with AWS Backup and retention policies

DATABASE COST OPTIMIZATION:
- RDS instance right-sizing and Aurora Serverless cost analysis
- DynamoDB on-demand vs provisioned capacity cost modeling
- Read replica optimization for cost-effective read scaling
- Database backup and snapshot cost optimization strategies

NETWORKING COST OPTIMIZATION:
- Data transfer cost analysis and optimization strategies
- NAT Gateway vs NAT Instance cost comparison with availability trade-offs
- VPC Endpoint implementation for reduced data transfer costs
- CloudFront caching optimization for reduced origin requests

Save technical AWS cost optimization to: docs/analysis/technical/aws/aws-cost-optimization.md
```

---

## AWS Migration Analysis Prompts

### Executive Level: AWS Migration Strategy
```
Analyze AWS migration from strategic business perspective:

MIGRATION BUSINESS CASE:
- Migration ROI analysis with TCO comparison over 3-5 year horizon
- Business continuity and risk mitigation benefits from cloud migration
- Competitive advantage and market agility improvements from AWS adoption
- Innovation acceleration through AWS managed services and AI/ML capabilities

MIGRATION STRATEGIC PLANNING:
- Migration wave strategy aligned with business priorities and dependencies
- Skills and organizational change management requirements
- Vendor and partner ecosystem alignment with AWS migration
- Post-migration optimization and modernization roadmap

MIGRATION RISK ASSESSMENT:
- Business continuity risks during migration with mitigation strategies
- Data security and compliance considerations during migration
- Application performance and user experience impact assessment
- Migration timeline risks and contingency planning

Save executive migration analysis to: docs/analysis/executive/aws/aws-migration-strategy.md
```

### Technical Level: AWS Migration Technical Assessment
```
Conduct detailed technical AWS migration analysis:

APPLICATION MIGRATION ASSESSMENT:
- Application portfolio analysis with migration strategy (6 R's framework)
- Application dependencies mapping and migration sequencing
- Database migration strategy with AWS DMS and SCT assessment
- Legacy application modernization opportunities and approaches

MIGRATION TECHNICAL PLANNING:
- Network connectivity requirements (Direct Connect, VPN, hybrid architecture)
- Data migration strategy with minimal downtime approaches
- Security and compliance requirements mapping to AWS services
- Performance testing and validation framework for migrated applications

MIGRATION AUTOMATION AND TOOLING:
- AWS Migration Hub and Application Discovery Service implementation
- CloudEndure or AWS MGN for server migration automation
- Database migration automation with AWS DMS and ongoing replication
- Migration testing automation and rollback procedures

POST-MIGRATION OPTIMIZATION:
- Cloud-native architecture refactoring opportunities
- AWS managed services adoption for operational efficiency
- Cost optimization implementation post-migration
- Monitoring and observability implementation for migrated workloads

Save technical migration analysis to: docs/analysis/technical/aws/aws-migration-technical.md
```

---

## AWS Well-Architected Framework Analysis Prompts

### Operational Excellence Pillar
```
Analyze AWS architecture against Operational Excellence pillar:

OPERATIONAL PROCEDURES:
- Infrastructure as Code implementation maturity (CloudFormation, CDK, Terraform)
- Deployment automation and CI/CD pipeline effectiveness
- Configuration management and drift detection implementation
- Operational runbook automation and incident response procedures

MONITORING AND OBSERVABILITY:
- CloudWatch metrics, logs, and alarms comprehensive coverage
- Distributed tracing implementation with X-Ray or third-party tools
- Application performance monitoring and business metrics tracking
- Automated remediation and self-healing architecture implementation

ORGANIZATION AND CULTURE:
- DevOps culture maturity and cross-functional team collaboration
- Operational knowledge sharing and documentation practices
- Continuous improvement processes and lessons learned integration
- Operational excellence metrics and KPI tracking

Save operational excellence analysis to: docs/analysis/aws/well-architected/operational-excellence.md
```

### Security Pillar
```
Analyze AWS architecture against Security pillar:

IDENTITY AND ACCESS MANAGEMENT:
- IAM policies and roles least privilege access implementation
- Multi-factor authentication and identity federation setup
- Service-to-service authentication and authorization patterns
- Privileged access management and administrative controls

DETECTIVE CONTROLS:
- AWS CloudTrail comprehensive logging and monitoring
- GuardDuty threat detection and automated response
- Security Hub centralized security posture management
- VPC Flow Logs and network traffic analysis

INFRASTRUCTURE PROTECTION:
- Network segmentation and security group configuration
- Web Application Firewall (WAF) and DDoS protection
- Vulnerability management and patch management processes
- Secure network architecture with defense in depth

DATA PROTECTION:
- Encryption at rest and in transit implementation
- Key management with AWS KMS and rotation policies
- Data classification and handling procedures
- Backup encryption and secure data disposal processes

Save security pillar analysis to: docs/analysis/aws/well-architected/security.md
```

### Reliability Pillar
```
Analyze AWS architecture against Reliability pillar:

FOUNDATIONS:
- Service quotas and limits monitoring and management
- Network topology design for fault isolation
- Multi-AZ and multi-region architecture implementation
- Dependency management and failure isolation strategies

WORKLOAD ARCHITECTURE:
- Microservices vs monolithic architecture reliability assessment
- Circuit breaker and retry logic implementation
- Graceful degradation and fallback mechanism design
- Load balancing and health check configuration

CHANGE MANAGEMENT:
- Deployment strategies (blue-green, canary, rolling) implementation
- Automated testing and validation in deployment pipeline
- Rollback procedures and automated failure detection
- Change impact assessment and risk mitigation

FAILURE MANAGEMENT:
- Disaster recovery and business continuity planning
- Backup and restore procedures testing and validation
- Incident response and post-incident review processes
- Chaos engineering and failure injection testing

Save reliability pillar analysis to: docs/analysis/aws/well-architected/reliability.md
```

### Performance Efficiency Pillar
```
Analyze AWS architecture against Performance Efficiency pillar:

SELECTION:
- Compute service selection optimization (EC2, Lambda, Fargate)
- Storage service selection based on access patterns and performance requirements
- Database service selection and configuration optimization
- Network service selection for optimal data transfer and latency

REVIEW:
- Performance monitoring and metrics collection implementation
- Performance testing and benchmarking procedures
- Capacity planning and scaling strategy effectiveness
- Performance regression detection and alerting

MONITORING:
- Real-time performance monitoring and alerting setup
- Performance dashboard and visualization implementation
- Automated performance optimization and scaling
- Performance anomaly detection and root cause analysis

TRADEOFFS:
- Performance vs cost optimization trade-off analysis
- Consistency vs availability trade-offs in distributed systems
- Latency vs throughput optimization strategies
- Caching strategy implementation and effectiveness

Save performance efficiency analysis to: docs/analysis/aws/well-architected/performance-efficiency.md
```

### Cost Optimization Pillar
```
Analyze AWS architecture against Cost Optimization pillar:

EXPENDITURE AND USAGE AWARENESS:
- Cost allocation tagging strategy and implementation
- AWS Cost Explorer and billing dashboard utilization
- Cost anomaly detection and automated alerting
- Chargeback and showback implementation for cost accountability

COST-EFFECTIVE RESOURCES:
- Right-sizing analysis and implementation across all services
- Reserved Instance and Savings Plan optimization strategy
- Spot Instance integration for fault-tolerant workloads
- Storage class optimization and lifecycle management

MANAGING DEMAND AND SUPPLYING RESOURCES:
- Auto Scaling implementation and optimization
- Demand-based scaling and resource provisioning
- Resource scheduling for non-production environments
- Serverless architecture adoption for variable workloads

OPTIMIZING OVER TIME:
- Regular cost optimization review and implementation processes
- New AWS service evaluation for cost optimization opportunities
- Cost optimization automation and tooling implementation
- Cost optimization culture and best practices adoption

Save cost optimization analysis to: docs/analysis/aws/well-architected/cost-optimization.md
```

### Sustainability Pillar
```
Analyze AWS architecture against Sustainability pillar:

SUSTAINABILITY IN THE CLOUD:
- Carbon footprint assessment and reduction strategies
- AWS renewable energy usage and sustainability reporting
- Resource efficiency optimization for environmental impact
- Sustainable architecture patterns and best practices

SUSTAINABLE WORKLOAD DESIGN:
- Energy-efficient compute and storage service selection
- Workload optimization for reduced resource consumption
- Data center efficiency and AWS region selection for sustainability
- Application lifecycle management for sustainability

Save sustainability analysis to: docs/analysis/aws/well-architected/sustainability.md
```
