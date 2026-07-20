from typing import Any

from langchain_core.messages import AIMessage


def get_message_text(message: AIMessage) -> str:
    content: Any = message.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts: list[str] = []

        for part in content: # type: ignore
            if (
                isinstance(part, dict)
                and part.get("type") == "text" # type: ignore
            ):
                text_parts.append(part["text"]) # type: ignore

        return "\n".join(text_parts)

    return str(content)