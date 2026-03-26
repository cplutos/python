# 关于GIL
import time
from threading import Thread, RLock, current_thread

#
# def show_info1(lock):
#     for index in range(10):
#         with lock:
#             print('a',end='')
#             print('b',end='')
#             print('c',end='')
# def show_info2(lock):
#     for index in range(10):
#         with lock:
#             print('e',end='')
#             print('f',end='')
#             print('g',end='')
#
# if __name__ == '__main__':
#     lock = RLock()
#     t1 = Thread(target=show_info1,args=(lock,))
#     t2 = Thread(target=show_info2,args=(lock,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

current  = 1

def sale(lock):
    global current
    while True:
        with lock:
            if current <= 20:
                print(f'{current_thread().name}出手了第{current}张票！')
                current += 1
            else:
                print('票已售空')
                break
        time.sleep(0.5)

if __name__ == '__main__':
    lock = RLock()
    t1 = Thread(target=sale, name='窗口1',args=(lock,))
    t2 = Thread(target=sale, name='窗口2',args=(lock,))
    t3 = Thread(target=sale, name='窗口3',args=(lock,))
    t1.start()
    t2.start()
    t3.start()