from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from typing import Any, List
from uuid import uuid4

from langchain_core.documents import Document
from src.tools.pdf_loader import load_pdf
from src.store.ingester import ingest_documents



rag_router = APIRouter(prefix="/rag", tags=["RAG"])


UPLOAD_DIR = Path("data/pdfs")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@rag_router.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)) -> dict[str, Any]:
    saved_files: List[Document] = []

    for file in files:
        filename = file.filename or f"uploaded_file_{uuid4().hex}"
        file_path = UPLOAD_DIR / filename

        content = await file.read()
        file_path.write_bytes(content)

        loaded_docs = load_pdf.run(str(file_path))
        if isinstance(loaded_docs, list):
            saved_files.extend(loaded_docs) # type: ignore
        elif loaded_docs is not None:
            saved_files.append(loaded_docs)

    ingest_documents(saved_files)

    return {
        "status": "success",
        "files_uploaded": len(saved_files),
        "message": "Documents indexed successfully."
    }