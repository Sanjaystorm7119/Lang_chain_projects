import os
from dotenv import  load_dotenv
load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


#langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGSMITH_ENDPOINT'] = os.getenv('LANGSMITH_ENDPOINT')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

ollama_model = ChatOllama(model="gemma:2b")

prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"you are a helpful assistant. Please respond to questions asked"),
        ('user',"Question:{question}")
    ]
)

st.title("ollama : google gemma model")
input_text = st.text_input("what's on your mind ?")

output = StrOutputParser()

chain = prompt | ollama_model | output

if input_text:
    st.write(chain.invoke({"question":input_text}))

