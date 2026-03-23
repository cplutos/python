# 迭代器是一次性的，状态智慧向前推进，且不会自动重置（迭代器在遍历的过程中会被消耗）
# region
# names = ['张三', '李四', '王五']
#
# it1 = iter(names)
# it2 = iter(names)
#
# print(next(it1))
# print(next(it1))
# print(next(it1))
#
# print(next(it2))
# print(next(it2))
# print(next(it2))
#

# endregion

# 需求：让for循环可以遍历Person的实力对象
# 实现方式一
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)
#
#
# class PersonIterator:
#     def __init__(self, p):
#         # 将外部传进来的数据保存好
#         self.p = p
#         # 初始化迭代器初始化状态，即指针位置
#         self.index = 0
#         # 配置好要遍历的内容
#         self.attrs = [p.name, p.age, p.gender, p.address]
#
#     #  返回迭代器本身
#     def __iter__(self):
#         return self
#
#     # 每次调用__next__方法，会根据当前的状态，返回下一个元素
#     def __next__(self):
#         # 如果指针的位置超出范围，那就抛出StopIteration异常
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.attrs[self.index]
#         # 更新迭代器状态，即指针位置
#         self.index += 1
#         return value
#
#
# # 目标
# p1 = Person('张三', 18, '男', '江西')
# # it = iter(p1)
#
# for item in p1:
#     print(item)
#
# for item in p1:
#     print(item)
# endregion

# 实现方式二
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 初始化迭代器初始化状态，即指针位置
#         self.__index = 0
#         # 配置好要遍历的内容
#         self.__attrs = [name, age, gender, address]
#
#     def __iter__(self):
#         self.__index = 0
#         return self
#
#     def __next__(self):
#         # 如果指针的位置超出范围，那就抛出StopIteration异常
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.__attrs[self.__index]
#         # 更新迭代器状态，即指针位置
#         self.__index += 1
#         return value
#
# # 目标：
# p1 = Person('张三', 18, '男', '江西')
#
# for item in p1:
#     print(item)
# endregion



# 进阶：迭代器玩的就是__next__
# region
from cn2an import an2cn
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 初始化迭代器初始化状态，即指针位置
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        # 将字符串转为大写
        if isinstance(value,str):
            value = value.upper()
        if isinstance(value,int):
            value = an2cn(value)
        # 更新迭代器状态，即指针位置
        self.__index += 1
        return value

# 目标：
p1 = Person('zhangsan', 18, '男', '江西')

for item in p1:
    print(item)
# endregion