async def executor_agent(memory):
    prompt = f"""
You are a code execution agent.

Run the project and output the results.
Use this command: python {memory["last_file"]}

If errors appear, report them.
"""
    result = run_code(f"python {memory['last_file']}")
    memory["exec_result"] = result
    return memory