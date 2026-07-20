from langgraph.checkpoint.memory import MemorySaver

# Development checkpointer.
# Later this can be replaced with SqliteSaver or PostgresSaver
# without changing the graph.

checkpointer = MemorySaver()