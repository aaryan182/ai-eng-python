from llm.client import call_llm
from .state import ResearchState

def summarizer_agent(state: ResearchState):
    prompt = f"""
    You are a summarization expert.
    Summarize the follwing research notes in 4 - 5 sentences:
     {state['research_notes']}
     """
    summary = call_llm(prompt)
    state['summary'] = summary.strip()
    return state