from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.messages import BaseMessage


def build_conversation(messages: list[BaseMessage]) -> str:
    conversation : list[str] = []

    for message in messages:

        if isinstance(message, HumanMessage):
            role = "User"

        elif isinstance(message, AIMessage):
            role = "Assistant"

        else:
            continue

        conversation.append(
            f"{role}: {message.content}"
        )

    return "\n".join(conversation)