import httpx
from readability import Document
from bs4 import BeautifulSoup

from .exceptions import ResourceURLDoesNotExist, HttpxRequestError

async def get_url_ingest(resourceURL: str):
    async with httpx.AsyncClient() as client: 
        # * AsyncClient -> used to keep the TCP connections open
        # * if AsyncClient is not used, it would open and close the connection for every lookup
        try:
            response = await client.get(resourceURL)

            if(response.status_code!=200):
                raise ResourceURLDoesNotExist("Error in Requested Resource URL")
            
            doc = Document(response.text)
            soup = BeautifulSoup(doc.summary(), "html.parser")
            text = soup.get_text(separator="\n")

            return text
        
        except httpx.RequestError as exc:
            raise HttpxRequestError(exc.message)