#!/usr/bin/env python3
"""
Build script for AI CLI package.
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and print it."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=check)
    return result.returncode == 0


def clean():
    """Clean build artifacts."""
    print("Cleaning build artifacts...")
    
    # Directories to remove
    dirs_to_remove = [
        "build",
        "dist",
        "*.egg-info",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "htmlcov",
    ]
    
    for pattern in dirs_to_remove:
        for path in Path(".").glob(f"**/{pattern}"):
            if path.is_dir():
                print(f"Removing directory: {path}")
                shutil.rmtree(path, ignore_errors=True)
    
    # Files to remove
    files_to_remove = [
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".coverage",
        "coverage.xml",
    ]
    
    for pattern in files_to_remove:
        for path in Path(".").glob(f"**/{pattern}"):
            if path.is_file():
                print(f"Removing file: {path}")
                path.unlink()


def test():
    """Run tests."""
    print("Running tests...")
    return run_command("python -m pytest tests/ -v")


def lint():
    """Run linting."""
    print("Running linting...")
    success = True
    
    # Run flake8
    if not run_command("python -m flake8 ai_cli/ tests/", check=False):
        success = False
    
    # Run mypy
    if not run_command("python -m mypy ai_cli/", check=False):
        success = False
    
    return success


def format_code():
    """Format code with black."""
    print("Formatting code...")
    return run_command("python -m black ai_cli/ tests/ scripts/")


def build():
    """Build the package."""
    print("Building package...")
    
    # Clean first
    clean()
    
    # Build source distribution
    if not run_command("python setup.py sdist"):
        return False
    
    # Build wheel
    if not run_command("python setup.py bdist_wheel"):
        return False
    
    print("Build completed successfully!")
    return True


def install_dev():
    """Install package in development mode."""
    print("Installing package in development mode...")
    return run_command("pip install -e .[dev]")


def check_package():
    """Check package with twine."""
    print("Checking package...")
    return run_command("python -m twine check dist/*")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python build.py <command>")
        print("Commands:")
        print("  clean      - Clean build artifacts")
        print("  test       - Run tests")
        print("  lint       - Run linting")
        print("  format     - Format code")
        print("  build      - Build package")
        print("  install    - Install in development mode")
        print("  check      - Check package")
        print("  all        - Run all steps")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "clean":
        clean()
    elif command == "test":
        test()
    elif command == "lint":
        lint()
    elif command == "format":
        format_code()
    elif command == "build":
        build()
    elif command == "install":
        install_dev()
    elif command == "check":
        check_package()
    elif command == "all":
        print("Running all build steps...")
        success = True
        success &= format_code()
        success &= lint()
        success &= test()
        success &= build()
        success &= check_package()
        
        if success:
            print("All steps completed successfully!")
        else:
            print("Some steps failed!")
            sys.exit(1)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
