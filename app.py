
import streamlit as st
from router import route_query, get_relevant_chunks

st.set_page_config(page_title="RAG QA Assistant", layout="centered")

st.title("🧠 RAG-Powered Multi-Agent Assistant")
st.markdown("Ask a question. The assistant will decide whether to calculate, define, or retrieve + answer.")

query = st.text_input("Your question", placeholder="E.g. Define entropy, What is 3 * (4 + 5), How do I return a product?")

if st.button("Get Answer") and query:
    with st.spinner("Processing..."):
        query_lower = query.lower()

        if any(k in query_lower for k in ["+", "-", "*", "/", "calculate", "sum", "multiply"]):
            route = " Calculator Tool"
        elif query_lower.startswith("define "):
            route = "Dictionary Tool"
        else:
            route = " RAG + LLM"

        st.write(f"**Agent Path Chosen:** {route}")

        if route == " RAG + LLM":
            chunks = get_relevant_chunks(query)
            st.subheader(" Retrieved Chunks")
            for i, chunk in enumerate(chunks, 1):
                st.markdown(f"**Chunk {i}:** {chunk.page_content}")

        answer = route_query(query)
        st.subheader("💬 Final Answer")
        st.markdown(answer)
