from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        "id": 1,
        "username": "ali"
    },
    {
        "id": 2,
        "username": "alisher",
    }
]

@app.get("/")
async def home_handler():
    return  {"message": "Hello, World!"}

@app.post("/post")
async def post_handler():
    return {"message": "this is post method"}

@app.put("/items/{id:int}")
async def put_handler(id: int):
    return {"id": id}

@app.get("/users")
async def users_get_handler_with_query(limit: Optional[int] = 0, is_all: bool = False):
    print(limit)
    print(is_all)
    return users

@app.get("/users/{id}")
async def user_get_handler(id: int):
    return users[id - 1]

class Item(BaseModel):
    id: int
    username: str

@app.post("/users")
async def create_user(item: Item):
    print(item)
    return item

@app.head("/")
async def head_heandler():
    return {'message': "Hello"}

@app.get("/query")
async def query_handler(q: str = Query("a", max_length=10, min_length=4)):
    print(q)
    return {"q": q}