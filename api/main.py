from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import argparse
import os
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv


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

    load_dotenv()

    # CHROMA_PATH = "chroma"

    PROMPT_TEMPLATE = """
  

    ---
    Act as an psychatrist,but dont mention that in answer.
    Answer the question based on the above context: {message}
    Provide answers like a human bieng talking to other human bieng.
    Make them feel happy.
    """

    # # Prepare the DB.
    # embedding_function = OpenAIEmbeddings(openai_api_key=os.environ["OPEN_API"])
    # db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # # Search the DB.
    # results = db.similarity_search_with_relevance_scores(query_text, k=1)
    # if len(results) == 0 or results[0][1] < 0.7:
    #     print(f"Unable to find matching results.")
    #     return

    # context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context="general", question=message)
    # print(prompt)

    model = ChatOpenAI()
    response_text = model.predict(prompt)
    # print(response_text)
    return response_text



@app.get("/")
def display():
    first_question = "Hello, Suvansh here!"
    return first_question

@app.get("/talk")
def ask_se(message: str):
    response = conversation(message)
    return response


