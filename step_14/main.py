from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/items/")
async def read_items(api_key: str = Header(...)):
    if api_key != "secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"message": "Access granted with valid API Key"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.1.0.1", port=8000)