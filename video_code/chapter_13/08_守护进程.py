import os
import time
from multiprocessing import Process


def monitor():
    while True:
        try:
            with open('log.txt','r+',encoding='utf-8') as file:
                lines = sum(1 for _ in file)
        except FileNotFoundError:
            lines = 0
        print(f'我是【守护进程({os.getpid()})】，log.txt 共有{lines}行')
        time.sleep(1)

def test():
    for index in range(10):
        print(f'我是test（{os.getpid()}）')
        time.sleep(1)


if __name__ == '__main__':
    print(f'主进程（{os.getpid()}）中的第一行代码')

    # 守护进程
    p1 = Process(target=monitor,daemon=True)
    p2 = Process(target=test)

    p1.start()
    p2.start()

    with open('log.txt','a+',encoding='utf-8') as file:
        for index in range(10):
            file.write(f'靓仔{index}\n')
            file.flush()
            time.sleep(1)

    # p1.join()
    print(f'主进程（{os.getpid()}）中的最后一行代码')
