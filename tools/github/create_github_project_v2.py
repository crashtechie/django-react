#!/usr/bin/env python3
"""
GitHub Project Creator for Customer Management Improvements
Uses GitHub Projects v2 GraphQL API to create and configure project automatically
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

def get_user_id():
    """Get the current user's ID"""
    success, output = run_command("gh api user")
    if not success:
        return None, output
    
    user_data = json.loads(output)
    return user_data["node_id"], user_data["login"]

def get_repo_id():
    """Get the current repository ID"""
    success, output = run_command("gh repo view --json id,name,owner")
    if not success:
        return None, None, output
    
    repo_data = json.loads(output)
    return repo_data["id"], f"{repo_data['owner']['login']}/{repo_data['name']}", None

def create_project_v2(owner_id, title, description):
    """Create a new GitHub Project v2"""
    query = f'''
    mutation {{
      createProjectV2(input: {{
        ownerId: "{owner_id}"
        title: "{title}"
      }}) {{
        projectV2 {{
          id
          number
          title
          url
        }}
      }}
    }}
    '''
    
    cmd = f'gh api graphql -f query=\'{query}\''
    success, output = run_command(cmd)
    
    if success:
        data = json.loads(output)
        return data["data"]["createProjectV2"]["projectV2"]
    return None

def add_field_to_project(project_id, field_name, field_type, options=None):
    """Add a custom field to the project"""
    if field_type == "SINGLE_SELECT" and options:
        options_str = ', '.join([f'{{name: "{opt}", color: "GRAY"}}' for opt in options])
        query = f'''
        mutation {{
          createProjectV2Field(input: {{
            projectId: "{project_id}"
            dataType: {field_type}
            name: "{field_name}"
            singleSelectOptions: [{options_str}]
          }}) {{
            projectV2Field {{
              id
              name
            }}
          }}
        }}
        '''
    else:
        query = f'''
        mutation {{
          createProjectV2Field(input: {{
            projectId: "{project_id}"
            dataType: {field_type}
            name: "{field_name}"
          }}) {{
            projectV2Field {{
              id
              name
            }}
          }}
        }}
        '''
    
    cmd = f'gh api graphql -f query=\'{query}\''
    success, output = run_command(cmd)
    
    if success:
        data = json.loads(output)
        return data["data"]["createProjectV2Field"]["projectV2Field"]
    return None

def link_repo_to_project(project_id, repo_id):
    """Link repository to the project"""
    query = f'''
    mutation {{
      linkProjectV2ToRepository(input: {{
        projectId: "{project_id}"
        repositoryId: "{repo_id}"
      }}) {{
        repository {{
          id
        }}
      }}
    }}
    '''
    
    cmd = f'gh api graphql -f query=\'{query}\''
    success, output = run_command(cmd)
    return success, output

def get_repo_issues():
    """Get all issues from the repository"""
    success, output = run_command('gh issue list --limit 100 --json number,title,milestone')
    if success:
        return json.loads(output)
    return []

def add_issue_to_project(project_id, issue_node_id):
    """Add an issue to the project"""
    query = f'''
    mutation {{
      addProjectV2ItemByContentId(input: {{
        projectId: "{project_id}"
        contentId: "{issue_node_id}"
      }}) {{
        item {{
          id
        }}
      }}
    }}
    '''
    
    cmd = f'gh api graphql -f query=\'{query}\''
    success, output = run_command(cmd)
    return success

def get_issue_node_id(issue_number):
    """Get the node ID for an issue"""
    success, output = run_command(f'gh issue view {issue_number} --json id')
    if success:
        data = json.loads(output)
        return data["id"]
    return None

def main():
    print("🚀 Creating GitHub Project v2 for Customer Management Improvements")
    print("=" * 70)
    
    # Step 1: Get user and repo information
    print("1. Getting user and repository information...")
    
    user_id, username = get_user_id()
    if not user_id:
        print(f"❌ Failed to get user information: {username}")
        return
    
    repo_id, repo_name, error = get_repo_id()
    if not repo_id:
        print(f"❌ Failed to get repository information: {error}")
        print("Make sure you're in a git repository with GitHub remote")
        return
    
    print(f"✅ User: {username}")
    print(f"✅ Repository: {repo_name}")
    
    # Step 2: Create the project
    print("2. Creating GitHub Project v2...")
    
    project = create_project_v2(
        user_id, 
        "Customer Management Improvements",
        "Track implementation progress for code analysis improvements and production readiness"
    )
    
    if not project:
        print("❌ Failed to create project")
        return
    
    project_id = project["id"]
    project_url = project["url"]
    
    print(f"✅ Created project: {project_url}")
    
    # Step 3: Add custom fields
    print("3. Adding custom fields...")
    
    # Add Status field
    status_options = ["To Do", "In Progress", "Done"]
    status_field = add_field_to_project(project_id, "Status", "SINGLE_SELECT", status_options)
    if status_field:
        print("✅ Added Status field")
    else:
        print("❌ Failed to add Status field")
    
    time.sleep(1)  # Rate limiting
    
    # Add Priority field
    priority_options = ["High", "Medium", "Low"]
    priority_field = add_field_to_project(project_id, "Priority", "SINGLE_SELECT", priority_options)
    if priority_field:
        print("✅ Added Priority field")
    else:
        print("❌ Failed to add Priority field")
    
    time.sleep(1)
    
    # Add Phase field
    phase_options = ["Phase 1: Foundation", "Phase 2: User Experience", "Phase 3: Production Features", "Phase 4: Advanced Features"]
    phase_field = add_field_to_project(project_id, "Phase", "SINGLE_SELECT", phase_options)
    if phase_field:
        print("✅ Added Phase field")
    else:
        print("❌ Failed to add Phase field")
    
    # Step 4: Link repository to project
    print("4. Linking repository to project...")
    success, output = link_repo_to_project(project_id, repo_id)
    if success:
        print("✅ Repository linked to project")
    else:
        print(f"❌ Failed to link repository: {output}")
    
    # Step 5: Add issues to project
    print("5. Adding issues to project...")
    
    # Get all repository issues
    issues = get_repo_issues()
    improvement_issues = [issue for issue in issues if any(keyword in issue['title'].lower() for keyword in 
                         ['loading', 'error boundary', 'test', 'mobile', 'monitoring', 'security', 'backup', 'search', 'bulk', 'performance'])]
    
    added_count = 0
    for issue in improvement_issues:
        issue_node_id = get_issue_node_id(issue['number'])
        if issue_node_id:
            success = add_issue_to_project(project_id, issue_node_id)
            if success:
                print(f"✅ Added issue #{issue['number']}: {issue['title']}")
                added_count += 1
            else:
                print(f"❌ Failed to add issue #{issue['number']}")
            time.sleep(0.5)  # Rate limiting
    
    print(f"\n🎉 Project setup complete!")
    print(f"📊 Summary:")
    print(f"   • Project URL: {project_url}")
    print(f"   • Custom fields: Status, Priority, Phase")
    print(f"   • Issues added: {added_count}")
    print(f"   • Repository linked: {repo_name}")
    
    print(f"\n📋 Next steps:")
    print(f"1. Visit the project: {project_url}")
    print("2. Create different views (Board, Table, etc.)")
    print("3. Set up automation rules if desired")
    print("4. Start tracking your improvements!")

if __name__ == "__main__":
    main()