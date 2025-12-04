import asyncio

async def get_pinecone(q):
    ...

async def get_redis(q):
    ...

async def get_pg(q):
    ...


async def safe(fn, q):
    try:
        res = await fn(q)
        return res or []
    except:
        return []

async def hybrid_retrieve(query):
    r1, r2, r3 = await asyncio.gather(
        safe(get_pinecone, query),
        safe(get_redis, query),
        safe(get_pg, query)
    )
    return r1 + r2 + r3