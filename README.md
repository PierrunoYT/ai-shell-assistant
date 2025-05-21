# AI Shell Assistant

AI Shell Assistant is a command-line tool that uses AI to convert natural language into shell commands. It allows you to describe what you want to do in plain English, and the AI will generate and execute the appropriate shell commands for you.

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

## License

MIT

## Credits

Created by PierrunoYT