import httpx
from readability import Document
from bs4 import BeautifulSoup

async def get_url_ingest(resourceURL: str):
    async with httpx.AsyncClient() as client: 
        # * AsyncClient -> used to keep the TCP connections open
        # * if AsyncClient is not used, it would open and close the connection for every lookup
        try:
            response = await client.get(resourceURL)
            if(response.status_code!=200):
                raise Exception("Resource Not Found")
            
            doc = Document(response.text)
            soup = BeautifulSoup(doc.summary(), "html.parser")
            text = soup.get_text(separator="\n")
            return {"url" : text}
        
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                detail=f"An error occurred while requesting {exc.request.url!r}."
            )