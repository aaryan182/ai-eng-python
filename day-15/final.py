async def final_agent(memory):
    prompt = f"""
Summarize the completed coding project.
Include:
- Steps
- Files created
- How it works
- Final output (stdout)

Project execution result:
{memory['exec_result']}
    """
    return await call_llm(prompt)