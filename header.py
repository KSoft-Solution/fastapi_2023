from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: str | None = Header(default=None), bearer_token: str | None = Header(default=None)):
    return {"x-token": x_token, "bearer_token": bearer_token}
