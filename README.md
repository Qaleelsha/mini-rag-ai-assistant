# Mini RAG AI Knowledge Assistant

**Version:** 0.1.0  
**Tech Stack:** FastAPI | PostgreSQL | SQLAlchemy | FAISS | JWT Authentication  

---

## Project Overview

The Mini RAG AI Knowledge Assistant is a backend-only application that allows users to:

- **Register and Login** securely using JWT authentication.
- **Upload, manage, and query documents** (text or PDF).
- **Retrieve answers using a simple RAG (Retrieval-Augmented Generation) pipeline** with FAISS embeddings.
- **Interact with the API via Swagger UI** for easy testing and exploration.

This project demonstrates a **full backend workflow** from user authentication to document-based AI retrieval, making it ideal for academic submissions, interviews, and portfolio showcases.

---

## Features

### 1. User Management
- **Registration:** `/auth/register` — create a new user with email and password (hashed securely using bcrypt).  
- **Login:** `/auth/login` — authenticate and receive a JWT token for accessing protected endpoints.  
- Passwords are securely hashed and JWT tokens are used for session management.

### 2. Document Management (CRUD)
- **Upload Documents:** `/documents/` — upload text or PDF files with a title.  
- **List Documents:** `/documents/` — view all uploaded documents.  
- JWT token required for all document operations.  
- Backend stores metadata in PostgreSQL and embeddings in FAISS for RAG queries.

### 3. Retrieval-Augmented Generation (RAG)
- Generates vector embeddings for uploaded documents.
- Query endpoint `/ask/` retrieves the most relevant content based on user input using FAISS.

### 4. API Documentation
- Swagger UI is available at `/docs` for testing all endpoints.  
- Supports JSON requests/responses and file uploads.

---

## Project Structure

```text
RAG-Assistant/
├─ app/
│  ├─ __init__.py
│  ├─ main.py           # FastAPI app and routes
│  ├─ config.py         # Database & environment configuration
│  ├─ database.py       # SQLAlchemy database connection
│  ├─ models.py         # User & Document models
│  ├─ auth/             # Authentication logic
│  │  ├─ routes.py
│  │  ├─ security.py
│  │  └─ schemas.py
│  └─ documents/        # Document upload & RAG logic
│     ├─ routes.py
│     ├─ schemas.py
│     └─ utils.py
├─ venv/                # Python virtual environment
├─ requirements.txt     # Python dependencies
└─ README.md
