from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Response Model Definition
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# Example: Basic Path Operation Configuration
@app.get(
    "/items/{item_id}",
    summary="Retrieve an item by ID",  
    description="This endpoint retrieves an item based on its ID. "
    "You can use this to fetch information about specific items.",  
    response_model=Item,  
    response_description="The retrieved item",  
    tags=["Items"],  
)
async def read_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "name": "Sample Item",
        "description": "A detailed description of the item.",
        "price": 10.99,
        "tax": 1.50,
    }


# Example: Using Default Response Codes and Marking Deprecated Endpoints
@app.post(
    "/items/",
    summary="Create a new item",
    description="This endpoint allows you to create a new item by providing the required data.",
    tags=["Items"],
    deprecated=True,  
)
async def create_item(item: Item):
    return {"message": "This endpoint is deprecated. Please use the new version."}


# Example: Organizing Endpoints with Tags
@app.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": "John Doe"}


# Example: Overriding Response Status Codes
@app.delete(
    "/items/{item_id}",
    summary="Delete an item",
    description="This endpoint deletes an item. If the item does not exist, it returns a 404 error.",
    tags=["Items"],
    responses={
        200: {"description": "Item deleted successfully"},
        404: {"description": "Item not found"},
    },
)
async def delete_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}


# Example: Custom Path Metadata
@app.get(
    "/health",
    summary="Health check",
    description="This endpoint checks the health of the API.",
    tags=["System"],
    responses={
        200: {"description": "API is healthy"},
        500: {"description": "API is not healthy"},
    },
)
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
