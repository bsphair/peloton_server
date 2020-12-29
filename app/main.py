from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/auth")
async def auth(data):
    return {"message": "Successful Login"}