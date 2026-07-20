from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda
from typing import Any, Mapping

# Memory (Disabled for now)
# from langchain_core.runnables.history import RunnableWithMessageHistory

from src.llm.model import llm
from src.rag.vectorstore import retriever
from src.rag.prompts import rag_prompt

# Memory (Disabled for now)
# from src.memory.history import get_session_history


output_parser = StrOutputParser()


def format_documents(documents: list[Document]) -> str:
    return "\n\n".join(
        document.page_content
        for document in documents
    )


def extract_question(inputs: Mapping[str, Any]) -> str:
    """Extract the question from inputs and ensure a string is returned."""
    value = inputs.get("question")
    if isinstance(value, str):
        return value
    if value is None:
        return ""
    return str(value)


rag_chain = (
    {
        "context": RunnableLambda(extract_question) | retriever | RunnableLambda(format_documents),

        "question": RunnableLambda(extract_question),
    }

    | rag_prompt

    | llm

    | output_parser
)


# ============================================================================
# Memory (Disabled)
# Will be replaced by LangGraph Persistence in Module 10+
# ============================================================================
#
# conversation_chain = RunnableWithMessageHistory(
#     rag_chain,
#     get_session_history,
#     input_messages_key="question",
#     history_messages_key="chat_history",
# )
#
# ============================================================================


def generate_answer(question: str) -> str:
    return rag_chain.invoke(
        {
            "question": question
        }
    )


# ============================================================================
# Old Memory Version (Disabled)
#
# def generate_answer(
#     question: str,
#     session_id: str = "default"
# ) -> str:
#
#     return conversation_chain.invoke(
#         {
#             "question": question
#         },
#         config={
#             "configurable": {
#                 "session_id": session_id
#             }
#         }
#     )
#
# ============================================================================


# def generate_answer(question: str) -> str:
#     documents = retriever.invoke(question)

#     context = format_documents(documents)

#     prompt = rag_prompt.invoke(
#         {
#             "context": context,

#             "question": question,
#         }
#     )

#     response = llm.invoke(prompt)

#     return output_parser.invoke(response)