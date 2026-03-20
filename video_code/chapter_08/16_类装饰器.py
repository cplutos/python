# 1. 包含 __call__方法的类，就是类装饰器
# 2. 像调用函数一样，去调用类装饰器的实例对象，就会触发 __call__方法的调用
# 3. __call__方法通常接收一个函数作为参数，并且会返回一个新函数

# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args,**kwargs):
#             print('你好，我要开始计算了')
#             return func(*args,**kwargs)
#         return wrapper
# # 使用@语法糖调用
# @SayHello()
# def add(x,y):
#     res1 = x + y
#     print(f'{x}和{y}相加的结果是：{res1}')
#     return res1
# # 正常调用
# res = add(10,20)
# print(res)

# 使用SayHello去装饰add函数（手动装饰）
# say = SayHello()
# add = say(add)
#
# res2 = add(10,20)
# print(res2)


# 带参数的类装饰器
# class SayHello:
#     def __init__(self,msg):
#         self.msg = msg
#     def __call__(self, func):
#         def wrapper(*args,**kwargs):
#             print(f'你好，我要开始{self.msg}计算了')
#             return func(*args,**kwargs)
#         return wrapper
#
# @SayHello('加法')
# def add(x,y):
#     res1 = x + y
#     print(f'{x}和{y}相加的结果是：{res1}')
#     return res1
# # 正常调用
# res = add(10,20)
# print(res)

# 多个类装饰器的使用
class Test1:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print('我是test1逻辑')
            return func(*args,**kwargs)
        return wrapper

class Test2:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print('我是test2逻辑')
            return func(*args,**kwargs)
        return wrapper

@Test1()
@Test2()
def add(x,y):
    res1 = x + y
    print(f'{x}和{y}相加的结果是：{res1}')
    return res1
# 正常调用
res = add(10,20)
print(res)
