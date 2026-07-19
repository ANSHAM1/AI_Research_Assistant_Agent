from src.rag.loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.vectorstore import (
    add_documents,
    similarity_search,
)

documents = load_pdf(
    "data/pdfs/sample.pdf"
)

chunks = split_documents(documents)

add_documents(chunks)

results = similarity_search(
    "Explain convolutional neural networks.",
    k=3,
)

print(f"Retrieved {len(results)} documents\n")

for index, document in enumerate(results, start=1):
    print(f"----- Result {index} -----")
    print(document.metadata)
    print(document.page_content[:300])
    print()