# AWS Services Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable AWS services analysis results for **Executive**, **General**, and **Technical** audiences across all major AWS service categories.

## Executive Level: AWS Strategic Assessment
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

## General Level: AWS Implementation Assessment
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

## Technical Level: Detailed AWS Architecture Analysis
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

## AWS Well-Architected Framework Analysis

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

## AWS Analysis Best Practices

### 1. **Comprehensive Service Assessment**
- Evaluate all AWS services in use for optimization opportunities
- Consider service integration and architectural coherence
- Assess alignment with AWS Well-Architected Framework principles

### 2. **Cost-Benefit Analysis**
- Quantify costs and benefits of AWS service optimizations
- Consider both immediate and long-term financial impacts
- Include operational efficiency and productivity improvements

### 3. **Security and Compliance Focus**
- Prioritize security best practices in all AWS service configurations
- Ensure compliance with relevant regulatory requirements
- Implement defense-in-depth security strategies

### 4. **Performance and Scalability Planning**
- Design for current and future performance requirements
- Implement auto-scaling and load balancing strategies
- Monitor and optimize performance continuously

### 5. **Operational Excellence Implementation**
- Automate operational tasks and monitoring
- Implement Infrastructure as Code for consistency
- Establish comprehensive logging and observability