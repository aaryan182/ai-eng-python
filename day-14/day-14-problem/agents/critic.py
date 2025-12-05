from core.llm import call_llm

async def critic_agent(memory):
    prompt = f"""
Review this code:

{memory["draft"]}

Return APPROVED or FIX_NEEDED with reasons.
"""
    review = await call_llm(prompt, model="gpt-4.1")
    memory["review"] = review
    memory["passed"] = ("APPROVED" in review.upper())
    return memory