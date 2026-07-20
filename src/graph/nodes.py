from typing import Any

from src.graph.state import GraphState
from src.rag.chain import generate_answer


def rag_node(state: GraphState) -> dict[str, Any]:
    answer = generate_answer(
        state["question"]
    )

    return {
        "answer": answer
    }