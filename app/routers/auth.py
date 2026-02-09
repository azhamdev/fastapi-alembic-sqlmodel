from app.schema.auth import LoginRequest
from fastapi import APIRouter, status, HTTPException



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/login")
def login(body: LoginRequest):

    email = body.email

    if email != "azham@techade.id":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")

    return {"message": "User logged in", "email": body.email}