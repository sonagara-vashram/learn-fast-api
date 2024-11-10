# FastAPI Header Parameters Guide

## Introduction

Header parameters allow you to send additional information with an HTTP request, which isn’t included directly in the URL or request body. In FastAPI, you can easily retrieve and handle these parameters for various purposes, such as security, authentication, or passing extra metadata in APIs.

## Understanding Header Parameters

Header Parameters are typically used for sending sensitive or additional information via HTTP headers, such as:

- `Authorization`: Contains credentials to authenticate a user.
- `User-Agent`: Identifies the type and version of the client making the request.
- `Content-Type`: Specifies the media type of the resource.

In FastAPI, you can access and work with these headers by using the `Header` class. This class helps retrieve values from headers sent by the client, allowing you to define headers as function parameters within your API endpoint.

### Defining a Header Parameter

To define a header parameter in FastAPI, you use the `Header` class, available in the `fastapi` library. You can set header parameters as optional or required, and even set default values for them.

## Code Example

Below is an example that demonstrates how to work with header parameters in FastAPI:

```python
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/items/")
async def read_items(api_key: str = Header(...)):
    # Check if the provided API key matches the expected value
    if api_key != "secret-key":
        # If the API key is incorrect, return a 403 error
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
    # If the API key is correct, allow access
    return {"message": "Access granted with valid API Key"}
```

### Explanation of the Code

- **`api_key: str = Header(...)`**: Here, `api_key` is a required header parameter defined using the `Header` class. The `...` (ellipsis) makes this parameter mandatory, meaning the client must include it in the request headers.
  
- **`raise HTTPException(...)`**: If the API key does not match the expected value (`"secret-key"` in this example), an HTTP 403 Forbidden error is raised. This is a common approach to secure endpoints by requiring a valid API key.

- If the provided API key is correct, a success message is returned, allowing the client to proceed with the request.
