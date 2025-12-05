# First drafts the solution 

async def worker_agent(memory):
    prompt = f"""
    You are a coding/worker agent.
    Task Steps: 
    {memory["steps"]}
    
    Produce a full solution for the next step.
    return code or explanation as needed.
    """
    
    res = await call_llm(prompt)
    memory["draft"] = res
    return memory