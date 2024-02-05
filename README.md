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

## 4. Query parameters

Code
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def query_parameters_handler(limit: int = 10):
    print(limit)
    return {"limit": limit}
```

## 5. Request body
Code
```py
from fastapi import FastAPI
from pydantic import BaseModel

class User:
    id: int
    username: string
    first_name: string
    last_name: string

@app.post("/add")
async def add(user: User):
    print(user)
    return user
```
## 6. Query object
Code
```py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def query_handler(q: str | None = Query(None, max_length=10, min_length=5)):
    return {"q": q}
```

## 7. Path object
Code
```py
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/user/{id}")
async def get_user(id: int = Path()):
    print(id)
    return {"user": "ali"}
```