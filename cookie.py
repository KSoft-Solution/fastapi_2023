from fastapi import FastAPI,Cookie

app = FastAPI()
@app.get('/')
def home():
    return{
        "home":"home page"
    }

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default="i am cookie")):
    return {"ads_id": ads_id}