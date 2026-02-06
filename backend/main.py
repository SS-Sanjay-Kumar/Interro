from fastapi import FastAPI
from api.v1 import uploads, url_ingest, yt_transcript

app = FastAPI()

app.include_router(
    uploads.router, 
    prefix="/api/v1/uploads", 
    tags=["Uploads"]
)

app.include_router(
    url_ingest.router,
    prefix="/api/v1/url-ingest",
    tags=["URL Ingest"]
)

app.include_router(
    yt_transcript.router,
    prefix="/api/v1/yt-transcript",
)