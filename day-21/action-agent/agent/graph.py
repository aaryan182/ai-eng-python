from langgraph.graph import StateGraph, END
from .state import ActionState
from .nodes import decide_action, execute_tool, respond_node

def build_graph():
    g = StateGraph(ActionState)

    g.add_node("decide", decide_action)
    g.add_node("execute", execute_tool)
    g.add_node("respond", respond_node)

    g.set_entry_point("decide")
    g.add_edge("decide", "execute")
    g.add_edge("execute", "respond")
    g.add_edge("respond", END)

    return g.compile()