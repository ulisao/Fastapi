from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None


@app.get("/")
async def root():
  return {"message": "Hello world"}
