from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def home():
    return {"message": "hello"}


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user.model_dump()
    }


@app.get("/items")
def get_items(name: str, price: int):
    return {
        "item_name": name,
        "item_price": price
    }


@app.get("/products")
def get_products(name: str = None, price: int = 0):
    return {
        "name": name,
        "price": price
    }


@app.post("/items/create")
def create_item(item: Item, category: str):
    return {
        "category": category,
        "item": item.dict()
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "updated_data": user.model_dump()
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }