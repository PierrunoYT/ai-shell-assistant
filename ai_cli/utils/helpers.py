"""
Helper functions for AI CLI.
"""
import os
import json
from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.markdown import Markdown

console = Console()


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    Args:
        config_path: Path to the configuration file.
        
    Returns:
        The configuration as a dictionary.
    """
    if not os.path.exists(config_path):
        return {}
    
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        console.print(f"[bold red]Error loading config: {str(e)}[/bold red]")
        return {}


def save_config(config_path: str, config: Dict[str, Any]) -> bool:
    """
    Save configuration to a JSON file.
    
    Args:
        config_path: Path to the configuration file.
        config: The configuration to save.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        console.print(f"[bold red]Error saving config: {str(e)}[/bold red]")
        return False


def print_markdown(text: str) -> None:
    """
    Print text as markdown using rich.
    
    Args:
        text: The text to print as markdown.
    """
    console.print(Markdown(text))


def print_error(message: str) -> None:
    """
    Print an error message.
    
    Args:
        message: The error message to print.
    """
    console.print(f"[bold red]Error: {message}[/bold red]")


def print_success(message: str) -> None:
    """
    Print a success message.
    
    Args:
        message: The success message to print.
    """
    console.print(f"[bold green]{message}[/bold green]")
