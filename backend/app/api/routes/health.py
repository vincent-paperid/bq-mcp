"""Health check endpoint."""

from fastapi import APIRouter, Depends

from app.api.dependencies import get_agent, get_mcp
from app.config import settings
from app.models.responses import HealthResponse
from app.services.agent_service import AgentService
from app.services.mcp_service import MCPService

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check(
    mcp: MCPService = Depends(get_mcp),
    agent: AgentService = Depends(get_agent),
) -> HealthResponse:
    """Check the health status of the API and its dependencies.

    Returns:
        HealthResponse with service status
    """
    return HealthResponse(
        status="healthy",
        mcp_server=settings.mcp_server_url,
        agent_ready=agent.is_ready,
    )