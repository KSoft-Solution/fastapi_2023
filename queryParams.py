from fastapi import FastAPI

app = FastAPI()
fake_items_db:list = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# this is the normal path
@app.get('/')
def getAllUsers():
    return {
        "hello":"world"
    }


# path params
@app.get('/user/{username}')
def showUser(username:str):
    return {
        "user":username
    }


# query params
@app.get('/user/')
def showUser(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}