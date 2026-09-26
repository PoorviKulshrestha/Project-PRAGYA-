import { SUBSIDIARIES } from '../data/stubs.js'

const NAV_ITEMS = [
  { id: 'dashboard',   icon: '▤',  label: 'Dashboard & Overview' },
  { id: 'documents',   icon: '⊟',  label: 'Document Management' },
  { id: 'query',       icon: '◎',  label: 'AI Query & Response' },
  { id: 'topics',      icon: '⊙',  label: 'Word Cloud & Topics' },
  { id: 'reports',     icon: '⊞',  label: 'Report Generator' },
  { id: 'validation',  icon: '✓',  label: 'Data Validation' },
]

export default function Sidebar({ activePage, setActivePage, activeSub, setActiveSub }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="sidebar-brand-title">⛏ PRAGYA</div>
        <div className="sidebar-brand-sub">CMPDI / Coal India Limited</div>
      </div>

      <div className="sidebar-subsidiary">
        <label>Active Subsidiary</label>
        <select value={activeSub} onChange={e => setActiveSub(e.target.value)}>
          {SUBSIDIARIES.map(s => (
            <option key={s.code} value={s.code}>{s.name}</option>
          ))}
        </select>
      </div>

      <div className="sidebar-section-label">Navigation</div>
      <nav className="sidebar-nav">
        {NAV_ITEMS.map(item => (
          <button
            key={item.id}
            className={`sidebar-item${activePage === item.id ? ' active' : ''}`}
            onClick={() => setActivePage(item.id)}
          >
            <span className="icon">{item.icon}</span>
            {item.label}
          </button>
        ))}
      </nav>


    </aside>
  )
}
