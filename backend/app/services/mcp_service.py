"""Service for managing MCP client connections and tools."""

from typing import List, Optional

from langchain.tools import StructuredTool
from toolbox_core import ToolboxClient

from app.config import settings
from app.services.tool_wrapper import wrap_mcp_tools


class MCPService:
    """Service for managing MCP ToolboxClient and tool loading."""

    def __init__(self):
        """Initialize MCP service."""
        self.client: Optional[ToolboxClient] = None
        self.tools: List[StructuredTool] = []

    async def connect(self) -> None:
        """Connect to the MCP server and load tools."""
        self.client = ToolboxClient(settings.mcp_server_url)
        await self.client.__aenter__()

        # Load tools from MCP server
        mcp_tools = await self.client.load_toolset()

        # Wrap tools for LangChain
        self.tools = wrap_mcp_tools(mcp_tools)

    async def disconnect(self) -> None:
        """Disconnect from the MCP server."""
        if self.client:
            await self.client.__aexit__(None, None, None)
            self.client = None

    def get_tools(self) -> List[StructuredTool]:
        """Get the loaded tools.

        Returns:
            List of wrapped StructuredTool instances

        Raises:
            RuntimeError: If tools haven't been loaded yet
        """
        if not self.tools:
            raise RuntimeError("Tools not loaded. Call connect() first.")
        return self.tools

    @property
    def is_connected(self) -> bool:
        """Check if the service is connected to MCP server."""
        return self.client is not None