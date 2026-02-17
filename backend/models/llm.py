from pydantic import BaseModel

class LLMCallRequest(BaseModel):
    # file content
    fileContent: str | None
    # url content
    urlContent: str | None
    # yt transcript
    ytTranscript: str | None
 