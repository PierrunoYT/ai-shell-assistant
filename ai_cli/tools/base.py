"""
Base class for AI CLI tools.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseTool(ABC):
    """Base class for all tools in the AI CLI."""

    name: str
    description: str
    
    def __init__(self):
        """Initialize the tool."""
        if not hasattr(self, 'name'):
            raise ValueError("Tool must have a name")
        if not hasattr(self, 'description'):
            raise ValueError("Tool must have a description")
    
    @abstractmethod
    def execute(self, args: Dict[str, Any]) -> str:
        """
        Execute the tool with the given arguments.
        
        Args:
            args: A dictionary of arguments for the tool.
            
        Returns:
            The result of the tool execution as a string.
        """
        pass
    
    @property
    @abstractmethod
    def parameters(self) -> List[Dict[str, Any]]:
        """
        Get the parameters that this tool accepts.
        
        Returns:
            A list of parameter definitions, each with at least 'name' and 'description'.
        """
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the tool to a dictionary representation.
        
        Returns:
            A dictionary representation of the tool.
        """
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        }
