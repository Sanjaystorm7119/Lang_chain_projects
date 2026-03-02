############ refer 10groq.ipynb

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


"""
MessagesPlaceholder  →  Empty glass (just a container slot)
ChatMessageHistory   →  Water (the actual stored messages)
RunnableWithHistory  →  Person who fills & refills the glass automatically
BaseChatMessageHistory → Blueprint to make your own bottle (Redis, DB, etc.)
"""

# Initialize the model
chatGroq_model = ChatGroq(model="llama-3.3-70b-versatile")

# Create a generic system + human prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful assistant. Please respond to questions asked."
    ),
    MessagesPlaceholder(variable_name="messages"),
    HumanMessagePromptTemplate.from_template(
        "{question}"
    ),
])

parser = StrOutputParser()
chain = prompt | chatGroq_model | parser


store = {}

def get_session_history(session_id : str) -> BaseChatMessageHistory :
    if session_id not in store :
        store[session_id] = ChatMessageHistory()
    return store[session_id]

config = {"configurable" : {"session_id" : "chat1"}}

with_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="question", history_messages_key="messages")


# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    print("Groq: ", end="", flush=True)

    for chunk in with_history.stream(
        {
            "question": user_input
        },
        config=config
    ):
        print(chunk, end="", flush=True)

    print()  
        

"""
# Fill the template - no stream 

    response = with_history.invoke({
        "language": "French",  # you can make this dynamic too
        "text": user_input
    }, config=config)

    # print(f"You: {user_input}")
    print(f"Groq: {response}")

"""
