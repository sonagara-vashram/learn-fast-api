# Debugging in FastAPI

Debugging in FastAPI helps you identify and fix issues in your code efficiently. Since FastAPI is built on **Python’s asyncio** framework, debugging is often focused on understanding asynchronous behavior, request flow, and server responses.

---

## Key Debugging Techniques

### 1. **Use FastAPI's Built-in Debug Mode**

FastAPI automatically enables a built-in debugger when running with the `--reload` flag using **Uvicorn**:

```bash
uvicorn main:app --reload
```

- **Features**:
  - Automatic server reload on code changes.
  - Detailed error messages and stack traces in the browser.

---

#### 2. **Using `print()` or `logging` Statements**

Insert `print()` statements or use Python's `logging` module to output variable values, flow information, and error details.

**Example:**

```python
import logging

logging.basicConfig(level=logging.INFO)

@app.get("/")
async def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Hello, Debugging!"}
```

- Logs will appear in the terminal where you started the server.

---

#### 3. **Using `pdb` (Python Debugger)**

Insert the `pdb` debugger into your code to pause execution and inspect variables step-by-step.

**Example:**

```python
import pdb

@app.get("/debug")
async def debug_endpoint():
    x = 10
    pdb.set_trace()  # Execution will stop here
    return {"result": x * 2}
```

Run the app and call the `/debug` endpoint. The terminal will enter debug mode, allowing you to inspect variables and execute commands.

---

#### 4. **Debugging with IDEs (VS Code, PyCharm)**

Modern IDEs like **VS Code** or **PyCharm** provide excellent debugging tools for FastAPI.

**VS Code Debugging Setup:**

1. Go to the **Run and Debug** tab (`Ctrl+Shift+D`).
2. Click **"Create a launch.json file"**.
3. Select **Python** and use this configuration:

   ```json
   {
       "name": "FastAPI Debug",
       "type": "python",
       "request": "launch",
       "module": "uvicorn",
       "args": [
           "main:app",
           "--reload"
       ],
       "jinja": true
   }
   ```

4. Set breakpoints in your code and press **F5** to start debugging.

**PyCharm Debugging Setup:**

1. Create a **Run/Debug Configuration** for FastAPI.
2. Set `main:app` as the entry point.
3. Start debugging and add breakpoints.

---

#### 5. **Debugging Async Code**

Debugging asynchronous code can be tricky. Use tools like `asyncio.run` or `await` in isolated scripts to debug specific parts of the code.

**Example:**

```python
import asyncio

async def async_func():
    await asyncio.sleep(1)
    print("Debugging async function!")

# Run directly for debugging
asyncio.run(async_func())
```

---

#### 6. **Use the `Exception Middleware`**

FastAPI's built-in exception handler provides detailed error messages. You can also use custom exception handlers for debugging.

**Example:**

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc), "type": type(exc).__name__},
    )
```

---

#### 7. **Inspect Request and Response**

Use `Middleware` to inspect incoming requests and outgoing responses.

**Example:**

```python
from starlette.middleware.base import BaseHTTPMiddleware

class DebugMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Request: {request.url}")
        response = await call_next(request)
        print(f"Response: {response.status_code}")
        return response

app.add_middleware(DebugMiddleware)
```

---

#### 8. **Testing for Debugging**

Use `pytest` to test endpoints in isolation. If tests fail, debug specific scenarios:

```bash
pytest --pdb test/test_app.py
```

- This opens the Python debugger (`pdb`) when a test fails.
