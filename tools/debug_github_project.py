#!/usr/bin/env python3
"""
GitHub Project Creator - Debug Version
Test and fix GraphQL API calls step by step
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

def test_basic_graphql():
    """Test basic GraphQL connectivity"""
    query = "query { viewer { login id } }"
    
    cmd = f'gh api graphql -f query="{query}"'
    return run_command(cmd)

def get_user_info():
    """Get user information using GraphQL"""
    query = "query { viewer { login id projectsV2(first: 5) { nodes { title id } } } }"
    
    cmd = f'gh api graphql -f query="{query}"'
    success, output = run_command(cmd)
    
    print(f"Query command: {cmd}")
    print(f"Success: {success}")
    print(f"Raw output: {output}")
    
    if success:
        data = json.loads(output)
        return data["data"]["viewer"]
    return None

def create_simple_project(owner_id):
    """Create a simple project first"""
    # Escape the query properly for Windows PowerShell
    query = '''mutation { createProjectV2(input: { ownerId: "''' + owner_id + '''", title: "Customer Management Improvements" }) { projectV2 { id number title url } } }'''
    
    cmd = f'gh api graphql -f query="{query}"'
    success, output = run_command(cmd)
    
    print(f"Command: {cmd}")
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    if success:
        data = json.loads(output)
        if "data" in data and data["data"]["createProjectV2"]:
            return data["data"]["createProjectV2"]["projectV2"]
    
    return None

def main():
    print("🔧 GitHub Project Creator - Debug Mode")
    print("=" * 50)
    
    # Test 1: Basic GraphQL connectivity
    print("1. Testing GraphQL connectivity...")
    success, output = test_basic_graphql()
    if success:
        print("✅ GraphQL connection working")
        data = json.loads(output)
        print(f"   User: {data['data']['viewer']['login']}")
    else:
        print(f"❌ GraphQL connection failed: {output}")
        return
    
    # Test 2: Get detailed user info
    print("2. Getting user information...")
    user_info = get_user_info()
    if user_info:
        print(f"✅ User ID: {user_info['id']}")
        print(f"   Login: {user_info['login']}")
        if user_info['projectsV2']['nodes']:
            print(f"   Existing projects: {len(user_info['projectsV2']['nodes'])}")
    else:
        print("❌ Failed to get user information")
        return
    
    # Test 3: Create simple project
    print("3. Creating simple project...")
    project = create_simple_project(user_info['id'])
    if project:
        print(f"✅ Created project!")
        print(f"   ID: {project['id']}")
        print(f"   URL: {project['url']}")
        print(f"   Number: {project['number']}")
    else:
        print("❌ Failed to create project")

if __name__ == "__main__":
    main()