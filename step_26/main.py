from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


# Define a dependency
def verify_token(token: str = "default-token"):
    if token != "secure-token":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"user": "admin", "permissions": ["read", "write"]}


# Apply the dependency in the decorator
@app.get("/secure-data/", dependencies=[Depends(verify_token)])
async def get_secure_data():
    return {"message": "Access granted to secure data"}


# Apply the dependency with additional logic in the function
@app.get("/secure-info/")
async def get_secure_info(user: dict = Depends(verify_token)):
    return {
        "message": f"Welcome {user['user']}, you have {user['permissions']} permissions."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
