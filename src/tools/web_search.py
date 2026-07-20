from typing import Any

from langchain_core.tools import tool
from tavily import TavilyClient  # type: ignore[import]

from src.config import settings


client = TavilyClient(
    api_key=settings.TAVILY_API_KEY, # type: ignore
)


@tool
def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web for recent information.

    Use this tool when the user's question requires
    information that is unavailable in the local RAG
    knowledge base or depends on current events.

    Args:
        query: The search query.
        max_results: Maximum number of results to retrieve.

    Returns:
        A formatted string containing the search results.
    """

    try:
        response: dict[str, Any] = client.search( # type: ignore
            query=query,
            max_results=max_results,
        )

        results: list[dict[str, Any]] = response.get("results", [])

        if not results:
            return "No relevant web results were found."

        formatted_results: list[str] = []

        for index, result in enumerate(results, start=1):
            title: str = result.get("title", "")
            url: str = result.get("url", "")
            content: str = result.get("content", "")

            formatted_results.append(
                (
                    f"Result {index}\n"
                    f"Title: {title}\n"
                    f"URL: {url}\n"
                    f"Content: {content}"
                )
            )

        return "\n\n".join(formatted_results)

    except Exception as exc:
        return f"Web search failed: {exc}"