from fastapi import FastAPI

from src.api.chat import router as chat_router


app = FastAPI(
    title="ResearchMind AI",
    version="1.0.0",
)


app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "ResearchMind AI Backend Running 🚀"
    }