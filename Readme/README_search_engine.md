# 🔍 LangChain - Chat with Search (search_engine.py)

This Streamlit app implements an **AI-powered search chatbot** that can query the web, academic papers, and Wikipedia in real-time. It uses **LangGraph's ReAct agent** with **Groq Cloud** for blazing-fast responses, backed by three powerful search tools.

## 🌟 Key Features

- **Multi-Source Search**: Combines DuckDuckGo web search, Arxiv academic papers, and Wikipedia for comprehensive answers.
- **Groq-Powered LLM**: Uses the `llama-3.3-70b-versatile` model via Groq for high-speed inference.
- **LangGraph ReAct Agent**: Leverages `langgraph.prebuilt.create_react_agent` — the modern, recommended way to build tool-calling agents (replaces the deprecated `AgentExecutor`).
- **Chat Interface**: Full conversational UI with persistent message history using Streamlit's `st.chat_message` and `st.chat_input`.

## 🛠️ Architecture Overview

The application uses LangGraph's prebuilt ReAct agent pattern:

1. **Tools**: Three search tools are initialized — DuckDuckGo (web), Arxiv (papers), and Wikipedia.
2. **LLM**: Groq's Llama3 model handles reasoning and tool selection.
3. **ReAct Agent**: `create_react_agent(llm, tools)` creates an agent that autonomously decides which tools to call and synthesizes the results.
4. **Chat History**: Streamlit session state maintains the full conversation across interactions.

```
User Query → LangGraph ReAct Agent → Tool Selection → Search Results → AI Response
                                          ↓
                              ┌───────────┼───────────┐
                              │           │           │
                         DuckDuckGo    Arxiv     Wikipedia
```

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed:

- Python 3.10+
- A Groq API Key (Get it from [Groq Cloud](https://console.groq.com/))

### 2. Installation

Install the required dependencies using the `req.txt` provided in the project directory:

```bash
pip install -r req.txt
```

Key dependencies include:

- `langchain-groq` — Groq LLM integration
- `langchain-community` — Search tools (Arxiv, Wikipedia, DuckDuckGo)
- `langgraph` — Modern agent framework
- `streamlit` — Web UI
- `duckduckgo-search` — Web search backend
- `arxiv` — Arxiv API wrapper
- `wikipedia` — Wikipedia API wrapper

### 3. Running the Application

Launch the Streamlit app from your terminal:

```bash
streamlit run search_engine.py
```

### 4. Configuration

Enter your **Groq API Key** in the sidebar when the app loads. No `.env` file is required — the key is entered directly in the UI.

## ⌨️ Usage

1. Open the app in your browser (default: `http://localhost:8501`).
2. Enter your Groq API key in the **Settings** sidebar.
3. Type your question in the chat input (e.g., "What is machine learning?").
4. The agent will automatically search the web, Arxiv, and/or Wikipedia as needed and return a synthesized answer.

## 📄 Code Breakdown

| Component             | Responsibility                                                   |
| :-------------------- | :--------------------------------------------------------------- |
| `ChatGroq`            | Interfaces with the Llama3 model via Groq API.                   |
| `create_react_agent`  | Creates a LangGraph ReAct agent that autonomously selects tools. |
| `DuckDuckGoSearchRun` | Performs real-time web searches via DuckDuckGo.                  |
| `ArxivQueryRun`       | Queries academic papers from the Arxiv repository.               |
| `WikipediaQueryRun`   | Fetches summaries from Wikipedia articles.                       |
| `st.session_state`    | Maintains chat history across Streamlit reruns.                  |
| `st.chat_message`     | Renders chat bubbles for user and assistant messages.            |

## 🔄 Migration Note

This app uses the **new LangGraph approach** instead of the deprecated `langchain.agents`:

| Old (Deprecated)                                  | New (LangGraph)                                        |
| :------------------------------------------------ | :----------------------------------------------------- |
| `from langchain.agents import create_react_agent` | `from langgraph.prebuilt import create_react_agent`    |
| Manual `PromptTemplate` with ReAct format         | Not needed — handled internally                        |
| `AgentExecutor(agent=agent, tools=tools)`         | `create_react_agent(llm, tools)` returns a ready agent |
| `executor.invoke({"input": ...})["output"]`       | `agent.invoke({"messages": [...]})["messages"]`        |
