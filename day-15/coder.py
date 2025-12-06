async def coder_agent(memory):
    prompt = f"""
You are an AI Software Engineer.

Steps: {memory["steps"]}

Write ONLY the code for the next required file.

Return JSON:
{{
  "filepath": "path/to/file.py",
  "content": "file content here"
}}
"""
    result = await call_llm(prompt, model="gpt-4.1")
    result = json.loads(result)

    write_file(result["filepath"], result["content"])  # TOOL
    memory["last_file"] = result["filepath"]
    return memory