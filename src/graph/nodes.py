from langchain_core.messages import AIMessage

from src.graph.state import ResearchState

from src.prompts.chat_prompt import chat_prompt
from src.prompts.router_prompt import router_prompt
from src.agent.agent import agent_llm

from src.vectors.vectorstore import retriever



def router_node(state: ResearchState) -> dict[str, object]:
    """
    Router node.
    Decides whether RAG retrieval is required.
    """

    chain = router_prompt | agent_llm

    response = chain.invoke(
        {
            "question": state["question"]
        }
    )

    decision = (
        response.content
        if isinstance(response.content, str)
        else str(response.content)
    )

    use_rag = decision.strip().upper() == "USE_RAG"

    return {
        "use_rag": use_rag
    }

  

def chatbot_node(state: ResearchState) -> dict[str, object]:
    """
    Final response generation node.
    Uses conversation history + retrieved context
    and updates only required state fields.
    """

    chain = chat_prompt | agent_llm

    response = chain.invoke(
        {
            "messages": state["messages"],
            "question": state["question"],
            "web_context": state.get("web_context", ""),
            "rag_context": state.get("rag_context", [])
        }
    )

    answer = (
        response.content
        if isinstance(response.content, str)
        else str(response.content)
    )

    return {
        "messages": [
            AIMessage(content=answer)
        ],
        "answer": answer
    }



def rag_node(state: ResearchState) -> dict[str, object]:
    """
    RAG node.
    Uses conversation history + current query
    and updates only required state fields.
    """

    result = retriever.invoke(state["question"])

    return {
        "rag_context": result
    }

