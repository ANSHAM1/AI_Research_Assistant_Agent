from src.rag.loader import load_pdf

from src.rag.splitter import split_documents


documents = load_pdf(
    "data/pdfs/sample.pdf"
)

chunks = split_documents(documents)


print(len(documents))

print(len(chunks))

print(chunks[0])

print(chunks[0].metadata)

print(chunks[1])