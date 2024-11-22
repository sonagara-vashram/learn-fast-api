# Global Dependencies in FastAPI

**Global dependencies** are dependencies applied to all the endpoints in your FastAPI application. You can define these dependencies at the application level using the `dependencies` parameter in the `FastAPI` instance.

## Benefits of Global Dependencies

1. Automatically applied to all routes without repeating logic.
2. Ideal for tasks like authentication, logging, or request validation.
