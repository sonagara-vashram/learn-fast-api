from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Endpoint to handle form data
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    # Basic check for username and password
    if username == "admin" and password == "secret":
        return {"message": "Login successful!"}
    
    # Raise an error if login credentials are incorrect
    raise HTTPException(status_code=400, detail="Invalid username or password")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)