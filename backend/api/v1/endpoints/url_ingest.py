from fastapi import APIRouter, status, HTTPException
import httpx
from readability import Document
from bs4 import BeautifulSoup

urlIngestRouter = APIRouter()
# prefix= /api/v1/url-ingest


@urlIngestRouter.get("/url-ingest", status_code=status.HTTP_200_OK)
async def get_url_ingest(resourceURL: str):
    async with httpx.AsyncClient() as client: 
        # * AsyncClient -> used to keep the TCP connections open
        # * if AsyncClient is not used, it would open and close the connection for every lookup
        try:
            response = await client.get(resourceURL)
            if(response.status_code!=200):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to fetch the resource"
                )
            doc = Document(response.text)
            soup = BeautifulSoup(doc.summary(), "html.parser")
            text = soup.get_text(separator="\n")
            return {"text" : text}
        
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                detail=f"An error occurred while requesting {exc.request.url!r}."
            )