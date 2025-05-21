"""
Tools package for AI CLI.
"""

from ai_cli.tools.base import BaseTool
from ai_cli.tools.search_file import SearchFileTool
from ai_cli.tools.rename import RenameTool
from ai_cli.tools.remove import RemoveFileTool
from ai_cli.tools.create_file import CreateFileTool

# Register all available tools
AVAILABLE_TOOLS = {
    "search_file": SearchFileTool,
    "rename": RenameTool,
    "remove": RemoveFileTool,
    "create_file": CreateFileTool,
}
