from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(pdf_path: str) -> list[Document]:
    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents