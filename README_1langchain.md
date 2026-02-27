# 🦜 LangChain: Document Loaders & Text Splitters

This notebook demonstrates the fundamental steps of data ingestion and preprocessing in the LangChain ecosystem. It covers how to load data from various sources and split them into manageable chunks for LLM processing.

## 🚀 Key Features

- **Document Loading**:
  - `TextLoader`: Loading plain text files.
  - `PyMuPDFLoader`: Extracting text from PDF documents.
  - `WebBaseLoader`: Scraping and parsing content from websites using BeautifulSoup.
- **Text Splitting**:
  - `RecursiveCharacterTextSplitter`: Intelligently splitting large documents into chunks with specified overlap to maintain context.

## 🛠️ Requirements

```bash
pip install langchain langchain-community pymupdf beautifulsoup4
```

## 📖 Usage Highlights

1. **Load a Text File**:

   ```python
   loader = TextLoader("textfile.txt")
   docs = loader.load()
   ```

2. **Load a PDF**:

   ```python
   loader = PyMuPDFLoader("path/to/file.pdf")
   pages = loader.load()
   ```

3. **Split into Chunks**:
   ```python
   splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
   chunks = splitter.split_documents(docs)
   ```

---

_Part of the GenAI with LangChain series._
