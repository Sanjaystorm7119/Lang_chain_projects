# 🧠 OpenAI Embeddings & ChromaDB

This notebook explores the creation of high-dimensional vector representations for text using OpenAI's state-of-the-art embedding models and storing them in an efficient vector database, ChromaDB.

## 🔥 Key Features

- **OpenAI Embeddings**: Utilizing `text-embedding-3-large` for high-quality semantic representations.
- **ChromaDB Integration**: Setting up a local vector store to persist and query your embeddings.
- **Environment Management**: Using `.env` files to securely manage API keys.

## 🛠️ Requirements

```bash
pip install langchain-openai langchain-chroma python-dotenv
```

## 📖 Usage Highlights

1. **Initialize Embeddings**:

   ```python
   embedd = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
   ```

2. **Vector Store Creation**:
   ```python
   db = Chroma.from_documents(documents=splitted_text, embedding=embedd)
   ```

## ⚠️ Notes

- Ensure you have a valid `OPENAI_API_KEY` in your `.env` file.
- The notebook contains troubleshooting steps for `ConfigError` related to Chroma configuration.

---

_Part of the GenAI with LangChain series._
