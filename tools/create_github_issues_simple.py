#!/usr/bin/env python3
"""
GitHub Issues Generator for Customer Management System Improvements
Simplified version that works better with Windows PowerShell
"""

import json
import subprocess
import sys
from pathlib import Path

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

def check_auth():
    """Check if GitHub CLI is authenticated"""
    success, output = run_command("gh auth status")
    return success

def create_milestone(title, description, due_date):
    """Create a milestone"""
    cmd = f'gh api repos/:owner/:repo/milestones --method POST --field "title={title}" --field "description={description}" --field "due_on={due_date}T23:59:59Z"'
    return run_command(cmd)

def create_issue(title, body, labels, milestone_number=None):
    """Create an issue with proper escaping"""
    # Escape quotes in body
    escaped_body = body.replace('"', '\\"')
    
    cmd = f'gh issue create --title "{title}" --body "{escaped_body}" --label "{labels}"'
    if milestone_number:
        cmd += f' --milestone {milestone_number}'
    
    return run_command(cmd)

def main():
    print("🚀 GitHub Project Setup for Customer Management Improvements")
    print("=" * 60)
    
    # Check authentication
    if not check_auth():
        print("❌ GitHub CLI not authenticated. Run 'gh auth login' first.")
        return
    
    print("✅ GitHub CLI authenticated")
    
    # Create milestones (simplified)
    milestones = [
        ("Phase 1: Foundation", "Critical improvements for production readiness", "2025-10-07"),
        ("Phase 2: User Experience", "Enhanced usability and mobile support", "2025-10-21"),
        ("Phase 3: Production Features", "Monitoring, security, and deployment", "2025-11-04"),
        ("Phase 4: Advanced Features", "Power user features and optimization", "2025-11-18")
    ]
    
    print("Creating milestones...")
    milestone_numbers = {}
    for i, (title, desc, due_date) in enumerate(milestones, 1):
        success, output = create_milestone(title, desc, due_date)
        if success:
            print(f"✅ Created milestone {i}: {title}")
            milestone_numbers[i] = i
        else:
            print(f"❌ Failed to create milestone {i}: {output}")
    
    # Create simplified issues
    issues = [
        {
            "title": "Add Loading Spinner Component",
            "body": "Create reusable LoadingSpinner component for all async operations. High priority for production readiness.",
            "labels": "enhancement,frontend,priority/high,ux,phase-1",
            "milestone": 1
        },
        {
            "title": "Implement Error Boundary Components", 
            "body": "Add React Error Boundaries to handle component crashes gracefully with fallback UI.",
            "labels": "enhancement,frontend,priority/high,error-handling,phase-1",
            "milestone": 1
        },
        {
            "title": "Comprehensive API Service Tests",
            "body": "Add test coverage for API service layer (currently 0% coverage). Critical for deployment confidence.",
            "labels": "enhancement,testing,priority/high,api,phase-1", 
            "milestone": 1
        },
        {
            "title": "Complete CustomerDetail Component Tests",
            "body": "Increase CustomerDetail test coverage from 17% to 85%. Core functionality needs comprehensive testing.",
            "labels": "enhancement,testing,priority/high,component-test,phase-2",
            "milestone": 2
        },
        {
            "title": "Complete CustomerForm Component Tests",
            "body": "Increase CustomerForm test coverage from 17% to 85%. Critical for form validation and data integrity.",
            "labels": "enhancement,testing,priority/high,forms,phase-2",
            "milestone": 2
        },
        {
            "title": "Mobile-Responsive Customer Cards",
            "body": "Replace desktop table view with mobile-friendly customer cards for better mobile UX.",
            "labels": "enhancement,frontend,priority/medium,mobile,responsive,phase-2",
            "milestone": 2
        },
        {
            "title": "Form Validation with Real-time Feedback",
            "body": "Add real-time validation, user-friendly error messages, and email uniqueness checking.",
            "labels": "enhancement,frontend,priority/medium,forms,validation,phase-2",
            "milestone": 2
        },
        {
            "title": "Application Monitoring & Observability",
            "body": "Implement Prometheus metrics, Grafana dashboards, structured logging, and health checks.",
            "labels": "enhancement,infrastructure,priority/high,monitoring,observability,phase-3",
            "milestone": 3
        },
        {
            "title": "Security Hardening & Rate Limiting",
            "body": "Implement rate limiting, security headers, SSL/TLS configuration, and DDoS protection.",
            "labels": "enhancement,security,priority/high,rate-limiting,ssl,phase-3",
            "milestone": 3
        },
        {
            "title": "Automated Backup & Recovery System",
            "body": "Create automated backup system with recovery procedures for production data protection.",
            "labels": "enhancement,infrastructure,priority/high,backup,disaster-recovery,phase-3",
            "milestone": 3
        },
        {
            "title": "Advanced Search & Filtering",
            "body": "Add advanced search interface with filter combinations and search result highlighting.",
            "labels": "enhancement,frontend,priority/medium,search,filtering,phase-4",
            "milestone": 4
        },
        {
            "title": "Bulk Operations for Customer Management",
            "body": "Implement bulk selection, edit, delete, and export functionality for power users.",
            "labels": "enhancement,frontend,priority/medium,bulk-operations,power-user,phase-4",
            "milestone": 4
        },
        {
            "title": "Performance Optimization & Bundle Size",
            "body": "Implement React.memo optimizations, code splitting, and performance monitoring.",
            "labels": "enhancement,frontend,priority/medium,performance,optimization,phase-4",
            "milestone": 4
        }
    ]
    
    print("Creating issues...")
    for i, issue in enumerate(issues, 1):
        milestone = issue.get("milestone")
        success, output = create_issue(
            issue["title"],
            issue["body"], 
            issue["labels"],
            milestone if milestone in milestone_numbers else None
        )
        
        if success:
            print(f"✅ Created issue {i}: {issue['title']}")
        else:
            print(f"❌ Failed to create issue {i}: {output}")
    
    print("\n🎉 GitHub project setup complete!")
    print("\n📋 Next steps:")
    print("1. Visit your GitHub repository")
    print("2. Check the Issues tab for all improvement tasks") 
    print("3. Review the Milestones for phase tracking")
    print("4. Start with Phase 1 high-priority issues")

if __name__ == "__main__":
    main()