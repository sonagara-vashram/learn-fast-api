# Dependencies with `yield` in FastAPI

In FastAPI, you can use `yield` in dependencies to handle **setup** and **teardown** logic. This is particularly useful for scenarios where you need to:

- Open and close database connections.
- Start and stop background tasks.
- Perform any resource cleanup.

## How it Works

1. **Setup**:
   - Code before the `yield` statement is executed **before** the endpoint is called.
2. **Teardown**:
   - Code after the `yield` statement is executed **after** the endpoint finishes.

### Explanation

1. **`get_resource` Dependency**:
   - Sets up a resource (e.g., opening a database connection).
   - Passes the resource via `yield` for use in the endpoint.
   - After the request is completed, the teardown code (closing the connection) runs.

2. **Endpoint (`/items/`)**:
   - Automatically receives the resource from `get_resource`.
   - Returns the resource details in the response.

3. **Logs**:
   - You can see when the setup and teardown occur.
