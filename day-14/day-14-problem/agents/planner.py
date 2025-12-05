from core.llm import call_llm
import json

async def planner_agent(task, memory):
    prompt = f"""
Break this task into steps:
{task}
Return JSON list only.
"""
    steps_json = await call_llm(prompt)
    memory["steps"] = json.loads(steps_json)
    return memory