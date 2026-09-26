import { useState } from 'react'
import { VALIDATION_RECORDS, LINEAGE_RECORDS, CONSISTENCY_CHECKS, AUDIT_LOG } from '../data/stubs.js'

const statusBadge = s => {
  if (s === 'Validated')   return <span className="badge badge-success">✓ Validated</span>
  if (s === 'Partial')     return <span className="badge badge-warning">⚠ Partial</span>
  return                          <span className="badge badge-error">✕ Unverified</span>
}
const confColor = c => c >= 90 ? '#2e7d32' : c >= 70 ? '#f57f17' : '#c62828'
const checkBadge = r => {
  if (r === 'Pass')    return <span className="badge badge-success">✓ Pass</span>
  if (r === 'Warning') return <span className="badge badge-warning">⚠ Warning</span>
  return                      <span className="badge badge-error">✕ Fail</span>
}

export default function DataValidation() {
  const [running,  setRunning]  = useState(false)
  const [done,     setDone]     = useState(false)
  const [fields,   setFields]   = useState([
    'Reserve Estimates','Production Statistics','Safety Metrics',
    'Environmental Data','Geological Seam Data',
  ])
  const [crossRefs, setCrossRefs] = useState([
    'GSI Reports','CIL Annual Report',
  ])

  const fieldOpts = ['Reserve Estimates','Production Statistics','Safety Metrics',
    'Environmental Data','Geological Seam Data','Borehole Logs','All Fields']
  const crossRefOpts = ['GSI Reports','DGMS Portal','MoEFCC Portal',
    'CIL Annual Report','Subsidiary Q-Reports','Borehole Survey Logs']

  const toggleOption = (list, setList, val) => {
    setList(prev => prev.includes(val) ? prev.filter(x => x !== val) : [...prev, val])
  }

  const handleRun = () => {
    setRunning(true); setDone(false)
    setTimeout(() => { setRunning(false); setDone(true) }, 1600)
  }

  const passed  = VALIDATION_RECORDS.filter(r => r.status === 'Validated').length
  const partial = VALIDATION_RECORDS.filter(r => r.status === 'Partial').length
  const failed  = VALIDATION_RECORDS.filter(r => r.status === 'Unverified').length

  const csvAudit = AUDIT_LOG.map(r =>
    `${r.ts},${r.action},"${r.doc}",${r.user},${r.status}`
  ).join('\n')
  const csvBlob  = `data:text/csv;charset=utf-8,Timestamp,Action,Document,User,Status\n${csvAudit}`

  return (
    <div>
      <div className="page-title">Data Validation, Consistency &amp; Traceability</div>
      <div className="page-subtitle">
        Ensures accuracy and consistency of extracted data across historical and contemporary datasets.
        Every data point is cross-referenced against source documents and logged for audit.
        Mandatory before finalising any report or parliamentary response.
      </div>

      {/* Config + run */}
      <div className="form-section">
        <div className="form-section-title">Validation Configuration</div>
        <div className="grid-2">
          <div>
            <div className="form-label" style={{ marginBottom: 8 }}>Fields to Validate</div>
            {fieldOpts.map(f => (
              <div key={f} className="checkbox-group">
                <input type="checkbox" id={`f-${f}`}
                  checked={fields.includes(f)}
                  onChange={() => toggleOption(fields, setFields, f)} />
                <label htmlFor={`f-${f}`}>{f}</label>
              </div>
            ))}
          </div>
          <div>
            <div className="form-label" style={{ marginBottom: 8 }}>Cross-reference Against</div>
            {crossRefOpts.map(c => (
              <div key={c} className="checkbox-group">
                <input type="checkbox" id={`c-${c}`}
                  checked={crossRefs.includes(c)}
                  onChange={() => toggleOption(crossRefs, setCrossRefs, c)} />
                <label htmlFor={`c-${c}`}>{c}</label>
              </div>
            ))}
          </div>
        </div>
        <div style={{ marginTop: 14 }}>
          <button className="btn btn-primary" onClick={handleRun} disabled={running}>
            {running ? '⟳ Running validation suite…' : '✓ Run Validation Suite'}
          </button>
        </div>
      </div>

      {running && (
        <div style={{ marginBottom: 14 }}>
          <div className="progress-bar-wrap">
            <div className="progress-bar-fill" style={{ width: '55%' }} />
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 5 }}>
            Cross-referencing extracted fields against source documents…
          </div>
        </div>
      )}

      {done && (
        <>
          {/* Summary KPIs */}
          <div className="grid-4" style={{ margin: '16px 0' }}>
            {[
              ['Fields Validated', VALIDATION_RECORDS.length, 'var(--primary)'],
              [`✓ Validated`, passed,  '#2e7d32'],
              [`⚠ Partial`,   partial, '#f57f17'],
              [`✕ Unverified`, failed,  '#c62828'],
            ].map(([l, v, c]) => (
              <div key={l} className="kpi-card" style={{ borderTopColor: c }}>
                <div className="kpi-val" style={{ color: c, fontSize: '1.5rem' }}>{v}</div>
                <div className="kpi-lbl">{l}</div>
              </div>
            ))}
          </div>

          {failed > 0 && (
            <div className="alert alert-error">
              <span>✕</span>
              {failed} field(s) could not be cross-referenced. Manual review required before report submission.
            </div>
          )}
          {partial > 0 && (
            <div className="alert alert-warning">
              <span>⚠</span>
              {partial} field(s) partially validated — confidence below threshold. Additional source verification recommended.
            </div>
          )}
        </>
      )}

      <hr className="section-divider" />

      {/* Validation Results Table */}
      <div className="section-title">Validation Results</div>
      <div className="table-wrap" style={{ marginBottom: 24 }}>
        <table>
          <thead>
            <tr>
              <th>Data Field</th><th>Extracted Value</th>
              <th>Cross-reference Source</th><th>Status</th><th>Confidence</th>
            </tr>
          </thead>
          <tbody>
            {VALIDATION_RECORDS.map((r, i) => (
              <tr key={i}>
                <td style={{ fontWeight: 500 }}>{r.field}</td>
                <td style={{ fontFamily: 'monospace', fontSize: '0.78rem' }}>{r.extracted}</td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.78rem' }}>{r.crosscheck}</td>
                <td>{statusBadge(r.status)}</td>
                <td>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <div className="progress-bar-wrap" style={{ width: 60 }}>
                      <div className="progress-bar-fill"
                        style={{ width: `${r.confidence}%`, background: confColor(r.confidence) }} />
                    </div>
                    <span style={{ fontSize: '0.72rem', fontWeight: 600, color: confColor(r.confidence) }}>
                      {r.confidence}%
                    </span>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <hr className="section-divider" />

      {/* Data Lineage */}
      <div className="section-title">Data Lineage &amp; Traceability</div>
      <div className="page-subtitle" style={{ marginBottom: 12 }}>
        Every extracted value is traceable back to its exact source document, page number, and vector chunk ID.
      </div>
      <div className="table-wrap" style={{ marginBottom: 24 }}>
        <table>
          <thead>
            <tr>
              <th>Extracted Value</th><th>Source Document</th>
              <th>Page</th><th>Chunk ID</th><th>Extraction Method</th>
            </tr>
          </thead>
          <tbody>
            {LINEAGE_RECORDS.map((r, i) => (
              <tr key={i}>
                <td style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: 'var(--primary)', fontWeight: 600 }}>{r.value}</td>
                <td style={{ fontSize: '0.73rem', color: 'var(--text-muted)' }}>{r.doc}</td>
                <td style={{ textAlign: 'center' }}>{r.page}</td>
                <td style={{ fontFamily: 'monospace', fontSize: '0.73rem' }}>{r.chunk}</td>
                <td><span className="badge badge-blue">{r.method}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <hr className="section-divider" />

      {/* Consistency Checks */}
      <div className="section-title">Automated Consistency Checks</div>
      <div className="page-subtitle" style={{ marginBottom: 12 }}>
        Detects contradictions and anomalies across documents. Run before every report generation.
      </div>
      <div className="table-wrap" style={{ marginBottom: 24 }}>
        <table>
          <thead>
            <tr><th>Check</th><th>Result</th><th>Detail</th></tr>
          </thead>
          <tbody>
            {CONSISTENCY_CHECKS.map((c, i) => (
              <tr key={i}>
                <td style={{ fontWeight: 500 }}>{c.check}</td>
                <td>{checkBadge(c.result)}</td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.78rem' }}>{c.detail}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <hr className="section-divider" />

      {/* Audit trail */}
      <div className="section-title">Full System Audit Trail</div>
      <div className="page-subtitle" style={{ marginBottom: 12 }}>
        Complete log of all platform actions for compliance, accountability, and governance.
      </div>
      <div className="table-wrap" style={{ marginBottom: 14 }}>
        <table>
          <thead>
            <tr><th>Timestamp</th><th>Action</th><th>Document / Query</th><th>User</th><th>Status</th></tr>
          </thead>
          <tbody>
            {AUDIT_LOG.map((r, i) => (
              <tr key={i}>
                <td style={{ fontFamily: 'monospace', fontSize: '0.73rem' }}>{r.ts}</td>
                <td style={{ fontWeight: 500 }}>{r.action}</td>
                <td style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{r.doc}</td>
                <td>{r.user}</td>
                <td>
                  <span className={`badge ${r.status === 'Success' ? 'badge-success' : 'badge-warning'}`}>
                    {r.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <a
        className="btn btn-outline btn-sm"
        href={csvBlob}
        download="mineinsight_audit_log.csv"
      >
        ⬇ Export Audit Log (.csv)
      </a>
    </div>
  )
}
