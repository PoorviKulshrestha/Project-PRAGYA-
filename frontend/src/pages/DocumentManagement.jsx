import { useState } from 'react'
import { STUB_DOCS, DATA_SOURCES, SUBSIDIARIES } from '../data/stubs.js'

export default function DocumentManagement() {
  const [ingesting, setIngesting]   = useState(false)
  const [progress,  setProgress]    = useState(0)
  const [done,      setDone]        = useState(false)
  const [histQ,     setHistQ]       = useState('')
  const [fromYear,  setFromYear]    = useState(1990)
  const [toYear,    setToYear]      = useState(2020)
  const [chunkSize, setChunkSize]   = useState(500)
  const [overlap,   setOverlap]     = useState(50)
  const [subTag,    setSubTag]      = useState('ALL')
  const [fileNames, setFileNames]   = useState([])

  const handleFiles = e => {
    setFileNames(Array.from(e.target.files).map(f => f.name))
    setDone(false)
  }

  const handleIngest = () => {
    if (!fileNames.length) return
    setIngesting(true); setProgress(0)
    let p = 0
    const iv = setInterval(() => {
      p += Math.random() * 25
      if (p >= 100) { p = 100; clearInterval(iv); setIngesting(false); setDone(true) }
      setProgress(Math.min(Math.round(p), 100))
    }, 350)
  }

  const totalChunks = STUB_DOCS.reduce((s, d) => s + d.chunks, 0)

  return (
    <div>
      <div className="page-title">Document Management &amp; Ingestion</div>
      <div className="page-subtitle">
        Ingest documents from multiple formats — PDFs, spreadsheets, images, Word documents,
        and historical archives — into the unified CMPDI knowledge base. All text is chunked,
        embedded, and stored in ChromaDB for semantic retrieval.
      </div>

      {/* Format support strip */}
      <div className="alert alert-info">
        <span>ℹ</span>
        <div>
          <strong>Supported Input Formats:&nbsp;</strong>
          <span className="fmt-chip fmt-pdf">PDF</span>
          <span className="fmt-chip fmt-excel">Excel / CSV</span>
          <span className="fmt-chip fmt-img">Images (JPG / PNG / TIFF)</span>
          <span className="fmt-chip fmt-word">Word (.docx)</span>
          <span className="fmt-chip fmt-arch">Archives (.zip)</span>
          &nbsp;—&nbsp;
          <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
            Scanned PDF / OCR support planned for Phase 6
          </span>
        </div>
      </div>

      {/* Upload + settings */}
      <div className="grid-2" style={{ marginBottom: 20 }}>
        <div>
          <div className="section-title">Upload Documents</div>
          <label
            className="upload-zone"
            htmlFor="file-input"
            style={{ display: 'block', cursor: 'pointer' }}
          >
            <div className="upload-icon">⊟</div>
            <div><strong>Click to browse or drag and drop</strong></div>
            <div style={{ marginTop: 4, color: 'var(--text-muted)', fontSize: '0.75rem' }}>
              PDF · XLSX · CSV · DOCX · JPG · PNG · TIFF · ZIP
            </div>
          </label>
          <input
            id="file-input" type="file" multiple
            accept=".pdf,.xlsx,.csv,.docx,.jpg,.jpeg,.png,.tiff,.zip"
            style={{ display: 'none' }}
            onChange={handleFiles}
          />
          {fileNames.length > 0 && (
            <div style={{ marginTop: 10 }}>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 6 }}>
                {fileNames.length} file(s) selected:
              </div>
              {fileNames.map((n, i) => (
                <div key={i} style={{ fontSize: '0.78rem', color: 'var(--primary)', padding: '2px 0' }}>
                  ◦ {n}
                </div>
              ))}
            </div>
          )}
        </div>

        <div>
          <div className="section-title">Ingestion Settings</div>
          <div className="form-group">
            <label className="form-label">Embedding Model</label>
            <select className="form-select">
              <option>all-MiniLM-L6-v2 (local · fast · recommended)</option>
              <option>all-mpnet-base-v2 (local · higher accuracy)</option>
            </select>
          </div>
          <div className="form-row">
            <div className="form-group">
              <label className="form-label">Chunk Size (tokens)</label>
              <input className="form-input" type="number" min={100} max={1000} step={50}
                value={chunkSize} onChange={e => setChunkSize(+e.target.value)} />
            </div>
            <div className="form-group">
              <label className="form-label">Overlap (tokens)</label>
              <input className="form-input" type="number" min={0} max={200} step={10}
                value={overlap} onChange={e => setOverlap(+e.target.value)} />
            </div>
          </div>
          <div className="form-group">
            <label className="form-label">Tag to Subsidiary</label>
            <select className="form-select" value={subTag} onChange={e => setSubTag(e.target.value)}>
              {SUBSIDIARIES.map(s => <option key={s.code} value={s.code}>{s.name}</option>)}
            </select>
          </div>
        </div>
      </div>

      {ingesting && (
        <div style={{ marginBottom: 14 }}>
          <div style={{ fontSize: '0.78rem', color: 'var(--primary)', marginBottom: 6 }}>
            Ingesting… {progress}%
          </div>
          <div className="progress-bar-wrap">
            <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
          </div>
        </div>
      )}
      {done && <div className="alert alert-success"><span>✓</span> Ingestion complete — documents indexed in ChromaDB.</div>}

      <div className="btn-group" style={{ marginBottom: 24 }}>
        <button className="btn btn-primary" onClick={handleIngest} disabled={ingesting || !fileNames.length}>
          {ingesting ? '⟳ Ingesting…' : '⚙ Ingest Selected Documents'}
        </button>
        <button className="btn btn-outline" onClick={() => { setFileNames([]); setDone(false) }}>
          Clear
        </button>
      </div>

      <hr className="section-divider" />

      {/* Corpus summary */}
      <div className="section-title">Indexed Document Corpus</div>
      <div className="grid-4" style={{ marginBottom: 16 }}>
        {[
          ['Total Documents', '8'],
          ['Total Chunks', totalChunks.toLocaleString()],
          ['Corpus Size', '~34.7 MB'],
          ['Formats Present', 'PDF (demo)'],
        ].map(([l, v]) => (
          <div key={l} className="kpi-card" style={{ borderTopColor: 'var(--accent)' }}>
            <div className="kpi-val" style={{ fontSize: '1.4rem' }}>{v}</div>
            <div className="kpi-lbl">{l}</div>
          </div>
        ))}
      </div>

      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Document Name</th><th>Type</th><th>Subsidiary</th>
              <th>Pages</th><th>Chunks</th><th>Size</th>
              <th>Status</th><th>Indexed On</th>
            </tr>
          </thead>
          <tbody>
            {STUB_DOCS.map((d, i) => (
              <tr key={i}>
                <td style={{ fontFamily: 'monospace', fontSize: '0.73rem', color: 'var(--primary)' }}>{d.name}</td>
                <td><span className="fmt-chip fmt-pdf">{d.type}</span></td>
                <td><span className="badge badge-primary">{d.subsidiary}</span></td>
                <td>{d.pages}</td>
                <td>{d.chunks}</td>
                <td>{d.size}</td>
                <td><span className="badge badge-success">{d.status}</span></td>
                <td style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{d.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <hr className="section-divider" />

      {/* Historical archive search */}
      <div className="section-title">Historical Archive Search</div>
      <div className="page-subtitle" style={{ marginBottom: 12 }}>
        Semantic search across digitised historical geological and mining records.
        Supports year-range filtering for temporal analysis.
      </div>
      <div className="form-row" style={{ alignItems: 'flex-end', marginBottom: 10 }}>
        <div className="form-group" style={{ gridColumn: 'span 1' }}>
          <label className="form-label">Search Query</label>
          <input className="form-input" placeholder="e.g. Jharia borehole survey 1998, Singrauli reserve estimation 2005"
            value={histQ} onChange={e => setHistQ(e.target.value)} />
        </div>
        <div className="form-group">
          <label className="form-label">From Year</label>
          <input className="form-input" type="number" min={1950} max={2024}
            value={fromYear} onChange={e => setFromYear(+e.target.value)} />
        </div>
        <div className="form-group">
          <label className="form-label">To Year</label>
          <input className="form-input" type="number" min={1950} max={2024}
            value={toYear} onChange={e => setToYear(+e.target.value)} />
        </div>
      </div>
      <button className="btn btn-outline">◎ Search Historical Archives</button>
      <div className="alert alert-info" style={{ marginTop: 12 }}>
        <span>ℹ</span>
        Historical archive search returns results from ChromaDB once documents are ingested.
        Currently in demo mode — ingest historical documents to enable this feature.
      </div>

      <hr className="section-divider" />

      {/* Data source coverage */}
      <div className="section-title">Data Source Coverage &amp; Roadmap</div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Data Source Type</th><th>Support Status</th><th>Notes</th></tr>
          </thead>
          <tbody>
            {DATA_SOURCES.map((d, i) => (
              <tr key={i}>
                <td>{d.type}</td>
                <td>
                  <span className={`badge ${d.support.startsWith('✓') ? 'badge-success' : 'badge-neutral'}`}>
                    {d.support}
                  </span>
                </td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.78rem' }}>{d.notes}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
