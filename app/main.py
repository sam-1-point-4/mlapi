from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/hello")
async def hello(data: NameRequest):
    return {"message": f"Hello {data.name}"}

@app.get("/hello")
async def hello_get(name: str = "World"):
    return {"message": f"Hello {name}"}