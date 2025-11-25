from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import RAGEngine

app = FastAPI()
engine = RAGEngine()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: Query):
    answer = engine.query(payload.question)
    return {"answer": answer}
