from fastapi import APIRouter
from youtube_transcript_api import YouTubeTranscriptApi

router = APIRouter()

@router.get("get-transcript/{videoId}")
def get_transcription_from_video_id(videoId):

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(videoId)
    transcript = ""
    for snippet in fetched_transcript:
        transcript+=snippet.text.strip() + " "
    
    return {"transcript": transcript}
