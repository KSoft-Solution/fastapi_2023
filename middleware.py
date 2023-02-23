from fastapi import FastAPI,Request
import time
app = FastAPI()

@app.middleware('http')
async def callMiddleware(req:Request,nextFn):
    start_time = time.time()
    response = await nextFn(req)
    return response
    process_time = time.time() - start_time
    # response.headers["X-Process-Siri'sTime"] = str(process_time)
    response.headers['X-token'] = 'barsa pani piyega bahar dance karega!'

    

@app.get('/')
async def getData():
    # time_Taken = time.gmtime(1677110400)
    time_Taken = time.time()
    return {
        # "createdAt": f'{time_Taken.tm_mday}-{time_Taken.tm_mon}-{time_Taken.tm_year}'
        "createdAt": f'{time_Taken}'
    }
