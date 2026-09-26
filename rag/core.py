"""
RAG core: retrieve relevant chunks and generate a cited answer via Gemini.
"""
import os
import numpy as np
import pickle
from typing import Optional

from google import genai
from google.genai import types as genai_types
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STORE_PATH = os.path.join(BASE_DIR, "data", "vectorstore.pkl")
MODEL_NAME = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-3.6-flash"

_embed_model: Optional[SentenceTransformer] = None
_store: Optional[dict] = None
_genai_client: Optional[genai.Client] = None


def _get_embed_model() -> SentenceTransformer:
    global _embed_model
    if _embed_model is None:
        _embed_model = SentenceTransformer(MODEL_NAME)
    return _embed_model


def _get_store() -> dict:
    global _store
    if _store is None:
        if not os.path.exists(STORE_PATH):
            raise FileNotFoundError(
                f"Vector store not found at {STORE_PATH}. "
                "Run: python -m ingestion.pipeline"
            )
        with open(STORE_PATH, "rb") as f:
            _store = pickle.load(f)
    return _store


def _get_genai_client() -> genai.Client:
    global _genai_client
    if _genai_client is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")
        _genai_client = genai.Client(api_key=api_key)
    return _genai_client


def cosine_similarity(query_vec: np.ndarray, corpus_vecs: np.ndarray) -> np.ndarray:
    """Both vectors should be L2-normalised; dot product equals cosine similarity."""
    return corpus_vecs @ query_vec


def retrieve(question: str, top_k: int = 5, subsidiary: str = "ALL") -> list[dict]:
    """Return top_k most relevant chunks for the question."""
    store = _get_store()
    model = _get_embed_model()

    q_vec = model.encode([question], normalize_embeddings=True)[0].astype(np.float32)
    scores = cosine_similarity(q_vec, store["embeddings"])

    # Filter by subsidiary if needed
    if subsidiary and subsidiary != "ALL":
        mask = np.array([
            subsidiary.upper() in m["document"].upper()
            for m in store["meta"]
        ])
        scores = np.where(mask, scores, -1.0)

    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        if scores[idx] < 0.0:
            continue
        meta = store["meta"][idx]
        results.append({
            "document": meta["document"],
            "page": meta["page"],
            "score": float(scores[idx]),
            "excerpt": meta["excerpt"],
            "text": store["texts"][idx],
        })
    return results


def answer_question(question: str, top_k: int = 5, subsidiary: str = "ALL") -> dict:
    """
    Retrieve relevant chunks and generate a cited answer via Gemini.
    Returns: {answer: str, sources: list[{document, page, score, excerpt}]}
    """
    client = _get_genai_client()
    chunks = retrieve(question, top_k=top_k, subsidiary=subsidiary)

    if not chunks:
        return {
            "answer": "No relevant information found in the indexed documents for this question.",
            "sources": [],
        }

    context_parts = []
    for i, c in enumerate(chunks, 1):
        context_parts.append(
            f"[SOURCE {i}] Document: {c['document']}, Page {c['page']}\n{c['text']}"
        )
    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are an expert assistant for CMPDI/CIL (Coal India Limited) geological and mining reports.
Answer the question below using ONLY the provided source excerpts.
Be specific and include numbers, dates, and figures where available.
At the end of your answer, explicitly state which source(s) you relied on.

QUESTION: {question}

SOURCES:
{context}

ANSWER (be concise, factual, and cite sources inline as [SOURCE 1], [SOURCE 2], etc.):"""

    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
    answer_text = response.text.strip()

    return {
        "answer": answer_text,
        "sources": [
            {
                "document": c["document"],
                "page": c["page"],
                "score": round(c["score"], 4),
                "excerpt": c["excerpt"][:300],
            }
            for c in chunks
        ],
    }


if __name__ == "__main__":
    # Quick test — run with: python -m rag.core
    test_questions = [
        "What are the total coal reserves in the Eastern Coalfields?",
        "What is the average seam thickness in the Jharia block?",
        "How did Q3 FY2024 production compare to target?",
    ]
    for q in test_questions:
        print(f"\nQ: {q}")
        result = answer_question(q, top_k=3)
        print(f"A: {result['answer'][:500]}")
        print("Sources:")
        for s in result["sources"]:
            print(f"  - {s['document']} p.{s['page']} (score {s['score']})")
        print("-" * 60)
