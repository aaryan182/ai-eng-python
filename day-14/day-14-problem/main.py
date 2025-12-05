import asyncio
from agents.planner import planner_agent
from agents.worker import worker_agent
from agents.critic import critic_agent
from agents.finalizer import final_agent
from core.memory import init_memory

async def multi_agent_system(task):
    memory = init_memory(task)

    memory = await planner_agent(task, memory)

    for _ in range(5):
        memory = await worker_agent(memory)
        memory = await critic_agent(memory)

        if memory["passed"]:
            break

    return await final_agent(memory)

if __name__ == "__main__":
    task = "Build a FastAPI endpoint to upload a PDF and return its summary."
    result = asyncio.run(multi_agent_system(task))
    print(result)