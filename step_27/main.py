from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


# Global dependency function
def verify_token(token: str = "default-token"):
    if token != "secure-token":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"user": "admin"}


# Attach global dependency to the app
app = FastAPI(dependencies=[Depends(verify_token)])


@app.get("/public/")
async def public_endpoint():
    return {"message": "This is a public endpoint, but still secured globally!"}


@app.get("/private/")
async def private_endpoint():
    return {
        "message": "This is a private endpoint, accessible after global token validation!"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
