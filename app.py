"""
CMPDI/CIL AI-Powered Geological & Mining Reporting Solution
Team Runtime Error — Smart India Hackathon 2024

Problem Statement: AI-Powered Geological, Mining and other Reporting Solution
for CMPDI/CIL subsidiaries (Ministry of Coal / Coal India Limited)

Tabs:
  1. 📊  Dashboard & Overview
  2. 📁  Document Management
  3. 🔍  AI Query & Response (RAG)
  4. ☁️  Word Cloud & Topics
  5. 📄  Report Generator
  6. ✅  Data Validation & Traceability

Run:  streamlit run app.py
"""

import streamlit as st
import time
import random
import pandas as pd
from datetime import date, datetime

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CMPDI MineInsight AI",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #1a3a5c 0%, #0d6e6e 100%);
    color: white;
    padding: 1.4rem 2rem;
    border-radius: 12px;
    margin-bottom: 1.2rem;
    display: flex; align-items: center; gap: 1.2rem;
}
.hero-banner h1 { margin: 0; font-size: 1.75rem; font-weight: 700; }
.hero-banner p  { margin: 0.2rem 0 0; font-size: 0.92rem; opacity: 0.88; }

/* KPI cards */
.kpi-grid { display: flex; gap: 0.8rem; flex-wrap: wrap; margin-bottom: 1.2rem; }
.kpi-card {
    background: white;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    border-top: 4px solid #0d6e6e;
    padding: 1rem 1.3rem;
    flex: 1; min-width: 150px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}
.kpi-card .kpi-val { font-size: 2rem; font-weight: 800; color: #1a3a5c; }
.kpi-card .kpi-lbl { font-size: 0.78rem; color: #666; margin-top: 0.1rem; }
.kpi-card .kpi-sub { font-size: 0.72rem; color: #0d6e6e; margin-top: 0.2rem; font-style: italic; }

/* Impact badge */
.impact-badge {
    display: inline-block; background: #e8f5e9; color: #2e7d32;
    border: 1px solid #a5d6a7; border-radius: 20px;
    padding: 0.25rem 0.9rem; margin: 0.2rem; font-size: 0.82rem; font-weight: 600;
}

/* Citation / source box */
.citation-box {
    background: #eef6f6; border: 1px solid #b2d8d8;
    border-radius: 8px; padding: 0.8rem 1rem; margin-top: 0.5rem; font-size: 0.88rem;
}
.citation-box .src-title { font-weight: 600; color: #0d6e6e; }
.citation-box .excerpt   { color: #444; margin-top: 0.3rem; font-style: italic; }

/* Answer card */
.answer-card {
    background: #fff; border: 1px solid #d0e4e4; border-radius: 10px;
    padding: 1.2rem 1.4rem; margin-top: 0.6rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05); line-height: 1.75;
}

/* Parliamentary inquiry card */
.parl-card {
    background: #fffde7; border: 1px solid #f9a825; border-radius: 10px;
    padding: 1.2rem 1.5rem; margin-top: 0.6rem; font-size: 0.9rem; line-height: 1.8;
}
.parl-card .parl-header { font-weight: 700; color: #e65100; margin-bottom: 0.5rem; font-size: 1rem; }

/* Topic badge */
.topic-badge {
    display: inline-block; background: #1a3a5c; color: white;
    border-radius: 20px; padding: 0.3rem 0.9rem; margin: 0.2rem; font-size: 0.82rem; font-weight: 500;
}

/* Status pills */
.pill-green  { background:#d4edda; color:#155724; border-radius:12px; padding:2px 10px; font-size:0.8rem; font-weight:600; }
.pill-yellow { background:#fff3cd; color:#856404; border-radius:12px; padding:2px 10px; font-size:0.8rem; font-weight:600; }
.pill-red    { background:#f8d7da; color:#721c24; border-radius:12px; padding:2px 10px; font-size:0.8rem; font-weight:600; }
.pill-blue   { background:#cce5ff; color:#004085; border-radius:12px; padding:2px 10px; font-size:0.8rem; font-weight:600; }

/* Document type chip */
.doc-chip {
    display: inline-block; border-radius: 6px; padding: 2px 8px;
    font-size: 0.78rem; font-weight: 600; margin-right: 4px;
}
.chip-pdf    { background:#ffebee; color:#c62828; }
.chip-excel  { background:#e8f5e9; color:#2e7d32; }
.chip-image  { background:#e3f2fd; color:#1565c0; }
.chip-word   { background:#ede7f6; color:#4527a0; }
.chip-archive{ background:#fff3e0; color:#e65100; }

/* Validation row */
.val-pass { color:#155724; font-weight:600; }
.val-warn  { color:#856404; font-weight:600; }
.val-fail  { color:#721c24; font-weight:600; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 3px; }
.stTabs [data-baseweb="tab"] { font-weight: 600; border-radius: 6px 6px 0 0; padding: 0.45rem 1rem; }

.section-divider { border:none; border-top:1px solid #e8e8e8; margin:1rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⛏️ MineInsight AI")
    st.caption("CMPDI / Coal India Limited")
    st.markdown("---")

    st.markdown("**System Status**")
    backend_ok = st.session_state.get("backend_ready", False)
    if backend_ok:
        st.markdown('<span class="pill-green">● Backend Live</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="pill-yellow">● Demo Mode</span>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Corpus Summary**")
    st.metric("Documents Indexed",  st.session_state.get("doc_count", "8 (demo)"))
    st.metric("Chunks in Vector DB", st.session_state.get("chunk_count", "~2,400 (demo)"))
    st.metric("Last Ingestion", "Demo mode")

    st.markdown("---")
    st.markdown("**CIL Subsidiary**")
    active_sub = st.selectbox("Active subsidiary context", [
        "All Subsidiaries",
        "ECL — Eastern Coalfields",
        "BCCL — Bharat Coking Coal",
        "CCL — Central Coalfields",
        "NCL — Northern Coalfields",
        "SECL — South Eastern Coalfields",
        "WCL — Western Coalfields",
        "MCL — Mahanadi Coalfields",
        "CMPDIL — HQ",
    ], key="active_sub")

    st.markdown("---")
    st.caption("Smart India Hackathon 2024 | Ministry of Coal | Team Runtime Error")

# ── Hero Banner ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div style="font-size:2.8rem;">⛏️</div>
  <div>
    <h1>CMPDI MineInsight AI</h1>
    <p>
      AI-Powered Geological, Mining &amp; Reporting Solution &nbsp;|&nbsp;
      Coal India Limited &amp; Ministry of Coal &nbsp;|&nbsp;
      Smart India Hackathon 2024
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# STUB / DEMO DATA
# ════════════════════════════════════════════════════════════════════════════
MINES = [
    "Jharia Coalfield (BCCL)", "Raniganj Coalfield (ECL)",
    "Singrauli Coalfield (NCL)", "Talcher Coalfield (MCL)",
    "Ib Valley Coalfield (MCL)", "Korba Coalfield (SECL)",
    "Chirimiri Coalfield (SECL)", "Wardha Valley Coalfield (WCL)",
]

STUB_DOCS = [
    {"name": "CMPDI_Annual_Geological_Survey_Report_2023.pdf",  "type": "PDF",   "pages": 84,  "size": "4.2 MB",  "status": "Indexed",    "chunks": 312, "date": "2024-01-15"},
    {"name": "ECL_Production_Report_Q3_FY2024.pdf",             "type": "PDF",   "pages": 38,  "size": "1.8 MB",  "status": "Indexed",    "chunks": 144, "date": "2024-01-18"},
    {"name": "Jharia_Coalfield_Resource_Assessment_2022.pdf",   "type": "PDF",   "pages": 112, "size": "7.1 MB",  "status": "Indexed",    "chunks": 418, "date": "2024-01-18"},
    {"name": "MCL_Environmental_Compliance_FY2023.pdf",         "type": "PDF",   "pages": 56,  "size": "3.4 MB",  "status": "Indexed",    "chunks": 208, "date": "2024-01-19"},
    {"name": "Coal_Reserve_Estimation_India_2023.pdf",          "type": "PDF",   "pages": 96,  "size": "5.6 MB",  "status": "Indexed",    "chunks": 357, "date": "2024-01-20"},
    {"name": "NCL_Safety_Incident_Report_FY2024.pdf",           "type": "PDF",   "pages": 44,  "size": "2.1 MB",  "status": "Indexed",    "chunks": 163, "date": "2024-01-21"},
    {"name": "Geological_Borehole_Survey_Singrauli_2022.pdf",   "type": "PDF",   "pages": 68,  "size": "9.3 MB",  "status": "Indexed",    "chunks": 251, "date": "2024-01-22"},
    {"name": "SECL_Production_Forecast_FY2025.pdf",             "type": "PDF",   "pages": 29,  "size": "1.2 MB",  "status": "Indexed",    "chunks": 109, "date": "2024-01-22"},
]

STUB_ANSWER = {
    "answer": (
        "Based on the geological survey reports and annual production data, "
        "**coal reserves in the Eastern Coalfields region are estimated at approximately "
        "18.7 billion tonnes** as of FY 2023-24. The Jharia coalfield alone accounts for "
        "nearly 19% of India's total prime coking coal reserves. Seam thickness varies "
        "between 1.2 m and 6.4 m across the surveyed blocks, with an average ash content "
        "of 24.3%. Production in Q3 FY 2023-24 reached **142.6 MT**, reflecting a 7.2% "
        "YoY increase driven by improved mechanisation in underground mines [¹][²][³]."
    ),
    "sources": [
        {"doc": "CMPDI_Annual_Geological_Survey_Report_2023.pdf",  "page": 14, "score": 0.92,
         "excerpt": "...total proven reserves in the Eastern Coalfields zone stand at 18.7 billion tonnes as assessed by GSI in collaboration with CMPDI during 2022-23..."},
        {"doc": "ECL_Production_Report_Q3_FY2024.pdf",             "page": 6,  "score": 0.87,
         "excerpt": "...quarterly coal dispatch reached 142.6 MT, surpassing the target of 138 MT. Improvement attributed to enhanced longwall deployment in Jharia and Raniganj blocks..."},
        {"doc": "Jharia_Coalfield_Resource_Assessment_2022.pdf",   "page": 22, "score": 0.81,
         "excerpt": "...prime coking coal reserves in Jharia coalfield estimated at 3.55 billion tonnes, representing 19.0% of the national total prime coking coal reserve base..."},
    ],
}

PARL_STUB = """**MINISTRY OF COAL — PARLIAMENTARY QUESTION RESPONSE**

**Question No.:** Starred Q. 47 (Lok Sabha Session — Demo)
**Subject:** Coal Reserve Status and Production Performance in Eastern India

---

**REPLY ON BEHALF OF THE MINISTER OF COAL:**

(a) The total proven coal reserves in the Eastern Coalfields region (covering Jharia, Raniganj, and adjoining blocks) stand at **18.7 billion tonnes** as assessed jointly by the Geological Survey of India (GSI) and CMPDI during the period 2022-23. This represents approximately **26.4%** of India's total coal reserve base.

(b) Production during Q3 FY 2023-24 reached **142.6 MT**, exceeding the set target of 138 MT by **3.3%**. This improvement is attributable to enhanced deployment of longwall technology and increased mechanisation in underground mines operated by ECL and BCCL.

(c) All environmental clearances for active coalfields in the region are **current and valid**, with the next scheduled review in FY 2026-27. No material non-compliance has been recorded under the Environment Protection Act, 1986 during the reporting period.

---

*Generated by CMPDI MineInsight AI | Sources: [1] CMPDI Annual Geological Survey Report 2023 (p. 14), [2] ECL Production Report Q3 FY2024 (p. 6), [3] Jharia Coalfield Resource Assessment 2022 (p. 22)*
*This response has been automatically drafted for review by the authorised officer before submission.*"""

STUB_TOPICS = [
    ("Coal Reserve Estimation", 0.89),
    ("Underground Mining Operations", 0.84),
    ("Environmental Compliance", 0.78),
    ("Production Targets & Output", 0.76),
    ("Geological Seam Analysis", 0.73),
    ("Overburden Removal (OBR)", 0.69),
    ("Safety & DGMS Compliance", 0.65),
    ("Hydrogeology & Water Table", 0.61),
    ("Borehole Drilling & Surveys", 0.58),
    ("Coking vs Non-Coking Coal", 0.54),
]

STUB_KEYWORDS = [
    "coalfield", "seam", "reserves", "overburden", "longwall",
    "borehole", "stratigraphy", "OBR ratio", "DGMS", "methane",
    "aquifer", "opencast", "washery", "coking coal", "dispatch",
    "non-coking", "blasting", "subsidence", "exploration", "MT",
    "CMPDI", "ECL", "BCCL", "NCL", "MCL", "stripping ratio",
    "geological section", "dip", "strike", "calorific value",
]

VALIDATION_RECORDS = [
    {"Field": "Total Proven Reserves (Eastern CF)",   "Extracted": "18.7 BT",    "Cross-check": "GSI 2023 Report",       "Status": "✅ Validated", "Confidence": "97%"},
    {"Field": "Q3 FY2024 Production",                 "Extracted": "142.6 MT",   "Cross-check": "ECL Q3 Report p.6",    "Status": "✅ Validated", "Confidence": "95%"},
    {"Field": "Average Seam Thickness (Jharia)",      "Extracted": "3.4 m",      "Cross-check": "Borehole Survey 2022", "Status": "✅ Validated", "Confidence": "91%"},
    {"Field": "Avg Ash Content",                      "Extracted": "24.3%",      "Cross-check": "Washery data FY2023",  "Status": "⚠️ Partial",  "Confidence": "78%"},
    {"Field": "OBR Ratio (opencast mines)",           "Extracted": "3.8:1",      "Cross-check": "SECL Annual Report",   "Status": "✅ Validated", "Confidence": "89%"},
    {"Field": "LTIFR (Safety Metric)",                "Extracted": "0.23",       "Cross-check": "DGMS Annual Stats",    "Status": "✅ Validated", "Confidence": "93%"},
    {"Field": "Env. Clearance Validity",              "Extracted": "Until 2027", "Cross-check": "MoEFCC Portal",        "Status": "⚠️ Partial",  "Confidence": "72%"},
    {"Field": "Active Mine Galleries",                "Extracted": "214",        "Cross-check": "No cross-ref found",   "Status": "❌ Unverified","Confidence": "45%"},
]

AUDIT_LOG = [
    {"Timestamp": "2024-01-22 09:14:32", "Action": "Document Ingested",   "Document": "SECL_Production_Forecast_FY2025.pdf", "User": "System", "Status": "Success"},
    {"Timestamp": "2024-01-22 09:10:05", "Action": "Document Ingested",   "Document": "Geological_Borehole_Survey_Singrauli_2022.pdf", "User": "System", "Status": "Success"},
    {"Timestamp": "2024-01-22 08:45:11", "Action": "Report Generated",    "Document": "Jharia_Q3_Summary_Report.docx",       "User": "Admin",  "Status": "Success"},
    {"Timestamp": "2024-01-21 16:30:22", "Action": "Query Answered",      "Document": "RAG Query #47",                       "User": "Admin",  "Status": "Success"},
    {"Timestamp": "2024-01-21 14:22:08", "Action": "Parliamentary Draft", "Document": "Starred Q.47 Draft",                  "User": "Admin",  "Status": "Success"},
    {"Timestamp": "2024-01-21 11:05:44", "Action": "Validation Run",      "Document": "Corpus-wide validation",              "User": "System", "Status": "Warning (2 fields partial)"},
]

# ════════════════════════════════════════════════════════════════════════════
# TABS
# ════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊  Dashboard",
    "📁  Document Management",
    "🔍  AI Query & Response",
    "☁️  Word Cloud & Topics",
    "📄  Report Generator",
    "✅  Data Validation",
])


# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — DASHBOARD & OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("System Dashboard & Impact Overview")
    st.caption(
        "Real-time platform health, key performance benefits, and workflow modernisation "
        "metrics for CMPDI/CIL subsidiaries."
    )

    # ── Expected Benefits KPIs ─────────────────────────────────────────────
    st.markdown("##### Expected Benefits (as per Problem Statement)")
    st.markdown("""
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-val">↓ 80%</div>
        <div class="kpi-lbl">Reduction in report preparation time</div>
        <div class="kpi-sub">From days → hours via automation</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val">97%</div>
        <div class="kpi-lbl">Accuracy in structured extraction</div>
        <div class="kpi-sub">Cross-validated against source docs</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val">90%</div>
        <div class="kpi-lbl">Automation of repetitive workflows</div>
        <div class="kpi-sub">Reporting, Q&amp;A, topic analysis</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val">&lt; 30s</div>
        <div class="kpi-lbl">Response to parliamentary queries</div>
        <div class="kpi-sub">vs. days with manual lookup</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val">8 CIL</div>
        <div class="kpi-lbl">Subsidiaries supported</div>
        <div class="kpi-sub">ECL, BCCL, CCL, NCL, SECL, WCL, MCL, HQ</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Module Status ──────────────────────────────────────────────────────
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown("#### 📄 Module 1 — Report Generation")
        st.markdown('<span class="pill-yellow">● Demo Mode</span>', unsafe_allow_html=True)
        st.markdown("""
        - Jinja2 template → structured `.docx`
        - Auto-extracts 8+ data fields from corpus
        - Parliamentary response formatting
        - Multi-subsidiary, multi-report-type support
        """)

    with col_m2:
        st.markdown("#### ☁️ Module 2 — Word Cloud & Topics")
        st.markdown('<span class="pill-yellow">● Demo Mode</span>', unsafe_allow_html=True)
        st.markdown("""
        - Word cloud from full corpus text
        - TF-IDF keyword extraction
        - BERTopic / topic modelling
        - Per-subsidiary and corpus-wide analysis
        """)

    with col_m3:
        st.markdown("#### 🔍 Module 3 — AI Query System (RAG)")
        st.markdown('<span class="pill-yellow">● Demo Mode</span>', unsafe_allow_html=True)
        st.markdown("""
        - Gemini 1.5 Flash / Pro LLM backend
        - ChromaDB vector store (local)
        - `all-MiniLM-L6-v2` embeddings
        - Cited answers with page-level sources
        """)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Problem Impact Summary ─────────────────────────────────────────────
    st.markdown("##### Problem Being Solved")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("**Current Pain Points**")
        st.markdown("""
        - 🔴 High dependence on individual expertise
        - 🔴 Delays in generating reports and analytics
        - 🔴 High probability of manual errors
        - 🔴 Limited ability to quickly retrieve insights
        - 🔴 Siloed data across PDFs, spreadsheets, images & archives
        """)
    with col_p2:
        st.markdown("**What This Platform Delivers**")
        st.markdown("""
        - 🟢 Automated multi-format document ingestion
        - 🟢 AI-generated, cited answers in &lt;30 seconds
        - 🟢 Automated report generation with traceability
        - 🟢 Parliamentary query drafts at the click of a button
        - 🟢 Historical archive search and data standardisation
        """)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Implementation Phases ─────────────────────────────────────────────
    st.markdown("##### Implementation Roadmap (Structured Phases)")
    phases = pd.DataFrame([
        {"Phase": "1 — Requirement Analysis",        "Status": "✅ Complete", "Description": "Problem scoping, data audit, stakeholder interviews"},
        {"Phase": "2 — Data Digitisation & Ingestion","Status": "🔄 In Progress", "Description": "PDF/Excel/image ingestion pipeline, chunking, embeddings"},
        {"Phase": "3 — Platform Development",        "Status": "🔄 In Progress", "Description": "RAG system, report generator, topic module, Streamlit UI"},
        {"Phase": "4 — System Testing",              "Status": "⏳ Upcoming",  "Description": "Accuracy benchmarks, validation suite, QA on sample corpus"},
        {"Phase": "5 — Integration & Training",      "Status": "⏳ Upcoming",  "Description": "CIL subsidiary workflow integration, user training"},
        {"Phase": "6 — Continuous Enhancement",      "Status": "⏳ Upcoming",  "Description": "Feedback loops, model fine-tuning, OCR addition, scaling"},
    ])
    st.dataframe(phases, hide_index=True, use_container_width=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Recent Activity ────────────────────────────────────────────────────
    st.markdown("##### Recent System Activity")
    st.dataframe(pd.DataFrame(AUDIT_LOG), hide_index=True, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — DOCUMENT MANAGEMENT
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.subheader("Document Management & Ingestion")
    st.caption(
        "Ingest documents from multiple formats — PDFs, spreadsheets, images, Word documents, "
        "and historical archives — into the unified knowledge base."
    )

    # ── Supported formats callout ──────────────────────────────────────────
    st.markdown("""
    <div style="background:#f0f4f8;border-radius:8px;padding:0.8rem 1.2rem;margin-bottom:1rem;border-left:4px solid #0d6e6e;">
      <strong>Supported Input Formats</strong>&nbsp;&nbsp;
      <span class="doc-chip chip-pdf">PDF</span>
      <span class="doc-chip chip-excel">Excel / CSV</span>
      <span class="doc-chip chip-image">Images (JPG/PNG/TIFF)</span>
      <span class="doc-chip chip-word">Word (.docx)</span>
      <span class="doc-chip chip-archive">Historical Archives (.zip)</span>
      &nbsp;|&nbsp; <small style="color:#555">Scanned PDFs: OCR support planned (Phase 6)</small>
    </div>
    """, unsafe_allow_html=True)

    # ── Upload widget ─────────────────────────────────────────────────────
    col_up, col_cfg = st.columns([2, 1])
    with col_up:
        uploaded_files = st.file_uploader(
            "Upload documents to ingest",
            accept_multiple_files=True,
            type=["pdf", "xlsx", "csv", "docx", "jpg", "jpeg", "png", "tiff", "zip"],
            help="Drag and drop or click to browse. Multiple files accepted.",
        )
    with col_cfg:
        st.markdown("**Ingestion Settings**")
        chunk_size    = st.number_input("Chunk size (tokens)", 200, 1000, 500, 50)
        chunk_overlap = st.number_input("Overlap (tokens)",      0,  200,  50, 10)
        embed_model   = st.selectbox("Embedding model", ["all-MiniLM-L6-v2 (local, fast)", "all-mpnet-base-v2 (local, accurate)"])
        subsidiary_tag = st.selectbox("Tag documents to subsidiary", [
            "All / Untagged", "ECL", "BCCL", "CCL", "NCL", "SECL", "WCL", "MCL", "CMPDIL HQ"])

    if uploaded_files:
        ingest_btn = st.button("⚙️ Ingest Selected Documents", type="primary")
        if ingest_btn:
            prog = st.progress(0, text="Starting ingestion…")
            for i, f in enumerate(uploaded_files):
                prog.progress(int((i + 0.5) / len(uploaded_files) * 100),
                              text=f"Processing: {f.name}")
                time.sleep(0.6)
            prog.progress(100, text="Ingestion complete!")
            st.success(f"✅ {len(uploaded_files)} file(s) queued for ingestion. "
                       "Embeddings will be computed and stored in ChromaDB.")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Current corpus ─────────────────────────────────────────────────────
    st.markdown("##### Indexed Document Corpus")
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    col_s1.metric("Total Documents", "8")
    col_s2.metric("Total Chunks",    "~2,400")
    col_s3.metric("Formats",         "PDF (demo)")
    col_s4.metric("Corpus Size",     "~34.7 MB")

    doc_df = pd.DataFrame(STUB_DOCS)
    st.dataframe(
        doc_df,
        column_config={
            "status": st.column_config.TextColumn("Status"),
            "chunks": st.column_config.NumberColumn("Chunks"),
        },
        hide_index=True,
        use_container_width=True,
    )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Historical archive search ─────────────────────────────────────────
    st.markdown("##### Historical Archive Search")
    st.caption("Search across digitised historical geological and mining records.")
    ha_col1, ha_col2, ha_col3 = st.columns([3, 1, 1])
    with ha_col1:
        hist_query = st.text_input("Search historical records", placeholder="e.g. Jharia borehole 1998, Singrauli reserve survey 2005")
    with ha_col2:
        year_from = st.number_input("From year", 1950, 2024, 1990)
    with ha_col3:
        year_to   = st.number_input("To year",   1950, 2024, 2020)

    if st.button("🔍 Search Archives"):
        with st.spinner("Searching historical records…"):
            time.sleep(1.0)
        st.info("ℹ️ Historical archive search returns results from the ChromaDB vector store once documents are ingested. Currently in demo mode.")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Data sources overview ────────────────────────────────────────────
    st.markdown("##### Data Source Coverage")
    src_df = pd.DataFrame([
        {"Data Source Type": "Geological Survey PDFs",      "Coverage": "Native PDF — supported ✅",          "Notes": "Text extraction via pdfplumber"},
        {"Data Source Type": "Production Reports (Excel/CSV)","Coverage": "Excel/CSV — supported ✅",         "Notes": "pandas read_excel / read_csv"},
        {"Data Source Type": "Images (maps, seam diagrams)", "Coverage": "Planned — Phase 6 ⏳",             "Notes": "OCR + vision model required"},
        {"Data Source Type": "Scanned PDFs / Archives",      "Coverage": "Planned — Phase 6 ⏳",             "Notes": "Tesseract OCR pipeline"},
        {"Data Source Type": "Word Documents (.docx)",       "Coverage": "Supported ✅",                      "Notes": "python-docx text extraction"},
        {"Data Source Type": "Historical Archive (.zip)",    "Coverage": "Supported — batch unzip ✅",        "Notes": "Recursive ingestion of contents"},
        {"Data Source Type": "SharePoint / Network Drive",   "Coverage": "Planned — Phase 5 ⏳",             "Notes": "Integration with CIL subsidiary file stores"},
    ])
    st.dataframe(src_df, hide_index=True, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — AI QUERY & RESPONSE (RAG)
# ─────────────────────────────────────────────────────────────────────────────
with tab3:
    st.subheader("AI Query & Response System")
    st.caption(
        "Ask any question about the indexed geological and mining documents. "
        "The system retrieves relevant chunks and generates a cited answer using Gemini LLM."
    )

    # ── Query mode ────────────────────────────────────────────────────────
    query_mode = st.radio(
        "Query Mode",
        ["General Query", "Parliamentary / Administrative Inquiry"],
        horizontal=True,
        help="Parliamentary mode formats the response as an official Ministry of Coal reply.",
    )

    if query_mode == "Parliamentary / Administrative Inquiry":
        st.markdown("""
        <div style="background:#fff3e0;border-left:4px solid #f9a825;border-radius:8px;
                    padding:0.7rem 1rem;font-size:0.88rem;margin-bottom:0.8rem;">
          <strong>⚠️ Parliamentary Mode</strong> — The response will be formatted as an official
          Ministry of Coal parliamentary reply, ready for officer review before submission.
          All claims include source citations.
        </div>
        """, unsafe_allow_html=True)
        parl_col1, parl_col2 = st.columns(2)
        with parl_col1:
            parl_q_no   = st.text_input("Question Number", placeholder="e.g. Starred Q. 47")
            parl_house  = st.selectbox("House", ["Lok Sabha", "Rajya Sabha"])
        with parl_col2:
            parl_session = st.text_input("Session", placeholder="e.g. Budget Session 2024")
            parl_ministry = st.text_input("Ministry", value="Ministry of Coal")

    col_q, col_hint = st.columns([3, 1])
    with col_q:
        question = st.text_area(
            "Your question",
            placeholder=(
                "e.g. What are the total coal reserves in the Eastern Coalfields?\n"
                "e.g. What is the average seam thickness in Jharia block?\n"
                "e.g. How did Q3 FY2024 production compare to target?\n"
                "e.g. What is the environmental compliance status of MCL mines?"
            ),
            height=110,
            key="rag_question",
        )
    with col_hint:
        st.markdown("**💡 Sample questions**")
        sample_qs = [
            "Coal reserves in Eastern Coalfields?",
            "Seam thickness in Jharia block?",
            "Q3 FY2024 production vs target?",
            "Environmental compliance status?",
            "OBR ratio in opencast mines?",
            "LTIFR safety statistics FY2024?",
            "Coking coal reserves in India?",
        ]
        for sq in sample_qs:
            if st.button(sq, key=f"sq_{sq[:18]}", use_container_width=True):
                st.session_state["rag_question"] = sq

    rcol1, rcol2, rcol3 = st.columns([1, 1, 4])
    with rcol1:
        top_k = st.selectbox("Top-K chunks", [3, 5, 8, 10], index=0)
    with rcol2:
        filter_sub = st.selectbox("Filter by subsidiary", ["All"] + ["ECL","BCCL","CCL","NCL","SECL","WCL","MCL"])

    acol1, acol2, _ = st.columns([1, 1, 4])
    with acol1:
        ask_btn = st.button("🔍 Ask", type="primary", use_container_width=True)
    with acol2:
        if st.button("✕ Clear", use_container_width=True):
            st.session_state.pop("rag_result", None)

    if ask_btn and question.strip():
        with st.spinner("Retrieving relevant chunks and generating answer…"):
            time.sleep(1.4)
            # ── Real call ──────────────────────────────────────────────
            # from rag.pipeline import query
            # result = query(question, top_k=top_k, subsidiary=filter_sub)
            # ──────────────────────────────────────────────────────────
            st.session_state["rag_result"] = STUB_ANSWER
            st.session_state["rag_mode"]   = query_mode

    if ask_btn and not question.strip():
        st.warning("Please enter a question before clicking Ask.")

    if "rag_result" in st.session_state:
        result = st.session_state["rag_result"]
        mode   = st.session_state.get("rag_mode", "General Query")

        if mode == "Parliamentary / Administrative Inquiry":
            st.markdown("#### Official Parliamentary Reply Draft")
            st.markdown(
                f'<div class="parl-card">'
                f'<div class="parl-header">MINISTRY OF COAL — PARLIAMENTARY QUESTION RESPONSE</div>'
                f'{PARL_STUB}'
                f'</div>',
                unsafe_allow_html=True,
            )
            dl_col1, dl_col2 = st.columns(2)
            dl_col1.download_button(
                "⬇️ Download as .docx (draft)",
                data=b"[Parliamentary reply docx placeholder]",
                file_name="Parliamentary_Reply_Draft.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
            dl_col2.button("📧 Send for Officer Review", help="Sends draft to authorised officer for approval before submission (integration required)")
        else:
            st.markdown("#### Answer")
            st.markdown(f'<div class="answer-card">{result["answer"]}</div>', unsafe_allow_html=True)

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.markdown(f"#### 📎 Source Citations  `top-{top_k} chunks`")
        for i, src in enumerate(result["sources"][:top_k], 1):
            score_pct = int(src["score"] * 100)
            score_color = "#155724" if src["score"] > 0.85 else "#856404" if src["score"] > 0.70 else "#721c24"
            st.markdown(
                f'<div class="citation-box">'
                f'<div class="src-title">[{i}] {src["doc"]} — Page {src["page"]}'
                f'&nbsp;<span style="color:{score_color};font-size:0.82rem">▲ {score_pct}% relevance</span></div>'
                f'<div class="excerpt">"{src["excerpt"]}"</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    if not backend_ok:
        st.info("ℹ️ **Demo mode** — answers are stub data. Wire in the FastAPI RAG backend for live responses.", icon="🔧")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 4 — WORD CLOUD & TOPICS
# ─────────────────────────────────────────────────────────────────────────────
with tab4:
    st.subheader("Word Cloud & Topic Identification Module")
    st.caption(
        "Automatically identifies dominant themes and key terminology across all indexed "
        "documents. Supports corpus-wide or per-subsidiary analysis."
    )

    wc_col1, wc_col2, wc_col3 = st.columns([2, 1, 1])
    with wc_col1:
        wc_btn = st.button("☁️ Generate Word Cloud & Topics", type="primary", use_container_width=True)
    with wc_col2:
        n_topics   = st.slider("Number of topics", 3, 12, 8, key="n_topics")
    with wc_col3:
        topic_algo = st.selectbox("Algorithm", ["TF-IDF (fast)", "BERTopic (accurate)"])

    analysis_scope = st.radio("Analysis Scope", ["Full Corpus", "By Subsidiary"], horizontal=True)
    if analysis_scope == "By Subsidiary":
        scope_sub = st.selectbox("Select Subsidiary", ["ECL","BCCL","CCL","NCL","SECL","WCL","MCL"])

    if wc_btn:
        with st.spinner(f"Analysing corpus with {topic_algo}…"):
            time.sleep(1.8)
            st.session_state["topics_ready"] = True

    if st.session_state.get("topics_ready"):
        img_col, topic_col = st.columns([1.3, 1])

        with img_col:
            st.markdown("##### Word Cloud")
            # Real: from topics.wordcloud_gen import generate_wordcloud_image; st.image(img)
            st.markdown("""
            <div style="background:#f0f4f8;border-radius:10px;padding:1.2rem;text-align:center;
                        min-height:280px;display:flex;align-items:center;justify-content:center;
                        flex-direction:column;border:2px dashed #b2d8d8;color:#0d6e6e;font-size:0.9rem;">
              <div style="font-size:3rem">☁️</div>
              <div style="margin-top:0.5rem;font-weight:600">Word Cloud renders here</div>
              <small style="color:#888">(populated after ingestion pipeline runs)</small>
            </div>
            """, unsafe_allow_html=True)
            st.caption(f"Algorithm: {topic_algo} | Corpus: 8 docs, ~2,400 chunks | Stopwords removed")

            # Download button for word cloud image
            st.download_button(
                "⬇️ Download Word Cloud (PNG)",
                data=b"[PNG bytes from wordcloud library]",
                file_name="wordcloud_corpus.png",
                mime="image/png",
            )

        with topic_col:
            st.markdown("##### Identified Topics")
            for i, (topic, score) in enumerate(STUB_TOPICS[:n_topics], 1):
                st.markdown(f'<span class="topic-badge">#{i} {topic}</span>', unsafe_allow_html=True)
                st.progress(int(score * 100) / 100, text=f"{int(score*100)}% weight")

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

        kw_col, bar_col = st.columns([1, 1.5])
        with kw_col:
            st.markdown("##### Top Keywords (TF-IDF)")
            cols5 = st.columns(3)
            for idx, kw in enumerate(STUB_KEYWORDS):
                cols5[idx % 3].markdown(
                    f"<span style='background:#e8f4f4;padding:3px 8px;border-radius:6px;"
                    f"font-size:0.8rem;color:#1a3a5c;display:inline-block;margin:2px'>🔑 {kw}</span>",
                    unsafe_allow_html=True,
                )

        with bar_col:
            st.markdown("##### Topic Weight Distribution")
            df_t = pd.DataFrame(STUB_TOPICS[:n_topics], columns=["Topic", "Weight"])
            st.bar_chart(df_t.set_index("Topic"), color="#0d6e6e", height=320)

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.markdown("##### Topic Trend Over Time (Historical)")
        st.caption("Shows how topic prominence has shifted across different reporting periods.")
        trend_df = pd.DataFrame({
            "Year": [2019, 2020, 2021, 2022, 2023, 2024],
            "Coal Reserve Estimation": [0.72, 0.74, 0.78, 0.82, 0.85, 0.89],
            "Environmental Compliance": [0.48, 0.55, 0.61, 0.68, 0.73, 0.78],
            "Safety & DGMS": [0.42, 0.50, 0.55, 0.58, 0.61, 0.65],
        })
        st.line_chart(trend_df.set_index("Year"), height=250)

    if not backend_ok:
        st.info("ℹ️ **Demo mode** — topics are stubs. Run ingestion to populate with real corpus analysis.", icon="🔧")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 5 — REPORT GENERATOR
# ─────────────────────────────────────────────────────────────────────────────
with tab5:
    st.subheader("Automated Report Generation Platform")
    st.caption(
        "Generate structured, data-backed reports in .docx format. "
        "Supports geological summaries, production reports, parliamentary responses, "
        "and environmental compliance reports for all CIL subsidiaries."
    )

    with st.form("report_form"):
        st.markdown("##### 1. Report Identity")
        r1, r2 = st.columns(2)
        with r1:
            report_title = st.text_input("Report Title", value="Geological & Production Summary Report")
            report_type  = st.selectbox("Report Type", [
                "Quarterly Production Report",
                "Annual Geological Survey Summary",
                "Reserve Estimation Report",
                "Environmental Compliance Report",
                "Parliamentary Question Response",
                "High-Priority Administrative Inquiry",
                "Safety & DGMS Compliance Report",
                "Borehole Survey Summary",
                "Mine Closure & Rehabilitation Report",
            ])
        with r2:
            subsidiary = st.selectbox("CIL Subsidiary", [
                "Eastern Coalfields Ltd (ECL)",
                "Bharat Coking Coal Ltd (BCCL)",
                "Central Coalfields Ltd (CCL)",
                "Northern Coalfields Ltd (NCL)",
                "South Eastern Coalfields Ltd (SECL)",
                "Western Coalfields Ltd (WCL)",
                "Mahanadi Coalfields Ltd (MCL)",
                "CMPDIL — HQ (All Subsidiaries)",
            ])
            mine_name = st.selectbox("Mine / Coalfield", MINES)

        st.markdown("##### 2. Reporting Period & Authorship")
        r3, r4 = st.columns(2)
        with r3:
            period_start = st.date_input("Period Start", value=date(2024, 1, 1))
            period_end   = st.date_input("Period End",   value=date(2024, 3, 31))
        with r4:
            author_name  = st.text_input("Prepared By", value="CMPDI Technical Division")
            approved_by  = st.text_input("Approved By / Reviewing Officer", value="General Manager, Mining")
            ref_number   = st.text_input("Reference / File Number", placeholder="e.g. CMPDI/GEO/2024/Q3/001")

        st.markdown("##### 3. Data Sections to Include")
        s1, s2, s3, s4 = st.columns(4)
        inc_reserves    = s1.checkbox("Reserve Estimates",         value=True)
        inc_production  = s1.checkbox("Production Statistics",     value=True)
        inc_geology     = s2.checkbox("Geological Profile",         value=True)
        inc_env         = s2.checkbox("Environmental Metrics",      value=True)
        inc_safety      = s3.checkbox("Safety Statistics (DGMS)",  value=True)
        inc_forecast    = s3.checkbox("Production Forecast",        value=False)
        inc_borehole    = s4.checkbox("Borehole / Seam Data",       value=False)
        inc_historical  = s4.checkbox("Historical Comparison",      value=False)

        st.markdown("##### 4. Data Sources to Reference")
        ds1, ds2, ds3 = st.columns(3)
        src_pdfs    = ds1.checkbox("Geological Survey PDFs",    value=True)
        src_excel   = ds1.checkbox("Production Excel Reports",  value=True)
        src_images  = ds2.checkbox("Geological Maps / Images",  value=False)
        src_archive = ds2.checkbox("Historical Archives",       value=False)
        src_live    = ds3.checkbox("Live API / Portal Data",    value=False)

        st.markdown("##### 5. Output Format & Additional Notes")
        f1, f2 = st.columns(2)
        with f1:
            output_fmt    = st.selectbox("Output Format", [".docx (Word)", ".pdf (via docx conversion)", "Both"])
            include_toc   = st.checkbox("Include Table of Contents", value=True)
            include_trail = st.checkbox("Include Data Traceability Appendix", value=True)
        with f2:
            notes = st.text_area("Remarks / Executive Summary (optional)",
                                 placeholder="Add context for the reviewing officer…", height=90)

        submitted = st.form_submit_button("📄 Generate Report", type="primary")

    if submitted:
        with st.spinner("Extracting data fields, filling template, rendering .docx…"):
            time.sleep(1.8)
            # Real: from reports.generator import generate_report; docx_bytes = generate_report(params)
            st.success("✅ Report generated successfully!", icon="📄")

        preview = {
            "Report Title":     report_title,  "Report Type":     report_type,
            "Subsidiary":       subsidiary,     "Mine / Coalfield": mine_name,
            "Period":           f"{period_start} → {period_end}",
            "Prepared By":      author_name,    "Approved By":     approved_by,
            "Reference":        ref_number or "Auto-generated",
            "Sections":         ", ".join(filter(None, [
                "Reserves" if inc_reserves else "", "Production" if inc_production else "",
                "Geology"  if inc_geology  else "", "Environment" if inc_env else "",
                "Safety"   if inc_safety   else "", "Forecast"    if inc_forecast else "",
                "Borehole" if inc_borehole else "", "Historical"  if inc_historical else "",
            ])),
            "Data Sources": ", ".join(filter(None, [
                "PDFs" if src_pdfs else "", "Excel" if src_excel else "",
                "Images" if src_images else "", "Archives" if src_archive else "",
                "Live API" if src_live else "",
            ])),
        }

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### Report Parameters")
            st.dataframe(pd.DataFrame(list(preview.items()), columns=["Field","Value"]),
                         hide_index=True, use_container_width=True)
        with c2:
            st.markdown("##### Auto-Extracted Data Points")
            stub_fields = {
                "Total Proven Reserves":     "18.7 billion tonnes",
                "Current Production Rate":   "142.6 MT / quarter",
                "Average Seam Thickness":    "3.4 m",
                "Average Ash Content":       "24.3%",
                "OBR Ratio (opencast)":      "3.8 : 1",
                "Active Mine Galleries":     "214",
                "LTIFR (Safety)":            "0.23 per lakh man-shifts",
                "Env. Clearances":           "Valid until 2027",
                "Methane Drainage Capacity": "12,400 m³/day",
                "Reserves Life Index":       "~82 years at current rate",
            }
            st.dataframe(pd.DataFrame(list(stub_fields.items()), columns=["Data Point","Extracted Value"]),
                         hide_index=True, use_container_width=True)

        dl1, dl2 = st.columns(2)
        dl1.download_button(
            "⬇️ Download .docx",
            data=b"[DOCX bytes from python-docx template engine]",
            file_name=f"{mine_name.split('(')[0].strip().replace(' ','_')}_Report_{period_start}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        dl2.download_button(
            "⬇️ Download .pdf",
            data=b"[PDF bytes]",
            file_name=f"{mine_name.split('(')[0].strip().replace(' ','_')}_Report_{period_start}.pdf",
            mime="application/pdf",
        )

    if not backend_ok:
        st.info("ℹ️ **Demo mode** — download contains placeholder bytes. Wire in `reports.generator` for real .docx output.", icon="🔧")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 6 — DATA VALIDATION & TRACEABILITY
# ─────────────────────────────────────────────────────────────────────────────
with tab6:
    st.subheader("Data Validation, Consistency & Traceability")
    st.caption(
        "Ensures accuracy and consistency of extracted data across historical and contemporary datasets. "
        "Every data point is cross-referenced against source documents and logged for audit."
    )

    # ── Run validation ─────────────────────────────────────────────────────
    v_col1, v_col2 = st.columns([2, 2])
    with v_col1:
        val_scope = st.multiselect("Validate fields", [
            "Reserve Estimates", "Production Statistics", "Safety Metrics",
            "Environmental Data", "Geological Seam Data", "All Fields",
        ], default=["All Fields"])
    with v_col2:
        val_cross = st.multiselect("Cross-reference against", [
            "GSI Reports", "DGMS Portal", "MoEFCC Portal", "CIL Annual Report",
            "Subsidiary Q-Reports", "Borehole Survey Logs",
        ], default=["GSI Reports", "CIL Annual Report"])

    if st.button("✅ Run Validation Suite", type="primary"):
        with st.spinner("Cross-referencing extracted fields against source documents…"):
            time.sleep(1.5)
        st.session_state["validation_done"] = True

    if st.session_state.get("validation_done"):
        passed  = sum(1 for r in VALIDATION_RECORDS if "✅" in r["Status"])
        partial = sum(1 for r in VALIDATION_RECORDS if "⚠️" in r["Status"])
        failed  = sum(1 for r in VALIDATION_RECORDS if "❌" in r["Status"])

        vc1, vc2, vc3, vc4 = st.columns(4)
        vc1.metric("Fields Validated", len(VALIDATION_RECORDS))
        vc2.metric("✅ Validated",  passed,  delta=None)
        vc3.metric("⚠️ Partial",    partial, delta=None)
        vc4.metric("❌ Unverified", failed,  delta=None)

        st.markdown("##### Validation Results")
        val_df = pd.DataFrame(VALIDATION_RECORDS)
        st.dataframe(val_df, hide_index=True, use_container_width=True)

        if failed > 0:
            st.warning(f"⚠️ {failed} field(s) could not be cross-referenced. Manual review required before report submission.")
        if partial > 0:
            st.info(f"ℹ️ {partial} field(s) partially validated — confidence below threshold. Recommend additional source verification.")

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Data Lineage / Traceability ────────────────────────────────────────
    st.markdown("##### Data Lineage & Traceability")
    st.caption("Every extracted value is traceable back to its source document, page, and chunk ID.")
    lineage_df = pd.DataFrame([
        {"Value": "18.7 BT reserves",     "Source Doc": "CMPDI_Annual_Geological_Survey_Report_2023.pdf", "Page": 14, "Chunk ID": "chk_0042", "Extraction Method": "RAG + regex"},
        {"Value": "142.6 MT production",  "Source Doc": "ECL_Production_Report_Q3_FY2024.pdf",            "Page":  6, "Chunk ID": "chk_0198", "Extraction Method": "RAG + regex"},
        {"Value": "3.4 m seam thickness", "Source Doc": "Jharia_Coalfield_Resource_Assessment_2022.pdf",  "Page": 22, "Chunk ID": "chk_0731", "Extraction Method": "RAG + NER"},
        {"Value": "24.3% ash content",    "Source Doc": "Coal_Reserve_Estimation_India_2023.pdf",         "Page": 47, "Chunk ID": "chk_1102", "Extraction Method": "RAG + regex"},
        {"Value": "3.8:1 OBR ratio",      "Source Doc": "SECL_Production_Forecast_FY2025.pdf",            "Page":  9, "Chunk ID": "chk_2201", "Extraction Method": "RAG + table parse"},
        {"Value": "0.23 LTIFR",           "Source Doc": "NCL_Safety_Incident_Report_FY2024.pdf",          "Page": 18, "Chunk ID": "chk_1874", "Extraction Method": "RAG + regex"},
    ])
    st.dataframe(lineage_df, hide_index=True, use_container_width=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Audit Trail ─────────────────────────────────────────────────────────
    st.markdown("##### Full Audit Trail")
    st.caption("Complete log of all system actions for compliance and accountability.")
    audit_df = pd.DataFrame(AUDIT_LOG)
    st.dataframe(audit_df, hide_index=True, use_container_width=True)

    st.download_button(
        "⬇️ Export Audit Log (.csv)",
        data=audit_df.to_csv(index=False).encode(),
        file_name="mineinsight_audit_log.csv",
        mime="text/csv",
    )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # ── Consistency checks ──────────────────────────────────────────────────
    st.markdown("##### Data Consistency Checks")
    st.caption("Automated checks for contradictions and anomalies across documents.")
    consistency_df = pd.DataFrame([
        {"Check": "Reserve figures — cross-doc consistency",        "Result": "✅ Pass",    "Details": "3 documents report same order of magnitude"},
        {"Check": "Production targets vs actuals",                  "Result": "✅ Pass",    "Details": "Q3 actuals exceed target by 3.3%"},
        {"Check": "Seam thickness — borehole vs survey report",     "Result": "⚠️ Warning", "Details": "Minor discrepancy: 3.4 m vs 3.6 m in two sources"},
        {"Check": "Date range consistency (reporting periods)",     "Result": "✅ Pass",    "Details": "All documents within declared FY scope"},
        {"Check": "Ash content — washery data vs geological survey","Result": "⚠️ Warning", "Details": "2.1% variance; may reflect different sampling methods"},
        {"Check": "LTIFR — matches DGMS published figure",          "Result": "✅ Pass",    "Details": "Exact match with DGMS Annual Statistics 2024"},
    ])
    st.dataframe(consistency_df, hide_index=True, use_container_width=True)
