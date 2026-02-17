from fastapi import APIRouter
from api.v1.endpoints import uploads, llm_call

api_v1_router = APIRouter()

api_v1_router.include_router(
    uploads.uploadsRouter, 
    prefix="/uploads", 
    tags=["Uploads"]
)

api_v1_router.include_router(
    llm_call.llmCallRouter,
    prefix="/llm-call",
    tags=["LLM Call"]
)
