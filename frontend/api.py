import requests

API_URL = "http://localhost:8000"


def send_message(question, files=None): # type: ignore

    payload = { # type: ignore
        "question": question
    }

    response = requests.post(
        f"{API_URL}/chat",
        data=payload, # type: ignore
        files=files # type: ignore
    )

    return response.json()


def upload_rag(files): # type: ignore

    response = requests.post(
        f"{API_URL}/rag/upload",
        files=files # type: ignore
    )

    return response.json()