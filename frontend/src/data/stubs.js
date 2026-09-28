export const SUBSIDIARIES = [
  { code: 'ALL',   name: 'All Subsidiaries' },
  { code: 'ECL',   name: 'ECL — Eastern Coalfields Ltd' },
  { code: 'BCCL',  name: 'BCCL — Bharat Coking Coal Ltd' },
  { code: 'CCL',   name: 'CCL — Central Coalfields Ltd' },
  { code: 'NCL',   name: 'NCL — Northern Coalfields Ltd' },
  { code: 'SECL',  name: 'SECL — South Eastern Coalfields Ltd' },
  { code: 'WCL',   name: 'WCL — Western Coalfields Ltd' },
  { code: 'MCL',   name: 'MCL — Mahanadi Coalfields Ltd' },
  { code: 'HQ',    name: 'CMPDIL — Headquarters' },
]

export const MINES = [
  'Jharia Coalfield (BCCL)',
  'Raniganj Coalfield (ECL)',
  'Singrauli Coalfield (NCL)',
  'Talcher Coalfield (MCL)',
  'Ib Valley Coalfield (MCL)',
  'Korba Coalfield (SECL)',
  'Chirimiri Coalfield (SECL)',
  'Wardha Valley Coalfield (WCL)',
]

export const REPORT_TYPES = [
  'Quarterly Production Report',
  'Annual Geological Survey Summary',
  'Reserve Estimation Report',
  'Environmental Compliance Report',
  'Parliamentary Question Response',
  'High-Priority Administrative Inquiry',
  'Safety & DGMS Compliance Report',
  'Borehole Survey Summary',
  'Mine Closure & Rehabilitation Report',
]

export const STUB_DOCS = [
  { name: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf',  type: 'PDF',   pages: 84,  size: '4.2 MB',  status: 'Indexed', chunks: 312, subsidiary: 'HQ',   date: '2024-01-15' },
  { name: 'ECL_Production_Report_Q3_FY2024.pdf',             type: 'PDF',   pages: 38,  size: '1.8 MB',  status: 'Indexed', chunks: 144, subsidiary: 'ECL',  date: '2024-01-18' },
  { name: 'Jharia_Coalfield_Resource_Assessment_2022.pdf',   type: 'PDF',   pages: 112, size: '7.1 MB',  status: 'Indexed', chunks: 418, subsidiary: 'BCCL', date: '2024-01-18' },
  { name: 'MCL_Environmental_Compliance_FY2023.pdf',         type: 'PDF',   pages: 56,  size: '3.4 MB',  status: 'Indexed', chunks: 208, subsidiary: 'MCL',  date: '2024-01-19' },
  { name: 'Coal_Reserve_Estimation_India_2023.pdf',          type: 'PDF',   pages: 96,  size: '5.6 MB',  status: 'Indexed', chunks: 357, subsidiary: 'HQ',   date: '2024-01-20' },
  { name: 'NCL_Safety_Incident_Report_FY2024.pdf',           type: 'PDF',   pages: 44,  size: '2.1 MB',  status: 'Indexed', chunks: 163, subsidiary: 'NCL',  date: '2024-01-21' },
  { name: 'Geological_Borehole_Survey_Singrauli_2022.pdf',   type: 'PDF',   pages: 68,  size: '9.3 MB',  status: 'Indexed', chunks: 251, subsidiary: 'NCL',  date: '2024-01-22' },
  { name: 'SECL_Production_Forecast_FY2025.pdf',             type: 'PDF',   pages: 29,  size: '1.2 MB',  status: 'Indexed', chunks: 109, subsidiary: 'SECL', date: '2024-01-22' },
]

export const DATA_SOURCES = [
  { type: 'Geological Survey PDFs',         support: '✓ Supported',   notes: 'Text via pdfplumber; digital PDFs only' },
  { type: 'Production Reports (Excel/CSV)', support: '✓ Supported',   notes: 'pandas read_excel / read_csv' },
  { type: 'Word Documents (.docx)',         support: '✓ Supported',   notes: 'python-docx text extraction' },
  { type: 'Historical Archives (.zip)',     support: '✓ Supported',   notes: 'Recursive unzip + ingestion' },
  { type: 'Geological Maps / Images',       support: '⏳ Phase 6',    notes: 'Vision model + OCR pipeline' },
  { type: 'Scanned PDFs',                   support: '⏳ Phase 6',    notes: 'Tesseract OCR integration' },
  { type: 'SharePoint / Network Drive',     support: '⏳ Phase 5',    notes: 'CIL subsidiary integration' },
  { type: 'Live Portal / API Data',         support: '⏳ Phase 5',    notes: 'MoEFCC / DGMS portal feeds' },
]

export const HISTORICAL_ARCHIVES = [
  { id: 'HA-1984-JH', year: 1984, mine: 'Jharia Coalfield', sub: 'BCCL', title: 'Deep Seam Stratigraphy & Firedamp Log (Borehole #JH-84-12)', depth: '480 m', type: 'Scanned Borehole Log', status: 'Digitized OCR (94% conf.)', score: 0.94, excerpt: 'Encountered Seam XVIII at depth 342.5m; gas emission rate 7.8 m3/tonne. Barakar formation sandstones predominate.' },
  { id: 'HA-1992-RG', year: 1992, mine: 'Raniganj Coalfield', sub: 'ECL', title: 'Raniganj Basin Geological Cross-Section & Fault Analysis', depth: '310 m', type: 'Digitized Map & Memoir', status: 'Digitized OCR (91% conf.)', score: 0.89, excerpt: 'Disraigarh seam thickness recorded at 4.2m with dip of 6 degrees. Colliery boundaries reconciled with GSI base map.' },
  { id: 'HA-1998-SG', year: 1998, mine: 'Singrauli Coalfield', sub: 'NCL', title: 'Jayant & Dudhichua Block Overburden & Stripping Ratio Study', depth: '220 m', type: 'Historical Technical Report', status: 'Digitized OCR (96% conf.)', score: 0.92, excerpt: 'Historical stripping ratio estimated at 2.9:1. Heavy earth moving machinery deployment roadmap for FY 1999-2004.' },
  { id: 'HA-2005-TL', year: 2005, mine: 'Talcher Coalfield', sub: 'MCL', title: 'Talcher Thermal Coal Reserve & Ash Content Assessment', depth: '190 m', type: 'Resource Assessment', status: 'Digitized PDF', score: 0.87, excerpt: 'Measured non-coking coal resources in Ananta and Bharatpur blocks total 4.2 billion tonnes. Average gross calorific value 4,200 kcal/kg.' },
  { id: 'HA-2011-KR', year: 2011, mine: 'Korba Coalfield', sub: 'SECL', title: 'Gevra Opencast Expansion & Hydrogeological Survey', depth: '260 m', type: 'Hydrogeological Memoir', status: 'Digitized PDF', score: 0.85, excerpt: 'Aquifer recharge rate measured at 14.2% of annual precipitation. Dewatering schedule formulated for lower seam extraction.' },
]

export const SUBSIDIARY_TOPICS = {
  'Full Corpus': [
    { label: 'Coal Reserve Estimation', weight: 0.89 },
    { label: 'Underground Longwall Mining', weight: 0.84 },
    { label: 'Environmental & Forest Clearance', weight: 0.78 },
    { label: 'Production Targets & Dispatch', weight: 0.76 },
    { label: 'Geological Seam Stratigraphy', weight: 0.73 },
    { label: 'Overburden Removal (OBR)', weight: 0.69 },
    { label: 'Safety & DGMS Compliance', weight: 0.65 },
    { label: 'Hydrogeology & Methane Drainage', weight: 0.61 },
  ],
  ECL: [
    { label: 'Raniganj Coalfield Seam Analysis', weight: 0.91 },
    { label: 'Sonepur Bazari & Rajmahal OCP', weight: 0.86 },
    { label: 'Longwall Mechanisation (Jhanjra)', weight: 0.82 },
    { label: 'OBR Stripping Ratio Compliance', weight: 0.74 },
  ],
  BCCL: [
    { label: 'Prime Coking Coal Reserves', weight: 0.93 },
    { label: 'Jharia Coalfield Mine Fire Control', weight: 0.88 },
    { label: 'Methane Gas (Firedamp) Drainage', weight: 0.81 },
    { label: 'Underground Gallery Rehabilitation', weight: 0.75 },
  ],
  NCL: [
    { label: 'Singrauli Opencast Operations', weight: 0.92 },
    { label: 'Dragline Utilisation & Stripping', weight: 0.87 },
    { label: 'Dudhichua & Jayant Block Output', weight: 0.81 },
    { label: 'LTIFR Zero-Accident Protocol', weight: 0.79 },
  ],
  MCL: [
    { label: 'Talcher & Ib Valley Exploration', weight: 0.90 },
    { label: 'Thermal Power Utility Coal Dispatch', weight: 0.85 },
    { label: 'MoEFCC Air & Water Compliance', weight: 0.80 },
    { label: 'Borehole Core Recovery Audits', weight: 0.74 },
  ],
  SECL: [
    { label: 'Gevra & Kusmunda Mega-OCP Output', weight: 0.94 },
    { label: 'Korba Coalfield Stratigraphy', weight: 0.86 },
    { label: 'Production Target Surpluses', weight: 0.79 },
    { label: 'Rail Infrastructure & Logistics', weight: 0.73 },
  ],
}

export const QA_KNOWLEDGE_BASE = [
  {
    keywords: ['reserve', 'eastern', 'ecl', 'total coal reserve'],
    answer: `Based on the geological survey reports and GSI data, **total proven coal reserves in the Eastern Coalfields region stand at 18.7 billion tonnes** (measured resources: 31.2 billion tonnes) as of FY 2023-24. The Jharia coalfield alone holds **3.55 billion tonnes of prime coking coal** (~19% of national total), while Raniganj and adjoining ECL blocks provide vital high-grade non-coking coal. Seam thickness ranges between 1.2m and 6.4m with an average ash content of 24.3%.`,
    sources: [
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 14, score: 0.95, excerpt: '...total proven reserves in Eastern Coalfields zone stand at 18.7 billion tonnes as assessed by GSI in collaboration with CMPDI...' },
      { doc: 'Coal_Reserve_Estimation_India_2023.pdf', page: 8, score: 0.91, excerpt: '...India total coal resources stand at 361.30 BT; Eastern Coalfields region accounts for 12.6% of national proven reserve base...' },
      { doc: 'Jharia_Coalfield_Resource_Assessment_2022.pdf', page: 22, score: 0.86, excerpt: '...prime coking coal reserves in Jharia estimated at 3.55 billion tonnes, representing 19.0% of national total...' },
    ],
  },
  {
    keywords: ['thickness', 'jharia', 'seam', 'kusunda'],
    answer: `In the Jharia coalfield, **coal seam thickness averages 3.4 metres**, with individual seams ranging from 0.8 m up to 24.0 m in the Lower Gondwana (Barakar) formation. The thickest recorded seam is the **XVIII seam in the Kusunda area measuring 24.0 metres**. Dip of seams ranges from 4° to 15° towards south/southeast at depths from surface to 600 metres. Average ash content is 24.3%, with metallurgical-grade coking seams registering 18–21% ash.`,
    sources: [
      { doc: 'Jharia_Coalfield_Resource_Assessment_2022.pdf', page: 22, score: 0.96, excerpt: '...seam thickness in Jharia block averages 3.4 metres, with individual seams ranging from 0.8 m to 24.0 m (XVIII seam, Kusunda)...' },
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 3, score: 0.89, excerpt: '...average coal seam thickness across surveyed blocks is 4.1 metres; Jharia Barakar formation exhibits seam dip 4 to 15 degrees...' },
    ],
  },
  {
    keywords: ['production', 'target', 'q3', 'dispatch', 'fy2024'],
    answer: `During Q3 FY 2023-24, **coal dispatch reached 142.6 MT**, exceeding the target of 138 MT by **3.3%**. Quarterly coal production reached **7.84 MT against a target of 7.50 MT (+4.5% achievement)**, marking a **7.2% YoY growth**. This performance was driven by enhanced deployment of powered roof support longwalls at Sonepur Bazari & Jhanjra mines, alongside 94% mechanical loading in Rajmahal opencast.`,
    sources: [
      { doc: 'ECL_Production_Report_Q3_FY2024.pdf', page: 1, score: 0.97, excerpt: '...quarterly coal production reached 7.84 MT (target 7.50 MT, +4.5%). Cumulative coal dispatch reached 142.6 MT, surpassing target of 138 MT...' },
      { doc: 'ECL_Production_Report_Q3_FY2024.pdf', page: 6, score: 0.90, excerpt: '...7.2% YoY increase driven by longwall deployment in Jhanjra and improved dragline cycle times at Rajmahal OCP...' },
    ],
  },
  {
    keywords: ['environment', 'compliance', 'mcl', 'moefcc', 'air', 'water'],
    answer: `All active coalfields across Mahanadi Coalfields Limited (MCL) maintain **current and valid environmental clearances (EC)** with the next comprehensive MoEFCC review scheduled for **FY 2026-27**. Continuous ambient air quality monitoring (CAAQMS) and effluent treatment systems operate at 100% compliance across Talcher and Ib Valley. Zero material non-compliance notices under the Environment Protection Act, 1986 were recorded during the reporting period.`,
    sources: [
      { doc: 'MCL_Environmental_Compliance_FY2023.pdf', page: 4, score: 0.94, excerpt: '...all environmental clearances for Talcher and Ib Valley operational blocks are valid through FY 2026-27 with zero non-compliance under EPA 1986...' },
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 62, score: 0.88, excerpt: '...effluent treatment and dust suppression systems meet CPCB norms; green belt plantation target achieved at 112%...' },
    ],
  },
  {
    keywords: ['obr', 'stripping', 'ratio', 'overburden', 'opencast'],
    answer: `The **average Overburden Removal (OBR) stripping ratio across CIL opencast mines is 3.8 cubic metres per tonne of coal extracted**. At Rajmahal OCP the stripping ratio is 3.2:1, while at Sonepur Bazari it stands at 4.1:1. Overburden removal during Q3 reached **42.1 million cubic metres (Mcm)** against a planned target of 40.0 Mcm (+5.25% achievement).`,
    sources: [
      { doc: 'ECL_Production_Report_Q3_FY2024.pdf', page: 1, score: 0.96, excerpt: '...overburden removal 42.1 Mcm vs target 40.0 Mcm; OBR stripping ratio recorded at 3.8 cubic metres per tonne of coal...' },
      { doc: 'SECL_Production_Forecast_FY2025.pdf', page: 9, score: 0.89, excerpt: '...opencast stripping ratios across mega projects (Gevra, Kusmunda) optimized with 42-cum shovel-dumper combinations...' },
    ],
  },
  {
    keywords: ['safety', 'ltifr', 'dgms', 'incident', 'fatality'],
    answer: `The **Lost Time Injury Frequency Rate (LTIFR) for FY 2023-24 improved to 0.23 per lakh man-shifts**, representing a **14% year-on-year reduction** and surpassing Directorate General of Mines Safety (DGMS) benchmarks. Zero fatal incidents occurred in mechanized longwall and continuous miner sections. Safety training coverage reached 98.4% of all front-line mining personnel.`,
    sources: [
      { doc: 'NCL_Safety_Incident_Report_FY2024.pdf', page: 18, score: 0.95, excerpt: '...LTIFR stands at 0.23 per lakh man-shifts vs 0.27 in FY2023; safety compliance audits completed across 100% of working districts...' },
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 71, score: 0.88, excerpt: '...mechanised roof bolting and real-time convergence monitoring reduced strata control incidents by 31%...' },
    ],
  },
  {
    keywords: ['methane', 'firedamp', 'drainage', 'gas'],
    answer: `Active **methane gas drainage capacity across Jharia coalfield mines is approximately 12,000 m³/hour** (approx. 288,000 m³/day) through a combined network of in-seam boreholes and surface pre-drainage wells. In shallow seams gas content averages 4.8 m³/tonne, rising to 8.2 m³/tonne in deep seams below 200m depth. Commercial coalbed methane (CBM) capture feasibility studies are ongoing with CMPDI.`,
    sources: [
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 3, score: 0.96, excerpt: '...firedamp drainage capacity in BCCL active mines is 12,000 m3/hr; gas content rises from 4.8 m3/t in shallow seams to 8.2 m3/t below 200m...' },
      { doc: 'Jharia_Coalfield_Resource_Assessment_2022.pdf', page: 31, score: 0.90, excerpt: '...drainage network prevents flammable gas accumulation in underground longwall return airways...' },
    ],
  },
  {
    keywords: ['coking', 'non-coking', 'grade', 'metallurgical'],
    answer: `India's total prime coking coal reserves stand at **3.55 billion tonnes**, situated almost exclusively in the **Jharia coalfield under BCCL jurisdiction** (~19% of national coking resource). Medium and semi-coking coals contribute an additional 5.1 billion tonnes across Raniganj and Central Coalfields. Non-coking coal constitutes 81.6% of national resources (predominantly Grades D through G), powering national thermal generation.`,
    sources: [
      { doc: 'Coal_Reserve_Estimation_India_2023.pdf', page: 12, score: 0.95, excerpt: '...coking coal constitutes 18.4% of national reserves; prime coking coal estimated at 3.55 BT concentrated in Jharia coalfield...' },
      { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 2, score: 0.91, excerpt: '...non-coking coal accounts for 81.6% of national proven inventory of 148.46 billion tonnes...' },
    ],
  },
]

export const STUB_ANSWER = QA_KNOWLEDGE_BASE[0]

export const PARL_STUB = `MINISTRY OF COAL — PARLIAMENTARY QUESTION RESPONSE

Question No.: Starred Q. 47 (Lok Sabha Session — Government of India)
Subject: Coal Reserve Status and Production Performance in Eastern India

REPLY ON BEHALF OF THE MINISTER OF COAL:

(a) The total proven coal reserves in the Eastern Coalfields region (covering Jharia, Raniganj, and adjoining blocks) stand at 18.7 billion tonnes as assessed jointly by the Geological Survey of India (GSI) and CMPDI during 2022-23. This represents approximately 12.6% of India's total proven coal reserve base.

(b) Production during Q3 FY 2023-24 reached 7.84 MT (exceeding target by 4.5%), while cumulative dispatch reached 142.6 MT, exceeding the set target of 138 MT by 3.3%. This improvement is attributable to enhanced deployment of longwall technology and increased mechanisation in underground mines operated by ECL and BCCL.

(c) All environmental clearances for active coalfields in the region are current and valid, with the next scheduled review in FY 2026-27. No material non-compliance has been recorded under the Environment Protection Act, 1986 during the reporting period.

—————————————————————————————
Sources: [1] CMPDI Annual Geological Survey Report 2023, p.14  |  [2] ECL Production Report Q3 FY2024, p.6  |  [3] Jharia Coalfield Resource Assessment 2022, p.22
This response has been automatically drafted for review by the authorised officer before submission.`

export const STUB_TOPICS = SUBSIDIARY_TOPICS['Full Corpus']

export const STUB_KEYWORDS = [
  'coalfield','seam','reserves','overburden','longwall','borehole',
  'stratigraphy','OBR ratio','DGMS','methane','aquifer','opencast',
  'washery','coking coal','dispatch','non-coking','blasting','subsidence',
  'exploration','MT','CMPDI','ECL','BCCL','NCL','MCL','stripping ratio',
  'geological section','dip','strike','calorific value',
]

export const VALIDATION_RECORDS = [
  { field: 'Total Proven Reserves (Eastern CF)',  extracted: '18.7 BT',     crosscheck: 'GSI 2023 Report p.14',    status: 'Validated', confidence: 97 },
  { field: 'Q3 FY2024 Production (ECL)',          extracted: '142.6 MT',    crosscheck: 'ECL Q3 Report p.6',       status: 'Validated', confidence: 95 },
  { field: 'Average Seam Thickness (Jharia)',     extracted: '3.4 m',       crosscheck: 'Borehole Survey 2022',    status: 'Validated', confidence: 91 },
  { field: 'Average Ash Content',                 extracted: '24.3%',       crosscheck: 'Washery data FY2023',     status: 'Partial',   confidence: 78 },
  { field: 'OBR Ratio (opencast mines)',          extracted: '3.8 : 1',     crosscheck: 'SECL Annual Report',      status: 'Validated', confidence: 89 },
  { field: 'LTIFR (Safety Metric)',               extracted: '0.23',        crosscheck: 'DGMS Annual Stats 2024',  status: 'Validated', confidence: 93 },
  { field: 'Environmental Clearance Validity',    extracted: 'Until 2027',  crosscheck: 'MoEFCC Portal',           status: 'Partial',   confidence: 72 },
  { field: 'Active Mine Galleries (total)',       extracted: '214',         crosscheck: 'No cross-ref available',  status: 'Unverified',confidence: 45 },
]

export const LINEAGE_RECORDS = [
  { value: '18.7 BT reserves',     doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf', page: 14, chunk: 'chk_0042', method: 'RAG + regex' },
  { value: '142.6 MT production',  doc: 'ECL_Production_Report_Q3_FY2024.pdf',            page:  6, chunk: 'chk_0198', method: 'RAG + regex' },
  { value: '3.4 m seam thickness', doc: 'Jharia_Coalfield_Resource_Assessment_2022.pdf',  page: 22, chunk: 'chk_0731', method: 'RAG + NER'   },
  { value: '24.3% ash content',    doc: 'Coal_Reserve_Estimation_India_2023.pdf',         page: 47, chunk: 'chk_1102', method: 'RAG + regex' },
  { value: '3.8:1 OBR ratio',      doc: 'SECL_Production_Forecast_FY2025.pdf',            page:  9, chunk: 'chk_2201', method: 'RAG + table' },
  { value: '0.23 LTIFR',           doc: 'NCL_Safety_Incident_Report_FY2024.pdf',          page: 18, chunk: 'chk_1874', method: 'RAG + regex' },
]

export const CONSISTENCY_CHECKS = [
  { check: 'Reserve figures — cross-doc consistency',         result: 'Pass',    detail: '3 documents report the same order of magnitude' },
  { check: 'Production targets vs actuals alignment',         result: 'Pass',    detail: 'Q3 actuals exceed target by 3.3%' },
  { check: 'Seam thickness — borehole vs survey report',      result: 'Warning', detail: 'Minor discrepancy: 3.4 m vs 3.6 m across two sources' },
  { check: 'Date range consistency (reporting periods)',       result: 'Pass',    detail: 'All documents within declared FY 2023-24 scope' },
  { check: 'Ash content — washery data vs geological survey', result: 'Warning', detail: '2.1% variance; may reflect different sampling methods' },
  { check: 'LTIFR — matches DGMS published figure',           result: 'Pass',    detail: 'Exact match with DGMS Annual Statistics 2024' },
]

export const AUDIT_LOG = [
  { ts: '2024-01-22 09:14', action: 'Document Ingested',   doc: 'SECL_Production_Forecast_FY2025.pdf',          user: 'System', status: 'Success' },
  { ts: '2024-01-22 09:10', action: 'Document Ingested',   doc: 'Geological_Borehole_Survey_Singrauli_2022.pdf', user: 'System', status: 'Success' },
  { ts: '2024-01-22 08:45', action: 'Report Generated',    doc: 'Jharia_Q3_Summary_Report.docx',                user: 'Admin',  status: 'Success' },
  { ts: '2024-01-21 16:30', action: 'Query Answered',      doc: 'RAG Query #47',                                user: 'Admin',  status: 'Success' },
  { ts: '2024-01-21 14:22', action: 'Parliamentary Draft', doc: 'Starred Q.47 Draft',                           user: 'Admin',  status: 'Success' },
  { ts: '2024-01-21 11:05', action: 'Validation Run',      doc: 'Corpus-wide validation',                       user: 'System', status: 'Warning — 2 fields partial' },
]

export const ROADMAP = [
  { phase: '1', title: 'Requirement Analysis',           status: 'Complete',     desc: 'Problem scoping, data audit, stakeholder interviews with CMPDI/CIL teams' },
  { phase: '2', title: 'Data Digitisation & Ingestion',  status: 'In Progress',  desc: 'PDF/Excel/image ingestion pipeline, chunking, embedding generation' },
  { phase: '3', title: 'Platform Development',           status: 'In Progress',  desc: 'RAG system, report generator, topic module, React + FastAPI application' },
  { phase: '4', title: 'System Testing & Validation',    status: 'Upcoming',     desc: 'Accuracy benchmarks, validation suite, QA on full sample corpus' },
  { phase: '5', title: 'CIL Integration & Training',     status: 'Upcoming',     desc: 'CIL subsidiary workflow integration, user training programmes' },
  { phase: '6', title: 'Continuous Enhancement',         status: 'Upcoming',     desc: 'OCR for scanned docs, model fine-tuning, scalability, feedback loops' },
]

export const SAMPLE_QUESTIONS = [
  'What are the total coal reserves in the Eastern Coalfields?',
  'What is the average seam thickness in the Jharia block?',
  'How did Q3 FY2024 production compare to target?',
  'What is the environmental compliance status of MCL mines?',
  'What is the OBR ratio in opencast mines?',
  'What are the LTIFR safety statistics for FY2024?',
  'What are India\'s total coking coal reserves?',
  'What is the methane drainage capacity in Jharia?',
]
