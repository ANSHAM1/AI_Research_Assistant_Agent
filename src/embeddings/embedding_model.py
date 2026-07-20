from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import settings


embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    api_key=settings.GOOGLE_API_KEY,
)