# AI CLI PyPI Package Structure

This document describes the complete PyPI package structure for the AI Shell Assistant project.

## Package Structure

```
ai-shell-assistant/
├── ai_cli/                     # Main package directory
│   ├── __init__.py            # Package metadata and imports
│   ├── cli.py                 # Main CLI entry point
│   ├── chat.py                # Chat session functionality
│   ├── config.py              # Configuration management
│   ├── shell_executor.py      # Shell command execution
│   ├── py.typed               # Type hints marker
│   ├── tools/                 # Tools package
│   │   ├── __init__.py        # Tools registry
│   │   ├── base.py            # Base tool class
│   │   ├── copy_file.py       # Copy file tool
│   │   ├── create_file.py     # Create file tool
│   │   ├── create_folder.py   # Create folder tool
│   │   ├── dangerous.py       # Dangerous operations helper
│   │   ├── move_file.py       # Move file tool
│   │   ├── remove.py          # Remove files tool
│   │   ├── rename.py          # Rename tool
│   │   └── search_file.py     # Search file tool
│   └── utils/                 # Utilities package
│       ├── __init__.py        # Utils package init
│       └── helpers.py         # Helper functions
├── tests/                     # Test directory
│   ├── __init__.py            # Tests package init
│   └── test_package.py        # Basic package tests
├── scripts/                   # Development scripts
│   ├── build.py               # Build automation script
│   └── bump_version.py        # Version bumping script
├── .github/                   # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml             # Continuous integration
│       └── publish.yml        # PyPI publishing
├── setup.py                   # Setup script (legacy)
├── pyproject.toml             # Modern Python packaging
├── setup.cfg                  # Additional configuration
├── MANIFEST.in                # Package manifest
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
├── LICENSE                    # MIT license
├── CHANGELOG.md               # Version history
├── .gitignore                 # Git ignore rules
├── Makefile                   # Development commands
├── main.py                    # Backward compatibility
└── PACKAGE_STRUCTURE.md       # This file
```

## Key Features

### 1. Modern Python Packaging
- **pyproject.toml**: Modern packaging configuration
- **setup.py**: Legacy compatibility
- **setup.cfg**: Additional configuration
- **MANIFEST.in**: Package manifest for additional files

### 2. Entry Points
- `ai-cli`: Main command-line interface
- `ai-shell`: Alternative entry point (same functionality)

### 3. Package Metadata
- Version: 0.1.0
- Author: PierrunoYT
- License: MIT
- Python: >=3.8

### 4. Dependencies
- openai>=1.0.0
- python-dotenv>=1.0.0
- requests>=2.31.0
- click>=8.1.7
- rich>=13.5.0
- pydantic>=2.4.0

### 5. Development Dependencies
- pytest>=7.0.0
- pytest-cov>=4.0.0
- black>=23.0.0
- flake8>=6.0.0
- mypy>=1.0.0
- pre-commit>=3.0.0

## Installation

### From PyPI
```bash
pip install ai-shell-assistant
```

### Development Installation
```bash
git clone https://github.com/PierrunoYT/ai-shell-assistant.git
cd ai-shell-assistant
pip install -e ".[dev]"
```

## Usage

### Command Line Interface
```bash
ai-cli --help                    # Show help
ai-cli chat                      # Start chat session
ai-cli shell                     # Start shell command generator
ai-cli tools                     # List available tools
ai-cli config_get                # View configuration
ai-cli config_set key value      # Set configuration
```

### Backward Compatibility
```bash
python main.py chat              # Still works
python main.py shell             # Still works
```

## Development Workflow

### Building the Package
```bash
make build                       # Build package
make test                        # Run tests
make lint                        # Run linting
make format                      # Format code
make all                         # Run all steps
```

### Version Management
```bash
python scripts/bump_version.py patch    # Bump patch version
python scripts/bump_version.py minor    # Bump minor version
python scripts/bump_version.py major    # Bump major version
```

### Publishing to PyPI
1. Update version with bump_version.py
2. Update CHANGELOG.md
3. Commit changes
4. Create GitHub release
5. GitHub Actions will automatically publish to PyPI

## CI/CD Pipeline

### Continuous Integration
- Runs on Python 3.8-3.12
- Tests on Ubuntu, Windows, macOS
- Linting with flake8
- Type checking with mypy
- Testing with pytest
- Coverage reporting

### Automatic Publishing
- Triggered on GitHub releases
- Builds and publishes to PyPI
- Uses GitHub secrets for authentication

## Type Support
- Full type hints throughout the codebase
- py.typed marker file included
- mypy configuration in pyproject.toml

## Quality Assurance
- Black code formatting
- flake8 linting
- mypy type checking
- pytest testing with coverage
- Pre-commit hooks support

This package structure follows Python packaging best practices and provides a solid foundation for distribution via PyPI.
