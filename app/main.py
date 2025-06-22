from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}