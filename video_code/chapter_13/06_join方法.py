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
    # 让主进程等五秒
    p1.join(5)
    p2.start()

    # p1.join(5)# 让主进程等p1进程执行完后，主进程在继续执行
    # p2.join()# 让主进程等p2进程执行完后，主进程在继续执行
    print("最后一行")
