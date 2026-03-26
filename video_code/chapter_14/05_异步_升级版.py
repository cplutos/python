import asyncio
from unittest import result


async def work(n,delay):
    print(f'work {n} begin')
    print(f'work {n} execute')
    await asyncio.sleep(delay)
    print(f'work {n} end')
    return f'work {n} result'

async def main():
    print('main begin')
    # asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中

    result = await asyncio.gather(work(1,2),work(2,2),work(3,2))

    print(result)
    print('main end')

    return 'main result'

# 将协程交给事件循环
reuslt = asyncio.run(main())
print(reuslt)