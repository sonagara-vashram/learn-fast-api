from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# List of allowed origins (domains)
origins = [
    "http://localhost:3000",
    "http://example.com",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed origins
    allow_credentials=True,  # Allow cookies or credentials
    allow_methods=["GET", "POST"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allowed headers
)


@app.get("/")
async def read_root():
    return {"message": "CORS is enabled for specified origins!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
