from fastapi import FastAPI

app = FastAPI(
    title="ResearchMind AI",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "ResearchMind AI Backend Running 🚀"
    }