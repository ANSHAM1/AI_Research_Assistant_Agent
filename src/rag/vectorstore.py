from langchain_chroma import Chroma
from langchain_core.documents import Document

from src.embeddings.model import embedding_model


vector_store = Chroma(
    collection_name="researchmind",
    embedding_function=embedding_model,
    persist_directory="data/chroma",
)


def add_documents(documents: list[Document]) -> None:
    vector_store.add_documents(documents)


# def similarity_search(query: str, k: int = 4) -> list[Document]:
#     return vector_store.similarity_search(query, k=k)


retriever = vector_store.as_retriever(search_kwargs={"k": 4})