from fastapi import FastAPI, Cookie, Response

app = FastAPI()

@app.get("/set-cookie")
async def set_cookie(response: Response):
    response.set_cookie(key="session_id", value="abc123")
    return {"message": "Cookie set successfully"}

@app.get("/get-cookie")
async def get_cookie(session_id: str = Cookie(None)):
    if session_id:
        return {"session_id": session_id}
    else:
        return {"error": "Cookie not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.1.0.1", port=8000)