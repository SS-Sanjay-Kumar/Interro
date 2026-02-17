from fastapi import APIRouter
from api.v1.endpoints import uploads, url_ingest, yt_transcript, llm_call

api_v1_router = APIRouter()

api_v1_router.include_router(
    uploads.uploadsRouter, 
    prefix="/uploads", 
    tags=["Uploads"]
)

api_v1_router.include_router(
    url_ingest.urlIngestRouter,
    prefix="/url-ingest",
    tags=["URL Ingest"]
)

api_v1_router.include_router(
    yt_transcript.ytTranscriptRouter,
    prefix="/yt-transcript",
    tags=["YT Transcript"]
)

api_v1_router.include_router(
    llm_call.llmCallRouter,
    prefix="/llm-call",
    tags=["LLM Call"]
)
