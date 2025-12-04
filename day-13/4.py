import asyncio

async def call_llm(prompt, model):
    return client.chat.completions.create(
        model = model,
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message["content"]

async def pipeline(text):
    summary_task = call_llm(f"summarize: {text}", "gpt-4.1-mini")
    sentiment_task = call_llm(f"sentiment: {text}", "gpt-4.1-mini")
    classify_task = call_llm(f"classify: {text}", "gpt-4.1-mini")

    summary, sentiment, category = await asyncio.gather(
        summary_task, sentiment_task, classify_task
    )

    return summary, sentiment, category