from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import settings


embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    api_key=settings.GOOGLE_API_KEY,
)


def embed_query(text: str) -> list[float]:
    return embedding_model.embed_query(text)


def embed_documents(documents: list[str]) -> list[list[float]]:
    return embedding_model.embed_documents(documents)