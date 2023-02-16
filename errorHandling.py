from fastapi import FastAPI, HTTPException, status, Request
import base64
from fastapi.responses import JSONResponse


app = FastAPI()


class CustomError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


@app.get('/')
def getData():
    return {
        "hello": "world"
    }


@app.exception_handler(CustomError)
async def error_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Oops! {exc.name} not found"},
    )


@app.exception_handler(CustomError)
async def error_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "message": f"{exc.name} is unAuthorized"},
    )


@app.get('/user/{username}/{token}')
def getUser(username: str, token: str):
    if token != 'token data':
        raise CustomError(name=token)
    if username != 'ashok':
        raise CustomError(name=username)
    return {
        "user": username,
        "token": token
    }


# handling error
# @app.get('/user/{username}/{token}')
# def getUser(username: str, token: str):
#     if not token:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="user is un authorized",
#             headers={"token": "no token is provided"}
#         )
#     if username != 'ashok':
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='username is invalid',
#             headers={"name": "ghusuri pila"}
#         )
#     return {
#         "user": username,
#         "token": token
#     }
