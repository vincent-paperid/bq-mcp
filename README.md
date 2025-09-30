# BigQuery MCP Server

A Model Context Protocol (MCP) server for Google BigQuery that integrates with Google's Agent Development Kit (ADK). This server exposes BigQuery operations through the MCP protocol, allowing AI models and agents to interact with BigQuery datasets.

## Features

- **MCP Server Implementation**: Full MCP server with stdio transport
- **BigQuery Integration**: Direct integration with Google BigQuery
- **ADK Agent Support**: Enhanced agent using Google ADK with BigQuery toolset
- **Read-Only Mode**: Safe, read-only operations by default
- **Table Formatting**: Returns query results as both text and formatted markdown tables
- **Comprehensive Tools**: List datasets, tables, get metadata, and execute SQL queries

## Quick Start

1. Install dependencies:
```bash
cd backend
uv sync  # or pip install -r requirements.txt
```

2. Configure Google Cloud authentication:
```bash
gcloud auth application-default login
```

3. Run the MCP server:
```bash
python main.py
```

4. Test with the MCP client:
```bash
python mcp_client.py
```

See the [backend README](backend/README.md) for detailed documentation.