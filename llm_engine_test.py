from retrieval import get_relevant_chunks
from llm_engine import generate_answer

query = "Do you ship internationally?"
chunks = get_relevant_chunks(query)
answer = generate_answer(query, chunks)

print("\n🧠 Final Answer:")
print(answer)
