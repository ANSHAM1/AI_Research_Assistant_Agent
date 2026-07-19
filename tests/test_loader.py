from src.rag.loader import load_pdf


documents = load_pdf(
    "data/pdfs/sample.pdf"
)


print(type(documents))

print(len(documents))

print(type(documents[0]))

print(documents[0])