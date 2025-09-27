# Automation Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable automation analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Automation Strategy Assessment
```
Analyze this project for automation opportunities with executive-level strategic focus:

AUTOMATION BUSINESS CASE:
- ROI analysis for implementing automated analysis workflows
- Cost-benefit comparison of manual vs automated code review processes
- Strategic competitive advantage from automated quality assurance
- Risk reduction quantification from continuous automated monitoring

AUTOMATION INVESTMENT ANALYSIS:
- Implementation costs for automated analysis infrastructure
- Ongoing operational costs for AI-powered code analysis
- Resource savings from reduced manual review time
- Quality improvement metrics and business impact

STRATEGIC AUTOMATION ROADMAP:
- Phase 1: Critical automation priorities with immediate ROI
- Phase 2: Enhanced automation capabilities for competitive advantage
- Phase 3: Advanced AI-driven insights for strategic decision making
- Success metrics and KPIs for automation effectiveness

EXECUTIVE AUTOMATION DECISIONS:
- Budget allocation for automation tools and infrastructure
- Team resource allocation for automation implementation
- Vendor selection criteria for automation platforms
- Governance framework for automated analysis results

Save executive automation assessment to: docs/analysis/executive/automation/automation-strategy-assessment.md
```

## General Level: Automation Implementation Planning
```
Provide comprehensive automation analysis with balanced technical and business context:

AUTOMATION OPPORTUNITY IDENTIFICATION:
- Repetitive analysis tasks suitable for automation
- Manual processes that could benefit from AI assistance
- Quality gates that could be automated in CI/CD pipeline
- Reporting and documentation generation automation potential

PRACTICAL AUTOMATION IMPLEMENTATION:
- Step-by-step automation implementation plan
- Tool selection criteria and evaluation framework
- Integration requirements with existing development workflow
- Training and change management for automated processes

AUTOMATION IMPACT ASSESSMENT:
- Developer productivity improvements from automation
- Code quality consistency through automated analysis
- Faster feedback loops and reduced time-to-market
- Risk mitigation through continuous automated monitoring

IMPLEMENTATION CONSIDERATIONS:
- Resource requirements for automation setup and maintenance
- Timeline for automation rollout with milestone planning
- Change management strategy for team adoption
- Success metrics and continuous improvement framework

Save automation implementation analysis to: docs/analysis/general/automation/automation-implementation-planning.md
```

## Technical Level: Detailed Automation Architecture
```
Conduct in-depth technical automation analysis covering:

AUTOMATION ARCHITECTURE DESIGN:
- CI/CD pipeline integration points for automated analysis
- API integration specifications for AI-powered code review
- Webhook and event-driven automation trigger mechanisms
- Scalable infrastructure design for automated analysis workflows

TECHNICAL AUTOMATION SPECIFICATIONS:
- GitHub Actions workflow configurations for automated analysis
- Docker containerization for consistent analysis environments
- Database schema for storing analysis results and metrics
- API endpoints for triggering and retrieving analysis results

AUTOMATION TOOL INTEGRATION:
- AI/LLM API integration patterns and error handling
- Version control system hooks for automated analysis triggers
- Issue tracking system integration for automated issue creation
- Notification system integration for analysis result distribution

PERFORMANCE AND SCALABILITY:
- Analysis execution time optimization strategies
- Parallel processing implementation for large codebases
- Caching mechanisms for improved analysis performance
- Resource usage monitoring and optimization

AUTOMATION QUALITY ASSURANCE:
- Automated testing for analysis automation workflows
- Result validation and quality control mechanisms
- Error handling and recovery procedures
- Monitoring and alerting for automation system health

Save technical automation analysis to: docs/analysis/technical/automation/detailed-automation-architecture.md
Include automation code examples in: docs/analysis/technical/automation/code-examples/
Include infrastructure diagrams in: docs/analysis/technical/automation/architecture-diagrams/
```

## Specialized Automation Analysis Prompts

### CI/CD Pipeline Analysis
```
Analyze the CI/CD pipeline for automation and optimization opportunities:

PIPELINE EFFICIENCY ANALYSIS:
- Build and deployment time optimization opportunities
- Parallel execution possibilities for faster feedback
- Resource utilization optimization in CI/CD workflows
- Bottleneck identification and resolution strategies

AUTOMATED QUALITY GATES:
- Code quality checks that should be automated in pipeline
- Security scanning integration points and optimization
- Performance testing automation and threshold management
- Compliance checking automation for regulatory requirements

PIPELINE RELIABILITY IMPROVEMENTS:
- Failure point analysis and resilience improvements
- Rollback and recovery automation mechanisms
- Environment consistency and infrastructure as code
- Monitoring and alerting for pipeline health

DEVELOPER EXPERIENCE OPTIMIZATION:
- Feedback loop speed improvements for developers
- Pipeline visibility and debugging capabilities
- Self-service capabilities for common pipeline operations
- Documentation and onboarding automation

Save CI/CD pipeline analysis to: docs/analysis/general/automation/cicd-pipeline-analysis.md
```

### Developer Productivity Analysis
```
Analyze development workflows for automation opportunities that improve productivity:

DEVELOPER WORKFLOW ANALYSIS:
- Repetitive tasks that could be automated to save developer time
- Code review process automation and AI-assisted review
- Documentation generation automation from code and comments
- Testing automation gaps and opportunities

PRODUCTIVITY IMPROVEMENT OPPORTUNITIES:
- IDE integration for automated analysis and suggestions
- Pre-commit hooks for automated code quality checks
- Automated dependency management and security updates
- Template and boilerplate code generation automation

COLLABORATION AUTOMATION:
- Automated project status reporting and dashboards
- Team communication automation for important events
- Knowledge sharing automation through documentation
- Onboarding process automation for new team members

QUALITY ASSURANCE AUTOMATION:
- Automated code formatting and style enforcement
- Test coverage monitoring and reporting automation
- Performance regression detection automation
- Code complexity analysis and refactoring suggestions

Save developer productivity analysis to: docs/analysis/general/automation/developer-productivity-analysis.md
```

### Advanced Development Automation
```
Conduct detailed technical analysis of development automation opportunities:

IDE AND TOOLING AUTOMATION:
- VS Code extension development for automated analysis
- IntelliJ plugin integration for real-time code analysis
- Command-line tool automation for common development tasks
- Git hooks automation for quality gates and analysis

CODE GENERATION AND SCAFFOLDING:
- Automated API endpoint generation from specifications
- Database migration automation and rollback procedures
- Test case generation automation from code analysis
- Documentation automation from code annotations

ADVANCED ANALYSIS AUTOMATION:
- Machine learning integration for pattern recognition
- Automated refactoring suggestions based on code analysis
- Performance profiling automation and optimization suggestions
- Security vulnerability detection and automated patching

DEVELOPMENT ENVIRONMENT AUTOMATION:
- Containerized development environment automation
- Database seeding and test data generation automation
- Environment configuration management automation
- Dependency conflict resolution automation

Save advanced development automation analysis to: docs/analysis/technical/automation/advanced-development-automation.md
```

## Automation Implementation Recommendations

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

## Automation Best Practices

### 1. **Start Small and Scale**
- Begin with high-impact, low-complexity automation
- Gradually expand automation coverage based on success
- Measure and optimize automation effectiveness continuously

### 2. **Focus on Developer Experience**
- Ensure automation enhances rather than hinders development workflow
- Provide clear feedback and actionable recommendations
- Make automation results easily accessible and understandable

### 3. **Quality and Reliability**
- Implement robust error handling and recovery mechanisms
- Validate automation results for accuracy and relevance
- Monitor automation system health and performance

### 4. **Continuous Improvement**
- Regularly review and update automation strategies
- Incorporate feedback from development teams
- Stay current with new automation tools and techniques