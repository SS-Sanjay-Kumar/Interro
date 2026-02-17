from fastapi import APIRouter, HTTPException, status
import httpx
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("FAST_API_BASE_URL")
llmCallRouter = APIRouter()

@llmCallRouter.get("/health", status_code = status.HTTP_200_OK)
def check_health():
    return {"status": "ok"}

@llmCallRouter.get("/", status_code=status.HTTP_200_OK)
async def make_llm_call():
    async with httpx.AsyncClient() as client:

        try:
            uploadsResponse = await client.get(f"{BASE_URL}/uploads/extract-data")
            urlResponse = await client.get(f"{BASE_URL}/url-ingest")
            transcriptResponse = await client.get(f"{BASE_URL}/yt-transcript/{video}")