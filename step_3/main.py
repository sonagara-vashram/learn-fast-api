from fastapi import FastAPI

app = FastAPI()

"""
This FastAPI application defines an endpoint to read items with pagination.

Endpoints:
- GET /items/
  - Query Parameters:
    - skip (int, optional): The number of items to skip. Default is 0.
    - limit (int, optional): The maximum number of items to return. Default is 10.
  - Response:
    - JSON object containing the 'skip' and 'limit' values.
"""

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Query parameter type conversion

"""
Endpoint to retrieve an item with optional query parameters.

Args:
    item_id (str): The unique identifier for the item.
    q (str, optional): An optional query string. Defaults to None.
    short (bool, optional): A flag to determine if the item description should be short. Defaults to False.

Returns:
    dict: A dictionary containing the item details. If 'q' is provided, it will be included in the response. If 'short' is False, a long description will be included.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Multiple path and query parameters

"""
Endpoint to read a specific item owned by a user.

Args:
    user_id (int): The ID of the user.
    item_id (str): The ID of the item.
    q (str, optional): An optional query string. Defaults to None.
    short (bool, optional): A flag to indicate if a short description is requested. Defaults to False.

Returns:
    dict: A dictionary containing item details including `item_id`, `owner_id`, and optionally `q` and `description`.
"""
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
