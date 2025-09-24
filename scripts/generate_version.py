#!/usr/bin/env python3
"""
Generate version file for Django backend using setuptools-scm
"""

import setuptools_scm
import sys
from pathlib import Path

def main():
    try:
        # Get version from setuptools-scm
        version = setuptools_scm.get_version()
        
        # Create version file
        version_file = Path("customer_management/_version.py")
        version_file.parent.mkdir(exist_ok=True)
        
        with open(version_file, "w") as f:
            f.write(f'__version__ = "{version}"\n')
        
        print(f"Generated version: {version}")
        print(f"Version file created: {version_file}")
        
    except Exception as e:
        print(f"Error generating version: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()