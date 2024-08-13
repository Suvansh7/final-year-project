from fastapi import FastAPI, Depends
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


app = FastAPI()

def get_corpus():
    return {"corpus": ""}

def next_question(ans: str, corpus: str) -> str:
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True,google_api_key="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E")
    ans = model(
    [
    SystemMessage(content="Only Generate a single line question relevant to given answer"),
    HumanMessage(content=f"Current Answer - {ans} /n You can also take refrence to previous answers which are - {corpus} "),
    ]
    )
    ques = ans.content
    return ques

@app.get("/")
def display():
    first_question = "Tell Me about Yourself?"
    return first_question

@app.get("/com")
def ask(ans: str, state: dict = Depends(get_corpus)):
    # Append the answer to the corpus
    state["corpus"] += ans
    
    # Generate the next question based on the updated corpus
    response = next_question(ans, state["corpus"])
    return response
