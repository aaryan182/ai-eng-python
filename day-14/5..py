# Devin Like loop

async def final_agent(memory):
    prompt = f"""
Format the final solution in clean markdown.

Task:
{memory["task"]}

Steps:
{memory["steps"]}

Approved answer:
{memory["draft"]}
"""
    return await call_llm(prompt)

async def multi_agent_system(task):
    memory = {"task": task, "steps":[], "draft":"", "review":"", "passed":False}
    
    # Step 1: Planner
    memory = await planner_agent(task,memory)
    
    # Step 2: Worker + critic loop
    for _ in range(5): # max retries
        memory = await worker_agent(memory)
        memory = await critic_agent(memory)
        
        if memory["passed"]:
            break
    
    # step 3: Final formatter agent
    return await final_agent(memory)
        