from pathlib import Path

from src.rag.loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.vectorstore import vector_store


def index_pdf(pdf_path: str) -> None:
    """
    Index a single PDF into ChromaDB.
    """

    print(f"Loading PDF: {pdf_path}")

    documents = load_pdf(pdf_path)

    print(f"Loaded {len(documents)} pages")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vector_store.add_documents(chunks)

    print("Indexing completed.")


def index_directory(directory: str) -> None:
    """
    Index all PDF files inside a directory.
    """

    pdf_directory = Path(directory)

    pdf_files = list(pdf_directory.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    for pdf_file in pdf_files:
        index_pdf(str(pdf_file))

    print("All PDFs indexed successfully.")