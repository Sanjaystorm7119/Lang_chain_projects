import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# --- Modern tool definitions using @tool decorator + standalone libraries ---
# Replaces deprecated langchain_community wrappers (ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun)

@tool
def arxiv_search(query: str) -> str:
    """Search Arxiv for academic papers. Use this for scientific or research-related questions."""
    import arxiv
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=1)
    results = list(client.results(search))
    if not results:
        return "No results found on Arxiv."
    paper = results[0]
    summary = paper.summary[:200] if paper.summary else "No summary available."
    return f"Title: {paper.title}\nSummary: {summary}\nURL: {paper.entry_id}"


@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for general knowledge. Use this for factual or encyclopedic questions."""
    import wikipedia
    try:
        page = wikipedia.page(query, auto_suggest=True)
        return page.content[:200]
    except wikipedia.exceptions.DisambiguationError as e:
        # Pick the first suggestion on disambiguation
        try:
            page = wikipedia.page(e.options[0])
            return page.content[:200]
        except Exception:
            return f"Wikipedia disambiguation: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for that query."
    except Exception as e:
        return f"Wikipedia error: {str(e)}"


@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo. Use this for current events, recent info, or general web queries."""
    from duckduckgo_search import DDGS
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        if not results:
            return "No web results found."
        return "\n\n".join(
            f"Title: {r['title']}\nSnippet: {r['body']}\nURL: {r['href']}"
            for r in results
        )
    except Exception as e:
        return f"Web search error: {str(e)}"


st.title("🔎 LangChain - Chat with Search")
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

    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile",
        streaming=False,
        max_retries=2,
    )
    tools = [web_search, arxiv_search, wikipedia_search]

    agent = create_react_agent(
        llm,
        tools,
        prompt="You are a helpful assistant. Use the available tools to answer questions accurately."
    )

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            try:
                response = agent.invoke({"messages": [("user", prompt)]})
                ai_messages = [
                    msg for msg in response["messages"]
                    if hasattr(msg, "type") and msg.type == "ai" and msg.content
                ]
                output = ai_messages[-1].content if ai_messages else "No response generated."
            except Exception as e:
                output = f"Error: {str(e)}. Please try again."

            st.write(output)
        st.session_state.messages.append({"role": "assistant", "content": output})
