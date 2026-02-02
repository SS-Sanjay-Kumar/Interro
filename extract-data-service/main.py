from fastapi import FastAPI
import pymupdf


app = FastAPI()

@app.get("/api/extract-data")
def extract_data_from_pdf(filePath : str):
    doc = pymupdf.open(filePath)
    text=""
    for page in doc: 
        text += page.get_text()
    
    return {"content": text}
