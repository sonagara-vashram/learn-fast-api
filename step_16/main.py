from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the response
class ItemResponse(BaseModel):
    item_id: int
    name: str
    description: str
    price: float
    available: bool

# Endpoint using the response model
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    # Mock data to simulate a database fetch
    item_data = {
        "item_id": item_id,
        "name": "Sample Item",
        "description": "A detailed description of the item.",
        "price": 19.99,
        "available": True,
        "created_at": "2024-11-10"  # Extra field not in response model
    }
    # Return only fields defined in the response model
    return item_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.1.0.1", port=8000)