import os
from multiprocessing import Process

num = 100
names = []

def test1():
    global num
    num += 1
    names.append('test1')
    print(f'test1进程，操作之后的num是{num},names:{names}')

def test2():
    global num
    num -= 1
    names.append('test2')
    print(f'test2进程，操作之后的num是{num},names:{names}')


if __name__ == '__main__':
    print(f'主进程（{os.getpid()}）中的第一行代码')

    # 守护进程
    p1 = Process(target=test1)
    p2 = Process(target=test2)

    p1.start()
    p2.start()

    print(f'主进程（{os.getpid()}）中的最后一行代码')
