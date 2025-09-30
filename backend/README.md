## ⚙️ Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app initialization
│   ├── config.py                  # Settings & environment variables
│   ├── models/
│   │   ├── __init__.py
│   │   ├── requests.py            # ChatRequest
│   │   ├── responses.py           # ChatResponse, HealthResponse
│   │   └── state.py               # LangGraph State
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py        # FastAPI dependency injection
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── health.py          # GET /health
│   │       └── chat.py            # POST /api/chat
│   ├── services/
│   │   ├── __init__.py
│   │   ├── mcp_service.py         # MCP client management
│   │   ├── agent_service.py       # LangGraph agent logic
│   │   └── tool_wrapper.py        # Tool wrapping utilities
│   └── core/
│       ├── __init__.py
│       └── lifespan.py            # App lifecycle management
├── main.py                        # Entry point
└── pyproject.toml
```

## ☝️ API Endpoints
- `GET /health` - Health check showing MCP server connection status
- `POST /api/chat` - Main endpoint that accepts prompts and returns LLM responses

Request and response example for `/api/chat` endpoint:
```
// Request
{"prompt": "Get all BigQuery datasets"}

// Response
{
  "response": "Here are your BigQuery datasets...",
  "tool_calls_made": 2
}
```

## 🚀 How to Run
```
python backend/main.py
```
Running the script here will start the server on `http://0.0.0.0:8000` with hot-reload enabled.