from fastapi import FastAPI, Depends

app = FastAPI()

# Define a class to handle query parameters
class QueryParams:
    def __init__(self, search: str | None = None, limit: int = 5):
        self.search = search
        self.limit = limit

@app.get("/items/")
async def get_items(params: QueryParams = Depends()):
    items = [
        {"id": 1, "name": "Apple"},
        {"id": 2, "name": "Banana"},
        {"id": 3, "name": "Cherry"},
        {"id": 4, "name": "Date"},
        {"id": 5, "name": "Elderberry"},
        {"id": 6, "name": "Fig"},
        {"id": 7, "name": "Grape"}
    ]

    # Filter items if `search` is provided
    if params.search:
        items = [item for item in items if params.search.lower() in item["name"].lower()]
    
    return {"items": items[:params.limit]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)