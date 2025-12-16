from llm.client import call_llm
from state import PlanState

def planner_node(state: PlanState):
    prompt = f"""
You are a planning agent.

User task:
{state['task']}

Explain briefly what needs to be done.
"""
    state["plan"] = call_llm(prompt)
    return state