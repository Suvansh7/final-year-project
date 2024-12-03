from fastapi import FastAPI
# from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT 
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage, SystemMessage
# import replicate
# import os

app = FastAPI()

# model_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True,google_api_key="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E")

def conversation(message): 

#     sys_prompt = '''
#     Act like a psychologist, and reply to the question.
# '''
#     human_prompt = message
    
#     output = model_gemini([ SystemMessage(content=sys_prompt), HumanMessage(content= human_prompt )])
    ques="chl gye oye hoye"
    # ques = output.content
    return ques



@app.get("/")
def display():
    first_question = "Hello, Suvansh here!"
    return first_question

@app.get("/talk")
def ask_se(message: str):
    response = conversation(message)
    return response


