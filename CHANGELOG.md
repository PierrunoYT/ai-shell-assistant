# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2024-01-XX

### Fixed
- Fixed Unicode encoding issues in shell command output on Windows
- Resolved UnicodeDecodeError when executing commands with special characters (e.g., 'help' command)
- Added UTF-8 encoding with error replacement for subprocess output handling

## [0.2.0] - 2024-01-XX

### Added
- Interactive setup wizard with `ai-cli init` command for easy configuration
- Rich formatting throughout the CLI with styled prompts and colored output
- Progress indicators and spinner animations for long-running operations
- Auto-execute mode for shell commands with `--auto-execute` flag
- System prompt support for chat sessions with `--system` or `-s` option
- Short option flags for common parameters (`-m` for model, `-t` for temperature)
- Welcome screen when running `ai-cli` without arguments
- Version information with `--version` flag
- Enhanced security features:
  - Password-protected input for API keys
  - API key masking in configuration display
  - Confirmation prompts with rich styling
- New helper functions: `print_info()`, `print_warning()`, `create_progress_bar()`, `prompt_user()`, `confirm_action()`
- Current directory display in shell mode prompts
- Tool enable/disable status display in tools list
- Command aliases for better readability (`config-set`, `config-get`)

### Changed
- Improved command help text with usage examples
- Enhanced user prompts with rich styling and colors
- Better error messages and warnings
- More informative status displays showing model, temperature, and enabled tools
- Modernized CLI interface with emoji icons and better formatting
- Configuration commands now use hyphens (config-set, config-get) instead of underscores

### Fixed
- Better handling of API key configuration
- Improved error handling in shell executor

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
