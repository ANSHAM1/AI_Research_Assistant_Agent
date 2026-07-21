from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages # type: ignore


class ResearchState(TypedDict):
    # Conversation
    messages: Annotated[list[BaseMessage], add_messages]

    # Current query
    question: str

    # Retrieved RAG documents
    rag_context: list[Document]

    # Router decision
    use_rag: bool

    # Tool outputs
    web_context: str

    # Final response
    answer: str