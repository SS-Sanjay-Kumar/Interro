import pymupdf, os
from .exceptions import UploadedFileDoesNotExist

async def extract_data_from_file(fileName : str):
    
    filePath = f"../uploads/{fileName}"

    if(os.path.exists(filePath) and os.path.isfile(filePath)):
        doc = pymupdf.open(filePath)
        text=""
        for page in doc: 
            text += page.get_text()
        print(f"File '{filePath}' contents extracted successfully")

        os.remove(filePath)
        print(f"File '{filePath}' deleted successfully")

        return text
    else:
        raise UploadedFileDoesNotExist("File does not exist or is not a file type")
