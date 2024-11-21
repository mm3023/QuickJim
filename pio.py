from fastapi import FastAPI

import sys
import os # if you want this directory

try:
    sys.path.index('/zenviroment/bin') # Or os.getcwd() for this directory
except ValueError:
    sys.path.append('/zenviroment/bin')



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
