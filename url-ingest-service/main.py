from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def check_url_ingest_service_health():
    return {
        "service": "url-ingest-service",
        "status" : "ok"
    }