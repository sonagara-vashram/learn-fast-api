from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define response model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Advanced Path Operation Configuration
@app.get(
    "/items/{item_id}",
    response_model=Item,
    status_code=200,
    summary="Retrieve an Item",
    description="Get an item by its ID. This will return all the details of the item, including price and tax.",
    tags=["Items"],
    responses={
        404: {"description": "Item not found"},
        200: {"description": "Successful Response"},
    },
)
async def read_item(item_id: int, q: str | None = None):
    """
    Fetch an item based on its ID.
    - **item_id**: The unique ID of the item.
    - **q**: Optional query string.
    """
    if item_id == 1:
        return Item(name="Item1", description="This is Item 1", price=100.0, tax=5.0)
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete(
    "/items/{item_id}",
    summary="Delete an Item",
    description="This endpoint allows you to delete an item by its ID.",
    tags=["Items"],
    deprecated=True,  # Marking the route as deprecated
)
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)