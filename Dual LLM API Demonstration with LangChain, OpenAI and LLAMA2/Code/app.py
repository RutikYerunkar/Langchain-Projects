#Responsible for creating all API's
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
  title="Langchain Server",
  version="1.0",
  description="Simple API Server"
)

model = ChatOpenAI()
llm = Ollama(model='llama2')

prompt1 = ChatPromptTemplate.from_template("Please provide information or perform a task related to {topic}.")
prompt2 = ChatPromptTemplate.from_template("Can you help me with details or perform a task related to {topic}?")

add_routes(
  app,
  prompt1|model,
  path='/openai'
)

add_routes(
  app,
  prompt2|llm,
  path='/ollama'
)

if __name__=="__main__":
  uvicorn.run(app,host='localhost',port=8000)