import os
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
from threading import get_native_id, RLock


# 1.创建线程池执行器，使用submit方法提交任务，使用shutdown方法等待任务完成

# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}........{os.getpid()}')
#     time.sleep(1)
#     # main中代码
#
# if __name__ == '__main__':
#     # 创建线程池
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     # 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
#
#     f1 = executor.submit(work,1,lock)
#     f2 = executor.submit(work,2,lock)
#     f3 = executor.submit(work,3,lock)
#     f4 = executor.submit(work,4,lock)
#     f5 = executor.submit(work,5,lock)
#     f6 = executor.submit(work,6,lock)
#     f7 = executor.submit(work,7,lock)
#     print(f1.result())
#     print(f2.result())
#     print(f3.result())
#     print(f4.result())
#     print(f5.result())
#     print(f6.result())
#     print(f7.result())

# 2.获取子进程执行后的返回结果（future类的实例对象）
# def work(n,lock):
#     with lock:
#         print(f'work正在执行线程{n}........{os.getpid()}')
#     time.sleep(1)
#     return f'我是线程{n}返回结果'
#     # main中代码
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建线程池
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     # 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
#     future = [executor.submit(work,index,lock) for index in range(1,8)]
#
#     # 阻塞主线程
#     executor.shutdown(wait=True)
#
#     for f in future:
#         print(f.result())
#
#     print('-----------end-----------')

# 3.使用as_completed：按“完成顺序”获取结果
# def work(n, lock):
#     with lock:
#         print(f'work正在执行线程{n}........{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'我是线程{n}返回结果'
#     # main中代码
#
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建线程池
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     # 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
#     future = [executor.submit(work, index, lock) for index in range(1, 8)]
#     # 收集结果
#     result_list = []
#
#     for f in future:
#         result_list.append(f.result())
#
#     # 阻塞主线程
#     executor.shutdown(wait=True)
#     print(result_list)
#     print('-----------end-----------')
#
# 4.使用add_done_callback方法：为任务完成后添加回调函数
# def work(n, lock):
#     with lock:
#         print(f'work正在执行线程{n}........{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'我是线程{n}返回结果'
#     # main中代码
#
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建线程池
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 收集结果
#     result_list = []
#
#     def done_func(f):
#         result_list.append(f.result())
#
#     # 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
#     for index in range(1,8):
#         f = executor.submit(work, index, lock)
#         f.add_done_callback(done_func)
#
#     # 阻塞主线程
#     executor.shutdown(wait=True)
#     print(result_list)
#     print('-----------end-----------')

# 5.使用map方法批量提交任务（结果按照提交的循序来）
#
# def work(n, lock):
#     with lock:
#         print(f'work正在执行线程{n}........{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'我是线程{n}返回结果'
#     # main中代码
#
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建线程池
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     result = executor.map(work,[1,2,3,4,5,6,7],[lock]*7)
#     # 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
#
#
#     # 阻塞主线程
#     executor.shutdown(wait=True)
#     print(list(result))
#     print('-----------end-----------')

# 6 使用with自动shutdown

def work(n, lock):
    with lock:
        print(f'work正在执行线程{n}........{os.getpid()}')
    if n == 1:
        time.sleep(10)
    elif n == 2:
        time.sleep(5)
    else:
        time.sleep(1)
    return f'我是线程{n}返回结果'
    # main中代码


if __name__ == '__main__':
    print('-----------start-----------')
    # 创建线程池
    with ThreadPoolExecutor(3) as executor:
        # 创建线程锁
        lock = RLock()
        result = executor.map(work,[1,2,3,4,5,6,7],[lock]*7)
        print(list(result))
    print('-----------end-----------')