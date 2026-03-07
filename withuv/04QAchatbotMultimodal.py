import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "{question}")
])

output_parser = StrOutputParser()

st.title("QA Chatbot")

# Sidebar settings
st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

model_name = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
)

max_token = st.sidebar.slider("Max Tokens", 50, 2000, 200)
temp = st.sidebar.slider("Temperature", 0.0, 2.0, 0.7)

# User input
user_input = st.text_input("You:")


def generate_response(user_input, api_key, model_name, max_token, temp):

    model = ChatOpenAI(
        model=model_name,
        temperature=temp,
        max_tokens=max_token,
        api_key=api_key
    )

    chain = prompt | model | output_parser
    response = chain.invoke({"question": user_input})

    return response


# Run when input exists
if user_input and api_key:
    if user_input.lower() in ["bye", "exit", "quit"]:
        st.write("Goodbye 👋")
    else:
        result = generate_response(user_input, api_key, model_name, max_token, temp)
        st.write(result)