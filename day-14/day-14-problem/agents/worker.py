from core.llm import call_llm

async def worker_agent(memory):
    prompt = f"""
Write the next part of the solution:

Steps:
{memory["steps"]}

Write FastAPI endpoint code.
"""
    memory["draft"] = await call_llm(prompt, model="gpt-4.1")
    return memory