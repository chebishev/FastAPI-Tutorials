from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("user/me")
async def read_user_me():
    return {"user_id": "the current user"}


# this must be second, because "me" can be interpretated as a parameter
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


