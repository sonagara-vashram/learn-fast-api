# Testing in FastAPI

FastAPI provides built-in support for testing using **Python's `unittest` module** or **`pytest`**. It offers an easy way to test your APIs using the **`TestClient`** from `fastapi.testclient`. With `TestClient`, you can simulate requests to your application just like a real client.

## Key Features of Testing in FastAPI

1. **`TestClient`**:
   - Simulates sending requests to your application for testing purposes.

2. **Assertions**:
   - Validate response status codes, data, and behavior of endpoints.

3. **Fast and Reliable**:
   - Run tests without starting the actual server, improving speed and ease of testing.

### Explanation of the Code

1. **App Code**:
   - Defines two endpoints:
     - `/`: Returns a welcome message.
     - `/items/{item_id}`: Returns an item or raises an error if the `item_id` is invalid.

2. **Test File**:
   - Uses `TestClient` to send test requests to the app without starting the server.

3. **Tests**:
   - **`test_read_root`**: Tests the `/` endpoint and asserts the status code and response body.
   - **`test_read_item_valid`**: Tests a valid request to `/items/{item_id}`.
   - **`test_read_item_invalid`**: Tests an invalid request and ensures an error is returned.
