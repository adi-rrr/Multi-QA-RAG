from router import route_query

while True:
    query = input("\n🔍 Ask something: ")
    if query.lower() in ["exit", "quit"]:
        break
    answer = route_query(query)
    print("\n💬 Answer:\n", answer)
