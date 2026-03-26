import asyncio


async def work(n,delay):
    print(f'work {n} begin')
    print(f'work {n} execute')
    await asyncio.sleep(delay)
    print(f'work {n} end')
    return f'work {n} result'

async def main():
    print('main begin')
    # asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    con1 = asyncio.create_task(work(1,2))
    con2 = asyncio.create_task(work(2,2))
    con3 = asyncio.create_task(work(3,2))

    res1 = await  con1
    print(res1)
    res2 = await con2
    print(res2)
    res3 = await con3
    print(res3)

    print('main end')

    return 'main result'

asyncio.run(main())