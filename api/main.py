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


def prompt_db(grade, topic, qno, subject):
    
    sys_prompt = ""
    human_prompt = ""

    if grade == "9" and subject == "science":
        sys_prompt = '''
        You are an expert in 9th-grade science with a deep understanding of biology,chemistry, and physics. 
        Your knowledge allows you to create challenging and insightful questions for students.
        '''
        human_prompt = f'''
        Please generate {qno} high-quality science questions for a 9th-grade student. 
        The questions should cover the topic "{topic}" and assess the student's understanding of fundamental scientific principles, critical thinking, and problem-solving skills.
        '''

    elif grade == "9" and subject == "maths":
        sys_prompt = '''
        You are a mathematics expert with a thorough understanding of 9th-grade math concepts, including algebra, geometry, and number theory. 
        You specialize in crafting questions that challenge students' mathematical reasoning.
        '''
        human_prompt = f'''
        Please generate {qno} math questions suitable for a 9th-grade student. 
        The questions should focus on the topic "{topic}" and assess the student's problem-solving abilities, understanding of mathematical concepts, and application of logic.
        '''

    elif grade == "9" and subject == "english":
        sys_prompt = '''
        You are an English language and literature expert with expertise in 9th-grade curricula. 
        You excel at creating questions that develop comprehension, analysis, and interpretation skills.
        '''
        human_prompt = f'''
        Please generate {qno} English questions for a 9th-grade student. 
        The questions should be centered on the topic "{topic}" and should evaluate the student's comprehension, analytical thinking, and ability to interpret texts and concepts.
        '''

    elif grade == "9" and subject == "computer":
        sys_prompt = '''
        You are an expert in computer science with a strong grasp of the 9th-grade syllabus, including basic programming, computer systems, and digital literacy.
        '''
        human_prompt = f'''
        Please generate {qno} computer science questions for a 9th-grade student. 
        The questions should cover the topic "{topic}" and assess the student's understanding of fundamental computer science concepts, logical reasoning, and practical application skills.
        '''


    elif grade == "10" and subject == "science":
        sys_prompt = '''
        You are a science educator with deep knowledge of 10th-grade science, including more advanced topics in biology, chemistry, and physics.
        '''
        human_prompt = f'''
        Please generate {qno} science questions for a 10th-grade student. 
        The questions should focus on the topic "{topic}" and challenge the student's critical thinking, understanding of scientific concepts, and ability to apply them in real-world scenarios.
        '''

    elif grade == "10" and subject == "maths":
        sys_prompt = '''
        You are a mathematics expert with extensive knowledge of 10th-grade topics, including trigonometry, algebra, and geometry. 
        You are adept at creating questions that test deep understanding and application.
        '''
        human_prompt = f'''
        Please generate {qno} math questions for a 10th-grade student. 
        The questions should focus on the topic "{topic}" and assess the student's ability to solve complex problems, understand mathematical principles, and apply them effectively.
        '''

    elif grade == "10" and subject == "english":
        sys_prompt = '''
        You are an English literature and language expert with a focus on 10th-grade education. 
        You create questions that enhance literary analysis, comprehension, and critical thinking.
        '''
        human_prompt = f'''
        Please generate {qno} English questions for a 10th-grade student. 
        The questions should revolve around the topic "{topic}" and should test the student's ability to analyze, comprehend, and interpret literary works and language concepts.
        '''

    elif grade == "10" and subject == "computer":
        sys_prompt = '''
        You are a computer science expert with a deep understanding of the 10th-grade curriculum, including programming, data structures, and basic algorithms.
        '''
        human_prompt = f'''
        Please generate {qno} computer science questions for a 10th-grade student. 
        The questions should cover the topic "{topic}" and evaluate the student's understanding of computer science concepts, coding skills, and logical reasoning.
        '''

    elif grade == "11" and subject == "physics":
        sys_prompt = '''
        You are a physics educator with a strong grasp of 11th-grade physics, including classical mechanics, electromagnetism, and thermodynamics.
        '''
        human_prompt = f'''
        Please generate {qno} physics questions for an 11th-grade student. 
        The questions should focus on the topic "{topic}" and challenge the student's understanding of physical laws, theories, and the ability to apply them to solve problems.
        '''

    elif grade == "11" and subject == "chemistry":
        sys_prompt = '''
        You are a chemistry expert with extensive knowledge of 11th-grade chemistry, including chemical reactions, stoichiometry, and atomic structure.
        '''
        human_prompt = f'''
        Please generate {qno} chemistry questions for an 11th-grade student. 
        The questions should focus on the topic "{topic}" and assess the student's understanding of chemical principles, reaction mechanisms, and problem-solving skills in chemistry.
        '''

    elif grade == "11" and subject == "maths":
        sys_prompt = '''
        You are a mathematics educator with expertise in 11th-grade topics, including calculus, linear algebra, and combinatorics.
        '''
        human_prompt = f'''
        Please generate {qno} math questions for an 11th-grade student. 
        The questions should be centered on the topic "{topic}" and should challenge the student's ability to solve complex mathematical problems, understand advanced concepts, and apply them effectively.
        '''

    elif grade == "11" and subject == "english":
        sys_prompt = '''
        You are an English literature and language expert focused on 11th-grade education. 
        You specialize in creating questions that develop critical analysis, comprehension, and interpretation skills.
        '''
        human_prompt = f'''
        Please generate {qno} English questions for an 11th-grade student. 
        The questions should focus on the topic "{topic}" and should evaluate the student's ability to analyze literary works, comprehend complex texts, and think critically about language and meaning.
        '''

    elif grade == "11" and subject == "computer":
        sys_prompt = '''
        You are a computer science expert with in-depth knowledge of 11th-grade topics, including algorithms, data structures, and software design.
        '''
        human_prompt = f'''
        Please generate {qno} computer science questions for an 11th-grade student. 
        The questions should cover the topic "{topic}" and assess the student's understanding of advanced computer science concepts, coding proficiency, and problem-solving skills.
        '''

    elif grade == "12" and subject == "physics":
        sys_prompt = '''
        You are an advanced physics educator with expertise in 12th-grade topics such as quantum mechanics, relativity, and wave theory.
        '''
        human_prompt = f'''
        Please generate {qno} physics questions for a 12th-grade student. 
        The questions should cover the topic "{topic}" and should challenge the student's understanding of advanced physical theories, mathematical modeling, and experimental analysis.
        '''

    elif grade == "12" and subject == "chemistry":
        sys_prompt = '''
        You are an expert in 12th-grade chemistry, including organic chemistry, physical chemistry, and advanced chemical analysis.
        '''
        human_prompt = f'''
        Please generate {qno} chemistry questions for a 12th-grade student. 
        The questions should focus on the topic "{topic}" and should test the student's mastery of chemical reactions, molecular structure, and theoretical concepts.
        '''

    elif grade == "12" and subject == "maths":
        sys_prompt = '''
        You are a mathematics educator with deep expertise in 12th-grade topics, including differential equations, complex numbers, and advanced calculus.
        '''
        human_prompt = f'''
        Please generate {qno} math questions for a 12th-grade student. 
        The questions should revolve around the topic "{topic}" and should assess the student's ability to tackle complex mathematical problems, understand theoretical concepts, and apply them effectively.
        '''

    elif grade == "12" and subject == "english":
        sys_prompt = '''
        You are an English expert with specialization in 12th-grade literary analysis, critical theory, and advanced language studies.
        '''
        human_prompt = f'''
        Please generate {qno} English questions for a 12th-grade student. 
        The questions should cover the topic "{topic}" and should challenge the student's ability to engage in deep literary analysis, comprehend complex texts, and critically evaluate language and meaning.
        '''

    elif grade == "12" and subject == "computer":
        sys_prompt = '''
        You are a computer science expert with advanced knowledge of 12th-grade topics, including software engineering, algorithm design, and machine learning.
        '''
        human_prompt = f'''
        Please generate {qno} computer science questions for a 12th-grade student. 
        The questions should focus on the topic "{topic}" and should assess the student's understanding of complex algorithms, software development practices, and modern computing challenges.
        '''

    return [sys_prompt, human_prompt]



def physics_chemistry(grade,topic,qno,subject):

    prompt = prompt_db(grade,topic,qno,subject)

    sys_prompt = prompt[0]
    human_prompt = prompt[1]

    completion = model_claude.completions.create(model="claude-2.1",  max_tokens_to_sample=350, prompt=f"{HUMAN_PROMPT}{sys_prompt}/n{human_prompt}{AI_PROMPT}")
    ques = completion.completion
    return ques

def science_english(grade,topic,qno,subject):

    prompt = prompt_db(grade,topic,qno,subject)

    sys_prompt = prompt[0]
    human_prompt = prompt[1]
    
    output = model_gemini([ SystemMessage(content=sys_prompt), HumanMessage(content= human_prompt )])
    ques=""
    ques = output.content
    return ques

def computer_maths(grade,topic,qno,subject):

    prompt = prompt_db(grade,topic,qno,subject)

    sys_prompt = prompt[0]
    human_prompt = prompt[1]
    
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
