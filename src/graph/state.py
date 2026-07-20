from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages # type: ignore
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]