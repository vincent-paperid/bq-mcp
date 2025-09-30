"""Response models for API endpoints."""

from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""

    response: str = Field(..., description="LLM agent response")
    tool_calls_made: int = Field(
        ..., description="Number of tool calls made during execution"
    )


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str = Field(..., description="Service health status")
    mcp_server: str = Field(..., description="MCP server URL")
    agent_ready: bool = Field(..., description="Whether the agent is initialized")