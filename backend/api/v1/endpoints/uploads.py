from fastapi import APIRouter, UploadFile, HTTPException, status
import pymupdf, math, random, datetime
import os

uploadsRouter= APIRouter()
#  prefix=/api/v1/uploads

@uploadsRouter.post("/upload-file")
async def upload_file(file: UploadFile):
    try:
        p1 = str(datetime.datetime.now()).replace(" ", "_")
        p2 = int(random.randint(1, 100) * (random.randint(5, 10)) )

        file_name = f"file_{p1}_{p2}_{file.filename}"

        filePath = f"../uploads/{file_name}"
        with open(filePath, "wb") as f:
            f.write(file.file.read())
        return {
            "fileName" : file_name,
            "message": "File saved successfully"
        }
    except Exception as e:
        return {"message": e.args}

@uploadsRouter.get("/extract-data")
async def extract_data_from_file(fileName : str):
    
    filePath = f"../uploads/{fileName}"

    doc = pymupdf.open(filePath)
    text=""
    for page in doc: 
        text += page.get_text()
    
    if(os.path.exists(filePath) and os.path.isfile(filePath)):
        try:
            os.remove(filePath)
            print(f"File '{filePath}' deleted successfully")
            return {"extracted_content": text}
        
        except PermissionError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied to delete file '{filePath}'"
            )
        except OSError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting file: {e}"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File '{filePath}' not found"
        )
