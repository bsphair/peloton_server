from fastapi import APIRouter, HTTPException

from ../schemas import authorization


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.get("/token")
async def user_login(creds: authorization.Credentials):
    print(creds)
    if (creds.username == ""):
        raise HTTPException(status_code=404, detail="Username field cannot be emtpy")
    elif (creds.password == ""):
        raise HTTPException(status_code=404, detail="Password field cannot be emtpy")
    return {"message": "logged in!!!!"}