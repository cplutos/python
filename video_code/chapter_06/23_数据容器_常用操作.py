# 以下五个函数：既能定义对应的【空容器】，又能将其他类型转换为对应的数据类型
# 1. list函数：定义空列表，将可迭代对象转换为列表
res1 = list(range(8))
res2 = list('北京欢迎你')
res3 = list({1,2,3,4,5,6})
res4 = list({'张三': 1, '李四': 2, '王五': 3}.items())
print(type(res1),res1)
print(type(res2),res2)
print(type(res3),res3)
print(type(res4),res4)


# 2. tuple函数：定义空元组，将可迭代对象转换为元组
res1 = tuple(range(8))
res2 = tuple('北京欢迎你')
res3 = tuple({1,2,3,4,5,6})
res4 = tuple({'张三': 1, '李四': 2, '王五': 3}.items())
print(type(res1),res1)
print(type(res2),res2)
print(type(res3),res3)
print(type(res4),res4)

# 3. set函数：定义空集合，将可迭代对象转换为和集合
res1 = set(range(8))
res2 = set('北京欢迎你')
res3 = set({1,2,3,4,5,6})
res4 = set({'张三': 1, '李四': 2, '王五': 3})
print(type(res1),res1)
print(type(res2),res2)
print(type(res3),res3)
print(type(res4),res4)

# 4. str函数：定义空字符串，将任意类型转为字符串
res1 = str(range(8))
res2 = str('北京欢迎你')
res3 = str({1,2,3,4,5,6})
res4 = str({'张三': 1, '李四': 2, '王五': 3}.items())
print(type(res1),res1)
print(type(res2),res2)
print(type(res3),res3)
print(type(res4),res4)
print(str(False))
print(str(True))

# 5. dict函数：定义空字典，将可迭代对象转换为字典
# 交给dict函数的内容必须是键值对，否则会报错
res1 = dict({'张三': 1, '李四': 2, '王五': 3})
res2 = dict([('张三', 1), ('李四', 2), ('王五', 3)])
res3 = dict((('张三', 1), ('李四', 2), ('王五', 3)))
res4 = dict({('张三', 1), ('李四', 2), ('王五', 3)})
print(type(res1),res1)
print(type(res2),res2)
print(type(res3),res3)
print(type(res4),res4)

# 所有的数据容器，都支持成员运算符：in / not in 作用：判断某个元素是否在于容器中