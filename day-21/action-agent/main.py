from agent.graph import build_graph

agent = build_graph()

result = agent.invoke({
    "user_input": "Create a file report.txt with summary of AI trends"
})

print(result["final_output"])