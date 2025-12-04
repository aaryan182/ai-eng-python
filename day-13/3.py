import asyncio

async def foo():
    await asyncio.sleep(1)
    return "foo"

async def bar():
    await asyncio.sleep(1)
    return "bar"

async def main():
    a, b = await asyncio.gather(foo(), bar())
    print(a, b)

asyncio.run(main())

