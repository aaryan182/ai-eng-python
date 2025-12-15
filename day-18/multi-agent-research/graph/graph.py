from langgraph.graph import StateGraph, END
from .state import ResearchState
from .research_agent import research_agent
from .summarizer_agent import summarizer_agent
from .formatter_agent import formatter_agent


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("research", research_agent)
    graph.add_node("summarize", summarizer_agent)
    graph.add_node("format", formatter_agent)

    graph.set_entry_point("research")

    graph.add_edge("research", "summarize")
    graph.add_edge("summarize", "format")
    graph.add_edge("format", END)

    return graph.compile()