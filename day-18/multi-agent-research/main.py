from graph.graph import build_graph

if __name__ == "__main__":
    agent = build_graph()

    query = "Impact of artificial intelligence on remote work productivity"

    result = agent.invoke({"query": query})

    print("\n==== FINAL OUTPUT ====\n")
    print(result["final_output"])