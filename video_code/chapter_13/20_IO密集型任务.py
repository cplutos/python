# io密集型任务，更适合用多线程
import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor


def copy_file(index):
    with open('pycharm-2025.3.3.exe', 'rb') as src,open(f'副本{index}.exe', 'wb') as dst:
        while True:
            data = src.read(1024*1024)
            if not data:
                break
            dst.write(data)

if __name__ == '__main__':
    # print('使用多进程完成io密集型任务')
    # start = time.time()
    # with ProcessPoolExecutor(4) as executor:
    #     for i in range(4):
    #         executor.submit(copy_file, i)
    # end = time.time() - start
    # print(f'多进程耗时：{end}秒')
    #
    print('使用多线程完成io密集型任务')
    start = time.time()
    with ThreadPoolExecutor(4) as executor:
        for i in range(4):
            executor.submit(copy_file, i)
    end = time.time() - start
    print(f'多进程耗时：{end}秒')