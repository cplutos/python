import os
import time
from multiprocessing import Process


def speak():
    for index in range(10):
        print(f'我在说话{index}，进程pid是；{os.getpid()},我的父进程pid为{os.getppid()}')
        time.sleep(1)


def study():
    for index in range(15):
        print(f'我在学习{index}，进程pid是：{os.getpid()},我的父进程pid为{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    print('第一行')
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()

    time.sleep(3)
    print('我是主进程，准备终止p1进程....')
    p1.terminate()
    # 等操作系统彻底终止p1进程
    p1.join()
    # 看p1是否活着
    print(p1.is_alive())

    print("最后一行")
