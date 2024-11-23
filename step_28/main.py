from fastapi import FastAPI, Depends

app = FastAPI()


# Dependency with setup and teardown using yield
async def get_resource():
    # Setup: Allocate or open a resource
    resource = {"connection": "Database connection opened"}
    print("Setup: Opening resource")
    yield resource  # Pass the resource to the endpoint
    # Teardown: Clean up the resource
    print("Teardown: Closing resource")


@app.get("/items/")
async def read_items(resource: dict = Depends(get_resource)):
    return {"message": "Using resource", "resource": resource}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
