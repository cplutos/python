# 队列是一种先进先出的数据结构
import time
from multiprocessing import Queue, Process

# q1 = Queue()

# 不限制大小，没有容量上限
# q2 = Queue(3)

# 1.put入队
# q1.put(1)
# q1.put(2)
# q1.put(3)

# 2.get出队
# print(q1.get())
# print(q1.get())
# print(q1.get())

# 3.full方法：判断队列是否已满
# q1.put(1)
# q1.put(2)
# q1.put(3)
# result = q1.full()
# print(result)
#
# q2.put(1)
# q2.put(2)
# q2.put(3)
# result2 = q2.full()
# print(result2)

# 4.qsize方法，获取队列长度
# q1.put(1)
# q1.put(2)
# q1.put(3)
# result = q1.qsize()
# print(result)

# 5.队列具备等待模式
# q2.put(1)
# q2.put(2)
# q2.put(3)
# 当队列已满，就会进度等待模式，等别人调用get方法，取走一个元素
# q2.put(4)
# print('放入完毕')
# 当队列已满，就会进度等待模式，等别人调用get方法，指定timeout等待秒数
# q2.put(4,timeout=3)
# print('放入完毕')
# put_nowait方法当队列已满，不会进入等待模式，直接加，满了就抛异常
# q2.put_nowait(4)
# print('放入完毕')

# 6.get读多了也会进入等待模式
# q2.get()
# q2.get()
# q2.get()
# 队列已空，继续get，机会进入等待模式
# q2.get()
# timeout指定等待秒数
# q2.get(timeout=3)
# get_nowait 方法，会直接取，空就抛异常
# q2.get_nowait()

def test(q):
    time.sleep(3)
    res = q.get()
    print(f'我从队列中取出了元素:{res}')

if __name__ == '__main__':
    q = Queue(2)
    q.put(1)
    q.put(2)
    print(f'队列是否已满：{q.full()}')

    p1 = Process(target=test,args=(q,))

    p1.start()

    print('向已满队列添加一个元素')

    q.put(3)

    print('目前有的元素：')
    print(q.get())
    print(q.get())
