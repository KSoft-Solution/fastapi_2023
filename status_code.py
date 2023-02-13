from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    instagram_followers: float
    is_married: bool
    friends: list[str]
    college: str


@app.get('/', status_code=status.HTTP_200_OK)
def getUser():
    return {
        "hello": "world"
    }


@app.post('/user', status_code=status.HTTP_201_CREATED)
def getUser(user: User):
    if not user:
        return {
            "message": "failed",
            "status_code": status.HTTP_400_BAD_REQUEST,
            "updated_at": datetime.now()
        }
    return {
        "message": "success",
        "status_code": status.HTTP_201_CREATED,
        "data": user,
        "created_at": datetime.now()
    }
