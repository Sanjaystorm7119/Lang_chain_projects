# 🤖 Interactive Chat App with LangChain & Groq (12App.py)

This script implements an interactive command-line chat application using **LangChain** and **Groq Cloud**. It features advanced message management like streaming responses, persistent session-based chat history, and intelligent message trimming to handle token limits.

## 🌟 Key Features

- **Groq Integration**: Powered by the `llama-3.3-70b-versatile` model for high-speed, intelligent responses.
- **Message Trimming**: Automatically manages context length using `trim_messages` to stay within token limits (30,000 tokens) while retaining the system message.
- **Session-based Chat History**: Uses `ChatMessageHistory` and `RunnableWithMessageHistory` to maintain conversation context across multiple turns for specific sessions.
- **Real-time Streaming**: Provides a dynamic user experience by streaming model responses chunk-by-chunk.

## 🛠️ Architecture Overview

The application follows a standard LangChain pattern:

1.  **Trimmer**: Ensures the conversation doesn't exceed the token count.
2.  **Prompt Template**: Defines a system persona and placeholders for chat history and user input.
3.  **Chat History Store**: An in-memory dictionary acting as a session-based database.
4.  **Chain**: Connects the Prompt, Model, and Output Parser.
5.  **RunnableWithMessageHistory**: Wraps the chain to automatically handle history injection and storage.

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed:

- Python 3.10+
- A Groq API Key (Get it from [Groq Cloud](https://console.groq.com/))

### 2. Installation

Install the required dependencies using the `req.txt` provided in the root directory:

```bash
pip install -r req.txt
```

### 3. Environment Configuration

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Running the Application

Execute the script from your terminal:

```bash
python 12App.py
```

## ⌨️ Usage

- Once started, you can type your questions in the prompt.
- The model will respond in real-time.
- Type `exit`, `quit`, or `bye` to terminate the session.

## 📄 Code Breakdown

| Component             | Responsibility                                                  |
| :-------------------- | :-------------------------------------------------------------- |
| `ChatGroq`            | Interfaces with the Llama 3.3 model via Groq API.               |
| `trim_messages`       | Keeps the last 30,000 tokens of the conversation.               |
| `ChatMessageHistory`  | Stores the messages in an in-memory list for each session.      |
| `MessagesPlaceholder` | Acts as a dynamic slot in the prompt where history is injected. |
| `stream()`            | Enables chunk-by-chunk output for better UX.                    |
