# Build a FAST async agent that: Takes a user query Parallelly 

# Retrieves RAG chunks
# Gets internet info (fake tool)
# Summarizes the user query
# Feeds all results to LLM
# Returns final answer


import asyncio
from openai import AsyncOpenAI

cleint = AsyncOpenAI()

async def summarize(text):
    res = await client.chat.completions.create(
        model= 'gpt-4.1-mini',
        messages= [{"role": "user", "content": f"Summarize: {text}"}]
    )
    return res.choices[0].message['content']

async def get_web_info(query):
    await asyncio.sleep(1)
    return f"Fake internet infor for: {query}"

async def rag_fetch(query):
    await asyncio.sleep(1)
    return f"Top chunks related to: {query}"


async def async_agent(query):
    summary_task = summarize(query)
    web_task = get_web_info(query)
    rag_task = rag_fetch(query)

    summary, web_data, rag_data = await asyncio.gather(
        summary_task, web_task, rag_task
    )

    final_prompt = f"""
Using these sources:

Summary: {summary}
Web: {web_data}
RAG: {rag_data}

Answer the user's question: {query}
    """

    final = await client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": final_prompt}]
    )

    return final.choices[0].message["content"]