import time
from multiprocessing import Process, Lock


def speak(lock):
    for index in range(10):
        # 上锁：锁是空闲的就立刻上锁
        lock.acquire()
        # lock.acquire()
        print('好好',end='')
        print('学习',end='')
        print('天天',end='')
        print('向上')
        lock.release()
        time.sleep(1)

# 推荐写法
def study(lock):

    for index in range(15):
        with lock:
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)

if __name__ == '__main__':
    print('第一行')
    lock = Lock()
    p1 = Process(target=speak,args=(lock,))
    p2 = Process(target=study,args=(lock,))

    p1.start()
    p2.start()
    print("最后一行")