from fastapi import APIRouter

from src.api.schemas import ChatRequest, ChatResponse
from src.llm.service import generate_response


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = generate_response(request.message)

    return ChatResponse(answer=answer)