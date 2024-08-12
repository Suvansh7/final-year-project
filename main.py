from fastapi import FastAPI
# from typing import Uvicorn
app = FastAPI()

@app.get("/")
def display():
    return{"Message":"Hello"}


