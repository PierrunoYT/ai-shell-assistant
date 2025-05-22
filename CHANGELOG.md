# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-XX

### Added
- Initial release of AI Shell Assistant
- AI-powered command-line interface with extensible tools
- Natural language to shell command conversion
- Interactive chat session with AI
- Extensible tool system with the following tools:
  - Search file tool
  - Rename tool  
  - Remove files tool
  - Create file tool
  - Copy file tool
  - Move file tool
  - Create folder tool
- Configuration management system
- Support for multiple OpenAI models (GPT-4.1, GPT-4o, GPT-4, GPT-3.5-turbo, GPT-4-turbo)
- Rich terminal UI with colorful output
- Safety confirmations for dangerous operations
- Cross-platform support (Windows, macOS, Linux)
- PyPI package distribution
- Comprehensive documentation
- GitHub Actions CI/CD pipeline
- Type hints and mypy support
- Unit tests with pytest
- Development tools and scripts

### Features
- `ai-cli chat` - Interactive AI chat session
- `ai-cli shell` - Natural language shell command generator
- `ai-cli tools` - List available tools
- `ai-cli config_get` - View configuration
- `ai-cli config_set` - Set configuration values
- Backward compatibility with `python main.py` commands

### Technical Details
- Built with Click for CLI interface
- Uses OpenAI API for AI functionality
- Rich library for terminal formatting
- Pydantic for data validation
- Comprehensive packaging with setuptools and pyproject.toml
- Type checking with mypy
- Code formatting with black
- Linting with flake8
- Testing with pytest
