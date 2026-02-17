from pydantic import BaseModel
from typing import Optional

class LLMCallRequest(BaseModel):
    fileName: Optional[str] = None
    resourceURL: Optional[str] = None
    ytVideoId: Optional[str] = None
