"""Entry point for running the FastAPI backend server."""

import uvicorn
from app.config import settings
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
