async def planner_agent(task, memory):
    prompt = f"""
    You are a Senior Software Architect.
    Break this coding task into actionable steps.
    
    Task:
    {task}
    
    Return JSON list of steps.
    """
    steps = await call_llm(prompt)
    memory["steps"] = json.loads(steps)
    return memory