#!/usr/bin/env python3
"""
GitHub Issues Generator - Test Migration Issues
Creates issues for the newly found test configuration problems
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
    print("Creating GitHub Issues for Test Migration Fixes")
    print("=" * 50)
    
    # Issues found during test migration
    issues = [
        {
            "title": "Fix Jest Configuration Property Name",
            "body": """**Priority: HIGH - Test Infrastructure**

Fix Jest configuration property name issue preventing frontend tests from running.

**Problem:**
- Jest configuration uses incorrect property `moduleNameMapping`
- Should be `moduleNameMapping` 
- Prevents frontend tests from executing properly

**Implementation Details:**
- Update `/tests/config/jest.config.cjs`
- Update `/frontend/jest.config.cjs`
- Verify test execution works correctly
- Update documentation if needed

**Files to Fix:**
- `tests/config/jest.config.cjs`
- `frontend/jest.config.cjs`

**Success Criteria:**
- Frontend tests run without configuration warnings
- All 12 frontend test files execute properly
- Jest configuration validates correctly

**Reference:** Test migration verification results""",
            "milestone": 1
        },
        {
            "title": "Install Missing django_filters Dependency",
            "body": """**Priority: HIGH - Backend Dependencies**

Install missing `django_filters` dependency preventing backend tests from running.

**Problem:**
- Backend tests fail with `ModuleNotFoundError: No module named 'django_filters'`
- Required for Django REST framework filtering functionality
- Prevents backend test execution

**Implementation Details:**
- Add `django-filter` to backend dependencies
- Update `pyproject.toml` or requirements file
- Verify backend tests run successfully
- Update Docker configuration if needed

**Files to Update:**
- `backend/pyproject.toml`
- `backend/uv.lock` (regenerate)
- Backend Dockerfile if needed

**Success Criteria:**
- Backend tests execute without import errors
- All 4 backend test files run properly
- Django application starts without dependency issues

**Reference:** Test migration verification results""",
            "milestone": 1
        },
        {
            "title": "Verify Test Path Resolution After Migration",
            "body": """**Priority: MEDIUM - Test Infrastructure**

Verify all import paths work correctly after test migration to centralized structure.

**Problem:**
- Tests moved from scattered locations to `/tests` directory
- Need to verify all relative imports still work
- Ensure test discovery works properly

**Implementation Details:**
- Run full test suite to verify functionality
- Check all import statements in test files
- Verify test fixtures and helpers are accessible
- Update any broken import paths

**Areas to Verify:**
- Backend test imports from `customers` app
- Frontend test imports from `src` directory
- E2E test helper utilities
- Test configuration file paths

**Success Criteria:**
- All tests run without import errors
- Test discovery finds all test files
- No broken relative imports
- Full test suite passes

**Reference:** Test migration verification results""",
            "milestone": 1
        },
        {
            "title": "Update CI/CD Pipelines for New Test Structure",
            "body": """**Priority: HIGH - DevOps**

Update GitHub Actions workflows to use new centralized test directory structure.

**Problem:**
- CI/CD pipelines likely reference old test paths
- May not run tests from new `/tests` directory
- Could cause build failures

**Implementation Details:**
- Update `.github/workflows/ci-cd.yml`
- Update test execution commands
- Verify all test types run in CI
- Update any test result reporting paths

**Areas to Update:**
- Backend test execution paths
- Frontend test execution paths
- E2E test execution paths
- Test result artifact collection

**Success Criteria:**
- CI/CD pipeline runs all tests successfully
- Test results are properly collected
- No broken workflow steps
- All test types execute in correct order

**Reference:** Test migration verification results""",
            "milestone": 1
        }
    ]
    
    print("Creating test migration fix issues...")
    created_count = 0
    
    for i, issue in enumerate(issues, 1):
        success, output = create_issue_simple(
            issue["title"],
            issue["body"], 
            issue.get("milestone")
        )
        
        if success:
            print(f"Created issue {i}: {issue['title']}")
            created_count += 1
        else:
            print(f"Failed to create issue {i}: {output}")
    
    print(f"\nSuccessfully created {created_count}/{len(issues)} test migration issues!")
    print("\nNext steps:")
    print("1. Fix Jest configuration property name")
    print("2. Install django_filters dependency")
    print("3. Run full test suite verification")
    print("4. Update CI/CD pipeline configurations")

if __name__ == "__main__":
    main()