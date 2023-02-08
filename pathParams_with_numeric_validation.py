from fastapi import FastAPI, Path, Query,Request
from pydantic import Required

app = FastAPI()


@app.get('/')
def homePage(req:Request):
    print(req._query_params,'request object')
    return {
        "hello world"
    }


# simple path param
@app.get('/{path}')
def pathParam(path):
    print({"path": path})
    return {
        "path": path
    }


# simple path param with Path class
@app.get('/path/{path}')
def pathParamWithPath(path: int | None =
                      Path(default=None,
                           description="Asubha pila",
                           ge=2,
                           le=5,
                           deprecated=True,
                           include_in_schema=True)):
    print({"path": path})
    return {
        "path": path
    }


# simple path param with Path class and query params with query class
@app.get('/path/query/{path}')
def pathAndQueryParam(
        q: str | None = Query(default=Required, description="Asubha pila"),
        path: int | None = Path(default=None, description="Subha pila", ge=2, le=5, deprecated=True, include_in_schema=True)):
    print({"path": path})
    if q:
        return {
            "query":q,
            "path": path
        }


# simple path param with Path class and query params with query class
@app.get('/req/{path}')
def requestObj(
        req:Request,
        q: str | None = Query(default=Required, description="Asubha pila"),
        path: int | None = Path(default=None, description="Subha pila", 
        ge=2, le=5, 
        deprecated=True, 
        include_in_schema=True,
        )
        ):
    print({"path": path})
    if q:
        return {
            # "query":q,
            "path": path,
            "query1":req._query_params
        }
    
