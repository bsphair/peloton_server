from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/token")
async def get_token():
    return {"message": "Get the token"}