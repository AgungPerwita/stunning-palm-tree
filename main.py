from typing import Union

from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()

# testEnv = os.environ.get("HELLO")
something = os.getenv("HELLO")
@app.get("/")
def read_root():
    return {"Hello": "World", 
            "testEnv": something}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}