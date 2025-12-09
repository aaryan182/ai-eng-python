# Build the langgraph with nodes + edges

from langgraph.graph import StateGraph, END
from .nodes import extract_intent, rewrite_message, formal_email
from .state import EmailState

def build_graph():
    graph = StateGraph(EmailState)

    graph.add_node("extract_intent", extract_intent)
    graph.add_node("rewrite_message", rewrite_message)
    graph.add_node("formal_email", formal_email)

    graph.set_entry_point("extract_intent")

    graph.add_edge("extract_intent", "rewrite_message")
    graph.add_edge("rewrite_message", "formal_email")
    graph.add_edge("formal_email", END)

    return graph.compile()