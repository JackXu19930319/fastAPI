from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

from typing import Optional  # Import Optional from typing module

router = APIRouter()


class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = Field(None,
                                     description="The full name of the user")


@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}


@router.post("/create")
async def create_user(user: User):
    print(user)
    print(123)
    return {"message": "User has been created successfully."}
