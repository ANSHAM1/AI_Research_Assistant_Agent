from langchain_chroma import Chroma

from src.embeddings.embedding_model import embedding_model


vector_store = Chroma(
    collection_name="researchmind",
    embedding_function=embedding_model,
    persist_directory="data/chroma",
)


retriever = vector_store.as_retriever(
    search_type="mmr",

    search_kwargs={
        "k":4,
        "fetch_k":20
    }
)