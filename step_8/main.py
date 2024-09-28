from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class Address(BaseModel):
    street: str
    city: str
    country: str

@app.post("/users/")
async def create_user(user: User, address: Address):
    return {
        "username": user.username,
        "email": user.email,
        "street": address.street,
        "city": address.city,
        "country": address.country,
        "message": "User created successfully"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
