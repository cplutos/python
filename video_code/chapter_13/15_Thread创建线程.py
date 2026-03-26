import os
import time
from threading import get_native_id, Thread,RLock


def speak(lock):
    for index in range(5):
        with lock:
            print(f'我在说话{index}，进程pid是；{os.getpid()}，线程为：{get_native_id()}')
        time.sleep(1)

def study(lock):
    for index in range(5):
        with lock:
            print(f'我在学习{index}，进程pid是：{os.getpid()}，线程为：{get_native_id()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程中的第一行打印,进程pid是：{os.getpid()}，线程为：{get_native_id()}')
    lock = RLock()
    # Thread 的参数
    # group: 默认值为None（应当始终为None）
    # target：子进程要执行的可调用对象，默认为None
    # name：进程名称，默认为None，如果设置为None，Python会自动分配名字
    # args：给target传的位置参数（元组）
    # kwargs：给target传的关键字参数（字典）
    # daemon：标记进程是否为守护进程，取值布尔值，（默认为None，表示从创建方进程继承）
    t1 = Thread(target=speak,args=(lock,))
    t2 = Thread(target=study,args=(lock,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('我是主进程中最后一行打印')

