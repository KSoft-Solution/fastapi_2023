from fastapi import FastAPI, Depends

app = FastAPI()
fake_items_db: list = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]

# function label dependency


def depending_fn(skip: int = 0, limit: int = 100):
    return fake_items_db[skip: skip + limit]


class DependingClass:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit


@app.get('/')
async def getUser():
    return {
        "hello": "world"
    }

# query params
# @app.get('/user/')
# def showUser(depends: any = Depends(depending_fn)):
#     return depends


@app.get('/user/')
def showUser(depends: DependingClass = Depends(DependingClass)):
    return fake_items_db[depends.skip: depends.skip + depends.limit]
