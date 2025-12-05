from core.llm import call_llm

async def final_agent(memory):
    prompt = f"""
Format the approved code beautifully:

{memory["draft"]}
"""
    return await call_llm(prompt)