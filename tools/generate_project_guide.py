#!/usr/bin/env python3
"""
GitHub Project Setup Guide Generator
Creates a comprehensive guide for manually setting up GitHub Projects
since the API requires complex authentication scopes
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

def get_repo_info():
    """Get current repository information"""
    success, output = run_command("gh repo view --json name,owner,url")
    if success:
        return json.loads(output)
    return None

def get_issues_info():
    """Get improvement issues from the repository"""
    success, output = run_command('gh issue list --limit 50 --json number,title,milestone')
    if success:
        issues = json.loads(output)
        improvement_issues = [
            issue for issue in issues 
            if any(keyword in issue['title'].lower() for keyword in [
                'loading', 'error boundary', 'test', 'mobile', 'monitoring', 
                'security', 'backup', 'search', 'bulk', 'performance', 'validation', 'spinner'
            ])
        ]
        return improvement_issues
    return []

def main():
    print("📋 GitHub Project Setup Guide Generator")
    print("=" * 45)
    
    # Get repository information
    repo_info = get_repo_info()
    if not repo_info:
        print("❌ Failed to get repository information")
        return
    
    repo_name = repo_info["name"]
    repo_owner = repo_info["owner"]["login"] 
    repo_url = repo_info["url"]
    
    print(f"Repository: {repo_owner}/{repo_name}")
    print(f"URL: {repo_url}")
    
    # Get improvement issues
    issues = get_issues_info()
    print(f"Found {len(issues)} improvement issues")
    
    # Generate setup guide
    guide_content = f"""# GitHub Project Setup Guide
## Customer Management Improvements Project

### Repository Information
- **Repository**: {repo_owner}/{repo_name}
- **URL**: {repo_url}
- **Improvement Issues**: {len(issues)} created

---

## Quick Setup Steps

### 1. Create the Project
1. Go to: **{repo_url}**
2. Click the **"Projects"** tab
3. Click **"Link a project"** → **"New project"**
4. Choose **"Board"** template
5. Name: **"Customer Management Improvements"**
6. Description: **"Track implementation progress for code analysis improvements and production readiness"**

### 2. Configure Project Fields
Add these custom fields to organize your work:

#### Status Field (Single select)
- 🆕 To Do
- 🔄 In Progress
- ✅ Done

#### Priority Field (Single select)  
- 🔴 High
- 🟡 Medium
- 🟢 Low

#### Phase Field (Single select)
- 📅 Phase 1: Foundation (Weeks 1-2)
- 📅 Phase 2: User Experience (Weeks 3-4)  
- 📅 Phase 3: Production Features (Weeks 5-6)
- 📅 Phase 4: Advanced Features (Weeks 7-8)

### 3. Add Issues to Project
Click **"+ Add item"** and add these improvement issues:

"""

    # Add each issue with details
    for i, issue in enumerate(issues, 1):
        milestone_info = f" (Milestone: {issue['milestone']['title']})" if issue.get('milestone') else ""
        guide_content += f"{i}. **#{issue['number']}**: {issue['title']}{milestone_info}\n"
    
    guide_content += f"""
### 4. Create Project Views

#### Board View (Default)
- **Group by**: Status
- **Sort by**: Priority (High → Medium → Low)
- **Filter**: All items

#### Phase Planning View  
- **View type**: Table
- **Group by**: Phase
- **Sort by**: Priority
- **Show**: All fields

#### Current Sprint View
- **View type**: Board
- **Group by**: Status  
- **Filter**: Phase 1 items only
- **Show**: High priority first

### 5. Set Field Values

#### High Priority Issues (Start First):
"""

    # Categorize issues by keywords for priority suggestions
    high_priority_keywords = ['loading', 'error', 'test', 'monitoring', 'security', 'backup']
    medium_priority_keywords = ['mobile', 'validation', 'search', 'performance']
    
    for issue in issues:
        is_high_priority = any(kw in issue['title'].lower() for kw in high_priority_keywords)
        is_medium_priority = any(kw in issue['title'].lower() for kw in medium_priority_keywords)
        
        if is_high_priority:
            guide_content += f"- #{issue['number']}: {issue['title']} → **High Priority, To Do**\n"
    
    guide_content += "\n#### Medium Priority Issues:\n"
    for issue in issues:
        is_high_priority = any(kw in issue['title'].lower() for kw in high_priority_keywords)
        is_medium_priority = any(kw in issue['title'].lower() for kw in medium_priority_keywords)
        
        if is_medium_priority and not is_high_priority:
            guide_content += f"- #{issue['number']}: {issue['title']} → **Medium Priority, To Do**\n"

    guide_content += f"""
### 6. Automation Setup (Optional)
1. Go to project settings
2. Add automation rules:
   - **Auto-add items**: Add issues with label "enhancement" 
   - **Auto-archive**: Move to "Done" when issue is closed

### 7. Start Development Workflow
1. Move first issue to "In Progress"
2. Implement the feature
3. Move to "Done" when complete
4. Track progress in your project board

---

## Direct Links
- **Repository Issues**: {repo_url}/issues
- **Repository Projects**: {repo_url}/projects
- **Milestones**: {repo_url}/milestones

## Next Steps
1. Follow the setup steps above
2. Start with Phase 1 high-priority issues
3. Use the project board to track daily progress
4. Review weekly progress against milestones

**Happy coding! 🚀**
"""

    # Write the guide to a file
    guide_filename = "GITHUB_PROJECT_SETUP_GUIDE.md"
    with open(guide_filename, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print(f"\n✅ Generated comprehensive setup guide: {guide_filename}")
    print(f"\n🎯 Summary:")
    print(f"   • Repository: {repo_owner}/{repo_name}")
    print(f"   • Issues to track: {len(issues)}")
    print(f"   • Guide created: {guide_filename}")
    
    print(f"\n📋 Next steps:")
    print(f"1. Open {guide_filename} for detailed instructions")
    print(f"2. Follow the step-by-step setup process")
    print(f"3. Visit {repo_url}/projects to create your project")
    print("4. Start implementing improvements!")

if __name__ == "__main__":
    main()