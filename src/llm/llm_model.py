from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import settings


llm_model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0,
)