from typing import List
from langchain_core.documents import Document

from src.store.splitter import split_documents
from src.store.vectorstore import vector_store


def ingest_documents(docs : List[Document]) -> None:
    chunks = split_documents(docs)
    vector_store.add_documents(chunks)

    print("Ingestion complete. Added {} documents to the vector store.".format(len(chunks)))
