from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import settings

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=settings.GOOGLE_API_KEY.get_secret_value(),
)

print(llm.invoke("Hello").content)