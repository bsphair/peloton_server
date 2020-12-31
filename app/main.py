from fastapi import FastAPI
from app.api import router as endpoint_router

app = FastAPI()
app.include_router(endpoint_router)


@app.get("/")
async def root():
    # data = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    # print(data.json())
    return {"message": "Hello, World"}


@app.post("/auth")
async def auth(data):
    return {"message": "Successful Login"}