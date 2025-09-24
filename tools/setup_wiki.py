#!/usr/bin/env python3
"""
One-Click Wiki Setup
===================

This script sets up your GitHub Wiki automation in one command.
Run this once to get everything configured and generate your first wiki.

Usage:
    python setup_wiki.py
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description, check=True):
    """Run a command with nice output."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            return False
        if result.stdout:
            print(f"   {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Set up GitHub Wiki automation."""
    print("🚀 GitHub Wiki Automation Setup")
    print("=" * 40)
    
    # Check if we're in a git repository
    if not Path(".git").exists():
        print("❌ Error: Not in a git repository")
        print("Please run this from your project's root directory")
        return 1
    
    print("✅ Git repository detected")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8+ required")
        print(f"Current version: {sys.version}")
        return 1
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Check for documentation files
    doc_files = []
    for pattern in ["*.md", "design_docs/*.md", "design_docs/**/*.md"]:
        doc_files.extend(Path().glob(pattern))
    
    if not doc_files:
        print("⚠️  Warning: No documentation files found")
        print("Consider adding some .md files before generating the wiki")
    else:
        print(f"✅ Found {len(doc_files)} documentation files")
    
    # Install dependencies if needed
    print("\n📦 Installing dependencies...")
    if not run_command("python -c 'import toml'", "Checking for toml package", check=False):
        if not run_command("pip install toml", "Installing toml package"):
            print("❌ Failed to install dependencies")
            print("Please install manually: pip install toml")
            return 1
    
    print("✅ Dependencies ready")
    
    # Validate the wiki tools
    print("\n🔍 Validating wiki tools...")
    if not run_command("python tools/wiki_manager.py validate", "Running validation"):
        print("❌ Wiki tools validation failed")
        return 1
    
    # Preview the wiki generation
    print("\n👀 Previewing wiki generation...")
    if not run_command("python tools/wiki_manager.py preview", "Running preview"):
        print("❌ Wiki preview failed")
        return 1
    
    # Ask user if they want to generate the wiki
    print("\n" + "=" * 40)
    print("🎉 Setup Complete!")
    print("\nYour GitHub Wiki automation is ready!")
    print("\nNext steps:")
    print("1. Generate your wiki:")
    print("   python tools/wiki_manager.py generate")
    print("\n2. Or preview changes first:")
    print("   python tools/wiki_manager.py preview")
    print("\n3. The GitHub Actions workflow will keep your wiki updated automatically")
    print(f"   when you push changes to documentation files.")
    print("\n4. Visit your wiki at:")
    print("   https://github.com/[your-username]/[your-repo]/wiki")
    
    # Offer to generate now
    try:
        response = input("\n❓ Generate wiki now? (y/N): ").strip().lower()
        if response in ['y', 'yes']:
            print("\n🚀 Generating wiki...")
            if run_command("python tools/wiki_manager.py generate", "Generating wiki"):
                print("\n✅ Wiki generated successfully!")
                print("🌐 Check it out at your GitHub repository's wiki tab")
            else:
                print("\n❌ Wiki generation failed")
                print("You can try again later with: python tools/wiki_manager.py generate")
        else:
            print("\n👍 You can generate the wiki later with:")
            print("   python tools/wiki_manager.py generate")
    except KeyboardInterrupt:
        print("\n\n👋 Setup complete! Generate your wiki when ready.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())