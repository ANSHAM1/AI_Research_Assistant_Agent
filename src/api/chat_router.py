from fastapi import APIRouter, Form
from src.api.schemas import ChatResponse

from langchain_core.messages import HumanMessage

from src.graph.state import ResearchState
from src.graph.workflow import graph


USER_SESSION_ID = "USER_1"


chat_router = APIRouter(prefix="/chat", tags=["Chat"])


@chat_router.post("/", response_model=ChatResponse)
async def chat(question: str = Form(...)) -> ChatResponse:

    state : ResearchState = { 
        "messages": [
            HumanMessage(content=question)
        ],

        "question": question,

        "rag_context": [],

        "use_rag": False,

        "web_context": "",

        "answer": ""
    }


    result = graph.invoke( # type: ignore        
        state,

        config={
            "configurable": {
                "thread_id": USER_SESSION_ID
            }
        }
    )

    return ChatResponse(
        answer=result["answer"]
    )