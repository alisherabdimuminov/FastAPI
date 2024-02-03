# FastAPI tutorial

## 1. Installation(O'rnatish)
```bash
virtualenv venv
```
```bash
source venv/bin/activate
```
```bash
pip install fastapi
```
```bash
pip install uvicorn
```

## 2. Hello, World!
Code
```py
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world_handler():
    return {"hello": "world"}
```

Run the app
```bash
uvicorn main:app --reload
```

## 3. Path parameters
Code
```py
from fastapi import FastAPI

app = FastAPI()

users = [
    {
        "id": 1,
        "username": "ali"
    },
    {
        "id": 2,
        "username": "alisher"
    }
]

@app.get("/users")
async def users_get_handler():
    return users

@app.get("/users/{id}")
async def user_get_handler(id: int):
    return users[id - 1]
```
Run the app
```bash
uvicorn main:app --reload
```

## 