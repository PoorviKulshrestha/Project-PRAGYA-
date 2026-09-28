import { useState, useRef } from 'react'
import { SUBSIDIARY_TOPICS, STUB_KEYWORDS } from '../data/stubs.js'

const TREND_DATA = [
  { year: 2019, 'Coal Reserve Estimation': 72, 'Environmental Compliance': 48, 'Safety & DGMS': 42, 'Production Targets': 65 },
  { year: 2020, 'Coal Reserve Estimation': 74, 'Environmental Compliance': 55, 'Safety & DGMS': 50, 'Production Targets': 68 },
  { year: 2021, 'Coal Reserve Estimation': 78, 'Environmental Compliance': 61, 'Safety & DGMS': 55, 'Production Targets': 70 },
  { year: 2022, 'Coal Reserve Estimation': 82, 'Environmental Compliance': 68, 'Safety & DGMS': 58, 'Production Targets': 74 },
  { year: 2023, 'Coal Reserve Estimation': 85, 'Environmental Compliance': 73, 'Safety & DGMS': 61, 'Production Targets': 76 },
  { year: 2024, 'Coal Reserve Estimation': 89, 'Environmental Compliance': 78, 'Safety & DGMS': 65, 'Production Targets': 76 },
]
const TREND_KEYS = ['Coal Reserve Estimation', 'Environmental Compliance', 'Safety & DGMS', 'Production Targets']
const TREND_COLORS = ['#116871', '#F5A08D', '#24777F', '#7cb8bb']

// Dynamic corpus vocabulary with relative sizing and coordinates for SVG word cloud
const CORPUS_WORDS = [
  { text: 'COAL RESERVES', x: 250, y: 155, size: 34, color: '#116871', weight: 800, tfidf: 0.94, freq: 412 },
  { text: 'Jharia Coalfield', x: 120, y: 90, size: 26, color: '#24777F', weight: 700, tfidf: 0.91, freq: 358 },
  { text: 'Overburden (OBR)', x: 380, y: 95, size: 24, color: '#E06D53', weight: 700, tfidf: 0.88, freq: 320 },
  { text: 'Seam Thickness', x: 230, y: 215, size: 25, color: '#116871', weight: 700, tfidf: 0.85, freq: 284 },
  { text: 'Longwall Mining', x: 90, y: 200, size: 21, color: '#0d9488', weight: 600, tfidf: 0.83, freq: 265 },
  { text: 'Borehole Drilling', x: 390, y: 210, size: 22, color: '#d97706', weight: 600, tfidf: 0.80, freq: 241 },
  { text: 'Prime Coking Coal', x: 250, y: 65, size: 20, color: '#b45309', weight: 700, tfidf: 0.79, freq: 230 },
  { text: 'DGMS Safety', x: 95, y: 140, size: 19, color: '#2e7d32', weight: 600, tfidf: 0.77, freq: 215 },
  { text: 'Raniganj Basin', x: 410, y: 150, size: 21, color: '#0f766e', weight: 600, tfidf: 0.74, freq: 198 },
  { text: 'Methane Drainage', x: 260, y: 260, size: 18, color: '#c2410c', weight: 600, tfidf: 0.72, freq: 185 },
  { text: 'Stratigraphy', x: 100, y: 255, size: 17, color: '#1e40af', weight: 600, tfidf: 0.70, freq: 172 },
  { text: 'Calorific Value', x: 400, y: 255, size: 17, color: '#0369a1', weight: 500, tfidf: 0.68, freq: 164 },
  { text: 'Barakar Formation', x: 250, y: 110, size: 18, color: '#047857', weight: 600, tfidf: 0.65, freq: 153 },
  { text: 'Opencast Dragline', x: 90, y: 45, size: 16, color: '#9333ea', weight: 500, tfidf: 0.61, freq: 138 },
  { text: 'MoEFCC Clearance', x: 395, y: 45, size: 16, color: '#15803d', weight: 500, tfidf: 0.58, freq: 124 },
  { text: 'Core Recovery 91%', x: 250, y: 290, size: 15, color: '#475569', weight: 500, tfidf: 0.54, freq: 110 },
  { text: 'Rajmahal OCP', x: 60, y: 105, size: 14, color: '#0284c7', weight: 500, tfidf: 0.52, freq: 98 },
  { text: 'Aquifer Protection', x: 440, y: 115, size: 14, color: '#0891b2', weight: 500, tfidf: 0.49, freq: 87 },
  { text: 'Subsidence Control', x: 75, y: 170, size: 13, color: '#64748b', weight: 500, tfidf: 0.47, freq: 82 },
  { text: 'Firedamp Sensor', x: 430, y: 180, size: 13, color: '#dc2626', weight: 500, tfidf: 0.45, freq: 76 },
]

export default function WordCloud() {
  const [ready,     setReady]     = useState(true)
  const [loading,   setLoading]   = useState(false)
  const [nTopics,   setNTopics]   = useState(8)
  const [algo,      setAlgo]      = useState('TF-IDF')
  const [scope,     setScope]     = useState('Full Corpus')
  const [scopeSub,  setScopeSub]  = useState('ECL')
  const [hoverWord, setHoverWord] = useState(null)
  const svgRef = useRef(null)

  const activeTopics = (scope === 'By Subsidiary' && SUBSIDIARY_TOPICS[scopeSub])
    ? SUBSIDIARY_TOPICS[scopeSub]
    : SUBSIDIARY_TOPICS['Full Corpus']

  const handleGenerate = () => {
    setLoading(true); setReady(false)
    setTimeout(() => { setLoading(false); setReady(true) }, 900)
  }

  const handleDownloadSvg = () => {
    if (!svgRef.current) return
    const serializer = new XMLSerializer()
    const svgStr = serializer.serializeToString(svgRef.current)
    const blob = new Blob([svgStr], { type: 'image/svg+xml;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `PRAGYA_WordCloud_${scope.replace(/\s+/g, '_')}.svg`
    a.click()
    URL.revokeObjectURL(url)
  }

  const handleDownloadPng = () => {
    if (!svgRef.current) return
    const serializer = new XMLSerializer()
    const svgStr = serializer.serializeToString(svgRef.current)
    const img = new Image()
    const svgBlob = new Blob([svgStr], { type: 'image/svg+xml;charset=utf-8' })
    const url = URL.createObjectURL(svgBlob)

    img.onload = () => {
      const canvas = document.createElement('canvas')
      canvas.width = 1060
      canvas.height = 640
      const ctx = canvas.getContext('2d')
      ctx.fillStyle = '#f8fdfd'
      ctx.fillRect(0, 0, canvas.width, canvas.height)
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
      URL.revokeObjectURL(url)

      const pngUrl = canvas.toDataURL('image/png')
      const a = document.createElement('a')
      a.href = pngUrl
      a.download = `PRAGYA_WordCloud_${scope.replace(/\s+/g, '_')}.png`
      a.click()
    }
    img.src = url
  }

  return (
    <div>
      <div className="page-title">Word Cloud &amp; Topic Identification Module</div>
      <div className="page-subtitle">
        Automatically identifies dominant themes, stratigraphy markers, and operational terminology
        across all indexed CMPDI/CIL mining documents using NLP keyword extraction and topic modeling.
      </div>

      {/* Controls */}
      <div className="form-section">
        <div className="form-section-title">Analysis Configuration</div>
        <div className="form-row-4" style={{ alignItems: 'flex-end' }}>
          <div className="form-group">
            <label className="form-label">Algorithm</label>
            <select className="form-select" value={algo} onChange={e => setAlgo(e.target.value)}>
              <option value="TF-IDF">TF-IDF (fast · local · high-precision)</option>
              <option value="BERTopic">BERTopic (sentence-transformers · semantic)</option>
            </select>
            <div className="form-hint">{algo === 'TF-IDF' ? 'Recommended for instant production analysis' : 'Contextual clustering across embeddings'}</div>
          </div>
          <div className="form-group">
            <label className="form-label">Number of Topics</label>
            <input className="form-input" type="number" min={3} max={12}
              value={nTopics} onChange={e => setNTopics(+e.target.value)} />
          </div>
          <div className="form-group">
            <label className="form-label">Analysis Scope</label>
            <select className="form-select" value={scope} onChange={e => setScope(e.target.value)}>
              <option>Full Corpus</option>
              <option>By Subsidiary</option>
              <option>By Document Type</option>
              <option>By Year Range</option>
            </select>
          </div>
          {scope === 'By Subsidiary' && (
            <div className="form-group">
              <label className="form-label">Subsidiary</label>
              <select className="form-select" value={scopeSub} onChange={e => setScopeSub(e.target.value)}>
                {['ECL','BCCL','CCL','NCL','SECL','WCL','MCL','HQ'].map(s =>
                  <option key={s}>{s}</option>)}
              </select>
            </div>
          )}
        </div>
        <button className="btn btn-primary" onClick={handleGenerate} disabled={loading}>
          {loading ? '⟳ Analysing corpus…' : '☁ Generate Word Cloud & Topics'}
        </button>
      </div>

      {loading && (
        <div style={{ marginBottom: 14 }}>
          <div style={{ fontSize: '0.78rem', color: 'var(--primary)', marginBottom: 6 }}>
            Running {algo} extraction across indexed corpus…
          </div>
          <div className="progress-bar-wrap">
            <div className="progress-bar-fill" style={{ width: '85%' }} />
          </div>
        </div>
      )}

      {ready && (
        <>
          <hr className="section-divider" />

          {/* Word cloud + topics side by side */}
          <div className="grid-2" style={{ marginBottom: 24 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                <div className="section-title" style={{ margin: 0 }}>
                  Interactive Word Cloud &nbsp;
                  <span className="badge badge-primary">{scope === 'By Subsidiary' ? scopeSub : 'All Subsidiaries'}</span>
                </div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                  Hover word for TF-IDF metrics
                </div>
              </div>

              {/* Rendered SVG Word Cloud Box */}
              <div style={{
                background: 'linear-gradient(145deg, #f7fdfd 0%, #eaf5f6 100%)',
                borderRadius: 10,
                border: '1px solid var(--border)',
                boxShadow: 'var(--shadow-sm)',
                overflow: 'hidden',
                position: 'relative',
              }}>
                <svg
                  ref={svgRef}
                  viewBox="0 0 530 320"
                  style={{ width: '100%', height: 320, display: 'block', cursor: 'pointer' }}
                >
                  {/* Subtle background grid pattern */}
                  <defs>
                    <radialGradient id="wcGlow" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stopColor="#ffffff" stopOpacity="0.8" />
                      <stop offset="100%" stopColor="#eef8f8" stopOpacity="0.2" />
                    </radialGradient>
                  </defs>
                  <rect width="530" height="320" fill="url(#wcGlow)" />

                  {/* Render words */}
                  {CORPUS_WORDS.map((w, i) => {
                    const isHovered = hoverWord?.text === w.text
                    return (
                      <g
                        key={i}
                        onMouseEnter={() => setHoverWord(w)}
                        onMouseLeave={() => setHoverWord(null)}
                        style={{ transition: 'transform 0.15s ease' }}
                      >
                        <text
                          x={w.x}
                          y={w.y}
                          textAnchor="middle"
                          fill={isHovered ? '#e05333' : w.color}
                          fontSize={isHovered ? w.size + 3 : w.size}
                          fontWeight={w.weight}
                          letterSpacing="0.02em"
                          style={{
                            fontFamily: 'Inter, Segoe UI, sans-serif',
                            userSelect: 'none',
                            transition: 'all 0.15s ease',
                          }}
                        >
                          {w.text}
                        </text>
                      </g>
                    )
                  })}
                </svg>

                {/* Word Tooltip Indicator */}
                {hoverWord ? (
                  <div style={{
                    position: 'absolute', bottom: 10, left: 14, right: 14,
                    background: 'rgba(17, 104, 113, 0.95)', color: '#fff',
                    borderRadius: 6, padding: '6px 12px', fontSize: '0.76rem',
                    display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                    backdropFilter: 'blur(4px)',
                  }}>
                    <span><strong>{hoverWord.text}</strong></span>
                    <span>TF-IDF Score: <strong>{hoverWord.tfidf}</strong></span>
                    <span>Corpus Mentions: <strong>{hoverWord.freq}</strong></span>
                  </div>
                ) : (
                  <div style={{
                    position: 'absolute', bottom: 8, right: 12,
                    fontSize: '0.70rem', color: 'var(--text-muted)',
                  }}>
                    Interactive NLP Visualisation
                  </div>
                )}
              </div>

              <div style={{ display: 'flex', gap: 10, marginTop: 12 }}>
                <button className="btn btn-outline btn-sm" onClick={handleDownloadPng}>⬇ Download PNG</button>
                <button className="btn btn-outline btn-sm" onClick={handleDownloadSvg}>⬇ Download SVG</button>
              </div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginTop: 8 }}>
                Corpus Scope: 8 CMPDI documents · 2,400 chunks · Mining stopwords &amp; non-geological terms filtered.
              </div>
            </div>

            <div>
              <div className="section-title">
                Identified Topics &nbsp;
                <span className="badge badge-primary">{algo}</span>
              </div>
              {activeTopics.slice(0, nTopics).map((t, i) => (
                <div key={i} className="topic-item">
                  <div className="topic-label">
                    <span>#{i + 1} {t.label}</span>
                    <span className="topic-pct">{Math.round(t.weight * 100)}%</span>
                  </div>
                  <div className="progress-bar-wrap">
                    <div className="progress-bar-fill" style={{ width: `${Math.round(t.weight * 100)}%` }} />
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Keywords */}
          <div className="section-title">Dominant Mining Terminology (TF-IDF Corpus-wide)</div>
          <div className="kw-cloud" style={{ marginBottom: 24 }}>
            {STUB_KEYWORDS.map((kw, i) => (
              <span key={i} className="kw-tag">⋅ {kw}</span>
            ))}
          </div>

          <hr className="section-divider" />

          {/* Topic table */}
          <div className="section-title">Topic Classification Breakdown</div>
          <div className="table-wrap" style={{ marginBottom: 24 }}>
            <table>
              <thead>
                <tr><th>#</th><th>Topic Label</th><th>Relevance Weight</th><th>Representative Keywords</th></tr>
              </thead>
              <tbody>
                {activeTopics.slice(0, nTopics).map((t, i) => (
                  <tr key={i}>
                    <td>{i + 1}</td>
                    <td><strong>{t.label}</strong></td>
                    <td>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <div className="progress-bar-wrap" style={{ width: 80 }}>
                          <div className="progress-bar-fill" style={{ width: `${Math.round(t.weight * 100)}%` }} />
                        </div>
                        <span style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 600 }}>
                          {Math.round(t.weight * 100)}%
                        </span>
                      </div>
                    </td>
                    <td style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                      {STUB_KEYWORDS.slice(i * 3, i * 3 + 4).join(', ')}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Historical trend — simple SVG line chart */}
          <div className="section-title">Historical Topic Trend (2019 – 2024)</div>
          <div className="card" style={{ padding: '20px 24px' }}>
            <div style={{ display: 'flex', gap: 16, marginBottom: 12, flexWrap: 'wrap' }}>
              {TREND_KEYS.map((k, i) => (
                <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 5, fontSize: '0.72rem' }}>
                  <div style={{ width: 12, height: 3, background: TREND_COLORS[i], borderRadius: 2 }} />
                  {k}
                </div>
              ))}
            </div>
            <svg viewBox="0 0 600 200" style={{ width: '100%', height: 200 }}>
              {/* Y grid */}
              {[0,25,50,75,100].map(v => (
                <g key={v}>
                  <line x1="40" x2="590" y1={180 - v * 1.6} y2={180 - v * 1.6}
                    stroke="#e0ecec" strokeWidth="1" />
                  <text x="35" y={184 - v * 1.6} textAnchor="end"
                    fontSize="9" fill="var(--text-muted)">{v}</text>
                </g>
              ))}
              {/* Lines per key */}
              {TREND_KEYS.map((key, ki) => {
                const pts = TREND_DATA.map((d, di) => {
                  const x = 50 + di * ((540) / (TREND_DATA.length - 1))
                  const y = 180 - d[key] * 1.6
                  return `${x},${y}`
                }).join(' ')
                return (
                  <g key={key}>
                    <polyline fill="none" stroke={TREND_COLORS[ki]} strokeWidth="2"
                      points={pts} strokeLinejoin="round" />
                    {TREND_DATA.map((d, di) => {
                      const x = 50 + di * ((540) / (TREND_DATA.length - 1))
                      const y = 180 - d[key] * 1.6
                      return <circle key={di} cx={x} cy={y} r="3" fill={TREND_COLORS[ki]} />
                    })}
                  </g>
                )
              })}
              {/* X axis labels */}
              {TREND_DATA.map((d, di) => {
                const x = 50 + di * ((540) / (TREND_DATA.length - 1))
                return <text key={d.year} x={x} y="196" textAnchor="middle"
                  fontSize="9" fill="var(--text-muted)">{d.year}</text>
              })}
            </svg>
          </div>
        </>
      )}

      {!ready && !loading && (
        <div className="alert alert-info" style={{ marginTop: 16 }}>
          <span>ℹ</span>
          Configure the analysis settings above and click &quot;Generate&quot; to run topic identification.
        </div>
      )}
    </div>
  )
}
