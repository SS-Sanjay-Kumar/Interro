from pydantic import BaseModel

class LLMCallRequest(BaseModel):
    # file content
    fileName: str | None
    # url content
    resourceURL: str | None
    # yt transcript
    ytVideoId: str | None

