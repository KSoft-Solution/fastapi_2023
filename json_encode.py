from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Model(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


fake_db = {}


app = FastAPI()


@app.get('/')
async def getData():
    return {
        "hello": "world"
    }


@app.put("/items/{id}")
def update_item(id: str, item: Model):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db
