from fastapi import Path, FastAPI, HTTPException  
from typing import Annotated

app = FastAPI()

# Path Parameters and Numeric Validations

"""
Endpoint to retrieve item details by item ID.

Path Parameters:
- item_id (int): The ID of the item to retrieve. Must be a positive integer.

Raises:
- HTTPException: If the item_id is less than 1, a 400 status code with a detail message is raised.

Returns:
- dict: A dictionary containing the item ID and a description message.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item ID must be a positive integer")
    return {"item_id": item_id, "description": f"Details for item {item_id}"}

# Order the parameters as you need
@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
