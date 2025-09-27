# Risk Assessment Analysis Prompts

This document provides structured prompts designed to generate detailed, actionable risk assessment results for **Executive**, **General**, and **Technical** audiences.

## Executive Level: Strategic Risk Assessment
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

## General Level: Comprehensive Risk Overview
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

## Technical Level: Detailed Technical Risk Analysis
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

## Risk Assessment Best Practices

### 1. **Comprehensive Risk Identification**
- Analyze all risk categories (security, operational, financial, compliance)
- Consider both immediate and long-term risks
- Assess interconnected and cascading risk scenarios

### 2. **Quantitative Risk Analysis**
- Use probability and impact scoring matrices
- Calculate potential financial losses and business impact
- Provide risk tolerance recommendations

### 3. **Risk Prioritization**
- Rank risks by business impact and likelihood
- Consider timeline sensitivity and urgency
- Balance risk mitigation costs with potential impact

### 4. **Risk Monitoring and Communication**
- Establish risk monitoring and reporting procedures
- Create stakeholder-appropriate communication formats
- Define success metrics for risk mitigation efforts