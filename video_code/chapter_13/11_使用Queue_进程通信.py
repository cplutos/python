import time
from multiprocessing import Process,Queue

def test1(q):
    for i in range(5):
        print(f'【test1】放入数据：{i}')
        q.put(i)
        time.sleep(0.5)


def test2(q):
    for i in range(5):
        data = q.get()
        print(f'【test2】取出数据：{data}')
        time.sleep(0.5)

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=test1,args=(q,))
    p2 = Process(target=test2,args=(q,))
    p1.start()
    p2.start()