from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Project": "EnergyWise"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
