# 🔎 LangChain Search Engine App

A high-performance search-enabled chatbot built with **LangChain**, **LangGraph**, and **Streamlit**. Powered by Groq for lightning-fast inference and modern tool wrappers for real-time information retrieval.

---

## 🚀 Modern Architecture (2025 Updates)

This project has been migrated from legacy `langchain_community` wrappers to the **Modern Tool Pattern**.

### Key Improvements:

- **Zero Community Dependency**: Tools are defined using the `langchain_core.tools.tool` decorator for maximum compatibility and modern feature-set.
- **Standalone Libraries**: Uses the latest standalone libraries (`duckduckgo-search`, `arxiv`, `wikipedia`) for more reliable data fetching and lower overhead.
- **Robust Error Handling**: Optimized for common search failure modes like Wikipedia disambiguation errors and empty Arxiv search results.
- **LangGraph Integration**: Uses `create_react_agent` for a structured, graph-based agent workflow that's easier to debug and extend.

---

## 🛠️ Tools Included

| Tool           | Library             | Description                                                  |
| -------------- | ------------------- | ------------------------------------------------------------ |
| **Web Search** | `duckduckgo-search` | Real-time web search for current events and general queries. |
| **Arxiv**      | `arxiv`             | Search for scientific papers and research summaries.         |
| **Wikipedia**  | `wikipedia`         | In-depth factual and encyclopedic background information.    |

---

## 💻 Tech Stack

- **Framework**: [LangChain](https://www.langchain.com/) 0.3.x
- **Agent Framework**: [LangGraph](https://langchain-ai.github.io/langgraph/)
- **Model**: `llama-3.3-70b-versatile` (via Groq)
- **UI**: Streamlit

---

## ⚙️ Setup & Installation

### 1. Prerequisites

Ensure you have `uv` installed (the modern, fast Python package manager):

```bash
# Install uv if you haven't
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Project Initializaton

```bash
# Initialize and create venv
uv init
uv venv
# Activate venv (Windows)
.venv\Scripts\activate
# Activate venv (Mac/Linux)
# source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# All standard dependencies + tools (arxiv, wikipedia, ddgs) are in req.txt
uv pip install -r req.txt
```

### 4. Running the App

```bash
streamlit run search_engine.py
```

---

## 📄 Environment Configuration

Ensure your `.env` file (at root) includes your **Groq API Key**:

```env
GROQ_API_KEY=your_api_key_here
```

---

_This project is part of the "GenAI with LangChain" series, optimized for the latest framework patterns._
