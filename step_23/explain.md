# Body - Updates in FastAPI

In FastAPI, **Body Updates** allow you to update existing data by accepting partial or full updates to a resource. This is commonly used in **PUT** or **PATCH** operations. Here's how you can handle updates efficiently in FastAPI, leveraging the Pydantic models and FastAPI's request body features.

---

## Key Concepts of Body Updates

1. **PUT vs PATCH**:
   - **PUT**: Used for full updates where the entire object is replaced or updated.
   - **PATCH**: Used for partial updates where only specified fields are updated.

2. **Merging Updates**:
   - Use Pydantic's `update` capability to merge existing data with the update request.
   - Ensure fields not provided in the update are preserved.

3. **Validation**:
   - Leverage Pydantic models to validate the incoming update data.

### Features in the Script

1. **Full Updates (PUT)**:
   - The `/items/{item_id}` endpoint replaces the entire resource with the new data provided.
   - The `Item` model validates the incoming request body to ensure all fields are present.

2. **Partial Updates (PATCH)**:
   - The `/items/{item_id}` endpoint updates only the provided fields.
   - The `ItemUpdate` model allows all fields to be optional, supporting partial updates.
   - The `exclude_unset=True` parameter ensures only fields explicitly provided in the request are updated.

3. **Mock Database**:
   - A dictionary is used to simulate a simple in-memory database for storing and retrieving item data.

4. **Validation**:
   - Both endpoints validate the incoming data using Pydantic models, ensuring type safety and correctness.

---

### Sample Requests

#### Full Update (PUT)

**Request:**

```json
{
    "name": "Updated Item",
    "description": "This item has been fully updated",
    "price": 15.99,
    "tax": 1.20
}
```

**Response:**

```json
{
    "message": "Item updated successfully",
    "item": {
        "name": "Updated Item",
        "description": "This item has been fully updated",
        "price": 15.99,
        "tax": 1.20
    }
}
```

#### Partial Update (PATCH)

**Request:**

```json
{
    "price": 18.99,
    "tax": 1.80
}
```

**Response:**

```json
{
    "message": "Item updated successfully",
    "item": {
        "name": "Item One",
        "description": "First item",
        "price": 18.99,
        "tax": 1.80
    }
}
```

---

### Key Takeaways

1. **PUT** is for full updates, while **PATCH** is for partial updates.
2. Use separate Pydantic models for full and partial updates to enforce validation effectively.
3. Use `copy(update=...)` with `exclude_unset=True` for merging updates with existing data.
