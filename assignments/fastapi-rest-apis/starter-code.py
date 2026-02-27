from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    response = {"item_id": item_id}
    if q:
        response["q"] = q
    return response

# To run the server use: uvicorn starter-code:app --reload
