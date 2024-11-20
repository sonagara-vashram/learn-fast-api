from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Primary Dependency: Validate an API Key
def get_api_key(api_key: str = "fake-api-key"):
    if api_key != "my-secure-api-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

# Sub-Dependency: Perform a user-level operation using the validated API key
def get_current_user(api_key: str = Depends(get_api_key)):
    if api_key == "my-secure-api-key":
        return {"username": "testuser", "role": "admin"}
    raise HTTPException(status_code=401, detail="Unauthorized")

# Route using the sub-dependency
@app.get("/users/me/")
async def read_current_user(current_user: dict = Depends(get_current_user)):
    return {"message": "User fetched successfully", "user": current_user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)