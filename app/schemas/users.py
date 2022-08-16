# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str

class User(UserLogin):
    id: int
    name: str
    lastname: str
    email: Optional[str]
    tel: Optional[str]

class ShowUser(BaseModel):
    name: str
    last_name: str
    email: Optional[str]






     