

import re
from retrieval import get_relevant_chunks
from llm_engine import generate_answer

def use_calculator(query):
    try:
       
        expression = re.findall(r"[-+*/().\d\s]+", query)
        expression = ''.join(expression).strip()
        result = eval(expression)
        return f" Result: {result}"
    except Exception as e:
        return f" Failed to calculate: {str(e)}"


from PyDictionary import PyDictionary
dictionary = PyDictionary()

def use_dictionary(query):
    match = re.search(r"define\s+(.*)", query.lower())
    if match:
        word = match.group(1).strip()
        meaning = dictionary.meaning(word)
        if meaning:
            output = [f" {k}: {v[0]}" for k, v in meaning.items()]
            return '\n'.join(output)
        else:
            return " Could not find definition."
    return " Invalid dictionary query."


def route_query(query):
    query = query.strip().lower()

    if any(k in query for k in ["+", "-", "*", "/", "calculate", "sum", "multiply"]):
        print(" Routed to: Calculator Tool")
        return use_calculator(query)

    elif query.startswith("define "):
        print(" Routed to: Dictionary Tool")
        return use_dictionary(query)

    else:
        print(" Routed to: RAG + LLM")
        chunks = get_relevant_chunks(query)
        
        return generate_answer(query, chunks)
