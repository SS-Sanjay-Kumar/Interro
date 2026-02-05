import fastapi from FastAPI()

app = FastAPI()

@app.get("/api/health")
def check_services_endpoint_health():
    return {"status": "ok"}
