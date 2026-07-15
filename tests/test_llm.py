from src.llm.service import generate_response


response = generate_response(
    "Explain RAG in exactly two sentences."
)

print(response)