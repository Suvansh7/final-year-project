from fastapi import FastAPI
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import replicate
import os

app = FastAPI()

model_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True,google_api_key="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E")
model_claude = Anthropic(api_key= "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")
os.environ["REPLICATE_API_TOKEN"] = "r8_0ExGCTh1bhkSNy4fyVHZQrX1QKt0pob3ILo7Q"



def physics_chemistry(grade,topic,qno,subject):
    sys_prompt = ""
    human_prompt = ""

    completion = model_claude.completions.create(model="claude-2.1",  max_tokens_to_sample=350, prompt=f"{HUMAN_PROMPT}{sys_prompt}/n{human_prompt}{AI_PROMPT}")
    ques = completion.completion
    return ques

def science_english(grade,topic,qno,subject):

    sys_prompt = ""
    human_prompt = ""
    
    output = model_gemini([ SystemMessage(content=sys_prompt), HumanMessage(content= human_prompt )])
    ques=""
    ques = output.content
    return ques

def computer_maths(grade,topic,qno,subject):

    sys_prompt = ""
    human_prompt = ""
    
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', input={"prompt": f"{sys_prompt} {human_prompt} Assistant: ", "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})
    ques = ""
    for item in output:
      ques += item

    return ques



@app.get("/")
def display():
    first_question = "Hello, Suvansh here!"
    return first_question

@app.get("/se")
def ask(grade: str, qno: str, topic : str,subject:str):
    response = science_english(grade , topic, qno,subject)
    return response

@app.get("/cm")
def ask(grade: str, qno: str, topic : str,subject:str):
    response = computer_maths(grade , topic, qno,subject)
    return response

@app.get("/pc")
def ask(grade: str, qno: str, topic : str,subject:str):
    response = physics_chemistry(grade , topic, qno,subject)
    return response
