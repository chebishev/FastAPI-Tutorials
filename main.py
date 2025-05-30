from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

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



@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


# this will never be reached
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


# test enum: Creates list of options to choose from
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# match any path
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
