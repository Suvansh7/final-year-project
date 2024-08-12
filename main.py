from fastapi import FastAPI
import LLM 
import localLM as llm


app = FastAPI()

@app.get("/text")
def display(ans:str):

    response = LLM.generate(ans)
    # reply = llm.transform(response)

    return response


