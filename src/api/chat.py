from fastapi import APIRouter
from langchain_core.messages import HumanMessage, SystemMessage

from src.api.schemas import ChatRequest, ChatResponse
from src.graph.workflow import graph
from src.memory.retriever import build_memory_context
from src.memory.service import process_memory
from src.utils.message_parser import get_message_text


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


# Later this should come from authentication/session
THREAD_ID = "research_session"


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:

    config = {
        "configurable": {
            "thread_id": THREAD_ID,
        }
    }

    memory_context = build_memory_context(THREAD_ID)

    messages = []

    if memory_context:
        messages.append( # type: ignore
            SystemMessage(
                content=f"""
You are an AI assistant with long-term memory.

The following facts about the user are true and should be used whenever they are relevant.

User Memory:
{memory_context}

Do not contradict these facts unless the user explicitly corrects them.
"""
            )
        )

    messages.append( # type: ignore
        HumanMessage(
            content=request.message
        )
    )

    result = graph.invoke( # type: ignore
        {
            "messages": messages,
        },
        config=config, # type: ignore
    )

    process_memory(
        user_id=THREAD_ID,
        messages=result["messages"],
    )

    answer = get_message_text(
        result["messages"][-1]
    )

    return ChatResponse(
        answer=answer,
    )