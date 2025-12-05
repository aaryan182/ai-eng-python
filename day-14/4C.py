# Reviews output and checks for errors then approves or requests fixes 

async def critic_agent(memory):
    prompt = f"""
    You are a critic agent. Review the draft:
    
    Draft: 
    {memory["draft"]}
    
    If correct, return: APPROVED
    If issues, return: FIX_NEEDED and describe what must be fixed.
    """
    
    review = await call_llm(prompt)
    memory["review"] = review
    memory["passed"] = ("APPROVED" in review.upper())
    return memory
        