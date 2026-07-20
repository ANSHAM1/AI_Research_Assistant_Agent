from langchain_core.messages import BaseMessage

from src.memory.manager import extract_memory
from src.memory.store import save_memory


def process_memory(user_id: str, messages: list[BaseMessage]) -> None:
    """
    Extract long-term memory from the conversation
    and persist it if appropriate.
    """

    try:
        memory = extract_memory(messages)

        if memory is None:
            return

        category, key, value = memory

        save_memory(
            user_id=user_id,
            category=category,
            memory_key=key,
            memory_value=value,
        )

    except Exception as e:
        print(f"Memory extraction failed: {e}")