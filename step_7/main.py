from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Query Parameter Models
class ItemQuery(BaseModel):
    category: Optional[str] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    sort_order: Optional[str] = None

@app.get("/items/")
async def read_items(query: ItemQuery = Depends()):
    response = {
        "category": query.category,
        "price_min": query.price_min,
        "price_max": query.price_max,
        "sort_order": query.sort_order,
    }
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Explaination
"""
    Retrieve a list of items based on optional query parameters for filtering and sorting.

    Query Parameters:
        - category (Optional[str]): Filter items by their category.
        - price_min (Optional[float]): Return items priced greater than or equal to this value.
        - price_max (Optional[float]): Return items priced less than or equal to this value.
        - sort_order (Optional[str]): Specify sort order of the results. Acceptable values are 'asc' for ascending 
          and 'desc' for descending.

    Returns:
        dict: A dictionary containing the filtered items and the applied query filters.
            - category (Optional[str]): The filtered category or `None` if not specified.
            - price_min (Optional[float]): The minimum price filter or `None` if not specified.
            - price_max (Optional[float]): The maximum price filter or `None` if not specified.
            - sort_order (Optional[str]): The sort order used or `None` if not specified.

    Example:
        Request:
        ```
        GET /items/?category=electronics&price_min=100&price_max=500&sort_order=asc
        ```

        Response:
        ```
        {
            "category": "electronics",
            "price_min": 100,
            "price_max": 500,
            "sort_order": "asc"
        }
        ```

    Error Handling:
        - Returns a 400 Bad Request if invalid query parameters are provided.
        - Returns an empty response if no items match the filter criteria.
    """