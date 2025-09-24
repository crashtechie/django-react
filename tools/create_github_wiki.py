#!/usr/bin/env python3
"""
GitHub Wiki Automation Script
=============================

This script automates the creation and maintenance of GitHub Wiki documentation
by extracting content from existing documentation files and formatting them
appropriately for the wiki.

Features:
- Automatically creates wiki structure from existing docs
- Generates sidebar navigation
- Cross-references between wiki pages
- Converts internal links to wiki format
- Creates categorized documentation

Usage:
    python create_github_wiki.py [--dry-run] [--update-existing]
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))


@dataclass
class WikiPage:
    """Represents a single wiki page."""
    title: str
    filename: str
    content: str
    category: str
    order: int
    links: Optional[List[str]] = None

    def __post_init__(self):
        if self.links is None:
            self.links = []


class GitHubWikiGenerator:
    """Generates and manages GitHub Wiki documentation."""
    
    def __init__(self, repo_path: Path, dry_run: bool = False):
        self.repo_path = repo_path
        self.dry_run = dry_run
        self.wiki_pages: List[WikiPage] = []
        self.wiki_structure = {
            "Getting Started": {
                "order": 1,
                "pages": []
            },
            "Development": {
                "order": 2,
                "pages": []
            },
            "Architecture": {
                "order": 3,
                "pages": []
            },
            "Security": {
                "order": 4,
                "pages": []
            },
            "Operations": {
                "order": 5,
                "pages": []
            },
            "Reference": {
                "order": 6,
                "pages": []
            }
        }
        
    def scan_existing_docs(self) -> List[Tuple[Path, str, str]]:
        """Scan existing documentation files."""
        docs = []
        doc_dirs = [
            self.repo_path / "design_docs",
            self.repo_path / "design_docs" / "improvements",
            self.repo_path,
        ]
        
        for doc_dir in doc_dirs:
            if not doc_dir.exists():
                continue
                
            for file_path in doc_dir.glob("*.md"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    category = self._determine_category(file_path, content)
                    docs.append((file_path, category, content))
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")
                    
            # Also check for .txt files
            for file_path in doc_dir.glob("*.txt"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    category = self._determine_category(file_path, content)
                    docs.append((file_path, category, content))
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")
                    
        return docs
    
    def _determine_category(self, file_path: Path, content: str) -> str:
        """Determine the appropriate wiki category for a document."""
        filename = file_path.name.lower()
        content_lower = content.lower()
        
        # Security-related documents
        if any(keyword in filename for keyword in ['security', 'docker-security']):
            return "Security"
        
        # Development-related documents    
        if any(keyword in filename for keyword in ['development', 'roadmap', 'implementation']):
            return "Development"
            
        # Architecture and design documents
        if any(keyword in filename for keyword in ['design', 'architecture']):
            return "Architecture"
            
        # Operations and production
        if any(keyword in filename for keyword in ['production', 'deployment', 'docker']):
            return "Operations"
            
        # Getting started documents
        if filename == 'readme.md' or 'getting started' in content_lower:
            return "Getting Started"
            
        # Default to Reference
        return "Reference"
    
    def _convert_to_wiki_format(self, content: str, source_path: Path) -> str:
        """Convert markdown content to wiki format."""
        # Convert relative links to wiki links
        def replace_link(match):
            link_text = match.group(1) if match.group(1) else match.group(2)
            link_url = match.group(2)
            
            # Convert relative file links to wiki pages
            if not link_url.startswith(('http', 'https', 'mailto')):
                # Convert file path to wiki page name
                wiki_page = self._path_to_wiki_page(link_url)
                return f"[[{link_text}|{wiki_page}]]"
            
            return match.group(0)  # Keep external links as-is
        
        # Replace markdown links: [text](url) -> [[text|WikiPage]]
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        # Add wiki-style navigation breadcrumbs
        category = self._determine_category(source_path, content)
        breadcrumb = f"> **{category}**\n\n"
        
        return breadcrumb + content
    
    def _path_to_wiki_page(self, path: str) -> str:
        """Convert a file path to wiki page name."""
        # Remove file extensions and convert to title case
        name = Path(path).stem
        name = name.replace('-', ' ').replace('_', ' ')
        return name.title()
    
    def create_home_page(self) -> WikiPage:
        """Create the main wiki home page."""
        readme_path = self.repo_path / "README.md"
        
        if readme_path.exists():
            readme_content = readme_path.read_text(encoding='utf-8')
        else:
            readme_content = "# Django React Customer Management\n\nWelcome to the project wiki!"
        
        # Add navigation section to home page
        nav_section = """
## Documentation Navigation

### 📚 Wiki Sections

| Section | Description |
|---------|-------------|
| **[Getting Started](Getting-Started)** | Installation, setup, and basic usage |
| **[Development](Development)** | Development guides, roadmaps, and best practices |  
| **[Architecture](Architecture)** | System design, data models, and technical decisions |
| **[Security](Security)** | Security policies, configurations, and best practices |
| **[Operations](Operations)** | Deployment, monitoring, and production considerations |
| **[Reference](Reference)** | API documentation, troubleshooting, and misc resources |

### 🔗 Quick Links
- [API Documentation](API-Documentation)
- [Development Setup](Development-Setup) 
- [Production Deployment](Production-Deployment)
- [Security Guidelines](Security-Guidelines)

---
"""
        
        home_content = readme_content + "\n\n" + nav_section
        
        return WikiPage(
            title="Home",
            filename="Home.md",
            content=home_content,
            category="Getting Started",
            order=0
        )
    
    def create_category_pages(self) -> List[WikiPage]:
        """Create overview pages for each category."""
        category_pages = []
        
        for category, info in self.wiki_structure.items():
            slug = category.replace(' ', '-')
            content = f"""# {category}

This section contains documentation related to {category.lower()}.

## Pages in this section:

"""
            # We'll populate the page list later
            content += "<!-- PAGE_LIST_PLACEHOLDER -->\n\n"
            
            if category == "Getting Started":
                content += """
## Quick Start Guide

1. **[Installation](Installation)** - Set up your development environment
2. **[Configuration](Configuration)** - Configure the application  
3. **[First Steps](First-Steps)** - Your first API calls and frontend setup
4. **[Examples](Examples)** - Common usage examples

"""
            elif category == "Development":
                content += """
## Development Resources

- **[Development Environment](Development-Environment)** - Set up your dev environment
- **[Code Style](Code-Style)** - Coding standards and conventions
- **[Testing](Testing)** - Running and writing tests
- **[Contributing](Contributing)** - How to contribute to the project

"""
            elif category == "Architecture":
                content += """
## System Architecture

- **[Overview](Architecture-Overview)** - High-level system architecture
- **[Database Design](Database-Design)** - Database schema and relationships
- **[API Design](API-Design)** - REST API structure and conventions
- **[Frontend Architecture](Frontend-Architecture)** - React application structure

"""
            elif category == "Security":
                content += """
## Security Documentation

- **[Security Policy](Security-Policy)** - Security guidelines and policies
- **[Authentication](Authentication)** - User authentication and authorization
- **[Data Protection](Data-Protection)** - Data security and privacy
- **[Security Scanning](Security-Scanning)** - Automated security checks

"""
            elif category == "Operations":
                content += """
## Operations and Deployment

- **[Deployment Guide](Deployment-Guide)** - Production deployment procedures
- **[Monitoring](Monitoring)** - Application monitoring and logging
- **[Backup and Recovery](Backup-Recovery)** - Data backup procedures  
- **[Troubleshooting](Troubleshooting)** - Common issues and solutions

"""
            elif category == "Reference":
                content += """
## Reference Documentation

- **[API Reference](API-Reference)** - Complete API documentation
- **[Configuration Reference](Configuration-Reference)** - All configuration options
- **[Error Codes](Error-Codes)** - Error codes and their meanings
- **[FAQ](FAQ)** - Frequently asked questions

"""
                
            category_pages.append(WikiPage(
                title=category,
                filename=f"{slug}.md",
                content=content,
                category=category,
                order=info["order"]
            ))
            
        return category_pages
    
    def process_existing_docs(self) -> List[WikiPage]:
        """Process existing documentation into wiki pages."""
        docs = self.scan_existing_docs()
        wiki_pages = []
        
        for file_path, category, content in docs:
            # Skip README if we're using it for home page
            if file_path.name.lower() == 'readme.md' and file_path.parent == self.repo_path:
                continue
                
            # Create wiki page title from filename
            title = self._path_to_wiki_page(str(file_path.name))
            filename = f"{title.replace(' ', '-')}.md"
            
            # Convert content to wiki format
            wiki_content = self._convert_to_wiki_format(content, file_path)
            
            # Determine order within category
            order = len([p for p in wiki_pages if p.category == category]) + 1
            
            wiki_page = WikiPage(
                title=title,
                filename=filename,
                content=wiki_content,
                category=category,
                order=order
            )
            
            wiki_pages.append(wiki_page)
            
        return wiki_pages
    
    def create_sidebar(self) -> str:
        """Create wiki sidebar navigation."""
        sidebar = "## Navigation\n\n"
        
        # Group pages by category
        categories = {}
        for page in self.wiki_pages:
            if page.category not in categories:
                categories[page.category] = []
            categories[page.category].append(page)
        
        # Sort categories by order
        sorted_categories = sorted(
            categories.items(), 
            key=lambda x: self.wiki_structure.get(x[0], {}).get("order", 999)
        )
        
        for category, pages in sorted_categories:
            sidebar += f"### {category}\n"
            
            # Sort pages within category by order
            sorted_pages = sorted(pages, key=lambda x: x.order)
            
            for page in sorted_pages:
                page_link = page.filename.replace('.md', '').replace(' ', '-')
                sidebar += f"- [[{page.title}|{page_link}]]\n"
            
            sidebar += "\n"
        
        return sidebar
    
    def clone_wiki_repo(self) -> Optional[Path]:
        """Clone the GitHub wiki repository."""
        try:
            # Get repository info
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True, cwd=self.repo_path)
            
            if result.returncode != 0:
                print("Error: Could not get repository URL")
                return None
            
            repo_url = result.stdout.strip()
            
            # Convert to wiki URL
            if repo_url.endswith('.git'):
                wiki_url = repo_url[:-4] + '.wiki.git'
            else:
                wiki_url = repo_url + '.wiki.git'
            
            # Create temporary wiki directory
            wiki_path = self.repo_path / '.wiki_temp'
            
            if wiki_path.exists():
                subprocess.run(['rm', '-rf', str(wiki_path)], check=True)
            
            # Clone wiki
            print(f"Cloning wiki from {wiki_url}...")
            result = subprocess.run(['git', 'clone', wiki_url, str(wiki_path)], 
                                  capture_output=True, text=True)
            
            if result.returncode != 0:
                print("Warning: Wiki repository doesn't exist yet. Will create initial wiki.")
                wiki_path.mkdir(exist_ok=True)
                subprocess.run(['git', 'init'], cwd=wiki_path, check=True)
                
                # Set up git config if needed
                subprocess.run(['git', 'config', 'user.email', 'action@github.com'], 
                             cwd=wiki_path, capture_output=True)
                subprocess.run(['git', 'config', 'user.name', 'GitHub Action'], 
                             cwd=wiki_path, capture_output=True)
            
            return wiki_path
            
        except Exception as e:
            print(f"Error cloning wiki: {e}")
            return None
    
    def write_wiki_pages(self, wiki_path: Path) -> bool:
        """Write all wiki pages to the wiki repository."""
        try:
            # Write home page
            home_page = self.create_home_page()
            home_file = wiki_path / "Home.md"
            
            if not self.dry_run:
                home_file.write_text(home_page.content, encoding='utf-8')
            print(f"{'[DRY RUN] ' if self.dry_run else ''}Created: Home.md")
            
            # Write sidebar
            sidebar_content = self.create_sidebar()
            sidebar_file = wiki_path / "_Sidebar.md"
            
            if not self.dry_run:
                sidebar_file.write_text(sidebar_content, encoding='utf-8')
            print(f"{'[DRY RUN] ' if self.dry_run else ''}Created: _Sidebar.md")
            
            # Write category pages
            category_pages = self.create_category_pages()
            for page in category_pages:
                page_file = wiki_path / page.filename
                
                # Update category page with actual page list
                category_pages_list = [p for p in self.wiki_pages if p.category == page.category]
                page_list = "\n".join([f"- [[{p.title}|{p.filename.replace('.md', '')}]]" 
                                     for p in sorted(category_pages_list, key=lambda x: x.order)])
                
                content = page.content.replace("<!-- PAGE_LIST_PLACEHOLDER -->", page_list)
                
                if not self.dry_run:
                    page_file.write_text(content, encoding='utf-8')
                print(f"{'[DRY RUN] ' if self.dry_run else ''}Created: {page.filename}")
            
            # Write content pages
            for page in self.wiki_pages:
                page_file = wiki_path / page.filename
                
                if not self.dry_run:
                    page_file.write_text(page.content, encoding='utf-8')
                print(f"{'[DRY RUN] ' if self.dry_run else ''}Created: {page.filename}")
            
            return True
            
        except Exception as e:
            print(f"Error writing wiki pages: {e}")
            return False
    
    def push_wiki_changes(self, wiki_path: Path) -> bool:
        """Commit and push wiki changes."""
        try:
            if self.dry_run:
                print("[DRY RUN] Would commit and push wiki changes")
                return True
            
            # Add all files
            subprocess.run(['git', 'add', '.'], cwd=wiki_path, check=True)
            
            # Check if there are changes to commit
            result = subprocess.run(['git', 'diff', '--cached', '--exit-code'], 
                                  cwd=wiki_path, capture_output=True)
            
            if result.returncode == 0:
                print("No wiki changes to commit")
                return True
            
            # Commit changes
            subprocess.run(['git', 'commit', '-m', 'Automated wiki update'], 
                         cwd=wiki_path, check=True)
            
            # Push changes
            subprocess.run(['git', 'push', 'origin', 'master'], 
                         cwd=wiki_path, check=True)
            
            print("Wiki changes pushed successfully!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error pushing wiki changes: {e}")
            return False
    
    def cleanup_temp_files(self, wiki_path: Path):
        """Clean up temporary wiki directory."""
        try:
            if wiki_path.exists() and not self.dry_run:
                subprocess.run(['rm', '-rf', str(wiki_path)], check=True)
                print("Cleaned up temporary wiki files")
        except Exception as e:
            print(f"Warning: Could not clean up temp files: {e}")
    
    def generate_wiki(self) -> bool:
        """Generate the complete GitHub wiki."""
        print("🚀 Starting GitHub Wiki generation...")
        
        # Process existing documentation
        print("📄 Processing existing documentation...")
        self.wiki_pages = self.process_existing_docs()
        print(f"Found {len(self.wiki_pages)} documentation files")
        
        # Clone wiki repository
        print("📥 Setting up wiki repository...")
        wiki_path = self.clone_wiki_repo()
        if not wiki_path:
            return False
        
        try:
            # Write wiki pages
            print("✍️  Writing wiki pages...")
            if not self.write_wiki_pages(wiki_path):
                return False
            
            # Push changes
            print("🔄 Committing and pushing changes...")
            if not self.push_wiki_changes(wiki_path):
                return False
            
            print("✅ Wiki generation completed successfully!")
            print(f"📚 Created {len(self.wiki_pages) + len(self.wiki_structure) + 1} wiki pages")
            
            return True
            
        finally:
            # Cleanup
            self.cleanup_temp_files(wiki_path)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate GitHub Wiki from project documentation")
    parser.add_argument("--dry-run", action="store_true", 
                       help="Show what would be done without making changes")
    parser.add_argument("--repo-path", type=Path, default=Path.cwd(),
                       help="Path to the repository (default: current directory)")
    
    args = parser.parse_args()
    
    # Validate repository path
    if not (args.repo_path / ".git").exists():
        print("Error: Not a git repository")
        return 1
    
    # Create wiki generator
    generator = GitHubWikiGenerator(args.repo_path, args.dry_run)
    
    # Generate wiki
    success = generator.generate_wiki()
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())