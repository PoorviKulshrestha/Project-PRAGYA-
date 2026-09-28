import { QA_KNOWLEDGE_BASE, STUB_ANSWER } from './data/stubs.js'

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

/**
 * Find the closest matching offline answer from our indexed knowledge base.
 */
function getOfflineAnswer(question, topK = 3) {
  const qLower = question.toLowerCase()
  let bestItem = null
  let maxScore = -1

  for (const item of QA_KNOWLEDGE_BASE) {
    let score = 0
    for (const kw of item.keywords) {
      if (qLower.includes(kw)) score += 1
    }
    if (score > maxScore) {
      maxScore = score
      bestItem = item
    }
  }

  const selected = (bestItem && maxScore > 0) ? bestItem : STUB_ANSWER
  return {
    answer: selected.answer,
    sources: selected.sources.slice(0, topK),
    isLive: false,
    mode: 'offline_index',
  }
}

/**
 * Ask the RAG backend a question, with seamless offline fallback if backend is offline.
 * @param {string} question
 * @param {number} topK
 * @param {string} subsidiary
 * @returns {Promise<{answer: string, sources: Array<{doc,page,score,excerpt}>, isLive: boolean}>}
 */
export async function askQuestion(question, topK = 3, subsidiary = 'ALL') {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 4000)

    const res = await fetch(`${BASE_URL}/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question, top_k: topK, subsidiary }),
      signal: controller.signal,
    })
    clearTimeout(timer)

    if (res.ok) {
      const data = await res.json()
      return {
        answer: data.answer,
        sources: (data.sources || []).map(s => ({
          doc: s.document || s.doc,
          page: s.page,
          score: s.score,
          excerpt: s.excerpt,
        })),
        isLive: true,
      }
    }
  } catch {
    // Backend offline or timeout — gracefully proceed to instant verified index
  }

  // Realistic processing delay for demo realism
  await new Promise(r => setTimeout(r, 650))
  return getOfflineAnswer(question, topK)
}

export async function checkHealth() {
  try {
    const res = await fetch(`${BASE_URL}/health`, { signal: AbortSignal.timeout(1500) })
    return res.ok
  } catch {
    return false
  }
}
