from fastapi import FastAPI

app = FastAPI(title="Mini API", version="1.0.0")

@app.get("/v1/health")
def health():
    return {"status": "ok", "version": "v1"}

@app.get("/v2/health")
def health_v2():
    return {"status": "ok", "version": "v2"}
