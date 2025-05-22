"""
Backward compatibility entry point for AI CLI.

This file maintains backward compatibility for users who were using:
python main.py <command>

The new recommended way is to use:
ai-cli <command>
"""
from ai_cli.cli import main

if __name__ == "__main__":
    main()
