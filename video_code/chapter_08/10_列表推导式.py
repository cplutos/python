# 定义：用一条简洁语句，从可迭代对象中，生成新列表的语法结构
# 备注：列表推导式本质上是对for循环+append（）的一种简写形式
# 语法格式：【表达式 for 变量 in 可迭代对象】

# 需求：让列表中的每个元素都变为原来的两倍，得到一个新的列表

# 方式一 map函数
nums = [10, 20, 30, 50]
res = list(map(lambda n: n * 2, nums))
print(res)

# 方式二 for循环 +append()
nums = [10, 20, 30, 50]
result = []
for n in nums:
    result.append(n * 2)
print(result)

# 方式三 用列表推导式
nums = [10, 20, 30, 50]
result = [n * 2 for n in nums]
print(result)
# 带条件的推导式
nums = [10, 20, 30, 50]
result = [n * 2 for n in nums if n > 20]
print(result)

# 字典推导式
names = ['张三', '李四', '王五']
scores = [13, 64, 78]
result = {names[index]: scores[index] for index in range(len(names))}
print(result)

# 集合推导式
names = ['张三', '李四', '王五']
result = {n + '!' for n in names}
print(result)

# Python中没有元组推导式，下面这种方法叫生成器
result = (n + '!' for n in names)
print(result)
