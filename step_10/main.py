from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# List fields
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Update an item with the given item ID.

    This endpoint updates the details of an item, including its name, description, price, tax, 
    and a list of associated tags.

    Args:
        item_id (int): The ID of the item to be updated.
        item (Item): A Pydantic model containing the following fields:
            - name (str): The name of the item.
            - description (str, optional): A brief description of the item. Default is None.
            - price (float): The price of the item.
            - tax (float, optional): The tax amount for the item. Default is None.
            - tags (list): A list of tags associated with the item. Default is an empty list.

    Returns:
        dict: A dictionary containing the updated item ID and item details.
            - item_id (int): The ID of the item that was updated.
            - item (Item): The updated item details.

    Example:
        Request:
        ```
        PUT /items/123
        {
            "name": "Smartphone",
            "description": "A flagship smartphone",
            "price": 999.99,
            "tax": 50.0,
            "tags": ["electronics", "mobile"]
        }
        ```

        Response:
        ```
        {
            "item_id": 123,
            "item": {
                "name": "Smartphone",
                "description": "A flagship smartphone",
                "price": 999.99,
                "tax": 50.0,
                "tags": ["electronics", "mobile"]
            }
        }
        ```
    """
    results = {"item_id": item_id, "item": item}
    return results


# Set Type

class User(BaseModel):
    name: str
    description: str | None = None
    tax: float | None = None
    tags: set[str] = set()

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    """
    Update a user with the given user ID.

    This endpoint updates the details of a user, including their name, description, tax, and a set of unique tags.

    Args:
        user_id (int): The ID of the user to be updated.
        user (User): A Pydantic model containing the following fields:
            - name (str): The name of the user.
            - description (str, optional): A brief description of the user. Default is None.
            - tax (float, optional): The tax information for the user. Default is None.
            - tags (set[str]): A set of unique tags associated with the user. Default is an empty set.

    Returns:
        dict: A dictionary containing the updated user ID and user details.
            - user_id (int): The ID of the user that was updated.
            - user (User): The updated user details.

    Example:
        Request:
        ```
        PUT /users/456
        {
            "name": "Alice",
            "description": "Software Developer",
            "tax": 100.0,
            "tags": ["developer", "backend"]
        }
        ```

        Response:
        ```
        {
            "user_id": 456,
            "user": {
                "name": "Alice",
                "description": "Software Developer",
                "tax": 100.0,
                "tags": ["developer", "backend"]
            }
        }
        ```
    """
    results = {"user_id": user_id, "user": user}
    return results


# Deeply nested models
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    """
    Create a new offer with multiple items and images.

    This endpoint allows you to create an offer that includes multiple items, with details such as name, 
    description, price, tax, tags, and associated images. Each item can have a list of images defined by a URL and name.

    Args:
        offer (Offer): A Pydantic model containing the following fields:
            - name (str): The name of the offer.
            - description (str, optional): A brief description of the offer. Default is None.
            - price (float): The price of the offer.
            - items (list[Item]): A list of items included in the offer, each with the following fields:
                - name (str): The name of the item.
                - description (str, optional): A brief description of the item. Default is None.
                - price (float): The price of the item.
                - tax (float, optional): The tax amount for the item. Default is None.
                - tags (set[str]): A set of tags associated with the item. Default is an empty set.
                - images (list[Image], optional): A list of image objects, each containing:
                    - url (HttpUrl): The URL of the image.
                    - name (str): The name of the image.

    Returns:
        Offer: The newly created offer with all the details of the items and images.

    Example:
        Request:
        ```
        POST /offers/
        {
            "name": "Holiday Special",
            "description": "Discounted items for the holiday season",
            "price": 199.99,
            "items": [
                {
                    "name": "Camera",
                    "description": "A high-quality camera",
                    "price": 300.0,
                    "tags": ["electronics", "photography"],
                    "images": [
                        {
                            "url": "http://example.com/camera.png",
                            "name": "Camera Image"
                        }
                    ]
                }
            ]
        }
        ```

        Response:
        ```
        {
            "name": "Holiday Special",
            "description": "Discounted items for the holiday season",
            "price": 199.99,
            "items": [
                {
                    "name": "Camera",
                    "description": "A high-quality camera",
                    "price": 300.0,
                    "tags": ["electronics", "photography"],
                    "images": [
                        {
                            "url": "http://example.com/camera.png",
                            "name": "Camera Image"
                        }
                    ]
                }
            ]
        }
        ```
    """
    return offer


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
