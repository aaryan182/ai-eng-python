# A multi step agent loop 

import asyncio


def ensure_async(fn):
    if asyncio.iscoroutinefunction(fn):
        return fn
    async def wrapper(*a, **kw):
        return fn(*a, **kw)
    return wrapper


async def agent_loop(memory):
    for step in range(5):

        llm_response = await llm_call(memory)

        # Tool use?
        if llm_response.tool:
            tasks = []

            for tool_call in llm_response.tool_calls:
                fn = ensure_async(tools[tool_call.name])
                args = tool_call.args

                tasks.append(fn(**args))

            results = await asyncio.gather(*tasks)

            memory.append({
                "role": "tool",
                "content": str(results)
            })

        else:
            return llm_response.final_answer

    return "Max steps reached"