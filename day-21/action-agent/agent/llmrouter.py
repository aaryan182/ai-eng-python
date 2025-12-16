from llm.client import call_llm

def decide_action(state):
    prompt = f"""
You are an action router.

User request:
{state['user_input']}

Choose ONE action:
- http_call
- db_query
- generate_file
- send_email
- respond_only

Return JSON:
{{ "action": "...", "tool_input": {{}} }}
"""
    decision = call_llm(prompt)
    data = eval(decision)  # in prod: json.loads
    state["action"] = data["action"]
    state["tool_input"] = data.get("tool_input", {})
    return state