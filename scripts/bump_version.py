#!/usr/bin/env python3
"""
Version bumping script for AI CLI package.
"""
import re
import sys
from pathlib import Path


def get_current_version():
    """Get the current version from __init__.py"""
    init_file = Path("ai_cli/__init__.py")
    content = init_file.read_text()
    
    match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    else:
        raise ValueError("Could not find version in __init__.py")


def bump_version(current_version, bump_type):
    """Bump version based on type (major, minor, patch)"""
    major, minor, patch = map(int, current_version.split('.'))
    
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError("bump_type must be 'major', 'minor', or 'patch'")
    
    return f"{major}.{minor}.{patch}"


def update_version_in_file(file_path, old_version, new_version):
    """Update version in a file"""
    content = Path(file_path).read_text()
    updated_content = content.replace(old_version, new_version)
    Path(file_path).write_text(updated_content)
    print(f"Updated {file_path}: {old_version} -> {new_version}")


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py <major|minor|patch>")
        sys.exit(1)
    
    bump_type = sys.argv[1]
    if bump_type not in ["major", "minor", "patch"]:
        print("Error: bump_type must be 'major', 'minor', or 'patch'")
        sys.exit(1)
    
    try:
        current_version = get_current_version()
        new_version = bump_version(current_version, bump_type)
        
        print(f"Bumping version from {current_version} to {new_version}")
        
        # Update version in __init__.py
        update_version_in_file("ai_cli/__init__.py", current_version, new_version)
        
        print(f"Version bumped successfully to {new_version}")
        print("Don't forget to:")
        print("1. Update CHANGELOG.md")
        print("2. Commit the changes")
        print("3. Create a git tag")
        print("4. Push to GitHub")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
