#!/usr/bin/env python3
"""
GitHub Project Creator for Customer Management Improvements
Creates a GitHub Project (beta) with proper columns and automation
"""

import subprocess
import json

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

def main():
    print("🚀 Creating GitHub Project for Customer Management Improvements")
    print("=" * 65)
    
    # Step 1: Create the project
    print("1. Creating GitHub Project...")
    
    project_cmd = '''gh api graphql -f query='
    mutation {
      createProjectV2(input: {
        ownerId: "MDQ6VXNlcjEyMzQ1Njc4"
        title: "Customer Management Improvements"
        repositoryId: "REPO_ID_PLACEHOLDER"
      }) {
        projectV2 {
          id
          number
          title
          url
        }
      }
    }'
    '''
    
    # First, let's get the current user and repo info
    print("Getting repository information...")
    
    # Get current user
    success, user_output = run_command("gh api user")
    if not success:
        print(f"❌ Failed to get user info: {user_output}")
        return
    
    user_data = json.loads(user_output)
    username = user_data["login"]
    print(f"✅ Found user: {username}")
    
    # Get current repository
    success, repo_output = run_command("gh repo view --json name,owner")
    if not success:
        print(f"❌ Failed to get repo info: {repo_output}")
        print("Make sure you're in a git repository with GitHub remote")
        return
    
    repo_data = json.loads(repo_output)
    repo_name = repo_data["name"]
    repo_owner = repo_data["owner"]["login"]
    print(f"✅ Found repository: {repo_owner}/{repo_name}")
    
    # Create project using simpler approach
    print("2. Creating project...")
    
    # Use the new GitHub Projects (beta) API
    create_cmd = f'gh api user/projects --method POST --field name="Customer Management Improvements" --field body="Track implementation progress for code analysis improvements and production readiness"'
    
    success, output = run_command(create_cmd)
    if success:
        project_data = json.loads(output)
        project_id = project_data["id"]
        project_url = project_data["html_url"]
        print(f"✅ Created project: {project_url}")
        
        # Instructions for manual setup since GitHub Projects v2 API is complex
        print("\n📋 Manual Setup Instructions:")
        print(f"1. Visit your project: {project_url}")
        print("2. Click 'Add field' and create these columns:")
        print("   - Status (Single select): To Do, In Progress, Done")
        print("   - Priority (Single select): High, Medium, Low")
        print("   - Phase (Single select): Phase 1, Phase 2, Phase 3, Phase 4")
        print("3. Add your repository to the project")
        print("4. Import existing issues by clicking '+ Add item'")
        
        print("\n🔧 Recommended Project Views:")
        print("• Board view grouped by Status")
        print("• Table view grouped by Phase")
        print("• Priority view filtered by High priority items")
        
    else:
        print(f"❌ Failed to create project: {output}")
        print("\n📋 Manual Creation Steps:")
        print("1. Go to https://github.com/tab/projects")
        print("2. Click 'New project'") 
        print("3. Choose 'Board' template")
        print("4. Name it 'Customer Management Improvements'")
        print("5. Add description: 'Track implementation progress for code analysis improvements'")

if __name__ == "__main__":
    main()