# ingest/ingest_docs.py

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

DATA_PATH = "data/docs"
INDEX_PATH = "data/faiss_index"

def load_documents(path):
    docs = []
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(path, filename))
            docs.extend(loader.load())
    return docs

def chunk_documents(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def embed_and_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(chunks, embeddings)
    vectordb.save_local(INDEX_PATH)
    print(f"✅ FAISS index saved to {INDEX_PATH}")

if __name__ == "__main__":
    raw_docs = load_documents(DATA_PATH)
    print(f"📄 Loaded {len(raw_docs)} documents.")
    chunks = chunk_documents(raw_docs)
    print(f"🔹 Split into {len(chunks)} chunks.")
    embed_and_store(chunks)
