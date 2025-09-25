#!/usr/bin/env python3
"""
GitHub Project Creator - Fixed Version
Handles authentication, API calls, and project setup automatically
No manual processes required
"""

import subprocess
import json
import time
import sys

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

def check_and_fix_auth():
    """Check GitHub CLI auth and fix scopes if needed"""
    print("🔐 Checking GitHub CLI authentication...")
    
    # Check current auth status
    success, output = run_command("gh auth status")
    if not success:
        print("❌ GitHub CLI not authenticated. Please run 'gh auth login' first.")
        return False
    
    print("✅ GitHub CLI authenticated")
    
    # Test if we can access Projects API
    success, output = run_command('gh api graphql -f query="query { viewer { login id } }"')
    if not success:
        print("❌ Basic GraphQL access failed")
        return False
    
    # Test Projects v2 access
    success, output = run_command('gh api graphql -f query="query { viewer { login id projectsV2(first: 1) { nodes { id } } } }"')
    if not success and "required scopes" in output:
        print("⚠️ Missing project scopes. Attempting to refresh authentication...")
        
        # Try to refresh with project scopes
        print("Please complete the authentication when prompted...")
        success, output = run_command("gh auth refresh --scopes project")
        
        if not success:
            print("❌ Failed to refresh authentication with project scopes")
            print("Manual fix: Run 'gh auth login' and ensure you grant project access")
            return False
        
        print("✅ Authentication refreshed with project scopes")
    
    return True

def get_user_and_repo_info():
    """Get user and repository information using GraphQL"""
    # Get user info
    query = 'query { viewer { login id } }'
    success, output = run_command(f'gh api graphql -f query="{query}"')
    
    if not success:
        return None, None, None, None
    
    user_data = json.loads(output)["data"]["viewer"]
    user_id = user_data["id"]
    username = user_data["login"]
    
    # Get repository info
    success, output = run_command("gh repo view --json id,name,owner")
    if not success:
        return user_id, username, None, None
    
    repo_data = json.loads(output)
    repo_id = repo_data["id"]
    repo_name = f"{repo_data['owner']['login']}/{repo_data['name']}"
    
    return user_id, username, repo_id, repo_name

def create_project_v2(user_id, title):
    """Create GitHub Project v2 using GraphQL"""
    # Escape quotes for PowerShell
    query = f'mutation {{ createProjectV2(input: {{ ownerId: "{user_id}", title: "{title}" }}) {{ projectV2 {{ id number title url }} }} }}'
    
    success, output = run_command(f'gh api graphql -f query="{query}"')
    
    if not success:
        print(f"GraphQL Error: {output}")
        return None
    
    try:
        data = json.loads(output)
        if "errors" in data:
            print(f"GraphQL Errors: {data['errors']}")
            return None
        return data["data"]["createProjectV2"]["projectV2"]
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Response parsing error: {e}")
        print(f"Raw response: {output}")
        return None

def create_project_field(project_id, field_name, field_type, options=None):
    """Create a custom field in the project"""
    if field_type == "SINGLE_SELECT" and options:
        options_json = json.dumps([{"name": opt, "color": "GRAY"} for opt in options])
        # Escape for PowerShell - use single quotes around the whole query
        query = f"mutation {{ createProjectV2Field(input: {{ projectId: \\\"{project_id}\\\", dataType: {field_type}, name: \\\"{field_name}\\\", singleSelectOptions: {options_json} }}) {{ projectV2Field {{ id name }} }} }}"
    else:
        query = f"mutation {{ createProjectV2Field(input: {{ projectId: \\\"{project_id}\\\", dataType: {field_type}, name: \\\"{field_name}\\\" }}) {{ projectV2Field {{ id name }} }} }}"
    
    # Use different quote strategy for PowerShell
    cmd = f"gh api graphql -f query='{query}'"
    success, output = run_command(cmd)
    
    if not success:
        print(f"Field creation error: {output}")
        return None
    
    try:
        data = json.loads(output)
        if "errors" in data:
            print(f"Field creation errors: {data['errors']}")
            return None
        return data["data"]["createProjectV2Field"]["projectV2Field"]
    except (json.JSONDecodeError, KeyError):
        print(f"Field response parsing error: {output}")
        return None

def link_repository(project_id, repo_id):
    """Link repository to the project"""
    query = f'mutation {{ linkProjectV2ToRepository(input: {{ projectId: "{project_id}", repositoryId: "{repo_id}" }}) {{ repository {{ id }} }} }}'
    
    success, output = run_command(f'gh api graphql -f query="{query}"')
    return success, output

def get_issues_and_add_to_project(project_id):
    """Get improvement issues and add them to the project"""
    # Get issues from repository
    success, output = run_command('gh issue list --limit 50 --json number,title,id')
    if not success:
        return 0
    
    issues = json.loads(output)
    improvement_issues = [
        issue for issue in issues 
        if any(keyword in issue['title'].lower() for keyword in [
            'loading', 'error boundary', 'test', 'mobile', 'monitoring', 
            'security', 'backup', 'search', 'bulk', 'performance', 'validation', 'spinner'
        ])
    ]
    
    added_count = 0
    for issue in improvement_issues:
        # Add issue to project
        query = f'mutation {{ addProjectV2ItemByContentId(input: {{ projectId: "{project_id}", contentId: "{issue["id"]}" }}) {{ item {{ id }} }} }}'
        
        success, output = run_command(f'gh api graphql -f query="{query}"')
        if success:
            print(f"✅ Added issue #{issue['number']}: {issue['title']}")
            added_count += 1
        else:
            print(f"❌ Failed to add issue #{issue['number']}: {output}")
        
        time.sleep(0.5)  # Rate limiting
    
    return added_count

def main():
    print("🚀 GitHub Project Creator - Fully Automated")
    print("=" * 55)
    
    # Step 1: Check and fix authentication
    if not check_and_fix_auth():
        print("❌ Authentication setup failed. Please resolve auth issues and retry.")
        return 1
    
    # Step 2: Get user and repo information
    print("\n📊 Getting repository information...")
    user_id, username, repo_id, repo_name = get_user_and_repo_info()
    
    if not user_id or not username:
        print("❌ Failed to get user information")
        return 1
    
    if not repo_id or not repo_name:
        print("❌ Failed to get repository information. Are you in a GitHub repository?")
        return 1
    
    print(f"✅ User: {username}")
    print(f"✅ Repository: {repo_name}")
    
    # Step 3: Create the project
    print("\n🏗️ Creating GitHub Project v2...")
    project = create_project_v2(user_id, "Customer Management Improvements")
    
    if not project:
        print("❌ Failed to create project. Check authentication and try again.")
        return 1
    
    project_id = project["id"]
    project_url = project["url"]
    project_number = project["number"]
    
    print(f"✅ Created project #{project_number}: {project_url}")
    
    # Step 4: Add custom fields
    print("\n🔧 Adding custom fields...")
    
    fields_created = []
    
    # Status field
    status_field = create_project_field(project_id, "Status", "SINGLE_SELECT", ["To Do", "In Progress", "Done"])
    if status_field:
        print(f"✅ Added Status field")
        fields_created.append("Status")
        time.sleep(1)
    
    # Priority field  
    priority_field = create_project_field(project_id, "Priority", "SINGLE_SELECT", ["High", "Medium", "Low"])
    if priority_field:
        print(f"✅ Added Priority field")
        fields_created.append("Priority")
        time.sleep(1)
    
    # Phase field
    phase_field = create_project_field(project_id, "Phase", "SINGLE_SELECT", [
        "Phase 1: Foundation", 
        "Phase 2: User Experience", 
        "Phase 3: Production Features", 
        "Phase 4: Advanced Features"
    ])
    if phase_field:
        print(f"✅ Added Phase field")
        fields_created.append("Phase")
        time.sleep(1)
    
    # Step 5: Link repository
    print("\n🔗 Linking repository to project...")
    success, output = link_repository(project_id, repo_id)
    if success:
        print("✅ Repository linked successfully")
    else:
        print(f"⚠️ Repository linking may have failed: {output}")
    
    # Step 6: Add issues to project
    print("\n📋 Adding improvement issues to project...")
    added_count = get_issues_and_add_to_project(project_id)
    
    # Final summary
    print(f"\n🎉 Project setup complete!")
    print(f"📊 Summary:")
    print(f"   • Project: {project_url}")
    print(f"   • Custom fields added: {len(fields_created)} ({', '.join(fields_created)})")
    print(f"   • Issues added: {added_count}")
    print(f"   • Repository linked: {repo_name}")
    
    print(f"\n📋 Next steps:")
    print(f"1. Visit your project: {project_url}")
    print("2. Create different project views (Board, Table, etc.)")
    print("3. Set field values for each issue")
    print("4. Start implementing improvements!")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)