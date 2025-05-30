# mcp-medium-accellerator

## Install

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt

## Launch MCP Insepector

mcp dev main.py

## Install MCP in Claude Desktop

mcp install main.py

## Config for Claude

```
{
  "mcpServers": {
    "mcp-medium-accellerator": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "--with",
        "bs4",
        "--with",
        "requests",
        "--with",
        "datetime",
        "--with",
        "tinydb",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/danielecarta/Documents/develop/mcp-server-demo/main.py"
      ]
    }
  }
}
```
