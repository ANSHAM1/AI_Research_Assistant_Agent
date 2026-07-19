from src.llm.model import generate_response


response = generate_response(
    "Explain RAG in exactly two sentences."
)

print(response)