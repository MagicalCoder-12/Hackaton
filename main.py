# main.py
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, HttpUrl
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import asyncio
import httpx

from perplexity_api import ask_perplexity # Import the service

app = FastAPI(title="HackRx LLM Query-Retrieval API",
              description="API for querying insurance/contract documents with LLM retrieval",
              version="0.1")

# but a constant is fine for this example.
TEAM_BEARER_TOKEN = os.getenv("TEAM_BEARER_TOKEN")
security = HTTPBearer()

class QueryRequest(BaseModel):
    documents: HttpUrl
    questions: List[str]

class QueryResponse(BaseModel):
    answers: List[str]

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Checks if the provided bearer token is valid."""
    if credentials.scheme.lower() != "bearer" or credentials.credentials != TEAM_BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid or missing authorization token")
    return True

@app.post("/hackrx/run", response_model=QueryResponse, summary="Run Query Retrieval")
async def run_query(request: QueryRequest, authorized: bool = Depends(verify_token)):
    """
    Submit a document URL and a list of questions to get structured answers
    based on the document's content.
    """
    document_text = ""
    # Download the document and extract plain text
    # Note: For PDFs or DOCX, you'd need a more robust library like PyPDF2 or python-docx
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.get(str(request.documents))
            resp.raise_for_status() # Check for download errors
            document_text = resp.text
    except httpx.RequestError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Failed to download document: {exc}")
    except Exception:
        # A catch-all for other potential errors
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred while processing the document.")

    # Define a helper function to call the perplexity service for one question
    async def query_one(question: str):
        return await ask_perplexity(question, context=document_text)

    # Run all the questions concurrently for speed
    answers = await asyncio.gather(*(query_one(q) for q in request.questions))

    return QueryResponse(answers=answers)
