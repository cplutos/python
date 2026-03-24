import os
import time
from multiprocessing import Process, current_process
print(100,__name__)

def speak(a,b,msg):
    for index in range(10):
        print(f'{msg}--{a}--{b}--{current_process().name}--我在说话{index}，进程pid是；{os.getpid()},我的父进程pid是：{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(10):
        print(f'我在学习{index}，进程pid是：{os.getpid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的第一行打印')
    # 创建两个Process类的实例对象（进程对象），分别是p1和p2
    # group: 默认值为None（应当始终为None）
    # target：子进程要执行的可调用对象，默认为None
    # name：进程名称，默认为None，如果设置为None，Python会自动分配名字
    # args：给target传的位置参数（元组）
    # kwargs：给target传的关键字参数（字典）
    # daemon：标记进程是否为守护进程，取值布尔值，（默认为None，表示从创建方进程继承）
    p1 = Process(target=speak,name='说话进程',args=(666,888),kwargs={'msg':'xyz'})
    p2 = Process(target=study)

    # 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且将该进程交由操作系统进行调整
    p1.start()
    p2.start()

    print('我是主进程中最后一行打印')

