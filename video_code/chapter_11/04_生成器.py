# 1.生成器：
# 1. 生成器函数：函数体如果出现了yield关键字，那该函数就是【生成器函数】
# 2. 生成器对象：调用【生成器函数】时，其函数体不会立刻执行，而是返回一个【生成器对象】
# 3. 不管能否执行到yield所在的位置，只要函数中有yield关键字，那该函数就是生成器函数

# region
# def demo():
#     print('demo函数开始执行')
#     print(199)
#     if 1==0:
#         yield
#         a = 1
#     a = 299
#     print(a)
# d = (demo())
# print(d)
# endregion

# 4. 写在【生成器函数】中的代码，需要通过【生成器对象】来执行
# 5. 调用【生成器对象】的__next__方法，会让【生成器函数】中的代码开始执行
# 6. 当【生成器函数】中的代码开始执行后，遇到yield会‘暂停’执行，并且其内部会记录‘暂停’的位置

# region
# def demo():
#     print('demo函数开始执行')
#     print(199)
#     yield '我是第一个yield'
#     a = 200
#     print(a)
#     yield '我是第二个yield'
#     b = 300
#     print(b)
#     return 'demo'
# d = demo()
# r1 = next(d)
# r2 = next(d)
# try:
#     r3 = next(d)
# except StopIteration as e:
#     print(e)
# endregion

# 3. 生成器对象是一种特殊的迭代器（本质是通过yield 自动实现了迭代器协议）
# region
def demo():
    print('demo函数开始执行')
    print(199)
    yield '我是第一个yield'
    a = 200
    print(a)
    yield '我是第二个yield'
    b = 300
    print(b)
    return 'demo'


d = demo()


# 验证：拥有iter和next方法
# print(d.__iter__())
# print(d.__next__())

# for循环遍历生成器
# for i in d:
#     print(i)

# for循环背后的逻辑
# gen = iter(d)
# while True:
#     try:
#         val = next(gen)
#         print(val)
#     except StopIteration:
#         break

# endregion

# 4. yield也能写在循环里
# region
# def create_car(total):
#     for i in range(total):
#         yield f'我是第{i}台车'
# # cars是生成器对象
# cars = create_car(10)
#
# # 调用一次cars的next方法，就会得到一台车
# c1 = next(cars)

# endregion

# 5. yield from 能把一个【可迭代对象】里的东西依次yield出去，代替for循环
# region
def demo():
    nums = [10, 20, 30, 40, 50]
    yield from nums
d = demo()
r1 = next(d)
print(r1)
# endregion

# 6. 使用：生成器.send（值）可以让生成器继续执行 的同时，给上一次yield传值
# 备注1：next只能取值，send既能取值，也能送值
# 备注2：第一次启动生成器，不能传值
# region
# def demo():
#     print('demo函数开始执行')
#     print(199)
#     a = yield '我是第一个yield'
#     print(a)
#     b = yield '我是第二个yield'
#     print(b)
#     return 'demo'
# d = demo()
# r1 = next(d)
# print(r1)
# r2 = d.send('666')
# print(r2)
# try:
#
#     d.send(7877)
# except StopIteration as e:
#     print(e)
# endregion

# 用生成器实现遍历Person类的实例对象
# region
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__attr = [self.name, self.age, self.gender, self.address]

    def __iter__(self):
        # yield self.name
        # yield self.age
        # yield self.gender
        # yield self.address
        yield from self.__attr

p1 = Person('张三',19,'男','北京')
for i in p1:
    print(i)


def fibo(total):
    pre = 1
    cur = 1

    for index in range(total):
        if index <2:
            yield 1
        else:
            value = pre + cur
            pre = cur
            cur = value
            yield value

f1 = fibo(10)
# for item in f1:
#     print(item)

# 无论是迭代器，还是生成器对象，都可以有list，tuple，set等直接拿到其里面的所有列（容易挤爆内存）
res = set(f1)
print(res)
# endregion

# 生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式
# 语法格式：（表达式 for 变量 in 可迭代对象）
# 什么时候适合用生成器表达式？ ——当每个结果，值依赖当前这一个元素时
nums = [10, 20, 30, 40, 50]

# 列表推导式
res1 = [n * 2 for n in nums]
print(res1)

# 生成器表达式
res2 = (n * 2 for n in nums)
print(res2)
for x in res2:
    print(x)
