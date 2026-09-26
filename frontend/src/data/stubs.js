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

export const STUB_ANSWER = {
  answer: `Based on the geological survey reports and annual production data, **coal reserves in the Eastern Coalfields region are estimated at approximately 18.7 billion tonnes** as of FY 2023-24. The Jharia coalfield alone accounts for nearly 19% of India's total prime coking coal reserves. Seam thickness varies between 1.2 m and 6.4 m across the surveyed blocks, with an average ash content of 24.3%. Production in Q3 FY 2023-24 reached **142.6 MT**, reflecting a 7.2% YoY increase driven by improved mechanisation in underground mines.`,
  sources: [
    { doc: 'CMPDI_Annual_Geological_Survey_Report_2023.pdf',  page: 14, score: 0.92, excerpt: '...total proven reserves in the Eastern Coalfields zone stand at 18.7 billion tonnes as assessed by GSI in collaboration with CMPDI during 2022-23...' },
    { doc: 'ECL_Production_Report_Q3_FY2024.pdf',             page: 6,  score: 0.87, excerpt: '...quarterly coal dispatch reached 142.6 MT, surpassing the target of 138 MT. Improvement attributed to enhanced longwall deployment in Jharia and Raniganj blocks...' },
    { doc: 'Jharia_Coalfield_Resource_Assessment_2022.pdf',   page: 22, score: 0.81, excerpt: '...prime coking coal reserves in Jharia coalfield estimated at 3.55 billion tonnes, representing 19.0% of the national total prime coking coal reserve base...' },
  ],
}

export const PARL_STUB = `MINISTRY OF COAL — PARLIAMENTARY QUESTION RESPONSE

Question No.: Starred Q. 47 (Lok Sabha Session — Demo)
Subject: Coal Reserve Status and Production Performance in Eastern India

REPLY ON BEHALF OF THE MINISTER OF COAL:

(a) The total proven coal reserves in the Eastern Coalfields region (covering Jharia, Raniganj, and adjoining blocks) stand at 18.7 billion tonnes as assessed jointly by the Geological Survey of India (GSI) and CMPDI during 2022-23. This represents approximately 26.4% of India's total coal reserve base.

(b) Production during Q3 FY 2023-24 reached 142.6 MT, exceeding the set target of 138 MT by 3.3%. This improvement is attributable to enhanced deployment of longwall technology and increased mechanisation in underground mines operated by ECL and BCCL.

(c) All environmental clearances for active coalfields in the region are current and valid, with the next scheduled review in FY 2026-27. No material non-compliance has been recorded under the Environment Protection Act, 1986 during the reporting period.

—————————————————————————————
Sources: [1] CMPDI Annual Geological Survey Report 2023, p.14  |  [2] ECL Production Report Q3 FY2024, p.6  |  [3] Jharia Coalfield Resource Assessment 2022, p.22
This response has been automatically drafted for review by the authorised officer before submission.`

export const STUB_TOPICS = [
  { label: 'Coal Reserve Estimation',        weight: 0.89 },
  { label: 'Underground Mining Operations',  weight: 0.84 },
  { label: 'Environmental Compliance',       weight: 0.78 },
  { label: 'Production Targets & Output',    weight: 0.76 },
  { label: 'Geological Seam Analysis',       weight: 0.73 },
  { label: 'Overburden Removal (OBR)',        weight: 0.69 },
  { label: 'Safety & DGMS Compliance',       weight: 0.65 },
  { label: 'Hydrogeology & Water Table',     weight: 0.61 },
  { label: 'Borehole Drilling & Surveys',    weight: 0.58 },
  { label: 'Coking vs Non-Coking Coal',      weight: 0.54 },
]

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
