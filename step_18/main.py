from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Define a Pydantic model for the form
class RegistrationForm(BaseModel):
    username: str
    password: str
    email: EmailStr
    age: int

# Dependency to parse form data into the model
def get_form_data(
    username: str = Form(...),
    password: str = Form(...),
    email: EmailStr = Form(...),
    age: int = Form(...)
) -> RegistrationForm:
    return RegistrationForm(username=username, password=password, email=email, age=age)

# Endpoint to handle registration using Form Model
@app.post("/register/")
async def register(form_data: RegistrationForm = Depends(get_form_data)):
    # Process registration data
    return {
        "message": "Registration successful!",
        "username": form_data.username,
        "email": form_data.email,
        "age": form_data.age
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)