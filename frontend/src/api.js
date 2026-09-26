const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

/**
 * Ask the RAG backend a question.
 * @param {string} question
 * @param {number} topK
 * @param {string} subsidiary  e.g. "ALL" or "ECL"
 * @returns {Promise<{answer: string, sources: Array<{doc,page,score,excerpt}>}>}
 */
export async function askQuestion(question, topK = 3, subsidiary = 'ALL') {
  const res = await fetch(`${BASE_URL}/query`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, top_k: topK, subsidiary }),
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error(err.detail || `API error ${res.status}`)
  }
  const data = await res.json()
  // Normalise backend field "document" → "doc" for frontend compatibility
  return {
    answer: data.answer,
    sources: (data.sources || []).map(s => ({
      doc: s.document || s.doc,
      page: s.page,
      score: s.score,
      excerpt: s.excerpt,
    })),
  }
}

export async function checkHealth() {
  try {
    const res = await fetch(`${BASE_URL}/health`, { signal: AbortSignal.timeout(3000) })
    return res.ok
  } catch {
    return false
  }
}
