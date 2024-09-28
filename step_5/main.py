from fastapi import FastAPI, Query
from typing import Optional, Annotated

app = FastAPI()

# Query Parameters and String Validations

"""
This FastAPI application defines an endpoint to read items based on a query parameter.

Endpoints:
- GET /items/:
    - Query Parameters:
        - q (Optional[str]): A query string that must be between 3 and 50 characters in length and can only contain alphanumeric characters and spaces.
    - Responses:
        - 200: A JSON object containing the query string.
"""
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^[a-zA-Z0-9 ]*$")):
    return {"query": q}

# Query - as the default value
@app.get("/items/")
async def read_item(q: Optional[str] = Query(None, min_length=3, max_length=50, default=None)):
    return {"query": q}

# Add more validations using Annotated
@app.get("/items/")
async def read_item_(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Default values with Annotated
@app.get("/users/")
async def read_users(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"users": [{"user_id": "Foo"}, {"user_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter list / multiple values
@app.get("/user/")
async def read_users(q: Annotated[list[str] | None, Query()] = None):
    query_users = {"q": q}
    return query_users


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
