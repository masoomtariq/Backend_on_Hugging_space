import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException, Body
from typing import Annotated, Optional
from services.rag_service import generate_rag_response

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",
    "https://masoomtariq.github.io",
    "https://robotics-liart.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Textbook Chatbot Backend!"}

@app.post("/rag/chat", tags=["rag"])
def chat_endpoint(
    user_query: Annotated[str, Body(..., description="The user's query")],
    selected_text: Annotated[Optional[str], Body(description="Optional selected text from the document for context")] = None
):
    """
    Handles RAG chat queries.
    """
    try:
        response = generate_rag_response(user_query, selected_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
