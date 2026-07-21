from src.memory.memstore import get_memories


def build_memory_context(user_id: str) -> str:
    memories = get_memories(user_id)

    if not memories:
        return ""

    return "\n".join(
        f"- {memory.key}: {memory.value}"
        for memory in memories
    )