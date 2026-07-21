from langchain.messages import AIMessage
from langgraph.graph import StateGraph, START, END # type: ignore

from src.graph.state import ResearchState
from src.graph.nodes import chatbot_node, rag_node, router_node
from src.agent.agent import tool_node

from src.memory.checkpointer import checkpointer


builder = StateGraph(ResearchState)

# Add nodes
builder.add_node("router", router_node) # type: ignore
builder.add_node("chatbot", chatbot_node) # type: ignore
builder.add_node("rag", rag_node) # type: ignore
builder.add_node("tool", tool_node) # type: ignore

# START -> router
builder.add_edge(START, "router")


# Router decision function
def decide_rag(state: ResearchState) -> str:

    if state["use_rag"]:
        return "rag"

    return "chatbot"


# Conditional routing
builder.add_conditional_edges(
    "router",
    decide_rag,
    {
        "rag": "rag",
        "chatbot": "chatbot"
    }
)

# After RAG, go back to chatbot
builder.add_edge("rag", "chatbot")


# Tool Decision
def should_continue(state: ResearchState) -> str:

    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tool"

    return "end"


# Conditional routing
builder.add_conditional_edges(
    "chatbot",
    should_continue,
    {
        "tool": "tool",
        "end": END
    }
)

# Tool result -> LLM again
builder.add_edge("tool", "chatbot")



graph = builder.compile(checkpointer=checkpointer) # type: ignore



# Final Graph:

#                          START
#                            |
#                            v
#                      router_node
#                     /            \
#                USE_RAG         NO_RAG
#                   |               |
#                   v               |
#              rag_node             |
#                   |               |
#                   +-------+-------+
#                           |
#                           v
#                     chatbot_node
#                           |
#                  Tool Required?
#                     /         \
#                   Yes         No
#                    |           |
#                    v           v
#                tool_node      END
#                    |
#                    v
#              chatbot_node
#                    |
#                    v
#                   END