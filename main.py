from fastapi import FastAPI, requests
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/ping")
def ping():
    return JSONResponse(content="pong", status_code=200)
