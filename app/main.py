from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_flow import run_rag_flow

app = FastAPI(title="Asturias Rústica Occidental RAG")

class Query(BaseModel):
    question: str

@app.post("/rag")
def rag_endpoint(query: Query):
    result = run_rag_flow(query.question)
    return {"answer": result}

@app.get("/")
def root():
    return {"message": "Asturias Rústica Occidental API"}

