# 🦜 GenAI with LangChain Series

A comprehensive collection of projects exploring Generative AI, Document Processing, and Vector Databases using the LangChain framework.

## 📂 Project Structure

| Project                   | Notebook                                             | Documentation                           | Description                                             |
| :------------------------ | :--------------------------------------------------- | :-------------------------------------- | :------------------------------------------------------ |
| **01. LangChain Basics**  | [1langchain.ipynb](./1langchain.ipynb)               | [README](./README_1langchain.md)        | Document Loaders (PDF, Web, Text) and Text Splitters.   |
| **02. OpenAI Embeddings** | [2embeddings.ipynb](./2embeddings.ipynb)             | [README](./README_2embeddings.md)       | Vector embeddings using OpenAI and storage in ChromaDB. |
| **03. Local Ollama**      | [3ollamaembeddings.ipynb](./3ollamaembeddings.ipynb) | [README](./README_3ollamaembeddings.md) | Privacy-focused local embeddings using Ollama.          |
| **04. Hugging Face**      | [4huggingace.ipynb](./4huggingace.ipynb)             | [README](./README_4huggingace.md)       | Open-source state-of-the-art embedding models.          |
| **05. FAISS Indexing**    | [5faiss.ipynb](./5faiss.ipynb)                       | [README](./README_5faiss.md)            | High-performance vector search using Meta's FAISS.      |

## 🛠️ Global Setup

To run any of these notebooks, it is recommended to create a virtual environment:

```bash
conda create -p venv python=3.10 -y
conda activate venv/
pip install -r req.txt
```

Ensure you have a `.env` file with the following keys if applicable:

- `OPENAI_API_KEY`
- `HUGGINGFACE_API_KEY`

---

_Developed as part of the LangChain Learning Journey._
