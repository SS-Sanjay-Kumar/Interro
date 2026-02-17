from fastapi import APIRouter, HTTPException, status
import os
from dotenv import load_dotenv
from google import genai

from models.llm import LLMCallRequest

from services.uploads import extract_data_from_file
from services.url_ingest import get_url_ingest
from services.yt_transcript import get_transcription_from_video_id

load_dotenv()

BASE_URL = os.getenv("FAST_API_BASE_URL")
llmCallRouter = APIRouter()

@llmCallRouter.get("/health", status_code = status.HTTP_200_OK)
def check_health():
    return {"status": "ok"}

@llmCallRouter.post("/", status_code=status.HTTP_200_OK)
async def make_llm_call(req : LLMCallRequest):

        fileContent = {"upload":""}
        urlContent = {"url":""}
        ytTranscript = {"transcript":""}

        if req.fileName!="":
            try:
                fileContent = await extract_data_from_file(req.fileName)
            except PermissionError:
                raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied to delete file '{req.fileName}'"
            )
            except OSError as e:
                raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting file: {e}"
            )
        if req.resourceURL!="":
            urlContent = await  get_url_ingest(req.resourceURL)
        if req.ytVideoId!="":
            ytTranscript = await get_transcription_from_video_id(req.ytVideoId)
        
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Summarize the below text using analogy, max word limit 50\n {fileContent["upload"]} \n{urlContent["url"]} \n{ytTranscript["transcript"]}"
        )

        print(response.text)
        return {"response":response.text}
