import os
import time
from multiprocessing import Process
print(100,__name__)

def speak():
    for index in range(10):
        print(f'我在说话{index}，进程pid是；{os.getpid()}')
        time.sleep(1)

def study():
    for index in range(10):
        print(f'我在学习{index}，进程pid是：{os.getpid()}')
        time.sleep(1)
# 注意：一定要写 if __name__ == '__main__': 这个判断，原因如下：
# 1.当创建子进程是，Python并不会把父进程里的speck函数直接交给子进程
# 2.Python会启动一个全新的Python解释器进程，重新执行当前的.py文件(作为模块)
# 3.在执行过程中，重新定义出一个speak函数，交给子进程

if __name__ == '__main__':
    print('我是主进程中的第一行打印')
    # 创建两个Process类的实例对象（进程对象），分别是p1和p2
    # 注意1:p1和p2 就对应着以后得两个子进程,在创建他们的时候,就指定好他们要执行的任务
    # 注意2:此时的p1和p2只是代码层面的两个进程对象,操作系统还没有真的创建两个进程
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且将该进程交由操作系统进行调整
    p1.start()
    p2.start()

    print('我是主进程中最后一行打印')

