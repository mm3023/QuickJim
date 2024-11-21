from fastapi import FastAPI

import sys
import os # if you want this directory

try:
    sys.path.index('/dir/path') # Or os.getcwd() for this directory
except ValueError:
    sys.path.append('/dir/path')



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
