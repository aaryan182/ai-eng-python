from agent.graph import build_graph

agent = build_graph()

result = agent.invoke({
    "user_id": "user_123",
    "input": "Please reply in a formal tone from now on"
})

print(result["response"])