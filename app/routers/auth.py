from app.schema.auth import LoginRequest
from fastapi import APIRouter, status, HTTPException



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/login")
def login(body: LoginRequest):

    email = body.email
    password = body.password

    if email != "azham@techade.id":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")

    if password != "123456":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    return {"message": "User logged in", "email": body.email}