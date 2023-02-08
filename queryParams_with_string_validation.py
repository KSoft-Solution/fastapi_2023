from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get('/')
def homePage():
    return {
        "homepage"
    }

# query params validation


@app.get('/asubha/')
def asubha_validation(village: str | None = None):
    results = {"data": [{"name": 'asubha samanta rai'}, {"age": 20}]}
    if village:
        results.update({"village": village})
    return results


@app.get('/sibani/')
def sibani_validation(korean_bhaina: str | None = Query(default=None, max_length=20, min_length=10)):
    results = {"data": [{"bhaina1": 'chin chu chanc'},
                        {"bhaina 2": "pun paan peen"}]}
    if korean_bhaina:
        results.update({"bada bhaina hauchi": korean_bhaina})
    return results


@app.get('/subha/')
def subha_validation(korean_bhaina: str | None = Query(default=Required, max_length=20, min_length=10)):
    results = {"data": [{"bhaina1": 'chin chu chanc'},
                        {"bhaina 2": "pun paan peen"}]}
    if korean_bhaina:
        results.update({"bada bhaina hauchi": korean_bhaina})
    return results


@app.get('/subha/')
def subha_validation(korean_bhaina: str | None = Query(max_length=20, min_length=10)):
    results = {"data": [{"bhaina1": 'chin chu chanc'},
                        {"bhaina 2": "pun paan peen"}]}
    if korean_bhaina:
        results.update({"bada bhaina hauchi": korean_bhaina})
    return results


@app.get('/subha/')
def subha_validation(korean_bhaina: str | None = Query(default=..., max_length=20, min_length=10)):
    results = {"data": [{"bhaina1": 'chin chu chanc'},
                        {"bhaina 2": "pun paan peen"}]}
    if korean_bhaina:
        results.update({"bada bhaina hauchi": korean_bhaina})
    return results


@app.get('/subha/')
def subha_validation(korean_bhai: str | None = Query(default=None, max_length=20, min_length=10)):
    results = {"data": [{"bhaina1": 'chin chu chanc'},
                        {"bhaina 2": "pun paan peen"}]}
    if korean_bhai:
        results.update({"bada bhaina hauchi": korean_bhai})
    return results


# multiple query parameters
# @app.get('/gandu_god/')
# def gandu_multi_validation(mandu:list[str] | None = Query(default=None)):
#     return {
#         "mandu":mandu
#     }
# multiple query parameters

# @app.get('/gandu_god/')
# def gandu_multi_validation(mandu:list[str] | None = Query(default=["foolo", "baro"])):
#     return {
#         "mandu":mandu
#     }


@app.get('/gandu_god/')
def gandu_multi_validation(mandu: list[str] | None =
                           Query(default=["foolo", "baro"],
                                 description='ee jaga re ame gandu ra sabu mandu janiba',
                                 title='gandu bhaina landa heichi',
                                 deprecated=True,
                                 alias='kan waa sabu right na',
                                 include_in_schema=True,
                                 lt=4,
                                 gt=10,
                                 le=3,
                                 ge=5
                                 )):
    return {
        "mandu": mandu
    }
