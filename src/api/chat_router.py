from pathlib import Path
from typing import List

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

# from src.graph.graph import research_graph



chat_router = APIRouter(prefix="/chat", tags=["Chat"])


TEMP_DIR = Path("data/temp")

PDF_DIR = TEMP_DIR / "pdf"
DOC_DIR = TEMP_DIR / "doc"

PDF_DIR.mkdir(parents=True, exist_ok=True)
DOC_DIR.mkdir(parents=True, exist_ok=True)


@chat_router.post("/")
async def chat(question: str = Form(...), files: List[UploadFile] = File(default=[])) -> dict[str, str]:
    pdf_files   : List[str] = []
    doc_files   : List[str] = []

    for file in files:
        if not file.filename: 
            raise HTTPException(status_code=400, detail="Uploaded file missing filename.")


        filename = file.filename
        suffix = Path(filename).suffix.lower()

        if suffix == ".pdf":
            path = PDF_DIR / filename
        elif suffix == ".docx":
            path = DOC_DIR / file.filename
        else:
            raise HTTPException(status_code=400, detail=f"{file.filename} is not supported.")


        with open(path, "wb") as f:
            f.write(await file.read())

        if suffix == ".pdf":
            pdf_files.append(str(path))
        else:
            doc_files.append(str(path))

    state : dict[str, str | list[str]] = { # type: ignore
        "question": question,
        "pdf_files": pdf_files,
        "doc_files": doc_files
    }

    # result = research_graph.invoke(state)

    return {
        # "answer": result["answer"]
    }