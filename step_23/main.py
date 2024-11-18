from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Mock database
database: Dict[int, Dict] = {
    1: {"name": "Item One", "description": "First item", "price": 10.99, "tax": 1.50},
    2: {"name": "Item Two", "description": "Second item", "price": 20.99, "tax": 2.50},
}

# Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None

# Full Update with PUT
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Replace the existing item with the new one
    database[item_id] = updated_item.dict()
    return {"message": "Item updated successfully", "item": database[item_id]}

# Partial Update with PATCH
@app.patch("/items/{item_id}")
async def partial_update_item(item_id: int, updates: ItemUpdate):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Get the existing item
    stored_item_data = database[item_id]
    stored_item_model = Item(**stored_item_data)
    
    # Apply the updates to the existing item
    updated_data = updates.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=updated_data)
    
    # Save the updated item back to the database
    database[item_id] = updated_item.dict()
    return {"message": "Item updated successfully", "item": database[item_id]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)