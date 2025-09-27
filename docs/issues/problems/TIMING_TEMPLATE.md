# Problem Timing Section Template

This template shows how to add timing information to problem documents.

## Timing Section Format

Add this section after the "Problem Classification" section in each problem document:

```markdown
## Timing Information
- **Introduced**: YYYY-MM-DD HH:MM:SS MST (Description of when/how problem was introduced)
- **Discovered**: YYYY-MM-DD HH:MM:SS MST (Description of discovery context)
- **Reported**: YYYY-MM-DD HH:MM:SS MST (When issue was documented)
- **Resolved**: YYYY-MM-DD HH:MM:SS MST (Resolution date) OR "Not resolved (Active problem)"
- **Time to Discovery**: X days (Time between introduced and discovered)
- **Time to Report**: X hours/minutes after discovery
- **Total Age**: X days (For resolved problems) OR "X+ days (ongoing)" for active problems
```

## Example Implementation

### For Active Problems:
```markdown
## Timing Information
- **Introduced**: 2024-01-15 02:00:00 MST (Initial development phase)
- **Discovered**: 2024-02-20 07:30:00 MST (During integration testing)
- **Reported**: 2024-02-20 08:45:00 MST (Documented in issue tracker)
- **Resolved**: Not resolved (Active problem)
- **Time to Discovery**: 36 days
- **Time to Report**: 1.25 hours after discovery
- **Total Age**: 45+ days (ongoing)
```

### For Resolved Problems:
```markdown
## Timing Information
- **Introduced**: 2024-01-10 01:30:00 MST (Jest configuration setup)
- **Discovered**: 2024-01-25 09:45:00 MST (Test execution failure)
- **Reported**: 2024-01-25 10:15:00 MST (Issue documented)
- **Resolved**: 2024-01-26 03:30:00 MST (Configuration fix applied)
- **Time to Discovery**: 15 days
- **Time to Report**: 30 minutes after discovery
- **Total Age**: 16 days (resolved in 1 day)
```

## Timing Guidelines

### Date/Time Format
- Use MST timezone for consistency
- Format: YYYY-MM-DD HH:MM:SS MST
- Include descriptive context in parentheses

### Time Calculations
- **Time to Discovery**: Days between introduced and discovered
- **Time to Report**: Hours/minutes between discovered and reported
- **Total Age**: For resolved problems, total days from introduced to resolved
- **Total Age**: For active problems, days from introduced to current date with "(ongoing)"

### Context Descriptions
- **Introduced**: Brief description of when/how the problem was introduced
- **Discovered**: Context of how the problem was found (testing, user report, etc.)
- **Reported**: When the problem was formally documented
- **Resolved**: When the problem was fixed (if applicable)

## Benefits of Timing Information

1. **Project Management**: Track problem lifecycle and resolution efficiency
2. **Process Improvement**: Identify patterns in discovery and resolution times
3. **Risk Assessment**: Understand how long problems can go undetected
4. **Team Performance**: Measure response times and resolution speed
5. **Historical Analysis**: Learn from past problem patterns
6. **Stakeholder Communication**: Provide concrete timelines for problem resolution

## Implementation Notes

- Add timing sections to all existing problem documents
- Estimate dates based on git history, commit messages, and development timeline
- For older problems, use best available estimates with appropriate context
- Update resolved dates when problems are fixed
- Maintain consistency in format across all documents

---

**Template Version**: 1.0
**Last Updated**: Current
**Usage**: Apply to all problem documents for comprehensive timing tracking