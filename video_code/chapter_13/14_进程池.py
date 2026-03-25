import os
from concurrent.futures import ProcessPoolExecutor,as_completed
from time import sleep


# 1.创建进程池执行器，使用submit方法提交任务，使用shutdown方法等待任务完成

# def work(n):
#     print(f'work正在执行任务{n}........{os.getpid()}')
#     sleep(1)
#     main中代码
# executor = ProcessPoolExecutor(3)
# 使用submit方法提交任务(submit 只负责提交任务，不会阻塞主进程)
# f1 = executor.submit(work,1)
# f2 = executor.submit(work,2)
# f3 = executor.submit(work,3)
# f4 = executor.submit(work,4)
# f5 = executor.submit(work,5)
# f6 = executor.submit(work,6)
# f7 = executor.submit(work,7)
# print(f1.result())
# print(f2.result())
# print(f3.result())
# print(f4.result())
# print(f5.result())
# print(f6.result())
# print(f7.result())

# 2.获取子进程执行后的返回结果（future类的实例对象）
# def work(n):
#     print(f'work正在执行任务{n}........{os.getpid()}')
#     sleep(1)
#     return f'我是任务{n}返回结果'
    # main中代码
    # executor = ProcessPoolExecutor(3)
    # future = [executor.submit(work,index) for index in range(1, 8)]
    # wait=False 的作用：阻塞主进程，等待进程池中所有任务执行完毕
    # executor.shutdown(wait=True)
    # for f in future:
        # print(f.result())

# 3.使用as_completed：按“完成顺序”获取结果
# def work(n):
#     print(f'work正在执行任务{n}........{os.getpid()}')
#     if n == 1:
#         sleep(15)
#     elif n == 2:
#         sleep(10)
#     else:
#         sleep(1)
#     return f'我是任务{n}返回结果'
#
#
# if __name__ == '__main__':
#     # 创建一个进程池执行器
#     print('------------start------------')
#     executor = ProcessPoolExecutor(3)
#
#     future = [executor.submit(work,index) for index in range(1, 8)]
#     # 为了有序打印，先收集在打印
#     result_list = []
#     for f in as_completed(future):
#         result_list.append(f.result())
#
#     # wait=False 的作用：阻塞主进程，等待进程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#     print(result_list)
#
#     print('------------end------------')


# 4.使用add_done_callback方法：为任务完成后添加回调函数
# def work(n):
#     print(f'work正在执行任务{n}........{os.getpid()}')
#     sleep(1)
#     return f'我是任务{n}返回结果'
#
#
# if __name__ == '__main__':
#     # 创建一个进程池执行器
#     print('------------start------------')
#     executor = ProcessPoolExecutor(3)
#
#     # 收集结果
#     result_list = []
#     # 任务完成后的回调函数
#     def done_func(future):
#         result_list.append(future.result())
#
#     for index in range(1,8):
#         f = executor.submit(work,index)
#         f.add_done_callback(done_func)
#
#     # wait=False 的作用：阻塞主进程，等待进程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#     # 打印结果
#     print(result_list)
#
#     print('------------end------------')



# 5.使用map方法批量提交任务（结果按照提交的循序来）
# def work(n):
#     print(f'work正在执行任务{n}........{os.getpid()}')
#     sleep(1)
#     return f'我是任务{n}返回结果'
#
#
# if __name__ == '__main__':
#     # 创建一个进程池执行器
#     print('------------start------------')
#     executor = ProcessPoolExecutor(3)
#
#     # 开启7个任务，并指定返回函数
#     # 使用map方法批量提交任务（结果按照提交的循序来）
#     results = executor.map(work,[1,2,3,4,5,6,7])
#     # 获取results生成器中的内容
#     print(list(results))
#
#     # wait=False 的作用：阻塞主进程，等待进程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#
#
#     print('------------end------------')

# 6 使用with自动shutdown
def work(n):
    print(f'work正在执行任务{n}........{os.getpid()}')
    sleep(1)
    return f'我是任务{n}返回结果'


if __name__ == '__main__':
    # 创建一个进程池执行器
    print('------------start------------')
    with ProcessPoolExecutor(2) as executor:
        # 开启7个任务，并指定返回函数
        # 使用map方法批量提交任务（结果按照提交的循序来）
        results = executor.map(work,[1,2,3,4,5,6,7])
        # 获取results生成器中的内容
        print(list(results))



    print('------------end------------')