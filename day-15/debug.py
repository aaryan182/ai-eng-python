async def debug_agent(memory):
    result = memory["exec_result"]

    if result.get("stderr"):

        prompt = f"""
You are a debugging agent.

Error:
{result['stderr']}

Fix the code in file: {memory['last_file']}
Rewrite the FULL corrected file content only.
"""
        fixed_content = await call_llm(prompt)
        write_file(memory["last_file"], fixed_content)
        memory["fixed"] = True
    else:
        memory["fixed"] = False

    return memory