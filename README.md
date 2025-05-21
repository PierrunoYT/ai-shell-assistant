# AI Shell Assistant

AI Shell Assistant is a command-line tool that uses AI to convert natural language into shell commands. It allows you to describe what you want to do in plain English, and the AI will generate and execute the appropriate shell commands for you.

## Warning

**USE AT YOUR OWN RISK**: This tool executes shell commands on your system. While it includes safety measures and requires confirmation before executing any command, there is always a risk when executing automatically generated commands. The authors are not responsible for any damage, data loss, or other negative consequences that may result from using this tool.

- Always carefully review commands before confirming execution
- Be especially cautious with commands that modify or delete files
- Consider running in a test environment for unfamiliar operations

## Features

- **Natural Language to Shell Commands**: Describe tasks in plain English and get the corresponding shell commands
- **Command Explanations**: Get detailed explanations of what each command does
- **Safety First**: All commands require confirmation before execution
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Interactive Chat**: Full AI chat capabilities for general assistance
- **Rich Terminal UI**: Colorful and informative terminal interface
- **Multiple AI Models**: Support for the latest OpenAI models including GPT-4o

## Supported AI Models

AI Shell Assistant supports multiple OpenAI models:

- **GPT-4o** (default): Latest and most capable model with improved reasoning
- **GPT-4**: Advanced reasoning and instruction following
- **GPT-4-turbo**: Faster version of GPT-4 with similar capabilities
- **GPT-3.5-turbo**: Faster and more economical model

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/ai-shell-assistant.git
   cd ai-shell-assistant
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Shell Command Generator

Generate shell commands from natural language descriptions:

```
python main.py shell
```

With specific model:
```
python main.py shell --model gpt-4
```

Example interactions:
- "List all Python files in the current directory"
- "Find all files modified in the last 7 days"
- "Create a backup of my project folder"
- "Show me system information"

### AI Chat

Start an interactive chat session with the AI:

```
python main.py chat
```

With specific model and parameters:
```
python main.py chat --model gpt-3.5-turbo --temperature 0.8
```

### Configuration

View current configuration:
```
python main.py config_get
```

Set configuration values:
```
python main.py config_set key value
```

Example configurations:
```
python main.py config_set model gpt-4o
python main.py config_set temperature 0.7
python main.py config_set max_tokens 2000
```

## Security Considerations

- The tool uses the OpenAI API to generate commands, which means your queries are sent to OpenAI's servers
- Commands are only executed after explicit user confirmation
- Consider reviewing the generated commands carefully before execution
- For sensitive operations, verify the command's correctness independently

## License

MIT

## Credits

Created by PierrunoYT