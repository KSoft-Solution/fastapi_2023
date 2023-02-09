from fastapi import FastAPI,Body
from pydantic import BaseModel, Field


class BodyField(BaseModel):
    name: str
    description: str | None = Field(
        default=None, max_length=10, description='please enter here the description')
    currency: float | None = Field(default=None, ge=10)


app = FastAPI()


@app.get('/')
def getReq():
    return {
        "hello ": "world"
    }


@app.post('/bodyData')
def getBodyData(profile: BodyField = Body(embed=False)):
    return {
        "body fields": profile
    }
