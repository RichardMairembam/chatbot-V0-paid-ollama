from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple Chat application."
)
add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)
llm_openai = ChatOpenAI()

llm_ollamma = Ollama(model='llama2')

prompt1=ChatPromptTemplate.from_template("Write an essay on {topic} with 100 words.")
prompt2=ChatPromptTemplate.from_template("Write an poem on {topic} with 100 words.")

add_routes(
    app,
    prompt1|llm_openai,
    path="/essay"    
)
add_routes(
    app,
    prompt1|llm_ollamma,
    path="/poem"    
)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)








