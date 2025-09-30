"""Service for managing LangGraph agent and execution."""

from typing import List, Optional

from langchain.chat_models import init_chat_model
from langchain.tools import StructuredTool
from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode

from app.config import settings
from app.models.state import State


class AgentService:
    """Service for managing LangGraph agent creation and execution."""

    def __init__(self):
        """Initialize agent service."""
        self.agent = None

    def create_agent(self, tools: List[StructuredTool]) -> None:
        """Create and compile the LangGraph agent.

        Args:
            tools: List of wrapped StructuredTool instances
        """
        # Create model with tools bound
        model_with_tools = init_chat_model(settings.llm_model).bind_tools(tools)

        # Create tool node
        tool_node = ToolNode(tools)

        # Define agent callback
        async def call_agent(state: State):
            response = await model_with_tools.ainvoke(state["messages"])
            return {"messages": [response]}

        # Define routing logic
        def should_continue(state: State):
            last_message = state["messages"][-1]
            if last_message.tool_calls:
                return "tools"
            return END

        # Build the graph
        graph_builder = StateGraph(State)
        graph_builder.add_node("agent", call_agent)
        graph_builder.add_node("tools", tool_node)
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", should_continue)
        graph_builder.add_edge("tools", "agent")

        # Compile the graph
        self.agent = graph_builder.compile()

    async def execute(self, prompt: str) -> tuple[str, int]:
        """Execute the agent with a given prompt.

        Args:
            prompt: User prompt to process

        Returns:
            Tuple of (response_content, tool_calls_count)

        Raises:
            RuntimeError: If agent hasn't been created yet
        """
        if not self.agent:
            raise RuntimeError("Agent not initialized. Call create_agent() first.")

        # Create input messages
        inputs = {"messages": [HumanMessage(content=prompt)]}

        # Run the agent
        final_state = None
        async for event in self.agent.astream(inputs, stream_mode="values"):
            final_state = event

        if not final_state or not final_state.get("messages"):
            raise RuntimeError("No response from agent")

        # Get the final message
        final_message = final_state["messages"][-1]

        # Count tool calls made during execution
        tool_calls_count = sum(
            1
            for msg in final_state["messages"]
            if hasattr(msg, "tool_calls") and msg.tool_calls
        )

        # Extract response content
        response_content = (
            final_message.content
            if hasattr(final_message, "content")
            else str(final_message)
        )

        return response_content, tool_calls_count

    @property
    def is_ready(self) -> bool:
        """Check if the agent is ready to execute."""
        return self.agent is not None