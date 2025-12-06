async def devin_like_system(task):
    memory = init_memory(task)

    # 1) Plan
    memory = await planner_agent(task, memory)

    # 2) Write → Run → Fix Loop
    for _ in range(5):  # max 5 iterations
        memory = await coder_agent(memory)
        memory = await executor_agent(memory)

        if memory["exec_result"].get("stderr"):
            memory = await debug_agent(memory)
        else:
            break

    # 3) Final summary
    return await final_agent(memory)