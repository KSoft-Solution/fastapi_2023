from fastapi import FastAPI, Form

app = FastAPI()


@app.get('/')
def getUser():
    return {
        "hello": "world"
    }


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {
        "username": username,
        "password": password
    }
