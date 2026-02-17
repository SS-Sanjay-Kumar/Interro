import pymupdf, os

async def extract_data_from_file(fileName : str):
    
    filePath = f"../uploads/{fileName}"

    doc = pymupdf.open(filePath)
    text=""
    for page in doc: 
        text += page.get_text()
    
    if(os.path.exists(filePath) and os.path.isfile(filePath)):
        os.remove(filePath)
        print(f"File '{filePath}' deleted successfully")
        return {"upload": text}
    else:
        raise Exception("Error while opening the file")
