# Entrypoint for running agent

from graph.graph import build_graph

if __name__ == "__main__":
    email_agent = build_graph()

    input_text = "hey, tell my manager i need one day off tomorrow due to a family event"

    result = email_agent.invoke({"user_input": input_text})
    
    print("\n=== FINAL EMAIL ===\n")
    print(result["final_email"])