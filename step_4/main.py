from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model for the request body

"""
This module defines an Item class and a FastAPI endpoint to create items.

Classes:
    Item(BaseModel): A Pydantic model representing an item with a name, price, and optional offer status.

Endpoints:
    @app.post("/items/"): Asynchronous endpoint to create an item and return its details.

Functions:
    create_item(item: Item): Receives an Item object and returns a dictionary with the item's name, price, and offer status.
"""
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}

# Request body + path parameters
class Items(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


"""
Update an item with the given item_id.

Args:
    item_id (int): The ID of the item to update.
    item (Item): The item data to update.

Returns:
    dict: A dictionary containing the item_id and the updated item data.
"""
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Items):
    return {"item_id": item_id, **item.dict()}

# Request body + path + query parameters
@app.put("/items/{item_id}")
async def update_items(item_id: int, item: Items, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
