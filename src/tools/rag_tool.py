from langchain_core.tools import tool

from src.store.chain import generate_answer


@tool
def rag_tool(query: str) -> str:
    """
    Search the local knowledge base and answer the user's question.

    Use this tool when information should come from the indexed documents.
    """

    return generate_answer(query)