# Middleware in FastAPI

**Middleware** in FastAPI is a way to process requests **before** they reach the endpoint and responses **before** they are sent back to the client. Middleware is useful for:

- Logging requests and responses.
- Managing authentication or authorization.
- Adding custom headers to responses.
- Handling cross-cutting concerns globally.

## How Middleware Works

1. **Request Processing**:
   Middleware intercepts an incoming HTTP request before it reaches the route handler.

2. **Response Processing**:
   Middleware modifies or processes the HTTP response before sending it back to the client.

3. Middleware is applied **globally** to all routes.

### Explanation

1. **`@app.middleware("http")`**:
   - A built-in decorator to define middleware for HTTP requests.
   - The `call_next` function is used to pass the request to the next middleware or endpoint.

2. **Request Logging**:
   - Logs the HTTP method and URL before passing the request to the endpoint.

3. **Response Customization**:
   - Adds a custom header (`X-Custom-Header`) to all responses.
   - Logs the response status code.

4. **Endpoint**:
   - The `/example/` route behaves as usual, but the middleware processes the request and response globally.
