from langgraph.graph import (StateGraph, START, END) # type: ignore

from src.graph.state import GraphState
from src.graph.nodes import rag_node


builder = StateGraph(GraphState)


builder.add_node("rag", rag_node) # type: ignore

builder.add_edge(START, "rag")
builder.add_edge("rag",END)


graph = builder.compile() # type: ignore