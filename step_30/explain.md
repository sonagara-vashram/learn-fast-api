# CORS (Cross-Origin Resource Sharing) in FastAPI

**CORS** (Cross-Origin Resource Sharing) is a mechanism that allows servers to specify which origins (domains) are permitted to access resources on the server. It is crucial for web applications that interact with APIs hosted on a different domain.

In FastAPI, CORS can be easily handled using the `CORSMiddleware` from `fastapi.middleware.cors`.

## Why Use CORS?

1. **Security**: CORS prevents unauthorized requests from unknown origins.
2. **Cross-Domain Requests**: Enable frontend applications (e.g., React, Angular, Vue) to interact with FastAPI running on a different origin.
3. **Custom Headers**: Allow headers like `Authorization` for APIs that require authentication.

### Explanation

1. **`origins`**:
   - A list of domains that are allowed to make requests to the FastAPI app.
   - Add your frontend domain(s) here (e.g., `localhost` during development, production domain later).

2. **`CORSMiddleware` Parameters**:
   - `allow_origins`: Specifies which origins can access the API.
   - `allow_credentials`: Allows cookies or credentials in cross-origin requests.
   - `allow_methods`: Limits the HTTP methods (e.g., `GET`, `POST`) allowed from those origins.
   - `allow_headers`: Specifies which request headers are allowed (e.g., `Authorization`, `Content-Type`).

3. **Middleware Setup**:
   - The `add_middleware` function integrates the `CORSMiddleware` into the FastAPI app, enabling CORS handling globally.
