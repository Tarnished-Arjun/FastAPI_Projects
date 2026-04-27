from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    email: str
    address: Address


@app.post("/nested-user")
def create_nested_user(user: User):
    return {
        "message": "User created successfully",
        "data": user.model_dump()
    }