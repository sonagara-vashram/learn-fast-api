from fastapi import FastAPI, Cookie, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for cookie parameters
class CookieModel(BaseModel):
    user_id: int
    session_token: str

# Dependency function to retrieve and validate cookies
async def get_cookie_data(user_id: int = Cookie(...), session_token: str = Cookie(...)) -> CookieModel:
    return CookieModel(user_id=user_id, session_token=session_token)

# Endpoint using the cookie model as a dependency
@app.get("/validate-session/")
async def validate_session(cookies: CookieModel = Depends(get_cookie_data)):
    if cookies.session_token != "valid-session-token":
        raise HTTPException(status_code=403, detail="Invalid session token")
    
    return {"message": f"User {cookies.user_id} authenticated successfully!"}
