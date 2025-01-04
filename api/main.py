from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import getpass
import os
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)
# model_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True,google_api_key="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E")

def conversation(message): 
    
    model = ChatOpenAI()
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass(os.environ["OPEN_API"])



    prompt = f"""
    Act as an psychatrist,but dont mention that in answer.
    Reply to the context: {message}
    Provide answers like a human bieng talking to other human being, and try to ask relevant question from it
    Your aim is to Make them feel happy.
    """

    
    response_text = model.predict(prompt)
    return response_text



@app.get("/")
def display():
    first_question = "Hello, Suvansh here!"
    return first_question

@app.get("/talk")
def ask_se(message: str):
    response = conversation(message)
    return response


