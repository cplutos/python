import asyncio

async def work():
    print('work begin')
    print('work execute')
    res = await asyncio.sleep(2)
    print(res)
    print('work end')
    return 'work result'

async def main():
    print('start')
    res = await work()
    print(res)
    print('end')
    return 'main的返回值'

result = asyncio.run(main())
print(result)