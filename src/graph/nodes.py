from src.graph.agent import agent_llm
from src.graph.state import GraphState

from src.memory.manager import extract_memory
from src.memory.store import save_memory


def memory_node(state: GraphState) -> GraphState:
    memory = extract_memory(
        state["messages"]
    )

    if memory is None:
        return state

    category, key, value = memory

    save_memory(
        user_id="research_session",
        category=category,
        memory_key=key,
        memory_value=value,
    )

    return state


def chatbot_node(state: GraphState) -> GraphState:
    response = agent_llm.invoke(state["messages"])

    return {
        "messages": [response]
    }