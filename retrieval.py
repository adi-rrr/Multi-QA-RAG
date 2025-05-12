# retriever.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

INDEX_PATH = "data/faiss_index"

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return vectordb

def get_relevant_chunks(query, k=3):
    vectordb = load_vector_store()
    docs = vectordb.similarity_search(query, k=k)
    return docs
