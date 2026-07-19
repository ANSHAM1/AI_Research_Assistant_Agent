from src.embeddings.model import (embed_documents,embed_query)
from src.embeddings.similarity import cosine_similarity


documents = [
    "NVIDIA develops graphics processing units and AI hardware.",
    "Mango is a tropical fruit known for its sweet taste.",
    "CUDA is a parallel computing platform for GPU programming.",
    "Delhi is the capital territory of India.",
    "PyTorch is a machine learning framework used to build neural networks.",
]


question = (
    "Which technology can be used for parallel programming on GPUs?"
)


document_vectors = embed_documents(documents)
query_vector = embed_query(question)


results: list[tuple[str, float]] = []


for document, document_vector in zip(
    documents,
    document_vectors,
):
    score = cosine_similarity(
        query_vector,
        document_vector,
    )

    results.append(
        (
            document,
            score,
        )
    )


results.sort(
    key=lambda item: item[1],
    reverse=True,
)


for document, score in results:
    print(f"\nScore: {score:.4f}")
    print(f"Document: {document}")