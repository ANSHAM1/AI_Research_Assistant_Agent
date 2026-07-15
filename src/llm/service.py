from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import settings


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0,
)


def generate_response(message: str) -> str:
    response : object = llm.invoke(message)

    return str(response.content)