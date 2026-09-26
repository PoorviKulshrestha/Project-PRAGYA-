"""
FastAPI backend for CMPDI MineInsight AI — RAG Query endpoint.
Start with: uvicorn backend:app --reload --port 8000
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

from rag.core import answer_question

app = FastAPI(
    title="CMPDI MineInsight AI",
    description="RAG-powered geological and mining document query system",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=2000)
    top_k: int = Field(default=3, ge=1, le=10)
    subsidiary: Optional[str] = Field(default="ALL")


class Source(BaseModel):
    document: str
    page: int
    score: float
    excerpt: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]


@app.get("/health")
def health():
    return {"status": "ok", "service": "CMPDI MineInsight AI"}


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    try:
        result = answer_question(
            question=req.question,
            top_k=req.top_k,
            subsidiary=req.subsidiary or "ALL",
        )
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except EnvironmentError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
