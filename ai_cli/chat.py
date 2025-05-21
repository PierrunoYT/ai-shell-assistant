"""
Core chat functionality for AI CLI.
"""
import json
import os
from typing import Any, Dict, List, Optional

import openai
from dotenv import load_dotenv

from ai_cli.config import config
from ai_cli.tools import AVAILABLE_TOOLS
from ai_cli.utils.helpers import print_error, print_markdown, print_success

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") or config.get("api_key")


class ChatSession:
    """A chat session with the AI."""
    
    def __init__(self):
        """Initialize the chat session."""
        self.history = []
        self.tools = self._load_tools()
    
    def _load_tools(self):
        """
        Load the enabled tools.
        
        Returns:
            A dictionary of tool instances.
        """
        enabled_tools = config.get("enabled_tools", [])
        tools = {}
        
        for tool_name in enabled_tools:
            if tool_name in AVAILABLE_TOOLS:
                try:
                    tool_class = AVAILABLE_TOOLS[tool_name]
                    tools[tool_name] = tool_class()
                except Exception as e:
                    print_error(f"Failed to load tool '{tool_name}': {str(e)}")
        
        return tools
    
    def get_tool_definitions(self):
        """
        Get the tool definitions for the OpenAI API.
        
        Returns:
            A list of tool definitions.
        """
        return [tool.to_dict() for tool in self.tools.values()]
    
    def execute_tool(self, tool_call):
        """
        Execute a tool call from the AI.
        
        Args:
            tool_call: The tool call from the OpenAI API.
            
        Returns:
            The result of the tool execution.
        """
        tool_name = tool_call.function.name
        
        if tool_name not in self.tools:
            return f"Error: Tool '{tool_name}' not found or not enabled"
        
        try:
            # Parse the arguments
            args = json.loads(tool_call.function.arguments)
            
            # Execute the tool
            result = self.tools[tool_name].execute(args)
            return result
        except json.JSONDecodeError:
            return "Error: Invalid JSON in tool arguments"
        except Exception as e:
            return f"Error executing tool '{tool_name}': {str(e)}"
    
    def chat(self, message: str) -> str:
        """
        Send a message to the AI and get a response.
        
        Args:
            message: The user's message.
            
        Returns:
            The AI's response.
        """
        if not openai.api_key:
            return "Error: OpenAI API key not set. Please set the OPENAI_API_KEY environment variable or configure it in the settings."
        
        # Add the user message to history
        self.history.append({"role": "user", "content": message})
        
        # Limit history size
        history_size = config.get("history_size", 10)
        if len(self.history) > history_size * 2:  # Each exchange is 2 messages
            self.history = self.history[-history_size * 2:]
        
        try:
            # Create the messages for the API
            messages = self.history.copy()
            
            # Get the model configuration
            model = config.get("model", "gpt-3.5-turbo")
            max_tokens = config.get("max_tokens", 1000)
            temperature = config.get("temperature", 0.7)
            
            # Get available tools
            tools = self.get_tool_definitions()
            
            # Make the API request
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                tools=tools if tools else None,
                tool_choice="auto"
            )
            
            # Process the response
            response_message = response.choices[0].message
            
            # Handle tool calls
            if hasattr(response_message, 'tool_calls') and response_message.tool_calls:
                # Execute each tool call
                for tool_call in response_message.tool_calls:
                    tool_result = self.execute_tool(tool_call)
                    
                    # Add the tool call and result to the history
                    self.history.append({
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [
                            {
                                "id": tool_call.id,
                                "type": "function",
                                "function": {
                                    "name": tool_call.function.name,
                                    "arguments": tool_call.function.arguments
                                }
                            }
                        ]
                    })
                    
                    self.history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    })
                
                # Get a new response with the tool results
                second_response = openai.chat.completions.create(
                    model=model,
                    messages=self.history,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                
                response_message = second_response.choices[0].message
            
            # Add the assistant's response to history
            self.history.append({
                "role": "assistant",
                "content": response_message.content
            })
            
            return response_message.content
            
        except Exception as e:
            error_message = f"Error communicating with OpenAI: {str(e)}"
            print_error(error_message)
            return error_message
