# Performance Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable performance analysis results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Performance Impact Business Assessment
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

## General Level: Comprehensive Performance Assessment
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

## Technical Level: Detailed Performance Technical Analysis
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

## Specialized Performance Analysis Areas

### Database Performance Analysis
```
Analyze database performance with focus on optimization opportunities:

DATABASE QUERY OPTIMIZATION:
- Slow query identification with execution plan analysis
- Index optimization and missing index recommendations
- Query rewriting opportunities for better performance
- Database schema normalization and denormalization trade-offs

DATABASE INFRASTRUCTURE PERFORMANCE:
- Connection pooling configuration and optimization
- Read replica strategy for read-heavy workloads
- Database caching implementation and effectiveness
- Database server resource utilization and scaling requirements

DATABASE MONITORING AND MAINTENANCE:
- Database performance monitoring and alerting setup
- Automated maintenance tasks and optimization procedures
- Database backup and recovery performance impact
- Database version upgrade performance considerations

Save database performance analysis to: doc/performance/database-performance-analysis.md
```

### Frontend Performance Analysis
```
Analyze frontend performance with focus on user experience optimization:

FRONTEND LOADING PERFORMANCE:
- Page load time analysis and optimization opportunities
- Resource bundling and minification effectiveness
- Image optimization and lazy loading implementation
- CDN usage and caching strategy optimization

FRONTEND RUNTIME PERFORMANCE:
- JavaScript execution performance and optimization
- DOM manipulation efficiency and virtual DOM usage
- Memory usage patterns and garbage collection impact
- Browser compatibility and performance variations

FRONTEND USER EXPERIENCE METRICS:
- Core Web Vitals measurement and optimization
- Time to Interactive (TTI) and First Contentful Paint (FCP) analysis
- User interaction responsiveness and perceived performance
- Mobile performance optimization and responsive design impact

Save frontend performance analysis to: doc/performance/frontend-performance-analysis.md
```

### API Performance Analysis
```
Analyze API performance with focus on scalability and responsiveness:

API RESPONSE TIME OPTIMIZATION:
- Endpoint response time analysis and bottleneck identification
- API caching strategy implementation and effectiveness
- Database query optimization for API endpoints
- Third-party service integration performance impact

API SCALABILITY ANALYSIS:
- Concurrent request handling capacity and limitations
- Rate limiting implementation and effectiveness
- Load balancing and horizontal scaling strategies
- API gateway performance and optimization opportunities

API MONITORING AND RELIABILITY:
- API performance monitoring and alerting setup
- Error rate analysis and reliability metrics
- API versioning performance impact and optimization
- API documentation and developer experience optimization

Save API performance analysis to: doc/performance/api-performance-analysis.md
```

## Performance Testing and Validation

### Load Testing Strategy
```
Develop comprehensive load testing strategy for performance validation:

LOAD TESTING PLANNING:
- Realistic load scenario development based on usage patterns
- Performance baseline establishment and target setting
- Test environment setup and production parity considerations
- Load testing tool selection and configuration

PERFORMANCE TEST EXECUTION:
- Gradual load increase testing to identify breaking points
- Sustained load testing for stability and reliability validation
- Spike testing for handling sudden traffic increases
- Stress testing to identify system failure modes

PERFORMANCE TEST ANALYSIS:
- Performance metrics collection and analysis procedures
- Bottleneck identification and root cause analysis
- Performance regression detection and prevention
- Performance test result reporting and stakeholder communication

Save load testing strategy to: doc/performance/load-testing-strategy.md
```

### Performance Monitoring Implementation
```
Implement comprehensive performance monitoring for ongoing optimization:

MONITORING INFRASTRUCTURE SETUP:
- Application Performance Monitoring (APM) tool implementation
- Custom metrics collection and dashboard creation
- Real-time alerting configuration for performance thresholds
- Performance data retention and historical analysis capabilities

PERFORMANCE METRICS DEFINITION:
- Key Performance Indicators (KPIs) aligned with business objectives
- Technical performance metrics for system health monitoring
- User experience metrics for customer satisfaction tracking
- Performance trend analysis and predictive monitoring

PERFORMANCE OPTIMIZATION WORKFLOW:
- Automated performance regression detection in CI/CD pipeline
- Performance issue escalation and response procedures
- Regular performance review and optimization planning
- Performance optimization impact measurement and validation

Save performance monitoring implementation to: doc/performance/performance-monitoring-implementation.md
```

## Performance Analysis Best Practices

### 1. **Holistic Performance Assessment**
- Consider all system components (frontend, backend, database, network)
- Analyze performance from both technical and user experience perspectives
- Include scalability and future growth considerations

### 2. **Data-Driven Analysis**
- Use real performance metrics and user data
- Establish baselines and set measurable performance targets
- Validate optimization efforts with before/after comparisons

### 3. **Continuous Performance Optimization**
- Implement ongoing performance monitoring and alerting
- Integrate performance testing into development workflow
- Regularly review and update performance optimization strategies

### 4. **Business Impact Focus**
- Connect performance improvements to business outcomes
- Quantify the cost of performance issues and benefits of optimization
- Prioritize performance improvements based on business value