import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize model (use lowercase model name)
model = ChatGroq(model="llama-3.3-70b-versatile")

# Create prompt template properly
question = input("You..").lower()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant."),
    ("human", "{question}")
])

# Instantiate parser
output = StrOutputParser()

# Build LCEL chain
chain = prompt | model | output

# Take user input
# question = input("You: ")

while True :
    if question in ['bye','exit']:
        break

response = chain.invoke({"question":question})
print("AI:",response)




############ refer 10groq.ipynb