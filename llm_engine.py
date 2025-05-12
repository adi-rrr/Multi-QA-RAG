import requests
import json

OPENROUTER_API_KEY = "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"  # Replace with your actual key or load from env
MODEL = "thudm/glm-4-9b:free" # or any model on OpenRouter like 'mistralai/mistral-7b-instruct'

def generate_answer(query, chunks):
    context = "\n".join([doc.page_content for doc in chunks])
    
    prompt = f"""You are a helpful assistant. Use the following context to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "RAG-QA-Assistant",  # Optional, helps ranking
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful knowledge assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print("❌ Error from OpenRouter:", response.status_code, response.text)
        return "Failed to generate answer."
