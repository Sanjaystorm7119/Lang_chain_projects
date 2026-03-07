import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

## Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name="Search")

st.title("LangChain - Chat with search")

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile", streaming=True)
    tools = [search, arxiv, wiki]

    # New LangGraph way — no need for PromptTemplate or AgentExecutor
    agent = create_react_agent(llm, tools)

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            response = agent.invoke({"messages": [("user", prompt)]})
            # Extract the final AI message from the response
            ai_messages = [
                msg for msg in response["messages"]
                if hasattr(msg, "type") and msg.type == "ai" and msg.content
            ]
            output = ai_messages[-1].content if ai_messages else "No response generated."
            st.write(output)
        st.session_state.messages.append({"role": "assistant", "content": output})