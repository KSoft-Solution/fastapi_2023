from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


class Tags(Enum):
    MANKADA = 'mankada python',
    GHUSURI = 'ghusuri python',

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.get('/',)
def getData():
    return {
        "hello": "world"
    }


@app.get('/1', tags=[Tags.MANKADA,Tags.GHUSURI],deprecated=True)
def getData1():
    return {
        "hello": "mankidi"
    }


@app.get('/2', tags=[Tags.MANKADA],summary='PORT 1 authentication login')
def getData2():
    return {
        "hello": "mankidi"
    }


@app.get('/3', tags=[Tags.GHUSURI],description='this api is which gives you the userdetails data')
def getData3():
    return {
        "hello": "ghusuri"
    }


@app.post('/4', tags=[Tags.GHUSURI],  response_model=Item,response_description="The created item",)
def getData4(item:Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
    
