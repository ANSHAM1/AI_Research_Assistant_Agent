from langchain_core.documents import Document
from langchain_community.document_loaders import Docx2txtLoader


def load_docx(docx_path: str) -> list[Document]:
    """
    Load a DOCX file and return a list of LangChain Documents.
    """

    loader = Docx2txtLoader(docx_path)

    return loader.load()