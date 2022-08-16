# Python
from email.policy import default
from enum import Enum
# FastAPI
from fastapi import FastAPI
from fastapi import Query, Path
# myFinPer
from app.schemas.users import ShowUser, User

app = FastAPI()

@app.get("/")
async def root():
    return {"Welcome":"to the jungle"}

@app.get("/user/{user_id}")
async def get_user(
    user_id: int = Path(
    title = "Search userr by id",
    description = "Search userr by id",
    gt = 0
)):
    return {"user_id":user_id}

@app.post("/user/", response_model = ShowUser)
async def create_user(user: User):
    return user

@app.get("/search_by_account/")
async def search_by_account(
    account: str = Query(
        default = "INGRESO", 
        title = "Search_by_account",
        description = "This path permit to search accounting events by name of account", 
        min_length = 3, 
        max_length=100
    )):
    return {"Account":account}