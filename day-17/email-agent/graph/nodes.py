# All 3 langgraph nodes in one file

from llm.client import call_llm
from .tools import email_template_tool
from .state import EmailState

def extract_intent(state: EmailState):
    prompt = f"""
    Extract the intent of this message in 3 - 8 words:

    {state['user_input']}
    """
    state["intent"] = call_llm(prompt).strip()
    return state

def rewrite_message(state: EmailState):
    prompt = f"""
Rewrite the following message to be clearer, professional, and grammatically correct:

{state['user_input']}
"""
    state["rewritten"] = call_llm(prompt).strip()
    return state


def formal_email(state: EmailState):
    email = email_template_tool(state["intent"], state["rewritten"])
    state["final_email"] = email
    return state


# This mirrors OpenAI/Langgraph production style : each node = a small pure function , no global state, easy to debug and extend