# Architecture Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable architecture analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Strategic Architecture Assessment
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

## General Level: Comprehensive Architecture Assessment
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

## Technical Level: Detailed Technical Architecture Analysis
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

## Specialized Architecture Analysis Areas

### Microservices Architecture Analysis
```
Analyze microservices architecture implementation and optimization:

MICROSERVICES DESIGN ASSESSMENT:
- Service boundary definition and domain-driven design alignment
- Service granularity and cohesion analysis
- Inter-service communication patterns and protocols
- Data consistency and transaction management across services

MICROSERVICES OPERATIONAL COMPLEXITY:
- Service discovery and load balancing implementation
- Configuration management and service deployment strategies
- Monitoring and observability across distributed services
- Error handling and circuit breaker pattern implementation

MICROSERVICES SCALABILITY AND PERFORMANCE:
- Individual service scaling strategies and resource optimization
- Network latency and communication overhead analysis
- Caching strategies for distributed data access
- Performance monitoring and bottleneck identification across services

Save microservices architecture analysis to: doc/architecture/microservices-architecture-analysis.md
```

### Data Architecture Analysis
```
Analyze data architecture for scalability, consistency, and performance:

DATA MODELING AND STORAGE:
- Database schema design and normalization analysis
- Data storage technology selection (SQL vs NoSQL) appropriateness
- Data partitioning and sharding strategies
- Data archival and retention policy implementation

DATA FLOW AND INTEGRATION:
- Data pipeline architecture and ETL/ELT process optimization
- Real-time vs batch data processing strategy
- Data synchronization across multiple systems and databases
- Data quality and validation architecture implementation

DATA SECURITY AND COMPLIANCE:
- Data encryption at rest and in transit implementation
- Data access control and authorization architecture
- Data privacy and GDPR/CCPA compliance architecture
- Data backup and disaster recovery architecture

Save data architecture analysis to: doc/architecture/data-architecture-analysis.md
```

### Security Architecture Analysis
```
Analyze security architecture for comprehensive threat protection:

SECURITY ARCHITECTURE DESIGN:
- Defense in depth strategy implementation and effectiveness
- Identity and access management architecture assessment
- Network security architecture and segmentation analysis
- Application security architecture and secure coding practices

SECURITY MONITORING AND INCIDENT RESPONSE:
- Security monitoring and SIEM implementation architecture
- Incident response and forensics capability architecture
- Vulnerability management and patch management processes
- Security testing and penetration testing integration

COMPLIANCE AND GOVERNANCE:
- Regulatory compliance architecture (SOX, HIPAA, PCI-DSS)
- Security governance and policy enforcement architecture
- Audit trail and logging architecture for compliance
- Privacy by design implementation in architecture

Save security architecture analysis to: doc/architecture/security-architecture-analysis.md
```

### Cloud Architecture Analysis
```
Analyze cloud architecture for optimization and best practices:

CLOUD ARCHITECTURE DESIGN:
- Cloud service selection and architecture pattern appropriateness
- Multi-cloud vs single-cloud strategy analysis
- Cloud-native architecture principles implementation
- Serverless vs container vs virtual machine architecture decisions

CLOUD SCALABILITY AND RESILIENCE:
- Auto-scaling configuration and effectiveness
- Multi-region and availability zone architecture
- Disaster recovery and business continuity architecture
- Cloud resource optimization and cost management

CLOUD SECURITY AND COMPLIANCE:
- Cloud security architecture and shared responsibility model
- Identity and access management in cloud environments
- Data protection and encryption in cloud storage
- Cloud compliance and governance architecture

Save cloud architecture analysis to: doc/architecture/cloud-architecture-analysis.md
```

## Architecture Modernization and Migration

### Legacy System Modernization
```
Analyze legacy system modernization opportunities and strategies:

LEGACY SYSTEM ASSESSMENT:
- Current legacy system architecture and technology stack analysis
- Business value and technical debt assessment of legacy components
- Integration complexity and dependency analysis
- Risk assessment of maintaining vs modernizing legacy systems

MODERNIZATION STRATEGY PLANNING:
- Strangler fig pattern implementation for gradual modernization
- API-first approach for legacy system integration
- Data migration and synchronization strategies
- Phased modernization roadmap with business value prioritization

MODERNIZATION RISK MITIGATION:
- Business continuity during modernization process
- Data integrity and consistency during migration
- User experience impact and change management
- Rollback and contingency planning for modernization failures

Save legacy modernization analysis to: doc/architecture/legacy-modernization-analysis.md
```

### Architecture Migration Planning
```
Develop comprehensive architecture migration strategy:

MIGRATION ASSESSMENT AND PLANNING:
- Current vs target architecture gap analysis
- Migration complexity and risk assessment
- Resource requirements and timeline estimation
- Business impact and stakeholder communication planning

MIGRATION EXECUTION STRATEGY:
- Phased migration approach with minimal business disruption
- Data migration and synchronization procedures
- Testing and validation strategies for migrated components
- Performance and security validation during migration

POST-MIGRATION OPTIMIZATION:
- Architecture optimization opportunities post-migration
- Performance tuning and scalability improvements
- Cost optimization and resource right-sizing
- Monitoring and observability enhancement

Save architecture migration planning to: doc/architecture/architecture-migration-planning.md
```

## Architecture Analysis Best Practices

### 1. **Holistic Architecture Assessment**
- Consider all architecture layers (presentation, business, data, infrastructure)
- Analyze both functional and non-functional requirements
- Include integration and external dependency considerations

### 2. **Quality Attribute Focus**
- Assess scalability, performance, security, maintainability, and reliability
- Consider trade-offs between different quality attributes
- Align architecture decisions with business priorities

### 3. **Future-Oriented Analysis**
- Consider long-term scalability and evolution requirements
- Assess technology lifecycle and modernization needs
- Plan for changing business requirements and market conditions

### 4. **Risk-Based Decision Making**
- Identify and assess architecture risks and mitigation strategies
- Consider business continuity and disaster recovery requirements
- Balance innovation with stability and reliability needs