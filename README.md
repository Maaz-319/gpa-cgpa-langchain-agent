# CGPA Guider

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `MODEL`, `BASE_URL`, `API_KEY`, and `MCP_SERVER_URL` in `.env`.

## Run

Start the MCP server in one terminal:

```bash
fastmcp run server.py:mcp --transport http --port 8000
```

Set `MCP_SERVER_URL=http://127.0.0.1:8000/mcp`, then start the client in another terminal:

```bash
uv run client.py
```

> I used Omni Route for this project.