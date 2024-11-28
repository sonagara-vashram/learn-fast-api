from fastapi import FastAPI

# FastAPI instance with custom metadata and documentation URLs
app = FastAPI(
    title="My API",
    description="A demo API showcasing metadata and custom documentation URLs.",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "API Support",
        "url": "https://example.com/contact/",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    docs_url="/swagger-docs",  # Swagger UI available at /swagger-docs
    redoc_url="/api-redoc",    # ReDoc documentation available at /api-redoc
)

@app.get("/")
async def root():
    return {"message": "Welcome to My API"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)