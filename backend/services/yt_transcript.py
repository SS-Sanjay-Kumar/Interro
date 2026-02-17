from youtube_transcript_api import YouTubeTranscriptApi, YouTubeTranscriptApiException

from .exceptions import YTVideoDoesNotExist

async def get_transcription_from_video_id(videoId):

    ytt_api = YouTubeTranscriptApi()
    try:
        fetched_transcript = ytt_api.fetch(videoId)
        transcript = ""
        for snippet in fetched_transcript:
            transcript+=snippet.text.strip() + " "
        
        return transcript
    
    except YouTubeTranscriptApiException as e:
        raise YTVideoDoesNotExist(e)
    
