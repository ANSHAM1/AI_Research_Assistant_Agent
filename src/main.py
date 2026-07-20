from fastapi import FastAPI

from src.api.rag_router import rag_router
from src.api.chat_router import chat_router

app = FastAPI(
    title="ResearchMind AI",
    version="1.0.0",
)

app.include_router(rag_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "ResearchMind AI Backend Running 🚀"
    }