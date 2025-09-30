"""FastAPI dependencies for dependency injection."""

from fastapi import Depends

from app.core.lifespan import get_agent_service, get_mcp_service
from app.services.agent_service import AgentService
from app.services.mcp_service import MCPService


def get_agent() -> AgentService:
    """Dependency to get the agent service.

    Returns:
        AgentService instance
    """
    return get_agent_service()


def get_mcp() -> MCPService:
    """Dependency to get the MCP service.

    Returns:
        MCPService instance
    """
    return get_mcp_service()