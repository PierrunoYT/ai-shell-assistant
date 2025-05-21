"""
Calculator tool for AI CLI.
"""
from typing import Any, Dict, List

from ai_cli.tools.base import BaseTool


class CalculatorTool(BaseTool):
    """A simple calculator tool."""
    
    name = "calculator"
    description = "Perform basic arithmetic calculations"
    
    @property
    def parameters(self) -> List[Dict[str, Any]]:
        """Get the parameters for the calculator tool."""
        return [
            {
                "name": "expression",
                "description": "The mathematical expression to evaluate",
                "type": "string",
                "required": True
            }
        ]
    
    def execute(self, args: Dict[str, Any]) -> str:
        """
        Execute the calculator tool.
        
        Args:
            args: A dictionary containing the 'expression' to evaluate.
            
        Returns:
            The result of the calculation as a string.
        """
        expression = args.get("expression", "")
        
        if not expression:
            return "Error: No expression provided"
        
        try:
            # Using eval is generally not safe, but for a simple calculator
            # in a controlled environment, it's acceptable
            # In a production environment, you'd want to use a safer alternative
            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"
