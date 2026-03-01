#pip install sse-starlette langserve
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

groq_model = ChatGroq(model="llama3.2")

prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"you are a helpful assistant. Please respond to questions asked"),
        ('user',"{question}")
    ]
)

output = StrOutputParser()
chain = prompt | groq_model | output

#App definition
app = FastAPI(title="Groq chatbot", description="Groq Api chat", version="0.0.1")
add_routes(app, chain, path="/chat")  #Adding the chain to the app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)