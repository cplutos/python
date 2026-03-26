import asyncio


async def work(n,delay):
    print(f'work {n} begin')
    print(f'work {n} execute')
    await asyncio.sleep(delay)
    print(f'work {n} end')
    return f'work {n} result'

async def main():
    print('main begin')

    con1 = work(1,2)
    con2 = work(2,2)
    con3 = work(3,2)

    res1 = await  con1
    print(res1)
    res2 = await con2
    print(res2)
    res3 = await con3
    print(res3)

    print('main end')

    return 'main result'

asyncio.run(main())