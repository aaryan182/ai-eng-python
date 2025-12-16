from langgraph.graph import StateGraph, END
from .state import PlanState

graph = StateGraph(PlanState)

graph.add_node("planner", planner_node)
graph.add_node("router", router_node)
graph.add_node("research", research_node)
graph.add_node("rag", rag_node)
graph.add_node("summarize", summarize_node)
graph.add_node("final", final_node)
graph.add_node("failover", failover_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "router")

graph.add_conditional_edges(
    "router",
    route_selector,
    {
        "research": "research",
        "rag": "rag",
        "simple_answer": "final",
        "fail": "failover"
    }
)

graph.add_edge("research", "summarize")
graph.add_edge("rag", "summarize")
graph.add_edge("summarize", "final")

graph.add_edge("failover", "router")
graph.add_edge("final", END)

agent = graph.compile()