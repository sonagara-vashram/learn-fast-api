# Extra JSON Schema data in Pydantic models
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None

    class Config: 
        json_schema_extra = {
            "example": {
                "name": "Example Item",
                "desc": "An example item.",
                "price": 19.99,
                "tax": 0.08
            }
        }

@app.post("/items/{item_id}")
async def create_item(item: Item):
    result = {
        "item": item.dict()
    }
    return result


# Field() additional arguments
class User(BaseModel):
    name: str = Field(examples=['xyz'])
    age: int = Field(gt=0, lt=100)
    course: str = Field(examples=['python'], default=None)
    fees: float = Field(examples=[1200.0], gt=0)
    
@app.post("/users/")
async def create_user(user: User):
    result = {
        'users': user.dict()
    }
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
