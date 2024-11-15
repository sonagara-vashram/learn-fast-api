from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()


# 1. Raise HTTPException
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item"}


# 2. Custom Exception Handling
class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=400, content={"error": f"Custom error occurred: {exc.name}"}
    )


@app.get("/trigger-custom-error/")
async def trigger_custom_error():
    raise CustomException(name="Invalid Operation")


# 3. Middleware for Global Errors
@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(
            status_code=500, content={"detail": "An unexpected error occurred"}
        )


@app.get("/cause-error/")
async def cause_error():
    raise ValueError("This is an unhandled exception")


# 4. Customize Validation Error Responses
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"errors": exc.errors(), "message": "Validation failed"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
