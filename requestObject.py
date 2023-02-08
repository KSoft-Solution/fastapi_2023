from fastapi import FastAPI,Request
from pydantic import BaseModel

class Ghusuri(BaseModel):
    name:str;
    age:int;
    village:str;
    phoneNumber:int;


app = FastAPI()

@app.post('/')
def showBody(req:Request):
    return {
        "baseURL":req.base_url,
        "method":req.method,
        "host":req.headers
    }



