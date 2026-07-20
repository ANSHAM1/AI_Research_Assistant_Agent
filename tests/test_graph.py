from langchain_core.messages import HumanMessage

from src.graph.workflow import graph
from src.utils.message_parser import get_message_text

from src.memory.store import save_memory

save_memory(
    user_id="research_session",
    category="preference",
    memory_key="language",
    memory_value="C++",
)

def main() -> None:

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        result = graph.invoke( # type: ignore
            {
                "messages": [
                    HumanMessage(content=question)
                ]
            },
            config={
                "configurable": {
                    "thread_id": "research_session"
                }
            }
)

        ai_message = get_message_text(result["messages"][-1])

        print(f"\nAI: {ai_message}")


if __name__ == "__main__":
    main()