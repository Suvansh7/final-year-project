from fastapi import FastAPI
# from typing import Uvicorn
app = FastAPI()

@app.get("/c")
def display():
    return{"hehehehe"}


