from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mini RAG AI Assistant")

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import your routes
from app.auth import routes as auth_routes
from app.documents import routes as doc_routes

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(doc_routes.router, prefix="/documents")

@app.get("/")
async def root():
    return {"message": "Mini RAG AI Assistant Backend Running"}