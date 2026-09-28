# PRAGYA — CMPDI MineInsight AI
**AI-Powered Geological, Mining & Reporting Solution**  
Smart India Hackathon · Ministry of Coal / Coal India Limited (CIL) · Team Runtime Error

---

## Quick Start

### 1. Install Node.js (required for React frontend)
Download from https://nodejs.org — LTS version for Windows.
Verify: `node --version` and `npm --version`

### 2. Install frontend dependencies
```bash
cd frontend
npm install
```

### 3. Run the React frontend
```bash
npm run dev
```
Open **http://localhost:3000** in your browser.

### 4. (Optional) Run the FastAPI RAG backend
```bash
# In the project root:
pip install -r requirements.txt
set GEMINI_API_KEY=your_key_here
uvicorn backend:app --reload --port 8000
```
*Note: The frontend has built-in offline retrieval and works seamlessly out of the box even without starting the backend.*

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
