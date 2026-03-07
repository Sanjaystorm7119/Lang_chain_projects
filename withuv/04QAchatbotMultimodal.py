from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

print(model.invoke("Hello, how are you?"))