from langchain_core.chat_history import (BaseChatMessageHistory)
from langchain_core.chat_history import (InMemoryChatMessageHistory)


store : dict[str, BaseChatMessageHistory] = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = (
            InMemoryChatMessageHistory()
        )

    return store[session_id]