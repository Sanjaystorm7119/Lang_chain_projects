# 🦙 Local Embeddings with Ollama

This notebook demonstrates how to run semantic embedding models entirely locally using Ollama. This approach provides privacy and avoids API costs by utilizing local hardware.

## 🌟 Key Features

- **Local Processing**: No data leaves your machine.
- **nomic-embed-text Model**: Using high-performance open-source embedding models.
- **Integration**: Seamlessly works with LangChain's existing vector store ecosystem (like FAISS).

## 🛠️ Requirements

- [Ollama](https://ollama.com/) installed and running.
- Python packages:

```bash
pip install langchain-community langchain-ollama
```

## 📖 Usage Highlights

1. **Get Local Embeddings**:

   ```python
   ollama_embeddings = OllamaEmbeddings(model='nomic-embed-text:latest')
   embeddings = ollama_embeddings.embed_documents(documents)
   ```

2. **Wait, it's local!**: You need to pull the model first:
   ```bash
   ollama pull nomic-embed-text
   ```

---

_Part of the GenAI with LangChain series._
