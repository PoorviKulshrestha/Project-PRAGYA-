import { ROADMAP, AUDIT_LOG } from '../data/stubs.js'

const PAIN_POINTS = [
  'High dependence on individual expertise for data retrieval',
  'Significant delays in generating reports and analytics',
  'High probability of manual errors in data compilation',
  'Limited ability to quickly retrieve insights when required',
  'Siloed data across PDFs, spreadsheets, images, and historical archives',
  'Slow response to parliamentary and administrative inquiries',
]
const SOLUTIONS = [
  'AI-automated multi-format document ingestion and indexing',
  'Cited AI responses to queries in under 30 seconds',
  'Automated report generation with structured data extraction',
  'Parliamentary inquiry drafts generated at a click',
  'Unified knowledge base across all CIL subsidiaries',
  'Historical archive search with semantic retrieval',
]

const statusBadge = s => {
  if (s === 'Complete')     return <span className="badge badge-success">{s}</span>
  if (s === 'In Progress')  return <span className="badge badge-warning">{s}</span>
  return                           <span className="badge badge-neutral">{s}</span>
}

export default function Dashboard() {
  return (
    <div>
      <div className="page-title">System Dashboard &amp; Impact Overview</div>
      <div className="page-subtitle">
        Real-time platform status, expected benefits, and workflow modernisation metrics
        for CMPDI / CIL subsidiaries as per the SIH problem statement.
      </div>

      {/* KPIs */}
      <div className="section-title">Expected Benefits — Key Performance Indicators</div>
      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-val">↓ 80%</div>
          <div className="kpi-lbl">Reduction in Report Preparation Time</div>
          <div className="kpi-sub">Days → Hours via full automation</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-val">97%</div>
          <div className="kpi-lbl">Accuracy in Structured Extraction</div>
          <div className="kpi-sub">Cross-validated against source documents</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-val">90%</div>
          <div className="kpi-lbl">Automation of Repetitive Workflows</div>
          <div className="kpi-sub">Reporting, Q&amp;A, topic analysis</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-val">&lt; 30s</div>
          <div className="kpi-lbl">Parliamentary Query Response Time</div>
          <div className="kpi-sub">vs. days with manual lookup</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-val">8</div>
          <div className="kpi-lbl">CIL Subsidiaries Supported</div>
          <div className="kpi-sub">ECL, BCCL, CCL, NCL, SECL, WCL, MCL, HQ</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-val">100%</div>
          <div className="kpi-lbl">Data Traceability</div>
          <div className="kpi-sub">Every claim linked to source + page</div>
        </div>
      </div>

      <hr className="section-divider" />

      {/* Three Modules */}
      <div className="section-title">Platform Modules — Problem Statement Coverage</div>
      <div className="grid-3">
        <div className="module-card">
          <div className="module-card-title">
            <span className="badge badge-primary">Module 1</span>
            Automated Report Generation
          </div>
          <ul>
            <li>Jinja2 template → structured .docx / .pdf</li>
            <li>9 report types across all CIL subsidiaries</li>
            <li>Auto-extraction of 10+ structured data fields</li>
            <li>Parliamentary inquiry response formatting</li>
            <li>Data traceability appendix in every report</li>
            <li>Officer review workflow with download/share</li>
          </ul>
        </div>
        <div className="module-card">
          <div className="module-card-title">
            <span className="badge badge-primary">Module 2</span>
            Word Cloud &amp; Topic Identification
          </div>
          <ul>
            <li>Word cloud generation from full corpus</li>
            <li>TF-IDF keyword extraction (fast, local)</li>
            <li>BERTopic for semantic topic modelling</li>
            <li>Full-corpus or per-subsidiary scope</li>
            <li>Historical topic trend analysis (time-series)</li>
            <li>Exportable word cloud image (PNG)</li>
          </ul>
        </div>
        <div className="module-card">
          <div className="module-card-title">
            <span className="badge badge-primary">Module 3</span>
            AI Query &amp; Response System (RAG)
          </div>
          <ul>
            <li>Gemini 1.5 Flash / Pro LLM backend</li>
            <li>ChromaDB local vector store</li>
            <li>all-MiniLM-L6-v2 local embeddings</li>
            <li>Page-level source citations (non-negotiable)</li>
            <li>General query + parliamentary inquiry modes</li>
            <li>Per-subsidiary and corpus-wide filtering</li>
          </ul>
        </div>
      </div>

      <hr className="section-divider" />

      {/* Pain Points vs Solutions */}
      <div className="section-title">Problem Being Solved</div>
      <div className="grid-2">
        <div className="card">
          <div className="card-title">Current Pain Points</div>
          {PAIN_POINTS.map((p, i) => (
            <div key={i} style={{ display: 'flex', gap: 8, marginBottom: 8, fontSize: '0.82rem' }}>
              <span style={{ color: '#c62828', flexShrink: 0 }}>✕</span>
              <span>{p}</span>
            </div>
          ))}
        </div>
        <div className="card">
          <div className="card-title">What This Platform Delivers</div>
          {SOLUTIONS.map((s, i) => (
            <div key={i} style={{ display: 'flex', gap: 8, marginBottom: 8, fontSize: '0.82rem' }}>
              <span style={{ color: '#2e7d32', flexShrink: 0 }}>✓</span>
              <span>{s}</span>
            </div>
          ))}
        </div>
      </div>

      <hr className="section-divider" />

      {/* Roadmap */}
      <div className="section-title">Implementation Roadmap — Structured Phases</div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Phase</th>
              <th>Title</th>
              <th>Status</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {ROADMAP.map(r => (
              <tr key={r.phase}>
                <td><strong>Phase {r.phase}</strong></td>
                <td>{r.title}</td>
                <td>{statusBadge(r.status)}</td>
                <td style={{ color: 'var(--text-muted)' }}>{r.desc}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <hr className="section-divider" />

      {/* Recent Activity */}
      <div className="section-title">Recent System Activity</div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Timestamp</th><th>Action</th><th>Document / Query</th><th>User</th><th>Status</th></tr>
          </thead>
          <tbody>
            {AUDIT_LOG.map((row, i) => (
              <tr key={i}>
                <td style={{ fontFamily: 'monospace', fontSize: '0.75rem' }}>{row.ts}</td>
                <td>{row.action}</td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.78rem' }}>{row.doc}</td>
                <td>{row.user}</td>
                <td>
                  <span className={`badge ${row.status === 'Success' ? 'badge-success' : 'badge-warning'}`}>
                    {row.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
