from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    x = 10
    y = 5
    # Debug with print
    print(f"x={x}, y={y}")
    return {"message": "Hello Debugging!", "sum": x + y}

@app.get("/error")
async def error_route():
    try:
        result = 1 / 0  # Intentional error
    except Exception as e:
        print(f"Error occurred: {e}")
        raise

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)