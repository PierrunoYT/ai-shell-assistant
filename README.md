# AI CLI

A command-line interface for AI chat with extensible tools.

## Features

- Interactive chat with AI powered by OpenAI's GPT models
- Extensible tool system for adding new capabilities
- Natural Language Understanding (NLU) for tool calling
- Built-in search file tool for finding content in files
- Configuration management for customizing behavior

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-cli.git
   cd ai-cli
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

   Or add it to a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Starting a Chat Session

```
python main.py chat
```

You can customize the chat session with options:
```
python main.py chat --model gpt-4 --temperature 0.8 --max-tokens 2000
```

### Configuration

Set configuration values:
```
python main.py config-set api_key your_api_key_here
python main.py config-set model gpt-4
python main.py config-set temperature 0.7
python main.py config-set enabled_tools search_file
```

View configuration:
```
python main.py config-get
python main.py config-get model
```

### Available Tools

List all available tools:
```
python main.py tools
```

## Natural Language Tool Calling

The AI CLI supports natural language understanding (NLU) for tool calling. This means you can use natural language to invoke tools instead of explicit commands. For example:

```
[You]: Can you search for "config" in the ai_cli directory?
[AI]: I'll use the search_file tool to help with that.

Here's what I found:
...
```

You can enable or disable NLU tool calling in the configuration:

```
python main.py config-set use_nlu_tool_calling true
```

## Adding New Tools

To add a new tool:

1. Create a new Python file in the `ai_cli/tools` directory
2. Define a class that inherits from `BaseTool`
3. Implement the required methods: `execute` and `parameters`
4. Register the tool in `ai_cli/tools/__init__.py`

Example:

```python
from typing import Any, Dict, List
from ai_cli.tools.base import BaseTool

class MyNewTool(BaseTool):
    name = "my_tool"
    description = "Description of what my tool does"

    @property
    def parameters(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "param1",
                "description": "Description of parameter 1",
                "type": "string",
                "required": True
            }
        ]

    def execute(self, args: Dict[str, Any]) -> str:
        param1 = args.get("param1", "")
        # Tool implementation here
        return f"Result: {param1}"
```

Then register it in `ai_cli/tools/__init__.py`:

```python
from ai_cli.tools.my_tool import MyNewTool

AVAILABLE_TOOLS = {
    # ... existing tools
    "my_tool": MyNewTool,
}
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
