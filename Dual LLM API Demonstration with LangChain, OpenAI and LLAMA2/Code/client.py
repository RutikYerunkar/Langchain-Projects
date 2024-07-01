#With which user will interact (In real life: Web App or Mobile App)
import requests
import streamlit as st

def get_openai_response(input_text):
  response = requests.post("http://localhost:8000/openai/invoke",
  json={'input':{'topic':input_text}})

  return response.json()['output']['content']

def get_ollama_response(input_text):
  response = requests.post("http://localhost:8000/ollama/invoke",
  json={'input':{'topic':input_text}})

  return response.json()['output']

#Streamlit Framework
st.title('Dual LLM API Demonstration with LangChain, OpenAI and LLAMA2')
input_text=st.text_input("Chat with OpenAI LLM")
input_text1=st.text_input("Chat with LLAMA LLM")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))