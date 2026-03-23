# 1. 迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用
# 2. 当数据量很大，不确定要用多少结果时，推荐使用迭代器

import tracemalloc

# 使用迭代器实现
class Fibo:
    def __init__(self,total):
        # 要生成多少个数
        self.total = total
        # 当前生成到第几个
        self.index = 0
        # 初始两值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.total:
            raise StopIteration
        if self.index < 2:
            value = 1
        else:
            value = self.pre + self.cur
            # 更新一下pre和cur
            self.pre = self.cur
            self.cur = value
            #
        self.index += 1
        return value

# 不使用迭代器实现
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1,1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return nums

tracemalloc.start()
f1 = Fibo(100000)
m = tracemalloc.get_tracemalloc_memory()
print(f'内存占用是{m/1024/1024}MB')

tracemalloc.start()
f2 = fibo(100000)
m2 = tracemalloc.get_tracemalloc_memory()
print(f'内存占用是{m2/1024/1024}MB')