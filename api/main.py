from fastapi import FastAPI, Depends
import google.generativeai as genai

app = FastAPI()

# Initialize the Generative AI model once at startup
GOOGLE_API_KEY = "AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Dependency to store and retrieve corpus
def get_corpus():
    return {"corpus": ""}

def next_question(ans: str, corpus: str) -> str:
    p = f'''
        Act Like an Interviewer and ask a question that should be relevant to the following answer -
        {ans}

        Make sure you ask questions that are relevant to {corpus}, you can also cross question the answer of interviewee if they contradict their own answers.
        You can easily do this as you have all the answers of the interviewee which are - {corpus}

        Dont give anything else rather that a single line question.
        Also dont include any astricts !
    '''
    
    response = model.generate_content(p)
    ques = response.text
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
