# CMPDI MineInsight AI
**AI-Powered Geological, Mining & Reporting Solution**  
Smart India Hackathon 2024 · Ministry of Coal / CIL · Team Runtime Error

---

## Quick Start

### 1. Install Node.js (required for React frontend)
Download from https://nodejs.org — pick the LTS version for Windows.
Verify: `node --version` and `npm --version`

### 2. Install frontend dependencies
```bash
cd "Team Runtime Error/frontend"
npm install
```

### 3. Run the React frontend
```bash
npm run dev
```
Open http://localhost:3000

### 4. (Later) Install Python backend dependencies
```bash
cd ..
pip install -r requirements.txt
```

### 5. (Later) Start the FastAPI backend
```bash
set GEMINI_API_KEY=your_key_here
uvicorn api.main:app --reload --port 8000
```

---

## Project Structure
```
frontend/          React + Vite frontend (all 6 pages)
  src/
    components/    Sidebar, Header
    pages/         Dashboard, DocumentManagement, QueryResponse,
                   WordCloud, ReportGenerator, DataValidation
    data/stubs.js  All mock/demo data
ingestion/         PDF parsing, chunking, ChromaDB loading
rag/               Retrieval + Gemini LLM query logic
topics/            Word cloud + TF-IDF/BERTopic
reports/           Jinja2 template + python-docx generation
data/sample_docs/  Synthetic PDF documents (8 files)
requirements.txt   Python dependencies
```
