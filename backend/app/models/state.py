"""LangGraph state definitions."""

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict


class State(TypedDict):
    """State for LangGraph agent."""

    messages: Annotated[list[BaseMessage], add_messages]