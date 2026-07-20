from typing import Literal
from pydantic import BaseModel

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage

from src.utils.build_conversation import build_conversation

from src.llm.llm_model import llm


class MemoryExtraction(BaseModel):
    should_save: bool
    category: Literal[
        "preference",
        "project",
        "environment",
        "goal",
        "other",
    ] | None = None
    memory_key: str | None = None
    memory_value: str | None = None


memory_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You extract long-term user memories.

Only save information that will likely be useful in future conversations.

Do NOT save:
- Greetings
- Questions
- Temporary requests
- Small talk
- Calculations

Save things like:
- User preferences
- User goals
- Current projects
- Development environment
- Stable personal facts

Return structured output only.
            """,
        ),
        (
            "human",
            "{message}",
        ),
    ]
)


memory_chain = (memory_prompt | llm.with_structured_output(MemoryExtraction)) # type: ignore


def extract_memory(messages: list[BaseMessage]) -> tuple[str, str, str] | None:
    conversation = build_conversation(messages)
    result = memory_chain.invoke( # type: ignore
        {
            "message": conversation,
        }
    )

    if not result.should_save: # type: ignore
        return None

    return (result.category, result.memory_key, result.memory_value) # type: ignore