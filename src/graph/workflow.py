from langgraph.graph import StateGraph, START, END # type: ignore
from langgraph.prebuilt import tools_condition

from src.graph.state import GraphState
from src.graph.nodes import chatbot_node
from src.graph.agent import tool_node

from src.memory.checkpointer import checkpointer
from src.memory.store import initialize_database


initialize_database()

builder = StateGraph(GraphState)

builder.add_node("chatbot", chatbot_node) # type: ignore
builder.add_node("tools", tool_node) # type: ignore

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge("tools", "chatbot")

builder.add_edge("chatbot", END)

graph = builder.compile(checkpointer=checkpointer) # type: ignore

# START
#    │
#    ▼
# Chatbot
#    │
#    ├── Tool Call?
#    │      │
#    │      ├── No ─────► END
#    │      │
#    │      └── Yes
#    │             │
#    ▼             ▼
#  ToolNode ─────► Chatbot
#                     │
#              More tool calls?
#                     │
#           Yes ──────┘
#           No
#           │
#           ▼
#          END