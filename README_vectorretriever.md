# 🔍 Vector Stores & Retrievers in LangChain

This notebook explores LangChain's core abstractions for data retrieval. It covers how to represent data as **Documents**, store them in **Vector Stores**, and use **Retrievers** to bridge the gap between stored data and Large Language Models (LLMs) via Retrieval-Augmented Generation (RAG).

## 🔥 Key Features

- **Document Abstraction**: Learning how to structure text data with associated metadata using LangChain's `Document` class.
- **HuggingFace Embeddings**: Utilizing the `all-MiniLM-L6-v2` model for generating semantic vector representations.
- **ChromaDB Integration**: Setting up and querying a local `Chroma` vector database.
- **Retriever Interface**: Converting vector stores into `Retriever` objects that are compatible with LangChain Expression Language (LCEL).
- **RAG Implementation**: Building a complete RAG chain using **Groq** (Llama3-8b-8192) to answer questions based on retrieved context.

## 🛠️ Requirements

Ensure you have the following packages installed:

```bash
pip install langchain langchain-chroma langchain-huggingface langchain-groq python-dotenv
```

## 📖 Usage Highlights

1. **Initialize Embeddings**:

   ```python
   from langchain_huggingface import HuggingFaceEmbeddings
   embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
   ```

2. **Vector Store Creation**:

   ```python
   vectorstore = Chroma.from_documents(documents, embedding=embeddings)
   ```

3. **Convert to Retriever**:

   ```python
   retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":1})
   ```

4. **RAG Chain Setup**:
   ```python
   rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm
   response = rag_chain.invoke("tell me about dogs")
   ```

## ⚠️ Notes

- Ensure you have a valid `GROQ_API_KEY` and `HF_TOKEN` in your `.env` file.
- The notebook demonstrates both synchronous (`similarity_search`) and asynchronous (`asimilarity_search`) query methods.

---

_Part of the GenAI with LangChain series._
