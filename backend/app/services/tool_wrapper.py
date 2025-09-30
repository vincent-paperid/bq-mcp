"""Utilities for wrapping MCP tools for LangChain integration."""

from typing import List

from langchain.tools import StructuredTool
from toolbox_core import ToolboxTool


def create_async_wrapper(tool: ToolboxTool):
    """Create an async wrapper for a ToolboxTool.

    Args:
        tool: The ToolboxTool instance to wrap

    Returns:
        Async function that calls the tool
    """

    async def async_wrapper(**kwargs):
        return await tool(**kwargs)

    return async_wrapper


def wrap_mcp_tools(tools: List[ToolboxTool]) -> List[StructuredTool]:
    """Wrap MCP tools as LangChain StructuredTools.

    Args:
        tools: List of ToolboxTool instances from MCP server

    Returns:
        List of wrapped StructuredTool instances
    """
    wrapped_tools = []

    for tool in tools:
        async_wrapper = create_async_wrapper(tool)
        async_wrapper.__name__ = tool.__name__
        async_wrapper.__doc__ = tool.__doc__

        wrapped_tool = StructuredTool.from_function(
            async_wrapper,
            name=tool.__name__,
            description=tool.__doc__ or "",
            coroutine=async_wrapper,
            parse_docstring=False,
        )
        wrapped_tools.append(wrapped_tool)

    return wrapped_tools