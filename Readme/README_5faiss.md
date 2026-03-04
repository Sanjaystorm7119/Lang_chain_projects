# ⚡ FAISS: Facebook AI Similarity Search

This notebook covers the use of FAISS (Facebook AI Similarity Search), one of the fastest and most efficient libraries for semantic search and clustering of dense vectors.

## 🦅 Key Features

- **Blazing Fast Search**: Optimized for large-scale vector similarity.
- **Local Indexing**: Store your index locally to disk for later use.
- **Similarity Search with Scores**: Retrieve documents along with their logical distance (similarity score).
- **As Retriever**: Easily convert a FAISS index into a LangChain retriever for RAG pipelines.

## 🛠️ Requirements

```bash
pip install faiss-cpu  # or faiss-gpu if available
pip install langchain-community
```

## 📖 Usage Highlights

1. **Create FAISS Store**:

   ```python
   db = FAISS.from_documents(documents, ollama_embeddings)
   ```

2. **Similarity Search**:

   ```python
   docs = db.similarity_search("What is an essay?")
   ```

3. **Save/Load Local Index**:
   ```python
   db.save_local("faiss_index")
   # To load later:
   # new_db = FAISS.load_local("faiss_index", ollama_embeddings)
   ```

---

_Part of the GenAI with LangChain series._
