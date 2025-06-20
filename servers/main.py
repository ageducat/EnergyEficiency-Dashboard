from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Project": "EnergyEficiency"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
