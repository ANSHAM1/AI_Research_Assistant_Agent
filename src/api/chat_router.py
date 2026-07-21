from fastapi import APIRouter, Form

from langchain_core.messages import HumanMessage

# from src.graph.graph import research_graph


chat_router = APIRouter(prefix="/chat", tags=["Chat"])


@chat_router.post("/")
async def chat(question: str = Form(...)) -> dict[str, str]:

    state : dict[str, object] = { # type: ignore
        "messages": [
            HumanMessage(content=question)
        ],

        "question": question,

        "retrieved_documents": [],

        "use_rag": False,

        "web_context": "",

        "answer": ""
    }

    # result = research_graph.invoke(state)

    return {
        # "answer": result["answer"]
    }