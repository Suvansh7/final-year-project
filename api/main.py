from fastapi import FastAPI



app = FastAPI()

@app.get("/text")
def display(ans:str):

    response  ="hellll"

    return response


