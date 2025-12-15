from llm.client import call_llm
from .state import ResearchState

def formatter_agent(state: ResearchState):
    prompt = f"""
    Format the following summary into a well structured, polished final output.
    Summary: 
    {state['summary']}
    Ensure: 
    - Professional tone
    - Clear sectioning
    - Bullet points where needed
    """
    final = call_llm(prompt)
    state['final_output'] = final.strip()
    return state
