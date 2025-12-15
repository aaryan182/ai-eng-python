from llm.client import call_llm
from .tools import web_search_tool
from .state import ResearchState

def research_agent(state: ResearchState):
    query = state["query"]
    
    # Step 1: Use the tool
    raw_notes = web_search_tool(query)
    
    # Step 2: Ask LLM to refine + extract useful facts
    prompt = f"""
    You are a research agent. Given the search results: 
    {raw_notes}
    
    Extract the most important facts, insights , numbers or arguments. Write 4-8 bullet points.
    """
    
    refined_notes = call_llm(prompt)
    state["research_notes"] = refined_notes.strip()
    return state
