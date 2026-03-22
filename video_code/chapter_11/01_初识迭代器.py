# 知识点1：能被for循环遍历的对象，被称为：可迭代对象{iterable}

# region
# names = ['张三','李四','王五']
# citys = ('北京','上海','深圳')
# msg = 'hello'
# age =10
# def test():
#     pass
# for item in test:
#     print(item)
# endregion

# 知识点2：可迭代对象（iterable）能调用__iter__方法
# region
# names = ['张三','李四','王五']
# citys = ('北京','上海','深圳')
# msg = 'hello'
# age =10
# def test():
#     pass
# print(names.__iter__())
# endregion

# 知识点3：调用__iter__方法会得到：迭代器（iterator）
# 备注1：__iter__是一个魔法方法，当调用iter函数时，__iter__会自动调用
# 备注2：可迭代对象.__iter__ 等价于 iter(可迭代对象)
# 备注3：如果iter（obj）能得到一个迭代器（iterator），那obj就是可迭代对象
# region
# names = ['张三','李四','王五']
# citys = ('北京','上海','深圳')
# msg = 'hello'
#
# print(names.__iter__())
# print(citys.__iter__())
# print(msg.__iter__())
#
# print(iter(names))
# print(iter(citys))
# print(iter(msg))
#

# endregion

# 知识点4：迭代器（iterator）拥有__next__方法，每次调用都会根据当前的状态，返回下一个元素
# region
# 备注1：迭代器.__next__()等价于 next(迭代器)
# 备注2：当所有元素全部取出后，若继续调用 __next__方法，python会抛出 StopIteration 异常
# names = ['张三','李四','王五']
# it = iter(names)
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# endregion

# for循环背后原理
# region
# names = ['张三','李四','王五']
#
# # for item in names:
# #     print(item)
# # for循环逻辑
# # 1. 先获取迭代器对象
# # 2. 开启无限循环
# it = iter(names)
# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break
# endregion

# 知识点5：迭代器（iterator）也拥有__iter__方法，并且放回值是迭代器自身
# 这么设计的原因如下：让for循环也能遍历迭代器（即：为了让 iter（迭代器）不出错）
names = ['张三', '李四', '王五']
#
# it = iter(names)
# print(it)
#
# result = iter(it)
# print(result)
#
# x = iter(result)
# print(x)

it = iter(names)
for item in it:
    print(item)

# 知识点6：迭代器协议
# 1.能被 iter() 接受
# 2.能被 next() 一步一步取值

