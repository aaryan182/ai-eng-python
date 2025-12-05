# Breaks user request into actionable steps 

async def planner_agent(task, memory):
    prompt = f"""
    You are a planner agent. Break the users task into clear actionable steps.
    
    User task: {task}
    
    Return steps as a JSON list.
    """
    res = await call_llm(prompt)
    memory["steps"] = json.loads(res)
    return memory