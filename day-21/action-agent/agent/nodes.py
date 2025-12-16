from tools.http_tool import http_call
from tools.db_tool import db_query
from tools.file_tool import generate_file
from tools.email_tool import send_email

def execute_tool(state):
    action = state["action"]
    args = state["tool_input"]

    if action == "http_call":
        state["observation"] = http_call(**args)

    elif action == "db_query":
        state["observation"] = db_query(**args)

    elif action == "generate_file":
        state["observation"] = generate_file(**args)

    elif action == "send_email":
        state["observation"] = send_email(**args)

    else:
        state["observation"] = None

    return state

def respond_node(state):
    state["final_output"] = f"""
Action executed: {state['action']}
Result:
{state['observation']}
"""
    return state