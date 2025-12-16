from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import load_memory_node, respond_node, update_memory_node

def build_graph():
    g = StateGraph(AgentState)

    g.add_node("load_memory", load_memory_node)
    g.add_node("respond", respond_node)
    g.add_node("update_memory", update_memory_node)

    g.set_entry_point("load_memory")

    g.add_edge("load_memory", "respond")
    g.add_edge("respond", "update_memory")
    g.add_edge("update_memory", END)

    return g.compile()