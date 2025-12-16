def router_node(state: PlanState):
    prompt = f"""
You are a routing agent.

Given this task:
{state['task']}

Choose the best next action.

Options:
- research
- rag
- simple_answer
- fail

Return ONLY one word.
"""
    decision = call_llm(prompt).strip().lower()
    state["route"] = decision
    return state
