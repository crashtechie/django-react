#!/usr/bin/env python3
"""
Quick Wiki Setup Script
=======================

This script provides a simple interface for managing your GitHub Wiki documentation.

Usage:
    python wiki_manager.py [command] [options]

Commands:
    generate     Generate the wiki from existing documentation
    preview      Preview what would be generated (dry-run)
    update       Update existing wiki with new content
    validate     Validate documentation files
    
Examples:
    python wiki_manager.py generate
    python wiki_manager.py preview
    python wiki_manager.py update --force
"""

import argparse
import sys
from pathlib import Path

# Add the tools directory to path
sys.path.append(str(Path(__file__).parent))

from create_github_wiki import GitHubWikiGenerator


def main():
    """Main entry point for wiki management."""
    parser = argparse.ArgumentParser(description="Manage GitHub Wiki documentation")
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Generate command
    generate_parser = subparsers.add_parser('generate', help='Generate wiki from documentation')
    generate_parser.add_argument('--force', action='store_true', 
                                help='Force update existing wiki pages')
    
    # Preview command
    preview_parser = subparsers.add_parser('preview', help='Preview wiki generation (dry-run)')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update existing wiki')
    update_parser.add_argument('--force', action='store_true',
                              help='Force update all pages')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate documentation files')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Get repository path
    repo_path = Path.cwd()
    if not (repo_path / '.git').exists():
        print("❌ Error: Not in a git repository")
        return 1
    
    try:
        if args.command == 'generate':
            print("🚀 Generating GitHub Wiki...")
            generator = GitHubWikiGenerator(repo_path, dry_run=False)
            success = generator.generate_wiki()
            
            if success:
                print("✅ Wiki generated successfully!")
                print(f"📚 Visit your wiki at: https://github.com/[your-username]/[your-repo]/wiki")
            else:
                print("❌ Wiki generation failed")
                return 1
        
        elif args.command == 'preview':
            print("👀 Previewing wiki generation (dry-run)...")
            generator = GitHubWikiGenerator(repo_path, dry_run=True)
            generator.generate_wiki()
            print("✅ Preview complete - no changes made")
        
        elif args.command == 'update':
            print("🔄 Updating wiki...")
            generator = GitHubWikiGenerator(repo_path, dry_run=False)
            success = generator.generate_wiki()
            
            if success:
                print("✅ Wiki updated successfully!")
            else:
                print("❌ Wiki update failed")
                return 1
        
        elif args.command == 'validate':
            print("🔍 Validating documentation files...")
            generator = GitHubWikiGenerator(repo_path, dry_run=True)
            docs = generator.scan_existing_docs()
            
            print(f"📄 Found {len(docs)} documentation files:")
            for file_path, category, content in docs:
                print(f"  - {file_path.name} → {category} ({len(content)} characters)")
            
            print("✅ Validation complete")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())