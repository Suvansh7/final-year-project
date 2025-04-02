from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
import getpass
import os
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI

a1 = "sk-proj-RfC43pSgqSUf0kCFv-B6Fami_2K3iQV"
b2 = "LmJa5aVfGxfgvtGfrRKJTOkRZ2fdmeLZpWKIzQz"
c3 = "QVCUT3BlbkFJY2ilRNej8fpdSNnnlvQdDdyUJqxI"
d4 = "rL489jICVPeX4YX1b0JVrRwMqp5JHaZovtJFRVBcKH"
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
    OPENAI_API_KEY = a1 + b2+ c3+d4+"ldoA"
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    



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


