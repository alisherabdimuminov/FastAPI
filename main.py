from fastapi import FastAPI

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
async def users_get_handler():
    return users

@app.get("/users/{id}")
async def user_get_handler(id: int):
    return users[id - 1]
