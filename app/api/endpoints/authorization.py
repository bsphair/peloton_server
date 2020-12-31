from fastapi import APIRouter, HTTPException
import requests
from app.schemas import Credentials

auth_router = APIRouter()


@auth_router.post("/token")
async def get_token(data: Credentials):
    if data.username == "":
        raise HTTPException(status_code=404, detail="Users is required")
    if data.password == "":
        raise HTTPException(status_code=404, detail="Password is required")

    payload = {
        "username_or_email": data.username,
        "password": data.password
    }

    response = requests.post("https://api.onepeloton.com/auth/login", json=payload)
    return response.json()
