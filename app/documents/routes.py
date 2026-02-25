# app/documents/routes.py

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.document import Document
from app.schemas import DocumentCreate, DocumentResponse
import shutil
import os
from PyPDF2 import PdfReader

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CREATE document (upload file or text)
@router.post("/", response_model=DocumentResponse)
def create_document(title: str, file: UploadFile = File(None), db: Session = Depends(get_db)):
    content = ""
    filename = None

    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as f:
            shutil.copyfileobj(file.file, f)
        # If PDF, extract text
        if filename.lower().endswith(".pdf"):
            reader = PdfReader(filepath)
            for page in reader.pages:
                content += page.extract_text() or ""
        else:  # assume text file
            content = open(filepath, "r", encoding="utf-8").read()
    else:
        raise HTTPException(status_code=400, detail="File is required")

    doc = Document(title=title, filename=filename, content=content)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

# READ all documents
@router.get("/", response_model=List[DocumentResponse])
def list_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    return docs

# READ one document
@router.get("/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

# UPDATE document
@router.put("/{doc_id}", response_model=DocumentResponse)
def update_document(doc_id: int, doc_in: DocumentCreate, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    doc.title = doc_in.title
    if doc_in.content:
        doc.content = doc_in.content
    db.commit()
    db.refresh(doc)
    return doc

# DELETE document
@router.delete("/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(doc)
    db.commit()
    return {"message": "Document deleted successfully"}