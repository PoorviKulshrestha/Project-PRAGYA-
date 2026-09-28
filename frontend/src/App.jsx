import { useState, useEffect } from 'react'
import Sidebar         from './components/Sidebar.jsx'
import Header          from './components/Header.jsx'
import Dashboard       from './pages/Dashboard.jsx'
import DocumentManagement from './pages/DocumentManagement.jsx'
import QueryResponse   from './pages/QueryResponse.jsx'
import WordCloud       from './pages/WordCloud.jsx'
import ReportGenerator from './pages/ReportGenerator.jsx'
import DataValidation  from './pages/DataValidation.jsx'
import { checkHealth } from './api.js'

const PAGES = {
  dashboard:  Dashboard,
  documents:  DocumentManagement,
  query:      QueryResponse,
  topics:     WordCloud,
  reports:    ReportGenerator,
  validation: DataValidation,
}

export default function App() {
  const [activePage, setActivePage] = useState('dashboard')
  const [activeSub,  setActiveSub]  = useState('ALL')
  const [backendLive, setBackendLive] = useState(false)

  useEffect(() => {
    checkHealth().then(live => setBackendLive(live))
    const interval = setInterval(() => {
      checkHealth().then(live => setBackendLive(live))
    }, 10000)
    return () => clearInterval(interval)
  }, [])

  const PageComponent = PAGES[activePage] || Dashboard

  return (
    <div className="shell">
      <Sidebar
        activePage={activePage}
        setActivePage={setActivePage}
        activeSub={activeSub}
        setActiveSub={setActiveSub}
      />
      <div className="main-area">
        <Header activePage={activePage} backendLive={backendLive} />
        <div className="page-content">
          <PageComponent activeSub={activeSub} />
        </div>
      </div>
    </div>
  )
}
