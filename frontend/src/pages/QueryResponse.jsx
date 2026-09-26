import { useState } from 'react'
import { SAMPLE_QUESTIONS, SUBSIDIARIES } from '../data/stubs.js'
import { askQuestion } from '../api.js'

/** Render **bold**, *italic*, and newlines from Gemini markdown output */
function MarkdownText({ text }) {
  const lines = text.split('\n')
  return (
    <div>
      {lines.map((line, i) => {
        const parts = line.split(/(\*\*[^*]+\*\*|\*[^*]+\*)/g)
        return (
          <div key={i} style={{ marginBottom: line.trim() ? 2 : 6 }}>
            {parts.map((part, j) => {
              if (part.startsWith('**') && part.endsWith('**'))
                return <strong key={j}>{part.slice(2, -2)}</strong>
              if (part.startsWith('*') && part.endsWith('*'))
                return <em key={j}>{part.slice(1, -1)}</em>
              return <span key={j}>{part}</span>
            })}
          </div>
        )
      })}
    </div>
  )
}

const scoreClass = s => s >= 0.70 ? 'high' : s >= 0.50 ? 'medium' : 'low'
const scoreLabel = s => `${Math.round(s * 100)}% relevance`

export default function QueryResponse() {
  const [mode,      setMode]      = useState('general')
  const [question,  setQuestion]  = useState('')
  const [topK,      setTopK]      = useState(3)
  const [filterSub, setFilterSub] = useState('ALL')
  const [loading,   setLoading]   = useState(false)
  const [result,    setResult]    = useState(null)
  const [error,     setError]     = useState(null)

  // Parliamentary form fields
  const [parlQNo,    setParlQNo]    = useState('')
  const [parlHouse,  setParlHouse]  = useState('Lok Sabha')
  const [parlSess,   setParlSess]   = useState('')
  const [parlMin,    setParlMin]    = useState('Ministry of Coal')

  const handleAsk = async () => {
    if (!question.trim()) return
    setLoading(true)
    setResult(null)
    setError(null)
    try {
      const data = await askQuestion(question.trim(), topK, filterSub)
      setResult({ ...data, mode })
    } catch (err) {
      setError(err.message || 'Failed to get answer. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) handleAsk()
  }

  return (
    <div>
      <div className="page-title">AI Query &amp; Response System</div>
      <div className="page-subtitle">
        Ask any question about the indexed geological and mining documents.
        The system retrieves the most relevant chunks and generates a cited answer via Gemini AI.
        All answers include source document and page citations.
      </div>

      {/* Mode selector */}
      <div className="section-title">Query Mode</div>
      <div className="btn-group" style={{ marginBottom: 20 }}>
        <button
          className={`btn ${mode === 'general' ? 'btn-primary' : 'btn-outline'}`}
          onClick={() => setMode('general')}
        >
          ◎ General Query
        </button>
        <button
          className={`btn ${mode === 'parliamentary' ? 'btn-primary' : 'btn-outline'}`}
          onClick={() => setMode('parliamentary')}
        >
          ⊟ Parliamentary / Administrative Inquiry
        </button>
      </div>

      {mode === 'parliamentary' && (
        <>
          <div className="alert alert-parl">
            <span>⚠</span>
            <div>
              <strong>Parliamentary Mode —</strong> The response will be formatted as an official
              Ministry of Coal parliamentary reply. All claims include source document and page citations.
            </div>
          </div>
          <div className="form-section">
            <div className="form-section-title">Parliamentary Question Details</div>
            <div className="form-row">
              <div className="form-group">
                <label className="form-label">Question Number</label>
                <input className="form-input" placeholder="e.g. Starred Q. 47"
                  value={parlQNo} onChange={e => setParlQNo(e.target.value)} />
              </div>
              <div className="form-group">
                <label className="form-label">House</label>
                <select className="form-select" value={parlHouse} onChange={e => setParlHouse(e.target.value)}>
                  <option>Lok Sabha</option>
                  <option>Rajya Sabha</option>
                </select>
              </div>
            </div>
            <div className="form-row">
              <div className="form-group">
                <label className="form-label">Session</label>
                <input className="form-input" placeholder="e.g. Budget Session 2024"
                  value={parlSess} onChange={e => setParlSess(e.target.value)} />
              </div>
              <div className="form-group">
                <label className="form-label">Ministry</label>
                <input className="form-input"
                  value={parlMin} onChange={e => setParlMin(e.target.value)} />
              </div>
            </div>
          </div>
        </>
      )}

      {/* Query input */}
      <div className="grid-2" style={{ alignItems: 'start' }}>
        <div>
          <div className="section-title">Your Question</div>
          <div className="form-group">
            <textarea
              className="form-textarea"
              style={{ minHeight: 110 }}
              placeholder={
                mode === 'parliamentary'
                  ? 'Enter the subject or question to address…'
                  : 'e.g. What are the total coal reserves in the Eastern Coalfields?\ne.g. What is the LTIFR safety statistic for NCL in FY2024?'
              }
              value={question}
              onChange={e => setQuestion(e.target.value)}
              onKeyDown={handleKeyDown}
            />
            <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginTop: 4 }}>
              Press Ctrl+Enter to submit
            </div>
          </div>

          <div className="form-row" style={{ marginBottom: 14 }}>
            <div className="form-group">
              <label className="form-label">Top-K Chunks</label>
              <select className="form-select" value={topK} onChange={e => setTopK(+e.target.value)}>
                {[1,2,3,5,8,10].map(k => <option key={k} value={k}>{k} chunks</option>)}
              </select>
            </div>
            <div className="form-group">
              <label className="form-label">Filter by Subsidiary</label>
              <select className="form-select" value={filterSub} onChange={e => setFilterSub(e.target.value)}>
                {SUBSIDIARIES.map(s => <option key={s.code} value={s.code}>{s.name}</option>)}
              </select>
            </div>
          </div>

          <div className="btn-group">
            <button className="btn btn-primary" onClick={handleAsk} disabled={loading || !question.trim()}>
              {loading ? '⟳  Generating answer…' : '◎  Ask'}
            </button>
            <button className="btn btn-outline" onClick={() => { setQuestion(''); setResult(null); setError(null) }}>
              Clear
            </button>
          </div>
        </div>

        {/* Sample questions */}
        <div>
          <div className="section-title">Sample Questions — click to load</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {SAMPLE_QUESTIONS.slice(0, 6).map(q => (
              <button key={q} className="btn btn-outline btn-sm"
                style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                onClick={() => { setQuestion(q); setResult(null); setError(null) }}>
                {q}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Loading state */}
      {loading && (
        <div className="alert alert-info" style={{ marginTop: 24, display: 'flex', alignItems: 'center', gap: 12 }}>
          <div className="spinner" />
          <span>Retrieving relevant document chunks and generating answer via Gemini AI…</span>
        </div>
      )}

      {/* Error state */}
      {error && (
        <div className="alert alert-warning" style={{ marginTop: 24 }}>
          <span>⚠</span>
          <div><strong>Error:</strong> {error}</div>
        </div>
      )}

      {/* Result */}
      {result && !loading && (
        <>
          <hr className="section-divider" />

          {result.mode === 'parliamentary' ? (
            <>
              <div className="section-title">Official Parliamentary Reply — Draft</div>
              <div className="alert alert-warning" style={{ marginBottom: 12 }}>
                <span>⚠</span>
                AI-generated draft. Must be reviewed and approved by the authorised officer before submission.
              </div>
              <div className="parl-card">
                <h4>MINISTRY OF COAL — PARLIAMENTARY QUESTION RESPONSE</h4>
                <div style={{ marginBottom: 12, fontWeight: 500 }}>
                  {parlQNo && <div>Question No.: {parlQNo} ({parlHouse}{parlSess ? ` — ${parlSess}` : ''})</div>}
                  <div>Ministry: {parlMin}</div>
                </div>
                <MarkdownText text={result.answer} />
                <div style={{ marginTop: 16, paddingTop: 12, borderTop: '1px solid var(--border)', fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  Sources:{' '}
                  {result.sources.map((s, i) => (
                    <span key={i}>[{i+1}] {s.doc} p.{s.page}{i < result.sources.length-1 ? '  |  ' : ''}</span>
                  ))}
                  <br />
                  This response has been automatically drafted for review by the authorised officer before submission.
                </div>
              </div>
              <div className="btn-group" style={{ marginTop: 14 }}>
                <button className="btn btn-outline">⬇ Download as .docx (Draft)</button>
                <button className="btn btn-outline">⊟ Copy to Clipboard</button>
              </div>
            </>
          ) : (
            <>
              <div className="section-title">Answer</div>
              <div className="answer-card"><MarkdownText text={result.answer} /></div>
            </>
          )}

          <div className="section-title" style={{ marginTop: 24 }}>
            Source Citations &nbsp;
            <span className="badge badge-primary">{result.sources.length} chunks retrieved</span>
          </div>
          {result.sources.map((src, i) => (
            <div key={i} className="citation">
              <div className="citation-header">
                <span>[{i + 1}] {src.doc} — Page {src.page}</span>
                <span className={`citation-score ${scoreClass(src.score)}`}>
                  ▲ {scoreLabel(src.score)}
                </span>
              </div>
              <div className="citation-excerpt">"{src.excerpt}"</div>
            </div>
          ))}
        </>
      )}

      {!result && !loading && !error && (
        <div className="alert alert-info" style={{ marginTop: 24 }}>
          <span>ℹ</span>
          Select a sample question or type your own, then click Ask.
        </div>
      )}
    </div>
  )
}
