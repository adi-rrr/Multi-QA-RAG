import requests
import json

def fetch_answer(query):
    # Prepare the request body
    request_data = {
        "model": "thudm/glm-z1-32b:free",
        "messages": [{"role": "user", "content": query}]
    }

    headers = {
        "Authorization": "Bearer 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",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    # Make the API call
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(request_data))

    # Check for success and handle the response
    if response.status_code == 200:
        response_data = response.json()

        # Extract the assistant's response
        if response_data.get('choices'):
            answer = response_data['choices'][0]['message']['content']
            return answer
        else:
            return "No answer found."
    else:
        return f"Error: {response.status_code}"

# Example Queries
queries = [
    "How much is 3 plus 5?",
    "What is Python?",
    "Tell me about the shipping policy."
]

# Fetch and print answers
for query in queries:
    answer = fetch_answer(query)
    print(f"Query: {query}\nAnswer: {answer}\n")
