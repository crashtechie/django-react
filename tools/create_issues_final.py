#!/usr/bin/env python3
"""
GitHub Issues Generator - Final Version
Creates issues without labels to avoid label not found errors
"""

import subprocess

def run_command(cmd):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def create_issue_simple(title, body, milestone_number=None):
    """Create an issue without labels"""
    cmd = f'gh issue create --title "{title}" --body "{body}"'
    if milestone_number:
        cmd += f' --milestone {milestone_number}'
    
    return run_command(cmd)

def main():
    print("🚀 Creating GitHub Issues for Customer Management Improvements")
    print("=" * 65)
    
    # Issues with detailed descriptions
    issues = [
        {
            "title": "Add Loading Spinner Component",
            "body": """**Priority: HIGH - Critical for production**

Create a reusable LoadingSpinner component and implement loading states across all async operations.

**Implementation Details:**
- Create LoadingSpinner component with size variants (sm, md, lg)
- Add loading states to CustomerList, CustomerDetail, CustomerForm
- Add loading states to Dashboard statistics
- Include proper accessibility attributes

**Success Criteria:**
- All async operations show loading feedback
- No more blank screens during API calls
- Component is reusable and well-tested

**Reference:** design_docs/improvements/minor-enhancements.md#1-loading-states--feedback""",
            "milestone": 1
        },
        {
            "title": "Implement Error Boundary Components",
            "body": """**Priority: HIGH - Critical for production**

Implement React Error Boundaries to gracefully handle component crashes.

**Implementation Details:**
- Create ErrorBoundary component with fallback UI
- Add error logging and reporting
- Implement retry functionality in error fallbacks
- Wrap main route components with boundaries

**Success Criteria:**
- Component crashes show user-friendly error messages
- Error reporting works for debugging
- Users can retry failed operations

**Reference:** design_docs/improvements/minor-enhancements.md#2-error-boundary-components""",
            "milestone": 1
        },
        {
            "title": "Comprehensive API Service Tests",
            "body": """**Priority: HIGH - Critical for deployment confidence**

Add comprehensive test coverage for API service layer (currently 0% coverage).

**Implementation Details:**
- Set up MSW (Mock Service Worker) for API mocking
- Test all CRUD operations for customers
- Test search, filtering, and pagination
- Test error scenarios and edge cases

**Success Criteria:**
- API service coverage increases from 0% to 90%+
- All customer endpoints tested
- Error handling verified

**Reference:** design_docs/improvements/frontend-test-coverage.md#1-api-service-layer-0-coverage""",
            "milestone": 1
        },
        {
            "title": "Complete CustomerDetail Component Tests",
            "body": """**Priority: HIGH - Core functionality testing**

Increase CustomerDetail component test coverage from 16.66% to 85%+.

**Implementation Details:**
- Test customer information rendering
- Test loading and error states
- Test navigation to edit page
- Test delete functionality and confirmations

**Success Criteria:**
- Coverage target of 85%+ achieved
- All user interactions tested
- Error scenarios covered

**Reference:** design_docs/improvements/frontend-test-coverage.md#customerdetailtsx-1666-coverage""",
            "milestone": 2
        },
        {
            "title": "Complete CustomerForm Component Tests", 
            "body": """**Priority: HIGH - Form validation critical**

Increase CustomerForm test coverage from 16.66% to 85%+.

**Implementation Details:**
- Test form rendering in new/edit modes
- Test field validation
- Test form submission flows
- Test error handling and user feedback

**Success Criteria:**
- Coverage target of 85%+ achieved
- All form validation tested
- Data integrity assured

**Reference:** design_docs/improvements/frontend-test-coverage.md#customerformtsx-1666-coverage""",
            "milestone": 2
        },
        {
            "title": "Mobile-Responsive Customer Cards",
            "body": """**Priority: MEDIUM - Mobile UX improvement**

Replace desktop table view with mobile-friendly customer cards.

**Implementation Details:**
- Design responsive customer card components
- Implement touch-friendly interactions
- Add proper mobile breakpoints
- Ensure accessibility on mobile devices

**Success Criteria:**
- Native mobile experience without horizontal scrolling
- Touch interactions work properly
- Google Mobile-Friendly test passes

**Reference:** design_docs/improvements/minor-enhancements.md#7-mobile-responsiveness""",
            "milestone": 2
        },
        {
            "title": "Application Monitoring & Observability",
            "body": """**Priority: HIGH - Production readiness**

Implement comprehensive monitoring with Prometheus, Grafana, and structured logging.

**Implementation Details:**
- Set up Prometheus metrics collection
- Configure Grafana dashboards
- Implement structured JSON logging
- Add health check endpoints
- Configure alerting rules

**Success Criteria:**
- Full application visibility
- Proactive issue detection
- <5 minute Mean Time To Detection (MTTD)

**Reference:** design_docs/improvements/production-readiness.md#2-monitoring--observability""",
            "milestone": 3
        },
        {
            "title": "Security Hardening & Rate Limiting",
            "body": """**Priority: HIGH - Production security**

Implement comprehensive security measures for production deployment.

**Implementation Details:**
- Django and Nginx rate limiting
- Security headers configuration
- SSL/TLS proper configuration
- CSP (Content Security Policy) headers
- DDoS protection measures

**Success Criteria:**
- Production-grade security implemented
- Protection against abuse and attacks
- Security audit passes

**Reference:** design_docs/improvements/production-readiness.md#5-rate-limiting--ddos-protection""",
            "milestone": 3
        },
        {
            "title": "Automated Backup & Recovery System",
            "body": """**Priority: HIGH - Data protection**

Create automated backup system with tested recovery procedures.

**Implementation Details:**
- Automated daily database backups
- Configuration and media files backup
- Recovery scripts and procedures
- Backup retention policy (30 days)
- Disaster recovery documentation

**Success Criteria:**
- Automated daily backups working
- Recovery procedures tested and documented
- RTO <15 minutes for critical issues

**Reference:** design_docs/improvements/production-readiness.md#8-backup--recovery-strategy""",
            "milestone": 3
        },
        {
            "title": "Advanced Search & Filtering",
            "body": """**Priority: MEDIUM - Power user features**

Add advanced search capabilities with multiple filter combinations.

**Implementation Details:**
- Advanced search UI with filter combinations
- Search result highlighting
- Search performance optimization
- Search history and suggestions

**Success Criteria:**
- Power user search capabilities
- Improved data discovery
- Better user productivity

**Reference:** design_docs/improvements/implementation-roadmap.md#week-7-advanced-ux-features""",
            "milestone": 4
        },
        {
            "title": "Bulk Operations for Customer Management",
            "body": """**Priority: MEDIUM - Efficiency features**

Implement bulk operations for efficient customer management.

**Implementation Details:**
- Bulk customer selection UI
- Bulk edit, delete, and export functionality
- Progress indicators for bulk operations
- Confirmation dialogs for destructive actions

**Success Criteria:**
- Efficient bulk operations working
- Power user productivity improvements
- Better data management workflow

**Reference:** design_docs/improvements/implementation-roadmap.md#bulk-operations""",
            "milestone": 4
        },
        {
            "title": "Performance Optimization & Bundle Size",
            "body": """**Priority: MEDIUM - User experience optimization**

Optimize application performance and reduce bundle sizes.

**Implementation Details:**
- React.memo optimizations
- Code splitting implementation
- Bundle size optimization
- Performance monitoring setup
- Core Web Vitals improvements

**Success Criteria:**
- <3s load times on 3G networks
- Improved Core Web Vitals scores
- Optimized bundle sizes

**Reference:** design_docs/improvements/production-readiness.md#performance-optimizations""",
            "milestone": 4
        }
    ]
    
    print("Creating issues...")
    created_count = 0
    
    for i, issue in enumerate(issues, 1):
        success, output = create_issue_simple(
            issue["title"],
            issue["body"], 
            issue.get("milestone")
        )
        
        if success:
            print(f"✅ Created issue {i}: {issue['title']}")
            created_count += 1
        else:
            print(f"❌ Failed to create issue {i}: {output}")
    
    print(f"\n🎉 Successfully created {created_count}/{len(issues)} issues!")
    print("\n📋 Next steps:")
    print("1. Visit your GitHub repository Issues tab")
    print("2. Add labels to organize issues (frontend, backend, testing, etc.)")
    print("3. Review milestones and issue assignments")
    print("4. Start with Phase 1 high-priority issues")
    print("5. Use GitHub Projects to track progress")

if __name__ == "__main__":
    main()