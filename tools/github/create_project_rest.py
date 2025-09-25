#!/usr/bin/env python3
"""
GitHub Project Creator - REST API Version
Uses GitHub REST API instead of GraphQL to avoid scope issues
"""

import subprocess
import json
import time

def run_command(cmd):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except Exception as e:
        return False, str(e)

def test_auth():
    """Test if we can access the API"""
    success, output = run_command("gh auth status")
    return success

def get_user_info():
    """Get current user information"""
    success, output = run_command("gh api user")
    if success:
        return json.loads(output)
    return None

def get_repo_info():
    """Get current repository information"""
    success, output = run_command("gh repo view --json id,name,owner,url")
    if success:
        return json.loads(output)
    return None

def create_project_classic(org_or_user, repo_name, project_name, description):
    """Create a classic project (since v2 requires special scopes)"""
    # Try organization-level project first
    success, output = run_command(f'gh api orgs/{org_or_user}/projects --method POST --field name="{project_name}" --field body="{description}"')
    
    if success:
        return json.loads(output), "org"
    
    # If that fails, try user-level project
    success, output = run_command(f'gh api user/projects --method POST --field name="{project_name}" --field body="{description}"')
    
    if success:
        return json.loads(output), "user"
    
    return None, None

def add_columns_to_project(project_id, columns):
    """Add columns to a classic project"""
    column_ids = []
    for column_name in columns:
        success, output = run_command(f'gh api projects/{project_id}/columns --method POST --field name="{column_name}"')
        if success:
            column_data = json.loads(output)
            column_ids.append((column_name, column_data["id"]))
            print(f"✅ Added column: {column_name}")
            time.sleep(0.5)  # Rate limiting
        else:
            print(f"❌ Failed to add column {column_name}: {output}")
    
    return column_ids

def get_repository_issues():
    """Get issues from the current repository"""
    success, output = run_command('gh issue list --limit 50 --json number,title,url,id')
    if success:
        return json.loads(output)
    return []

def add_issue_to_project_column(column_id, issue_id):
    """Add an issue to a project column"""
    success, output = run_command(f'gh api projects/columns/{column_id}/cards --method POST --field content_id={issue_id} --field content_type=Issue')
    return success

def main():
    print("🚀 GitHub Project Creator - REST API Version")
    print("=" * 55)
    
    # Step 1: Test authentication
    print("1. Testing GitHub CLI authentication...")
    if not test_auth():
        print("❌ GitHub CLI not authenticated. Run 'gh auth login' first.")
        return
    print("✅ GitHub CLI authenticated")
    
    # Step 2: Get user and repo info
    print("2. Getting user and repository information...")
    
    user_info = get_user_info()
    if not user_info:
        print("❌ Failed to get user information")
        return
    
    repo_info = get_repo_info()
    if not repo_info:
        print("❌ Failed to get repository information")
        return
    
    username = user_info["login"]
    repo_name = repo_info["name"]
    repo_owner = repo_info["owner"]["login"]
    
    print(f"✅ User: {username}")
    print(f"✅ Repository: {repo_owner}/{repo_name}")
    
    # Step 3: Create the project
    print("3. Creating GitHub Project...")
    
    project_name = "Customer Management Improvements"
    description = "Track implementation progress for code analysis improvements and production readiness"
    
    project_data, project_type = create_project_classic(username, repo_name, project_name, description)
    
    if not project_data:
        print("❌ Failed to create project")
        print("Note: You might need to enable GitHub Projects in your repository settings")
        return
    
    project_id = project_data["id"]
    project_url = project_data["html_url"]
    
    print(f"✅ Created {project_type}-level project: {project_url}")
    
    # Step 4: Add columns
    print("4. Adding project columns...")
    
    columns = ["🆕 To Do", "🔄 In Progress", "✅ Done", "📋 Phase 1", "📋 Phase 2", "📋 Phase 3", "📋 Phase 4"]
    column_ids = add_columns_to_project(project_id, columns)
    
    if not column_ids:
        print("❌ Failed to create columns")
        return
    
    # Step 5: Get and add issues
    print("5. Getting repository issues...")
    
    issues = get_repository_issues()
    improvement_issues = [
        issue for issue in issues 
        if any(keyword in issue['title'].lower() for keyword in [
            'loading', 'error boundary', 'test', 'mobile', 'monitoring', 
            'security', 'backup', 'search', 'bulk', 'performance', 'validation', 'spinner'
        ])
    ]
    
    print(f"Found {len(improvement_issues)} improvement-related issues")
    
    # Add issues to "To Do" column (first column)
    if column_ids and improvement_issues:
        todo_column_id = column_ids[0][1]  # First column ID
        print("6. Adding issues to 'To Do' column...")
        
        added_count = 0
        for issue in improvement_issues:
            # Extract numeric ID from the issue ID (format: I_kwDOKsxxxxx)
            success, output = run_command(f'gh issue view {issue["number"]} --json id')
            if success:
                issue_data = json.loads(output)
                # The REST API expects the numeric database ID, not the node ID
                # Let's try using the issue number directly
                success = add_issue_to_project_column(todo_column_id, issue["number"])
                if success:
                    print(f"✅ Added issue #{issue['number']}: {issue['title']}")
                    added_count += 1
                else:
                    print(f"❌ Failed to add issue #{issue['number']}")
                time.sleep(0.5)  # Rate limiting
        
        print(f"Added {added_count}/{len(improvement_issues)} issues to project")
    
    print(f"\n🎉 Project setup complete!")
    print(f"📊 Summary:")
    print(f"   • Project URL: {project_url}")
    print(f"   • Columns: {len(column_ids)}")
    print(f"   • Issues added: {len(improvement_issues)}")
    
    print(f"\n📋 Next steps:")
    print(f"1. Visit the project: {project_url}")
    print("2. Organize issues by moving them between columns")
    print("3. Add labels and priorities to issues")
    print("4. Start implementing improvements!")

if __name__ == "__main__":
    main()