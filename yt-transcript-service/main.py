from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/yt-transcript/health")
def check_transcript_service_health():
    return {
        "service": "yt-transcript-service",
        "status": "ok"
    }

@app.get("/yt-transcript/{videoId}")
def get_transcription_from_video_id(videoId):

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(videoId)
    transcript = ""
    for snippet in fetched_transcript:
        transcript+=snippet.text.strip() + " "
    
    return {"transcript": transcript}
