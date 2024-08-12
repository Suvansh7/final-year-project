def generate (text):
    import os
    from constants import openai_key
    from langchain.llms import OpenAI
    
    #initialise the model
    os.environ["OPENAI_API_KEY"] = openai_key
    llm_model = OpenAI(temperature=0.8)
    res = llm_model(text)
    

    return res