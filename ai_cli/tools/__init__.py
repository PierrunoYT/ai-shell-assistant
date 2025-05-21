"""
Tools package for AI CLI.
"""

from ai_cli.tools.base import BaseTool
from ai_cli.tools.calculator import CalculatorTool
from ai_cli.tools.weather import WeatherTool

# Register all available tools
AVAILABLE_TOOLS = {
    "calculator": CalculatorTool,
    "weather": WeatherTool,
}
