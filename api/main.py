from fastapi import FastAPI

app = FastAPI()

def next_question(ans):
    corpus = corpus + ans

    import google.generativeai as genai
    GOOGLE_API_KEY="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    p=f'''

        Act Like a Interviewer and ask question which should be revelant to following answer -
        {ans}

        Make sure you ask questions which must be relevant to {corpus}

    '''

    response = model.generate_content(p)
    ques = response.text
    return ques
    

@app.get("/")
def display():

    first_question ="Tell Me about Yourself ?"

    return first_question

@app.get("/com")
def ask(ans:str):

    response  = next_question(ans)

    return response


