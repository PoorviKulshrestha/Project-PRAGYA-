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

  const [copied,    setCopied]    = useState(false)

  const handleCopyText = (text) => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2200)
    })
  }

  const handleDownloadParlDocx = () => {
    if (!result) return
    const qNo = parlQNo || 'Starred Q. 47'
    const house = parlHouse || 'Lok Sabha'
    const sess = parlSess || 'Budget Session 2024'
    const htmlContent = `
      <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
      <head><meta charset='utf-8'><title>Parliamentary Reply - ${qNo}</title>
      <style>
        body { font-family: 'Calibri', 'Segoe UI', Arial, sans-serif; font-size: 11pt; color: #111; line-height: 1.5; padding: 24px; }
        h2 { text-align: center; color: #116871; margin-bottom: 4px; text-transform: uppercase; font-size: 14pt; }
        h3 { text-align: center; color: #555; margin-top: 0; font-size: 12pt; border-bottom: 2px solid #116871; padding-bottom: 8px; }
        .meta-table { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 20px; }
        .meta-table td { padding: 8px 12px; border: 1px solid #c4dfe1; font-size: 10pt; background: #fafefe; }
        .reply-body { margin-top: 18px; margin-bottom: 22px; font-size: 11pt; line-height: 1.7; background: #ffffff; padding: 15px; border: 1px solid #e0ecec; }
        .sources-box { background: #f0f7f7; border-left: 4px solid #116871; padding: 12px 16px; margin-top: 20px; font-size: 9.5pt; color: #333; }
        .footer { margin-top: 30px; font-size: 8.5pt; color: #666; border-top: 1px solid #ccc; padding-top: 8px; font-style: italic; }
      </style>
      </head>
      <body>
        <h2>Government of India &middot; Ministry of Coal</h2>
        <h3>${house.toUpperCase()} &mdash; PARLIAMENTARY QUESTION REPLY</h3>
        <table class="meta-table">
          <tr><td><strong>Question Number:</strong> ${qNo}</td><td><strong>House / Session:</strong> ${house} (${sess})</td></tr>
          <tr><td><strong>Ministry:</strong> ${parlMin}</td><td><strong>Date Generated:</strong> ${new Date().toLocaleDateString('en-IN', { day: '2-digit', month: 'long', year: 'numeric' })}</td></tr>
          <tr><td colspan="2"><strong>Subject:</strong> ${question || 'Coal Reserves, Production & Geological Status in Eastern Coalfields'}</td></tr>
        </table>
        <h4>REPLY ON BEHALF OF THE MINISTER OF COAL:</h4>
        <div class="reply-body">${result.answer.replace(/\n/g, '<br/>')}</div>
        <div class="sources-box">
          <strong>Mandatory Source Traceability (CMPDI / CIL Archives):</strong><br/>
          ${result.sources.map((s, i) => `[${i+1}] <strong>${s.doc}</strong> &mdash; Page ${s.page} (Relevance: ${Math.round(s.score * 100)}%)<br/><em>"${s.excerpt}"</em>`).join('<br/><br/>')}
        </div>
        <div class="footer">
          Generated automatically by PRAGYA MineInsight AI (Smart India Hackathon 2024 &middot; Ministry of Coal).<br/>
          This draft must be reviewed and countersigned by the designated Nodal Officer prior to submission to Parliament.
        </div>
      </body>
      </html>
    `
    const blob = new Blob([htmlContent], { type: 'application/msword' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `Parliamentary_Reply_${qNo.replace(/[^a-zA-Z0-9]/g, '_')}.doc`
    a.click()
    URL.revokeObjectURL(url)
  }

  const handleAsk = async () => {
    if (!question.trim()) return
    setLoading(true)
    setResult(null)
    setError(null)
    try {
      const data = await askQuestion(question.trim(), topK, filterSub)
      setResult({ ...data, mode })
    } catch (err) {
      setError(err.message || 'Failed to get answer.')
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
                <button className="btn btn-primary btn-sm" onClick={handleDownloadParlDocx}>
                  ⬇ Download as .docx (Official Format)
                </button>
                <button className="btn btn-outline btn-sm" onClick={() => handleCopyText(result.answer)}>
                  {copied ? '✓ Copied to Clipboard!' : '⊟ Copy Reply to Clipboard'}
                </button>
              </div>
            </>
          ) : (
            <>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 16 }}>
                <div className="section-title" style={{ margin: 0 }}>Answer</div>
                <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                  <span className={`badge ${result.isLive ? 'badge-success' : 'badge-primary'}`}>
                    {result.isLive ? '⚡ Live Gemini RAG' : '✓ Verified RAG Index'}
                  </span>
                  <button className="btn btn-outline btn-sm" onClick={() => handleCopyText(result.answer)}>
                    {copied ? '✓ Copied' : '⊟ Copy'}
                  </button>
                </div>
              </div>
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
