#!/usr/bin/env python
"""Version management script for ml-project-generator."""

import re
import sys
from pathlib import Path
from typing import Optional, Tuple

def read_version_from_pyproject() -> str:
    """Read version from pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")
    
    content = pyproject_path.read_text()
    version_match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
    if not version_match:
        raise ValueError("Version not found in pyproject.toml")
    return version_match.group(1)

def read_version_from_init() -> str:
    """Read version from __init__.py."""
    init_path = Path("ml_project_generator/__init__.py")
    if not init_path.exists():
        raise FileNotFoundError("__init__.py not found")
    
    content = init_path.read_text()
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
    if not version_match:
        raise ValueError("Version not found in __init__.py")
    return version_match.group(1)

def update_version(version: str, bump_type: str) -> str:
    """Update version number based on bump type."""
    major, minor, patch = map(int, version.split('.'))
    
    if bump_type == 'major':
        return f"{major + 1}.0.0"
    elif bump_type == 'minor':
        return f"{major}.{minor + 1}.0"
    elif bump_type == 'patch':
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")

def update_pyproject_version(version: str) -> None:
    """Update version in pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    new_content = re.sub(
        r'(version\s*=\s*["\'])[^"\']+(["\'])',
        f'\\1{version}\\2',
        content
    )
    pyproject_path.write_text(new_content)

def update_init_version(version: str) -> None:
    """Update version in __init__.py."""
    init_path = Path("ml_project_generator/__init__.py")
    content = init_path.read_text()
    new_content = re.sub(
        r'(__version__\s*=\s*["\'])[^"\']+(["\'])',
        f'\\1{version}\\2',
        content
    )
    init_path.write_text(new_content)

def check_versions_match() -> bool:
    """Check if versions match across files."""
    try:
        pyproject_version = read_version_from_pyproject()
        init_version = read_version_from_init()
        return pyproject_version == init_version
    except (FileNotFoundError, ValueError) as e:
        print(f"Error checking versions: {e}", file=sys.stderr)
        return False

def main() -> None:
    """Main function for version management."""
    if len(sys.argv) < 2:
        print("Usage: python manage_version.py [check|bump-major|bump-minor|bump-patch]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'check':
        if check_versions_match():
            print("Versions match across files")
        else:
            print("Versions do not match!", file=sys.stderr)
            sys.exit(1)
    
    elif command.startswith('bump-'):
        bump_type = command.split('-')[1]
        if bump_type not in ['major', 'minor', 'patch']:
            print(f"Invalid bump type: {bump_type}", file=sys.stderr)
            sys.exit(1)
        
        try:
            current_version = read_version_from_pyproject()
            new_version = update_version(current_version, bump_type)
            
            update_pyproject_version(new_version)
            update_init_version(new_version)
            
            print(f"Version bumped to {new_version}")
        except Exception as e:
            print(f"Error updating version: {e}", file=sys.stderr)
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()