import os
import time
from threading import get_native_id, Thread,RLock


class SpeakThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__(**kwargs)
        self.lock = lock
    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在说话{index}，进程pid是；{os.getpid()}，线程为：{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在学习{index}，进程pid是：{os.getpid()}，线程为：{get_native_id()}')
            time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程中的第一行打印,进程pid是：{os.getpid()}，线程为：{get_native_id()}')
    lock = RLock()

    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('我是主进程中最后一行打印')

