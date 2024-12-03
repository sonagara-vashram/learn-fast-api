from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# Create an item with a 201 status code
@app.post(
    "/items/",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Item created successfully"},
        400: {"description": "Bad Request"},
    },
)
async def create_item(item: Item):
    """
    Create a new item in the system.
    - **name**: Name of the item.
    - **price**: Price of the item.
    - **description**: Optional description.
    """
    if item.price <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price must be greater than 0",
        )
    return {"message": "Item created", "item": item}


# Return 204 (No Content) for successful deletion
@app.delete(
    "/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Item deleted successfully"},
        404: {"description": "Item not found"},
    },
)
async def delete_item(item_id: int):
    """
    Delete an item by its ID.
    - **item_id**: The unique ID of the item.
    """
    if item_id != 1:  # Assuming only item_id=1 exists for this example
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return None


# Return 202 (Accepted) for an async operation
@app.put(
    "/items/{item_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        202: {"description": "Request accepted for processing"},
        404: {"description": "Item not found"},
    },
)
async def update_item(item_id: int, item: Item):
    """
    Update an item in the system.
    - **item_id**: ID of the item to update.
    - **name**, **price**, **description**: Updated details.
    """
    if item_id != 1:  # Assuming only item_id=1 exists
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return {"message": "Update accepted", "item": item}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)