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

### Configuration

View current configuration:
```
python main.py config_get
```

Set configuration values:
```
python main.py config_set key value
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