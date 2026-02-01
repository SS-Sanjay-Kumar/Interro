from fastapi import FastAPI, status, HTTPException
import httpx

app = FastAPI()

@app.get("/api/health")
def check_url_ingest_service_health():
    return {
        "service": "url-ingest-service",
        "status" : "ok"
    }

@app.get("/api/url-ingest", status_code=status.HTTP_200_OK)
async def get_url_ingest(resourceURL: str):
    async with httpx.AsyncClient() as client: # * AsyncClient -> used to keep the TCP connections open
        # if AsyncClient is not used, it would open and close the connection for every lookup
        try:
            print("Resource URL -> ",resourceURL)
            response = await client.get(resourceURL)
            if(response.status_code!=200):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to fetch the resource"
                )
            return response.text
        
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                detail=f"An error occurred while requesting {exc.request.url!r}."
            )