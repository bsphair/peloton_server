from fastapi import FastAPI
from pydantic import BaseModel

# from routers import authorization

class Auth(BaseModel):
    username: str
    password: str


app = FastAPI()

# app.include_router(authorization.router)

@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/auth")
async def auth(data: Auth):
    print(data)
    return {"message": "Successful Login"}