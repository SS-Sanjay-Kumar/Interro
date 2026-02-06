from fastapi import FastAPI, UploadFile
import pymupdf

uploadsRouter= FastAPI()
# api/v1/uploads/

@uploadsRouter.post("/upload-file")
async def upload_file(file: UploadFile):
    try:
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}

@uploadsRouter.get("/extract-data")
def extract_data_from_file(filePath : str):
    
    filePath = f"uploads/{filePath}"

    doc = pymupdf.open(filePath)
    text=""
    for page in doc: 
        text += page.get_text()
    
    return {"extracted_content": text}
