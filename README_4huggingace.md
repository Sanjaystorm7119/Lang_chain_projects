# 🤗 Hugging Face Embeddings

This notebook showcases the use of open-source embedding models from the Hugging Face hub, specifically the popular `sentence-transformers` library.

## ✨ Key Features

- **Pre-trained Models**: Access to thousands of community models.
- **all-MiniLM-L6-v2**: Using a lightweight yet powerful model for fast inference.
- **Flexibility**: Easily swap models to find the best fit for your specific use case.

## 🛠️ Requirements

```bash
pip install langchain-huggingface sentence-transformers
```

## 📖 Usage Highlights

1. **Initialize Model**:

   ```python
   huggingface_embedding_model = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
   ```

2. **Generate Embeddings**:
   ```python
   huggingface_embedding = huggingface_embedding_model.embed_query("Your text here")
   ```

## 💡 Pro Tip

Check out the [MTEB (Massive Text Embedding Benchmark)](https://huggingface.co/spaces/mteb/leaderboard) to find the best-performing models on Hugging Face.

---

_Part of the GenAI with LangChain series._
