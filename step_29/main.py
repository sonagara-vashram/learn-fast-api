from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Custom Middleware
@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    # Call the next middleware or actual endpoint
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Hello from Middleware"
    print(f"Outgoing response status: {response.status_code}")
    return response

@app.get("/example/")
async def example_route():
    return {"message": "This is an example endpoint!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
