# [Bug/Issue ID]: [Brief Descriptive Title]

## Dependencies
- **Blocks**: [List of issues, features, or processes that cannot proceed until this problem is resolved]
- **Depends On**: [List of issues, features, or infrastructure that must be completed before this problem can be addressed]
- **Related**: [List of related issues that share context, components, or impact areas]

## Problem Classification
- **Type**: [Bug/Enhancement/Security/Performance/Infrastructure]
- **Category**: [Frontend/Backend/Testing/Security/Integration/User Experience]
- **Impact**: [Critical/High/Medium/Low] ([Brief impact description])
- **Urgency**: [Critical/High/Medium/Low] ([Brief urgency description])
- **Severity**: [Blocker/Major/Minor/Trivial]

## Timing Information
- **Introduced**: YYYY-MM-DD HH:MM:SS MST ([Description of when/how problem was introduced])
- **Discovered**: YYYY-MM-DD HH:MM:SS MST ([Description of discovery context])
- **Reported**: YYYY-MM-DD HH:MM:SS MST ([When issue was documented])
- **Resolved**: YYYY-MM-DD HH:MM:SS MST ([Resolution date]) OR "Not resolved (Active problem)"
- **Time to Discovery**: [X days] ([Time between introduced and discovered])
- **Time to Report**: [X hours/minutes] after discovery
- **Total Age**: [X days] (For resolved problems) OR "[X+ days] (ongoing)" for active problems

## Executive Summary

**Business Impact**: [Describe how this problem affects business operations, user experience, and strategic objectives. Include specific business processes or workflows that are impacted.]

**Financial Impact**: [Quantify the financial impact with specific dollar amounts or ranges. Include weekly/monthly costs, potential revenue loss, productivity impact, or risk exposure costs.]

**Strategic Risk**: [Explain the broader strategic implications, competitive disadvantage, compliance risks, or long-term consequences if not addressed.]

## General Summary

**Problem Overview**: [Provide a clear, non-technical description of the problem that stakeholders can understand. Explain what is broken, missing, or not working as expected.]

**User Impact**: 
- [List specific ways users are affected]
- [Include workflow disruptions]
- [Note any workarounds users might be using]
- [Describe user experience degradation]

**Business Context**: [Explain why this problem matters to the business, how it relates to business objectives, and the importance of the affected functionality.]

## Technical Summary

### Root Cause Analysis

**Primary Cause**: [Identify the main technical reason for the problem]

**Technical Details**:
```[language]
// Current problematic implementation or error
[Include relevant code snippets, error messages, or configuration issues]
```

**Contributing Factors**:
1. [List secondary causes or conditions that contribute to the problem]
2. [Include environmental factors, dependencies, or design issues]
3. [Note any technical debt or architectural issues]

### Suggested Resolution

**Immediate Fix ([timeframe])**:
```[language]
// Proposed solution with code examples
[Include specific implementation details, configuration changes, or fixes]
```

**Long-term Solution ([timeframe])**:
[Describe comprehensive solution approach including:]
1. **[Solution Component 1]**: [Description and implementation approach]
2. **[Solution Component 2]**: [Description and implementation approach]
3. **[Solution Component 3]**: [Description and implementation approach]

**Alternative Approaches**:
- **Option 1**: [Brief description with pros/cons]
- **Option 2**: [Brief description with pros/cons]
- **Option 3**: [Brief description with pros/cons]

### Monitoring and Alerting

**Performance Monitoring**:
```[language]
// Monitoring implementation
[Include code for tracking metrics, performance, or system health]
```

**Error Tracking**:
- [Specify what errors to monitor]
- [Define alerting thresholds]
- [Include logging requirements]

**Health Checks**:
- [Define system health indicators]
- [Specify monitoring intervals]
- [Include automated testing requirements]

### Testing Strategy

**Unit Tests**:
```[language]
describe('[Component/Function] Testing', () => {
  it('[test description]', () => {
    // Test implementation
  })
  
  it('[test description for error cases]', () => {
    // Error handling test
  })
})
```

**Integration Tests**:
- [Describe integration test requirements]
- [Include API testing needs]
- [Specify cross-component testing]

**End-to-End Tests**:
- [Define user workflow testing]
- [Include browser/device testing requirements]
- [Specify performance testing needs]

**Security Testing** (if applicable):
- [Define security test requirements]
- [Include penetration testing needs]
- [Specify vulnerability scanning]

### Implementation Timeline

**Phase 1 ([timeframe])**: [Description of immediate fixes]
**Phase 2 ([timeframe])**: [Description of core implementation]
**Phase 3 ([timeframe])**: [Description of testing and validation]
**Phase 4 ([timeframe])**: [Description of monitoring and documentation]

### Success Criteria

**Technical Metrics**:
- [ ] [Specific technical requirement or performance target]
- [ ] [System reliability or availability target]
- [ ] [Performance benchmark or response time target]
- [ ] [Test coverage or quality metric]

**Business Metrics**:
- [ ] [User experience improvement target]
- [ ] [Business process efficiency gain]
- [ ] [Cost reduction or revenue impact target]
- [ ] [Customer satisfaction improvement]

**Quality Metrics**:
- [ ] [Code quality or maintainability improvement]
- [ ] [Security compliance achievement]
- [ ] [Documentation completeness target]
- [ ] [Team productivity or velocity improvement]

---

**Priority**: [Critical/High/Medium/Low] - [Brief justification for priority level and urgency of resolution]

---

## Template Usage Instructions

### When to Use This Template
- Creating problem records for bugs, issues, or technical debt
- Documenting security vulnerabilities or performance problems
- Planning major feature implementations or system improvements
- Communicating technical issues to business stakeholders

### How to Fill Out Each Section

1. **Problem Classification**: Use consistent categories and severity levels across all problem documents
2. **Timing Information**: Use MST timezone consistently, estimate dates based on git history or development timeline, include descriptive context for each timestamp
3. **Executive Summary**: Focus on business language and quantifiable impacts
4. **General Summary**: Write for non-technical stakeholders who need to understand the problem
5. **Technical Summary**: Include detailed technical analysis for development teams
6. **Success Criteria**: Make criteria specific, measurable, and time-bound

### Customization Guidelines

- **Remove sections** that don't apply to your specific problem type
- **Add sections** for domain-specific requirements (e.g., compliance, accessibility)
- **Adjust technical detail level** based on your audience and problem complexity
- **Include relevant code examples** in the appropriate programming language
- **Update monitoring and testing sections** to match your technology stack

### Quality Checklist

Before finalizing a problem document, ensure:
- [ ] All placeholders are replaced with actual content
- [ ] Timing information is complete with MST timestamps and context descriptions
- [ ] Financial impacts are quantified where possible
- [ ] Technical solutions include specific implementation details
- [ ] Success criteria are measurable and achievable
- [ ] Timeline is realistic and accounts for dependencies
- [ ] Document is reviewed by both technical and business stakeholders