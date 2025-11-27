from fastapi import FastAPI
from routers.summarize_route import router as summarize_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI API!"}

@app.get("/add")
def add(a: int, b: int):
    return  {"result": a + b}

app.include_router(summarize_router)


