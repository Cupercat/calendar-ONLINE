from fastapi import FastAPI
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service")

@app.get("/")
def root():
    return {"message": "Auth Service is running"}