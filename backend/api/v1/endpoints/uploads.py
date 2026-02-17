from fastapi import APIRouter, UploadFile, HTTPException, status
import random, datetime

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