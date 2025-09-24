#!/usr/bin/env python3
"""
GitHub Issues Generator for Customer Management System Improvements

This script generates GitHub issues based on the improvement roadmap.
Run with: python scripts/generate_github_issues.py

Prerequisites:
- GitHub CLI installed and authenticated
- Run from project root directory
"""

import json
import subprocess
import sys
from pathlib import Path

# Define all issues based on the improvement roadmap
MILESTONES = [
    {
        "title": "Phase 1: Foundation (Weeks 1-2)",
        "description": "Critical UX and stability improvements - Loading states, error handling, and API testing foundation",
        "due_date": "2025-10-07"  # 2 weeks from Sept 23
    },
    {
        "title": "Phase 2: User Experience (Weeks 3-4)", 
        "description": "Enhanced usability and mobile support - Form improvements, mobile responsiveness, accessibility",
        "due_date": "2025-10-21"  # 4 weeks from Sept 23
    },
    {
        "title": "Phase 3: Production Features (Weeks 5-6)",
        "description": "Production stability and monitoring - Observability, security hardening, deployment automation",
        "due_date": "2025-11-04"  # 6 weeks from Sept 23
    },
    {
        "title": "Phase 4: Advanced Features (Weeks 7-8)",
        "description": "Enhanced functionality and developer experience - Power user features, performance optimization",
        "due_date": "2025-11-18"  # 8 weeks from Sept 23
    }
]

ISSUES = [
    # Phase 1: Foundation
    {
        "title": "Add Loading Spinner Component",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category  
- [x] User Experience
- [x] Frontend

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/minor-enhancements.md#1-loading-states--feedback`

### 📝 Description
Create a reusable LoadingSpinner component and implement loading states across all async operations to eliminate blank screens and improve user experience.

### 🎯 Success Criteria
- [x] LoadingSpinner component created with size variants (sm, md, lg)
- [x] Loading states added to CustomerList during fetch
- [x] Loading states added to CustomerDetail during fetch  
- [x] Loading states added to CustomerForm during save
- [x] Loading states added to Dashboard statistics

### 🧪 Testing Requirements
- [x] Component unit tests
- [x] Loading state integration tests
- [x] Visual regression tests for spinners

### 📊 Metrics Impact
**Before:**
- Blank screens during API calls
- Users unsure if app is working

**After (Expected):**
- Clear loading indicators for all async operations
- Improved perceived performance

### ✅ Definition of Done
- [x] LoadingSpinner component implemented
- [x] Used in all page components
- [x] Tests written and passing
- [x] Storybook stories created
- [x] Documentation updated""",
        "labels": ["enhancement", "frontend", "priority/high", "ux", "phase-1"],
        "milestone": 1
    },
    
    {
        "title": "Implement Error Boundary Components",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] User Experience
- [x] Frontend
- [x] Production Readiness

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/minor-enhancements.md#2-error-boundary-components`

### 📝 Description
Implement React Error Boundaries to gracefully handle component crashes and provide fallback UI instead of blank screens.

### 🎯 Success Criteria
- [x] ErrorBoundary component created
- [x] ErrorFallback component with retry functionality
- [x] Error logging integration
- [x] Wrapped around main route components
- [x] Different fallbacks for different component types

### 🧪 Testing Requirements
- [x] Error boundary unit tests
- [x] Error scenario simulation tests
- [x] Error logging verification

### 📊 Metrics Impact
**Before:**
- Component crashes cause blank screens
- No error reporting or recovery

**After (Expected):**
- Graceful error handling with user-friendly messages
- Error tracking for debugging
- Recovery options for users

### ✅ Definition of Done
- [x] ErrorBoundary implemented and tested
- [x] Deployed across all major components
- [x] Error logging working
- [x] Fallback UI provides good UX""",
        "labels": ["enhancement", "frontend", "priority/high", "error-handling", "phase-1"],
        "milestone": 1
    },

    {
        "title": "Implement Comprehensive API Service Tests",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Testing
- [x] Frontend

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/frontend-test-coverage.md#1-api-service-layer-0-coverage`

### 📝 Description
Add comprehensive test coverage for the API service layer which currently has 0% coverage. This is critical for deployment confidence.

### 🎯 Success Criteria
- [x] API service coverage: 0% → 90%
- [x] All CRUD operations tested
- [x] Search and filtering tested  
- [x] Pagination handling tested
- [x] Error scenarios tested
- [x] Request/response interceptors tested

### 🧪 Testing Requirements
- [x] MSW (Mock Service Worker) configured
- [x] Test fixtures and mock data created
- [x] Network error simulation
- [x] Authentication error handling

### 📊 Metrics Impact
**Before:**
- API service coverage: 0%
- No confidence in API integration

**After (Expected):**
- API service coverage: 90%+
- Full confidence in deployment
- Better error handling

### 🔄 Implementation Notes
- Set up MSW for API mocking
- Create shared test utilities
- Test all customer endpoints
- Include edge cases and error scenarios

### ✅ Definition of Done
- [x] API service tests implemented
- [x] Coverage target achieved (90%+)
- [x] All CRUD operations covered
- [x] Error scenarios tested
- [x] CI pipeline updated""",
        "labels": ["enhancement", "testing", "priority/high", "api", "phase-1"],
        "milestone": 1
    },

    {
        "title": "Complete CustomerDetail Component Tests", 
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Testing
- [x] Frontend

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/frontend-test-coverage.md#customerdetailtsx-1666-coverage`

### 📝 Description
Increase CustomerDetail component test coverage from 16.66% to 85%. This is core user functionality that needs comprehensive testing.

### 🎯 Success Criteria
- [x] CustomerDetail coverage: 17% → 85%
- [x] Customer information rendering tested
- [x] Loading states tested
- [x] Error handling tested (404, etc.)
- [x] Navigation to edit page tested
- [x] Delete functionality tested
- [x] Confirmation dialogs tested

### 🧪 Testing Requirements
- [x] Component rendering tests
- [x] User interaction tests
- [x] API integration tests
- [x] Route navigation tests

### 📊 Metrics Impact
**Before:**
- CustomerDetail coverage: 17%
- Core functionality untested

**After (Expected):**
- CustomerDetail coverage: 85%+
- All user paths tested
- Confidence in customer detail workflow

### ✅ Definition of Done
- [x] Coverage target achieved (85%+)
- [x] All user interactions tested
- [x] Error scenarios covered
- [x] Navigation flows tested""",
        "labels": ["enhancement", "testing", "priority/high", "component-test", "phase-2"],
        "milestone": 2
    },

    {
        "title": "Complete CustomerForm Component Tests",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Testing  
- [x] Frontend

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/frontend-test-coverage.md#customerformtsx-1666-coverage`

### 📝 Description
Increase CustomerForm component test coverage from 16.66% to 85%. Critical for data entry validation and form handling.

### 🎯 Success Criteria
- [x] CustomerForm coverage: 17% → 85%
- [x] Form rendering (new/edit modes) tested
- [x] Field validation tested
- [x] Form submission tested
- [x] Error handling tested
- [x] Navigation after save tested

### 🧪 Testing Requirements
- [x] Form validation tests
- [x] Submission flow tests
- [x] Error scenario tests
- [x] User input simulation tests

### 📊 Metrics Impact
**Before:**
- CustomerForm coverage: 17%
- Form validation untested

**After (Expected):**
- CustomerForm coverage: 85%+
- All form scenarios tested
- Data integrity assured

### ✅ Definition of Done
- [x] Coverage target achieved (85%+)
- [x] All form validation tested
- [x] Submission flows tested
- [x] Error handling verified""",
        "labels": ["enhancement", "testing", "priority/high", "forms", "phase-2"],
        "milestone": 2
    },

    {
        "title": "Implement Mobile-Responsive Customer Cards",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] Medium (Important for UX)

### 📂 Category
- [x] User Experience
- [x] Frontend
- [x] Mobile

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/minor-enhancements.md#7-mobile-responsiveness`

### 📝 Description
Replace desktop-only table view with mobile-friendly customer cards to improve mobile user experience.

### 🎯 Success Criteria
- [x] Mobile customer cards created
- [x] Responsive breakpoints implemented
- [x] Touch-friendly interactions
- [x] Proper spacing and typography
- [x] Accessible on mobile devices

### 🧪 Testing Requirements
- [x] Mobile viewport testing
- [x] Touch interaction tests
- [x] Responsive breakpoint tests
- [x] Accessibility testing on mobile

### 📊 Metrics Impact
**Before:**
- Poor mobile experience with tables
- Horizontal scrolling required

**After (Expected):**
- Native mobile experience
- Google Mobile-Friendly test passes

### ✅ Definition of Done
- [x] Mobile cards implemented
- [x] Responsive across all breakpoints  
- [x] Touch interactions working
- [x] Mobile usability improved""",
        "labels": ["enhancement", "frontend", "priority/medium", "mobile", "responsive", "phase-2"],
        "milestone": 2
    },

    {
        "title": "Add Form Validation with Real-time Feedback",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] Medium (Important for UX)

### 📂 Category
- [x] User Experience
- [x] Frontend
- [x] Forms

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/minor-enhancements.md#3-form-validation--feedback`

### 📝 Description
Enhance form validation with real-time feedback, user-friendly error messages, and email uniqueness checking.

### 🎯 Success Criteria
- [x] Real-time validation feedback
- [x] User-friendly error messages
- [x] Email uniqueness validation
- [x] Phone format validation
- [x] Visual validation states (success/error)

### 🧪 Testing Requirements
- [x] Validation logic tests
- [x] Real-time feedback tests
- [x] API integration tests for uniqueness
- [x] User experience tests

### 📊 Metrics Impact
**Before:**
- Basic validation with generic messages
- Poor user guidance

**After (Expected):**
- Professional form experience
- Reduced form submission errors
- Better data quality

### ✅ Definition of Done
- [x] Enhanced validation implemented
- [x] Real-time feedback working
- [x] User-friendly error messages
- [x] Form UX significantly improved""",
        "labels": ["enhancement", "frontend", "priority/medium", "forms", "validation", "phase-2"],
        "milestone": 2
    },

    {
        "title": "Implement Application Monitoring & Observability",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Production Readiness
- [x] Monitoring
- [x] Infrastructure

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/production-readiness.md#2-monitoring--observability`

### 📝 Description
Implement comprehensive monitoring with Prometheus, Grafana dashboards, structured logging, and health check endpoints.

### 🎯 Success Criteria
- [x] Prometheus metrics collection
- [x] Grafana dashboards configured
- [x] Structured JSON logging
- [x] Health check endpoints
- [x] Performance monitoring middleware
- [x] Alert rules configured

### 🧪 Testing Requirements
- [x] Monitoring stack deployment tests
- [x] Metrics collection verification
- [x] Dashboard functionality tests
- [x] Alert rule tests

### 📊 Metrics Impact
**Before:**
- No application observability
- Manual troubleshooting

**After (Expected):**
- Full application visibility
- Proactive issue detection
- <5 minute MTTD (Mean Time To Detection)

### 🔄 Implementation Notes
- Set up Prometheus and Grafana containers
- Configure Django performance middleware
- Implement structured logging
- Create alerting rules

### ✅ Definition of Done
- [x] Monitoring stack deployed
- [x] Dashboards showing key metrics
- [x] Logging structured and searchable
- [x] Alerts configured and tested""",
        "labels": ["enhancement", "infrastructure", "priority/high", "monitoring", "observability", "phase-3"],
        "milestone": 3
    },

    {
        "title": "Implement Security Hardening & Rate Limiting",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Security
- [x] Production Readiness

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/production-readiness.md#5-rate-limiting--ddos-protection`

### 📝 Description
Implement rate limiting, security headers, SSL/TLS configuration, and DDoS protection for production security.

### 🎯 Success Criteria
- [x] Django rate limiting implemented
- [x] Nginx rate limiting configured
- [x] Security headers configured
- [x] SSL/TLS properly configured  
- [x] CSP headers implemented
- [x] Rate limit testing completed

### 🧪 Testing Requirements
- [x] Rate limiting functionality tests
- [x] Security header verification
- [x] SSL/TLS configuration tests
- [x] Load testing with rate limits

### 📊 Metrics Impact
**Before:**
- Basic security configuration
- Vulnerable to abuse

**After (Expected):**
- Production-grade security
- Protection against DDoS and abuse
- Security best practices implemented

### ✅ Definition of Done
- [x] Rate limiting working on all endpoints
- [x] Security headers configured
- [x] SSL/TLS properly configured
- [x] Security audit passes""",
        "labels": ["enhancement", "security", "priority/high", "rate-limiting", "ssl", "phase-3"],
        "milestone": 3
    },

    {
        "title": "Create Automated Backup & Recovery System",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] High (Critical for production)

### 📂 Category
- [x] Production Readiness
- [x] Infrastructure
- [x] Data Protection

### 🔗 Related Documentation  
**Reference**: `design_docs/improvements/production-readiness.md#8-backup--recovery-strategy`

### 📝 Description
Implement automated backup system with recovery procedures to protect production data and ensure business continuity.

### 🎯 Success Criteria
- [x] Automated daily database backups
- [x] Media files backup (if applicable)
- [x] Configuration backup
- [x] Recovery scripts tested
- [x] Backup retention policy (30 days)
- [x] Disaster recovery documentation

### 🧪 Testing Requirements
- [x] Backup script functionality tests
- [x] Recovery procedure tests
- [x] Backup integrity verification
- [x] Disaster recovery simulation

### 📊 Metrics Impact
**Before:**
- No automated backup system
- Risk of data loss

**After (Expected):**
- Automated daily backups
- Tested recovery procedures
- RTO <15 minutes for critical issues

### ✅ Definition of Done
- [x] Automated backup system working
- [x] Recovery procedures tested
- [x] Documentation complete
- [x] Retention policy implemented""",
        "labels": ["enhancement", "infrastructure", "priority/high", "backup", "disaster-recovery", "phase-3"],
        "milestone": 3
    },

    {
        "title": "Implement Advanced Search & Filtering",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] Medium (Important for UX)

### 📂 Category
- [x] User Experience
- [x] Frontend
- [x] Advanced Features

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/implementation-roadmap.md#week-7-advanced-ux-features`

### 📝 Description
Add advanced search interface with filter combinations, search result highlighting, and optimized search performance.

### 🎯 Success Criteria
- [x] Advanced search UI implemented
- [x] Multiple filter combinations
- [x] Search result highlighting  
- [x] Search performance optimized
- [x] Search history/suggestions

### 🧪 Testing Requirements
- [x] Search functionality tests
- [x] Filter combination tests
- [x] Performance tests with large datasets
- [x] UI/UX tests

### 📊 Metrics Impact
**Before:**
- Basic search functionality
- Limited filtering options

**After (Expected):**
- Power user search capabilities
- Improved data discovery
- Better user productivity

### ✅ Definition of Done
- [x] Advanced search implemented
- [x] All filter combinations working
- [x] Performance requirements met
- [x] User testing completed""",
        "labels": ["enhancement", "frontend", "priority/medium", "search", "filtering", "phase-4"],
        "milestone": 4
    },

    {
        "title": "Add Bulk Operations for Customer Management",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] Medium (Important for UX)

### 📂 Category
- [x] User Experience
- [x] Advanced Features
- [x] Power User Features

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/implementation-roadmap.md#bulk-operations`

### 📝 Description
Implement bulk operations for power users: bulk selection, edit, delete, and export functionality for efficient customer management.

### 🎯 Success Criteria
- [x] Bulk customer selection UI
- [x] Bulk edit capabilities
- [x] Bulk delete with confirmation
- [x] Bulk export functionality
- [x] Progress indicators for bulk operations

### 🧪 Testing Requirements
- [x] Bulk operation functionality tests
- [x] Performance tests with large selections
- [x] Confirmation dialog tests
- [x] Export format tests

### 📊 Metrics Impact
**Before:**
- Individual operations only
- Time-consuming for large datasets

**After (Expected):**
- Efficient bulk operations
- Power user productivity gains
- Better data management workflow

### ✅ Definition of Done
- [x] Bulk operations implemented
- [x] Confirmation dialogs working
- [x] Export functionality complete
- [x] Performance acceptable""",
        "labels": ["enhancement", "frontend", "priority/medium", "bulk-operations", "power-user", "phase-4"],
        "milestone": 4
    },

    {
        "title": "Optimize Performance & Bundle Size",
        "body": """## 📋 Enhancement Details

### 🎯 Priority Level
- [x] Medium (Important for UX)

### 📂 Category
- [x] Performance
- [x] Frontend
- [x] Production Readiness

### 🔗 Related Documentation
**Reference**: `design_docs/improvements/production-readiness.md#performance-optimizations`

### 📝 Description
Implement React.memo optimizations, code splitting, bundle optimization, and performance monitoring for better user experience.

### 🎯 Success Criteria
- [x] React.memo optimizations added
- [x] Code splitting implemented
- [x] Bundle size optimized
- [x] Performance monitoring setup
- [x] Core Web Vitals improved

### 🧪 Testing Requirements
- [x] Performance benchmark tests
- [x] Bundle size analysis
- [x] Loading time tests
- [x] Core Web Vitals measurement

### 📊 Metrics Impact
**Before:**
- No performance optimizations
- Large bundle sizes

**After (Expected):**
- <3s load times on 3G networks
- Improved Core Web Vitals scores
- Optimized bundle sizes

### ✅ Definition of Done
- [x] Performance optimizations implemented
- [x] Bundle size reduced
- [x] Loading times improved
- [x] Performance monitoring active""",
        "labels": ["enhancement", "frontend", "priority/medium", "performance", "optimization", "phase-4"],
        "milestone": 4
    }
]

def run_command(cmd):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None

def create_milestones():
    """Create GitHub milestones"""
    print("Creating milestones...")
    
    for i, milestone in enumerate(MILESTONES, 1):
        cmd = f'''gh api repos/:owner/:repo/milestones \\
            --method POST \\
            --field title="{milestone['title']}" \\
            --field description="{milestone['description']}" \\
            --field due_on="{milestone['due_date']}T23:59:59Z"'''
        
        result = run_command(cmd)
        if result:
            print(f"✅ Created milestone {i}: {milestone['title']}")
        else:
            print(f"❌ Failed to create milestone {i}")

def create_issues():
    """Create GitHub issues"""
    print("Creating issues...")
    
    for i, issue in enumerate(ISSUES, 1):
        # Prepare labels
        labels = ','.join(issue['labels'])
        
        # Create issue
        cmd = f'''gh issue create \\
            --title "{issue['title']}" \\
            --body "{issue['body']}" \\
            --label "{labels}" \\
            --milestone {issue['milestone']}'''
        
        result = run_command(cmd)
        if result:
            print(f"✅ Created issue {i}: {issue['title']}")
        else:
            print(f"❌ Failed to create issue {i}")

def create_project_board():
    """Create GitHub project board"""
    print("Creating project board...")
    
    # Create project
    cmd = '''gh api user/projects \\
        --method POST \\
        --field name="Customer Management Improvements" \\
        --field body="Track implementation of code analysis improvements"'''
    
    result = run_command(cmd)
    if result:
        project_data = json.loads(result)
        project_id = project_data['id']
        print(f"✅ Created project board (ID: {project_id})")
        
        # Add columns
        columns = ["📋 Backlog", "🟢 Ready", "🔵 In Progress", "🟣 Review", "✅ Done"]
        for column in columns:
            cmd = f'''gh api projects/{project_id}/columns \\
                --method POST \\
                --field name="{column}"'''
            run_command(cmd)
        
        print("✅ Added project columns")
    else:
        print("❌ Failed to create project board")

def main():
    """Main function"""
    print("🚀 GitHub Project Setup for Customer Management Improvements")
    print("=" * 60)
    
    # Check if GitHub CLI is installed and authenticated
    if not run_command("gh auth status"):
        print("❌ GitHub CLI not authenticated. Run 'gh auth login' first.")
        sys.exit(1)
    
    print("✅ GitHub CLI authenticated")
    
    # Create milestones first
    create_milestones()
    
    # Create issues  
    create_issues()
    
    # Create project board
    create_project_board()
    
    print("\n🎉 GitHub project setup complete!")
    print("\n📋 Next steps:")
    print("1. Visit your GitHub repository")
    print("2. Check the Issues tab for all improvement tasks")
    print("3. Review the Milestones for phase tracking")
    print("4. Use the Project board for workflow management")
    print("5. Start with Phase 1 high-priority issues")

if __name__ == "__main__":
    main()