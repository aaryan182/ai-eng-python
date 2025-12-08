# FULL MINI LANGGRAPH EXAMPLE (Planner → Worker → Critic → Loop)

# Step 1 — Define state
class AgentState(TypedDict):
    task: str
    steps: list
    draft: str
    review: str
    approved: bool

# Step 2 — Nodes
# Planner Node
def planner(state: AgentState):
    state["steps"] = llm.plan(state["task"])
    return state

# Worker Node
def worker(state: AgentState):
    state["draft"] = llm.write_code(state["steps"])
    return state

# Critic Node
def critic(state: AgentState):
    review = llm.review(state["draft"])
    state["review"] = review
    state["approved"] = "APPROVED" in review
    return state

# Final Node
def final(state: AgentState):
    return state

# Step 3 — Build Graph
graph = StateGraph(AgentState)

# Register nodes
graph.add_node("planner", planner)
graph.add_node("worker", worker)
graph.add_node("critic", critic)
graph.add_node("final", final)

# Entry point
graph.set_entry_point("planner")

# Normal edges
graph.add_edge("planner", "worker")
graph.add_edge("worker", "critic")

# Conditional edges
graph.add_conditional_edges(
    "critic",
    lambda s: "final" if s["approved"] else "worker",
    {
        "final": "final",
        "worker": "worker"
    }
)

graph.add_edge("final", END)

executor = graph.compile()

# Step 4 — Run
result = executor.invoke({"task": "Write a FastAPI PDF summarizer"})
print(result)