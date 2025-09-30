"""Application configuration and environment variables."""

import os
from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Google Cloud credentials
    google_application_credentials: str | None = os.getenv(
        "GOOGLE_APPLICATION_CREDENTIALS"
    )
    google_api_key: str | None = os.getenv("GOOGLE_API_KEY")

    # MCP Server configuration
    mcp_server_url: str = "http://127.0.0.1:5000"

    # LLM configuration
    llm_model: str = "google_genai:gemini-2.0-flash"

    # API configuration
    api_title: str = "BigQuery MCP FastAPI Backend"
    api_description: str = (
        "FastAPI backend integrated with BigQuery MCP server via LangGraph"
    )
    api_version: str = "0.1.0"

    # CORS configuration
    cors_origins: List[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["*"]
    cors_allow_headers: List[str] = ["*"]

    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()