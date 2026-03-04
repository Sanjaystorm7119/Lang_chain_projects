import os
import bs4
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
import nest_asyncio


nest_asyncio.apply()  # fixes jupyter event loop conflict (stupid jupyter ipynb conflits)

import asyncio

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HUGGINGFACE_API_KEY'] = os.getenv("HUGGINGFACE_API_KEY")

# Embeddings
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load Wikipedia page
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
documents = loader.load()
print(f" Loaded {len(documents)} documents")

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_documents = splitter.split_documents(documents)
print(f" Split into {len(splitted_documents)} chunks")

# Vectorstore + Retriever
vectorstore = FAISS.from_documents(splitted_documents, hf_embeddings)
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "fetch_k": 10}
)

# LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

#  Prompt now has 3 slots:
#    1. system   — instructions
#    2. chat_history — past conversation (MessagesPlaceholder)
#    3. question — current user input

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the question based on the context below:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),  # ← memory slot
    ("user", "{question}")
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# RAG chain — context + question + chat_history
rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
        # "chat_history": RunnablePassthrough()   # passed through from history
        # RunnableWithMessageHistory injects it automatically
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Session store
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Wrap chain with memory
rag_with_history = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="question",      # current question key
    history_messages_key="chat_history" # matches MessagesPlaceholder name
)

config = {"configurable": {"session_id": "user1"}}

# Chat loop
# async def chat():
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    response = rag_with_history.invoke(
        {"question": user_input},
        config=config
    )
    print(f"Ai: {response}")

# asyncio.run(chat())

### What Changed From Original

# Original prompt:                    New prompt:
# ───────────────                     ───────────
# system + context                    system + context
# question                            MessagesPlaceholder  <= added
#                                     question

# ## Memory + RAG Work Together 

# User: "What is AI?"
#         ↓
# RunnableWithMessageHistory
#     ├── retriever fetches relevant Wikipedia chunks  → context
#     ├── ChatMessageHistory fetches past messages     → chat_history
#     └── question passed as-is                        → question
#         ↓
# Prompt filled with all 3 slots
#         ↓
# LLM answers WITH document context AND conversation memory 
#         ↓
# New Human + AI messages saved back to ChatMessageHistory