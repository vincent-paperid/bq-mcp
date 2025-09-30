"""Chat endpoint for LLM interactions."""

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_agent
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.services.agent_service import AgentService

router = APIRouter(prefix="/api", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    agent: AgentService = Depends(get_agent),
) -> ChatResponse:
    """Process a chat prompt through the LLM agent with BigQuery tools.

    Args:
        request: Chat request with user prompt
        agent: Injected agent service

    Returns:
        ChatResponse with LLM response and metadata

    Raises:
        HTTPException: If agent is not ready or execution fails
    """
    if not agent.is_ready:
        raise HTTPException(status_code=503, detail="Agent not initialized")

    try:
        response_content, tool_calls_count = await agent.execute(request.prompt)

        return ChatResponse(
            response=response_content,
            tool_calls_made=tool_calls_count,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing request: {str(e)}"
        )