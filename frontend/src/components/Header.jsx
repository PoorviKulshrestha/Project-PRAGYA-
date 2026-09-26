const PAGE_TITLES = {
  dashboard:  { title: 'Dashboard & Overview',        crumb: 'System Overview' },
  documents:  { title: 'Document Management',         crumb: 'Ingestion & Archives' },
  query:      { title: 'AI Query & Response System',  crumb: 'RAG Module' },
  topics:     { title: 'Word Cloud & Topic Analysis', crumb: 'NLP Module' },
  reports:    { title: 'Automated Report Generator',  crumb: 'Report Module' },
  validation: { title: 'Data Validation & Traceability', crumb: 'Quality Assurance' },
}

export default function Header({ activePage, backendLive }) {
  const meta = PAGE_TITLES[activePage] || PAGE_TITLES.dashboard
  const now  = new Date().toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' })

  return (
    <header className="header">
      <div className="header-left">
        <div className="header-page-title">{meta.title}</div>
        <div className="header-breadcrumb">MineInsight AI &rsaquo; {meta.crumb}</div>
      </div>
      <div className="header-right">
        <div className="header-status">
          <span className={`status-dot${backendLive ? ' live' : ''}`} />
          {backendLive ? 'Backend Live' : 'Demo Mode'}
        </div>
        <div className="header-meta">Date: {now}</div>
      </div>
    </header>
  )
}
