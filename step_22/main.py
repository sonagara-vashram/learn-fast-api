from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Define a Pydantic Model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    created_at: datetime

# Example: Mock Database
database = {}

@app.post("/items/")
async def create_item(item: Item):
    # Use jsonable_encoder to convert the Pydantic model to JSON-compatible format
    item_data = jsonable_encoder(item)
    item_id = len(database) + 1
    database[item_id] = item_data
    return {"message": "Item created", "item_id": item_id, "item_data": item_data}

# Example: Nested Serialization
class Order(BaseModel):
    order_id: int
    items: List[Item]
    total_price: float

@app.post("/orders/")
async def create_order(order: Order):
    # Use jsonable_encoder to handle nested serialization
    order_data = jsonable_encoder(order)
    return {"message": "Order processed", "order_data": order_data}

# Example: Handling Non-Serializable Data
class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

@app.get("/custom-object/")
async def get_custom_object():
    obj = CustomObject(name="SampleObject", value=42)
    # jsonable_encoder does not handle non-serializable objects directly, so custom serialization is needed
    obj_data = jsonable_encoder(obj, custom_encoder={CustomObject: lambda x: {"name": x.name, "value": x.value}})
    
    return {"custom_object": obj_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)