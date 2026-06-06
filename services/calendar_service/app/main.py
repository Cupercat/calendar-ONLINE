from fastapi import FastAPI

app = FastAPI(title="Calendar Service")

@app.get("/")
def root():
    return {"message": "Calendar Service is running"}