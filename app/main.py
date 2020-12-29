from fastapi import FastAPI
import uvicorn
from app.api import router as endpoint_router

app = FastAPI()
app.include_router(endpoint_router)


@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/auth")
async def auth(data):
    return {"message": "Successful Login"}