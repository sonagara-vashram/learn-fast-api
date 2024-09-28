from fastapi import FastAPI

app = FastAPI()

# Path Parameters

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types
"""
Endpoint to retrieve an item by its ID.

Args:
    item_id (int): The unique identifier of the item to be retrieved.

Returns:
    dict: A dictionary containing the item ID.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)