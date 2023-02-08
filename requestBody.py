import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    firstname: str
    lastname: str
    # date: datetime
    diagnosed: bool


@app.get('/')
def getHome():
    return {
        "home": "page"
    }

@app.post('/user')
def createUser(user:User):
    return {
        "message":"user created successfully!",
        "status_code":201,
        "data":user,
        "createdAt":datetime.date(2023,2,3)
    }