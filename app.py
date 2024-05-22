from fastapi import FastAPI,HTTPException
import uvicorn
import sys
import os
import tensorflow as tf
from source.components.inferencing import Inference
from pathlib import Path
import numpy as np
# from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
# from fastapi.responses import Response
import json
import numpy as np


app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")
 

@app.post("/predict")
async def predict_route(inp:dict):
    try:
        # inp = np.array(json.loads(inp)["input"])
        inp = np.array(inp["input"])
        if inp.shape != (1,256,256,1):
            raise HTTPException(status_code=422, detail="Input array shape should be (1, 256, 256, 1)")
        obj = Inference()
        pred = str(obj.predict(inp))
        # return json.dumps({"predictions":pred})
        return {"predictions":pred}
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
