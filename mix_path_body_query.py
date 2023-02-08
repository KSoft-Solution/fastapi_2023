from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel


class Mix(BaseModel):
    name: str
    age: int
    job: str


app = FastAPI()


@app.get('/get')
def getMixPath():
    return {
        "message": "au sabu right na"
    }


# body params
@app.post('/body')
def postMix(data: Mix):
    return {
        "data": data
    }


# path, query params
@app.put('/put/{name}')
def putMix(*,
           name: str = Path(default=None),
           q: str = Query(default=None),
           b: Mix
           ):
    return {
        "path": name,
        "q": q,
        "b": b
    }


class TCS(BaseModel):
    job: str
    timing: str
    like: bool
    work: str


class Protiviti(BaseModel):
    job: str
    timing: str
    like: bool
    work: str
    whatBest: TCS


@app.post('/body_nested')
def bodyNested(betterPlaceToWork: Protiviti):
    return {
        "data": betterPlaceToWork
    }



####################################################################
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(gt=0,embed=True),
#     instagram: int = Body(lt=3),
#     q: str | None = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance,"instagram":instagram}
#     if q:
#         results.update({"q": q})
#     return results

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=False)):
    results = {"item_id": item_id, "item": item}
    return results