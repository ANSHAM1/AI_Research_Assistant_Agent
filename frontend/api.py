import requests


API_URL = "http://localhost:8000"


def send_message(question: str) -> dict[str, object]:
    """
    Send user question to chat API.
    """

    response = requests.post(
        f"{API_URL}/chat",
        data={
            "question": question
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()


def upload_rag(files: list[object]) -> dict[str, object]:
    """
    Upload PDF files for RAG indexing.
    """

    response = requests.post(
        f"{API_URL}/rag/upload",
        files=files,  # type: ignore
        timeout=120
    )

    response.raise_for_status()

    return response.json()