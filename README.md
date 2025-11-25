# Urban_Policy_RAG_Assistant-_FAISS-FastAPI
RAG-based Intelligent Policy Assistant (Python, FAISS, FastAPI, LangChain)

#### https://www.youtube.com/watch?v=_HQ2H_0Ayy0
    

✅ 1. Project Overview

Project Name:
📌 RAG-Based Intelligent Policy Assistant (Python, FAISS, FastAPI, LangChain)

Goal:
Allow a user to upload or query urban planning rules (PDF, DOCX…), index them, and ask questions using RAG.

✅ 2. Architecture (simple but complete)

```
  Documents (PDF, DOCX)
             ↓
  Ingestion pipeline
             ↓
  Text splitter (LangChain)
             ↓
  Embeddings (SentenceTransformers)
             ↓
  Vector Store (FAISS or ChromaDB)
            ↓
  FastAPI RAG endpoint
            ↓
  UI (Streamlit)
```


✅ 3. Recommended Tech Stack

```
| Component     | Choice                                           |
| ------------- | ------------------------------------------------ |
| Language      | Python 3.10+                                     |
| Embeddings    | `sentence-transformers` (e.g., all-MiniLM-L6-v2) |
| Vector DB     | FAISS (simple) OR ChromaDB (easier persistence)  |
| RAG Framework | LangChain                                        |
| Backend API   | FastAPI                                          |
| UI            | Streamlit                                        |
| Docs parsing  | `pypdf`, `docx2txt`                              |
| Container     | Docker + Docker Compose                          |
```


✅ 4. Repository Structure (copy/paste)

```
rag-intelligent-policy-assistant/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion.py
│   ├── embed_store.py
│   ├── rag_engine.py
│   ├── api.py   (FastAPI)
│   └── ui.py    (Streamlit)
│
├── models/
│   └── faiss_index/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

















