#!/usr/bin/env python3
"""
Version display script for Customer Management System
Usage: python scripts/version.py
"""

import json
import sys
from pathlib import Path

# Add backend to Python path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

try:
    from customer_management._version import __version__ as backend_version
except ImportError:
    backend_version = "0.1.0"

# Read frontend version
frontend_package_json = Path(__file__).parent.parent / "frontend" / "package.json"
if frontend_package_json.exists():
    with open(frontend_package_json, "r") as f:
        frontend_data = json.load(f)
        frontend_version = frontend_data.get("version", "0.1.0")
else:
    frontend_version = "0.1.0"

# Read root version
root_package_json = Path(__file__).parent.parent / "package.json"
if root_package_json.exists():
    with open(root_package_json, "r") as f:
        root_data = json.load(f)
        root_version = root_data.get("version", "0.1.0")
else:
    root_version = "0.1.0"

print("🏷️  Customer Management System - Version Information")
print("=" * 55)
print(f"📦 Root Project:     v{root_version}")
print(f"⚛️  Frontend (React): v{frontend_version}")
print(f"🐍 Backend (Django): v{backend_version}")
print()

# Check if versions are in sync
versions = [root_version, frontend_version, backend_version]
if len(set(versions)) == 1:
    print("✅ All versions are in sync!")
else:
    print("⚠️  Version mismatch detected:")
    for component, version in [
        ("Root", root_version),
        ("Frontend", frontend_version), 
        ("Backend", backend_version)
    ]:
        print(f"   {component}: v{version}")
    print("\n💡 Consider running the version sync workflow")