from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, Required


class Student(BaseModel):
    name: str | None = Field(default=Required, max_length=5, example='mankidi')
    college: str | None = Field(default='bhadrak bhandari college',
                                max_length=20, min_length=10, example='mankada college')
    age: int | None = Field(default=20, gt=20, example=15)
    daysAlive: float = Field(..., lt=10, gt=40)
    course: str
    friends: list
    isMarried: bool


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get('/')
def getField():
    return {
        "hello": "world!"
    }


# @app.post('/example')
# def example(student: Student):
#     return {
#         "data": student
#     }


# @app.put("/items")
# def update_item(
#     item: Item = Body(
#         example={
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2,
#         },
#     ),
# ):
#     results = {"item": item}
#     return results


@app.put("/items")
def update_item(
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item": item}
    return results
