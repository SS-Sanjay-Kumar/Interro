from fastapi import APIRouter, Depends, HTTPException, status
import json
from dotenv import load_dotenv
from google import genai
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from lib.db import get_db
from models.llm import LLMCallRequest
from schemas.questions import SaveQuestionRequest 

from services.exceptions import ServiceErrors
from services.uploads import extract_data_from_file
from services.url_ingest import get_url_ingest
from services.yt_transcript import get_transcription_from_video_id
from services.questions_service import save_question_service

from lib.prompt import prompt

load_dotenv()

llmCallRouter = APIRouter()

@llmCallRouter.get("/health", status_code = status.HTTP_200_OK)
def check_health():
    return {"status": "ok"}

@llmCallRouter.post("/", status_code=status.HTTP_200_OK)
async def make_llm_call(req : LLMCallRequest, db: Session = Depends(get_db)):

        fileContent = ""
        urlContent = ""
        ytTranscript = ""
        
        # uploads
        if req.fileName:
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
            except ServiceErrors as se:
                raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Service Error: {se}"
            )
        
        # url ingest
        if req.resourceURL:
            try:
                urlContent = await  get_url_ingest(req.resourceURL)
            except ServiceErrors as se:
                raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Service Error: {se}"
            )

        # yt transript
        if req.ytVideoId:
            try:
                ytTranscript = await get_transcription_from_video_id(req.ytVideoId)
            except ServiceErrors as se:
                raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Service Error: {se}"
            )
        
        # llm cal
        
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"{prompt}\nContent from the uploaded file:\n{fileContent}\nContent from a online resource URL:\n{urlContent}\nContent from a youtube video(transcript):\n{ytTranscript}"
        )

        raw_text = response.text.strip()
        # Clean the text if the LLM adds markdown backticks
        if raw_text.startswith("```"):
            # Removes the first line (```json) and the last line (```)
            raw_text = "\n".join(raw_text.split("\n")[1:-1])
            
        try:
            parsed_json = json.loads(raw_text)
            validated_data = SaveQuestionRequest(**parsed_json)

            saved_record = save_question_service(validated_data, db)
        
            return saved_record 
        
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="LLM returned invalid JSON")
        
        except ValidationError as ve:
            raise HTTPException(status_code=500, detail=f"LLM JSON didn't match schema: {ve}")
        
        except SQLAlchemyError as sqla_e:
            db.rollback()
            print("SQLAlchemy Error:", sqla_e)

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="SQLAlchemy Error"
            )
