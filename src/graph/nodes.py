from src.api.schemas import extract_response_text

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

    if isinstance(response.content, str):
        decision = response.content.strip()
    else:
        try:
            first = response.content[0]
            if isinstance(first, dict) and "text" in first:
                decision = first["text"].strip()
            else:
                decision = str(response.content).strip()
        except Exception:
            decision = str(response.content).strip()


    use_rag = decision.upper() == "USE_RAG"

    # print("====================")
    # print("QUESTION:", state["question"])
    # print("ROUTER OUTPUT:", decision)
    # print("USE RAG:", use_rag)
    # print("====================")

    return {
        "use_rag": use_rag
    }

  

def chatbot_node(state: ResearchState) -> dict[str, object]:

    chain = chat_prompt | agent_llm

    response = chain.invoke(
        {
            "messages": state["messages"],
            "question": state["question"],
            "web_context": state.get("web_context", ""),
            "rag_context": state.get("rag_context", []),
        }
    )

    answer = extract_response_text(response.content)

    return {
        "messages": [response],
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