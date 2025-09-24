# GitHub Wiki Automation

This directory contains tools to automatically generate and maintain GitHub Wiki documentation from your project's documentation files.

## 🚀 Quick Start

### Prerequisites
- Git repository with documentation files
- Python 3.8+
- GitHub repository with wiki enabled

### Generate Wiki (One-time Setup)
```bash
# Navigate to your project root
cd /path/to/your/project

# Generate the wiki
python tools/wiki_manager.py generate
```

### Preview Changes (Dry Run)
```bash
# See what would be generated without making changes
python tools/wiki_manager.py preview
```

## 📚 Features

### ✨ Automated Wiki Generation
- **Smart categorization**: Automatically categorizes documentation into logical sections
- **Navigation sidebar**: Generates a structured navigation sidebar
- **Cross-references**: Converts relative links to wiki page links
- **Home page integration**: Uses your README.md as the wiki home page
- **Category overview pages**: Creates overview pages for each documentation category

### 🏗️ Wiki Structure
The tool organizes documentation into these categories:

| Category | Description | Auto-detected Files |
|----------|-------------|-------------------|
| 🚀 **Getting Started** | Setup, installation, quick start | README.md, setup guides |
| 👨‍💻 **Development** | Development guides, roadmaps | DEVELOPMENT.md, implementation files |
| 🏗️ **Architecture** | System design, technical decisions | design_document.txt, architecture docs |
| 🔒 **Security** | Security policies, configurations | SECURITY*.md, docker-security files |
| ⚙️ **Operations** | Deployment, monitoring, production | production-readiness.md, ops guides |
| 📖 **Reference** | API docs, troubleshooting, misc | Reference materials, resolution docs |

### 🤖 Continuous Updates
- **GitHub Actions integration**: Automatically updates wiki when docs change
- **Smart change detection**: Only updates when documentation files are modified
- **Manual triggers**: Force updates via GitHub Actions interface

## 🛠️ Tools Overview

### `create_github_wiki.py`
The main wiki generation script that:
- Scans your documentation files
- Converts content to wiki format
- Creates navigation structure
- Pushes changes to GitHub wiki

**Usage:**
```bash
python tools/create_github_wiki.py [--dry-run] [--repo-path PATH]
```

**Options:**
- `--dry-run`: Preview changes without making them
- `--repo-path`: Specify repository path (default: current directory)

### `wiki_manager.py`
Simplified interface for common wiki operations:

```bash
# Generate complete wiki
python tools/wiki_manager.py generate

# Preview changes (dry-run)
python tools/wiki_manager.py preview

# Update existing wiki
python tools/wiki_manager.py update

# Validate documentation files
python tools/wiki_manager.py validate
```

### `wiki_config.toml`
Configuration file for customizing wiki generation:
- Category definitions and ordering
- File mapping and custom titles
- Content templates
- Link conversion rules
- Sidebar configuration

### `.github/workflows/update-wiki.yml`
GitHub Actions workflow that automatically:
- Detects documentation changes
- Updates wiki when files are modified
- Provides manual trigger option
- Reports update status

## 📝 Configuration

### Customizing Categories
Edit `tools/wiki_config.toml` to customize how files are categorized:

```toml
[wiki.file_mapping]
"my-custom-doc.md" = { category = "Development", title = "Custom Title", order = 1 }
```

### Adding New Content Templates
Define templates for consistent page formatting:

```toml
[wiki.templates]
my_template = """
# {title}

## Overview
{overview}

## Details
{details}
"""
```

## 🔧 Troubleshooting

### Common Issues

**Wiki repository doesn't exist**
- Enable wiki in your GitHub repository settings
- The script will create an initial wiki if none exists

**Permission errors**
- Ensure your GitHub token has wiki access
- Check that the repository allows wiki edits

**Content formatting issues**
- Use `--dry-run` to preview changes
- Check that markdown files are properly formatted
- Verify links are using correct relative paths

**No changes detected**
- Ensure documentation files are in tracked locations
- Check the workflow's path filters in `.github/workflows/update-wiki.yml`

### Getting Help

1. **Run validation**: `python tools/wiki_manager.py validate`
2. **Preview changes**: `python tools/wiki_manager.py preview`
3. **Check file detection**: Look at the validation output to see which files are found
4. **Review configuration**: Check `wiki_config.toml` for correct mappings

## 🚀 Advanced Usage

### Custom File Processing
You can extend the `GitHubWikiGenerator` class to add custom processing logic:

```python
from tools.create_github_wiki import GitHubWikiGenerator

class CustomWikiGenerator(GitHubWikiGenerator):
    def _convert_to_wiki_format(self, content: str, source_path: Path) -> str:
        # Add your custom processing here
        content = super()._convert_to_wiki_format(content, source_path)
        # Additional custom formatting
        return content
```

### Integration with CI/CD
The wiki automation integrates with your existing CI/CD pipeline:

- **Automatic updates**: Wiki updates when documentation changes
- **Pull request previews**: Preview wiki changes in PRs (with additional setup)
- **Multi-branch support**: Can be configured for different branches

### API Documentation Integration
For API documentation, consider integrating with tools like:
- **OpenAPI/Swagger**: Generate API reference from OpenAPI specs
- **Django REST Framework**: Auto-generate endpoint documentation
- **Postman Collections**: Convert collections to wiki format

## 📖 Examples

### Basic Wiki Generation
```bash
# Generate wiki with default settings
python tools/create_github_wiki.py
```

### Custom Repository Path
```bash
# Generate wiki for different repository
python tools/create_github_wiki.py --repo-path /path/to/other/repo
```

### Preview Only
```bash
# See what would be generated
python tools/create_github_wiki.py --dry-run
```

## 🤝 Contributing

To improve the wiki automation tools:

1. **Add new templates** in `wiki_config.toml`
2. **Extend file detection** in `create_github_wiki.py`
3. **Improve formatting** in the `_convert_to_wiki_format` method
4. **Add new categories** by updating the wiki structure

## 📄 License

This wiki automation system is part of your project and follows the same license terms.