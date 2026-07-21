from langgraph.graph import StateGraph, START, END # type: ignore

from src.graph.state import ResearchState
from src.graph.nodes import chatbot_node, rag_node, router_node

from src.memory.checkpointer import checkpointer


builder = StateGraph(ResearchState)

# Add nodes
builder.add_node("router", router_node) # type: ignore
builder.add_node("chatbot", chatbot_node) # type: ignore
builder.add_node("rag", rag_node) # type: ignore

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

# Final node
builder.add_edge("chatbot", END)



graph = builder.compile(checkpointer=checkpointer) # type: ignore



# flow:

# START
#  |
#  v
# router_node
#  |
#  |---- no rag ----> chatbot_node ----> END
#  |
#  |---- rag -------> rag_node
#                        |
#                        v
#                   chatbot_node
#                        |
#                        v
#                       END


# Final graph:

#           START
#             |
#             v
#       decision_node
#          /      \
#       RAG        Direct
#        |          |
#        v          |
#    rag_node       |
#        |          |
#        └----> chatbot_node
#                    |
#                    v
#                   END