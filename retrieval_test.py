from retrieval import get_relevant_chunks

query = "What is the return policy?"
chunks = get_relevant_chunks(query)

for i, doc in enumerate(chunks):
    print(f"\n🔹 Chunk {i+1}:\n{doc.page_content}")
