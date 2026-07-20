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

    # Temporary chat attachments
    pdf_files: list[str]
    doc_files: list[str]
    audio_files: list[str]

    # Retrieved RAG documents
    retrieved_documents: list[Document]

    # Tool outputs
    attachment_context: str
    rag_context: str
    web_context: str

    # Final response
    answer: str