from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# path parameters


@app.get('/users')
def getUsers():
    return [
        {
            "name": "ashok sahu",
            "age": 28
        },
        {
            "name": "subrat kumar gandu",
            "age": 99
        },
        {
            "name": "sibani panday",
            "age": 6
        }
    ]


@app.get('/users/{username}/{age}')
def getUsers(username:str,age:int):
    return {
        "name":username ,
        "age": age
    }


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
