from fastapi import FastAPI
from app.rq_tasks import process_ai_request

app = FastAPI(title="Neural Service")

@app.get("/")
def root():
    return {"message": "Neural Service is running"}

@app.post("/ask")
def ask_ai(prompt: str):
    job = process_ai_request.delay(prompt)
    return {"job_id": job.id, "status": "queued"}