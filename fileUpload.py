from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get('/')
def getData():
    return {
        "hello": "world"
    }


@app.post('/upload')
def postFIle(file: bytes = File()):
    return {
        "fileDetails": len(file)
    }


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    print(contents)
    return {"filename": file.filename,
            "filetype": file.content_type,
            "max_size": file.spool_max_size,
            }
