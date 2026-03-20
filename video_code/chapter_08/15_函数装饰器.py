# 1. 装饰器是一种【可调用对象】（通常是函数），他能接受一个函数作为参数，并且会返回一个新的函数
# 2. 装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能
# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print('你好，我要开始计算了')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @say_hello
# def add(x, y, z):
#     print('你好，我要开始计算了')
#     res = x + y + z
#     print(f'{x}和{y}和{z}相加的结果是：{res}')
#     return res
#
#
# @say_hello
# def sub(x, y):
#     res = x - y
#     print(f'{x}和{y}相减的结果是：{res}')
#     return res
#

# 正常调用
# result = add(1, 2, 3)
# print(result)
#
# result = sub(1, 2)
# print(result)

# 需求，在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前先打印一句欢迎
# 实现方法：使用装饰器
# 下面这行代码，是手动装饰，写起来会麻烦一些，不推荐，推荐：@装饰器名
# add_pro = say_hello(add)
# result = add_pro(10, 20)
# print(result)


# 进阶: 带参数的装饰器（三层嵌套，外层接收配置，中间层接受函数，内层接受具体函数）
# def say_hello(msg):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始进行{msg}计算了')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return outer
#
#
# @say_hello('加法')
# def add(x, y):
#     return x + y
#
#
# @say_hello('减法')
# def add(x, y):
#     return x - y
#
#
# res = add(1, 2)
# print(res)


# 进阶：多个装饰器一起使用
def test1(func):
    print('我是test1装饰器')

    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('test1追加的逻辑')
        return r

    return wrapper


def test2(func):
    print('我是test2装饰器')

    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('test2追加的逻辑')
        return r

    return wrapper

@test1
@test2
def add(x,y):
    res1 = x + y
    print(f'{x}和{y}相加的结果是：{res1}')
    return res1
# 这种写法等于 add = test1(test2(add))
res = add(1, 2)
print(res)

# 打印顺序
# 我是test2装饰器
# 我是test1装饰器
# 1和2相加的结果是：3
# test2追加的逻辑
# test1追加的逻辑
# 3