"""Application lifecycle management."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.services.agent_service import AgentService
from app.services.mcp_service import MCPService

# Global service instances
mcp_service: MCPService | None = None
agent_service: AgentService | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage the application lifecycle.

    Handles:
    - Startup: Initialize MCP service and agent
    - Shutdown: Clean up connections

    Args:
        app: FastAPI application instance
    """
    global mcp_service, agent_service

    # Startup: Initialize services
    mcp_service = MCPService()
    agent_service = AgentService()

    try:
        # Connect to MCP server and load tools
        await mcp_service.connect()

        # Create agent with loaded tools
        tools = mcp_service.get_tools()
        agent_service.create_agent(tools)

        yield

    finally:
        # Shutdown: Disconnect from MCP server
        if mcp_service:
            await mcp_service.disconnect()


def get_mcp_service() -> MCPService:
    """Get the global MCP service instance.

    Returns:
        MCPService instance

    Raises:
        RuntimeError: If service not initialized
    """
    if mcp_service is None:
        raise RuntimeError("MCP service not initialized")
    return mcp_service


def get_agent_service() -> AgentService:
    """Get the global agent service instance.

    Returns:
        AgentService instance

    Raises:
        RuntimeError: If service not initialized
    """
    if agent_service is None:
        raise RuntimeError("Agent service not initialized")
    return agent_service