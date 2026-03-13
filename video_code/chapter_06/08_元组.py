# 定义
# 元组中的内容不可修改
t1 = (23,34,64,21)
print(type(t1))
t2 = ('a','b','v')
# t2[1] = 'c'
print(t2[2])

# 元组中如果存放了可变类型（列表），那么可变类型中的内容仍可修改
t3 = (1,'c',[1,3,5])
t3[2][1] = 7
print(t3[2])

# 定义空元组
t4 = ()
t5 = tuple()

# 定义一个元素的元组
t6 = ('abc',)
print(type(t6))
# 不带逗号类型是字符串
t7= ('abc')
print(type(t7))

# 常用方法：
# index方法，获取当前值的第一次出现的下标
t1 = (23,34,64,21)
s = t1.index(23)
print(s)

# count方法，获取元素出现限次数
t1 = (23,34,64,21,21)
s = t1.count(21)
print(s)

# 常用内置函数
# a.sorted(数据容器，reverse = 布尔值)：对数据容器排序，从小到大
t1 = (23,34,64,21,21)
print(sorted(t1))
# b.len（数据容器）：数据容器元素个数
t1 = (23,34,64,21,21)
print(len(t1))
# c.max（数据容器）：数据容器最大值
t1 = (23,34,64,21,21)
print(max(t1))
# d.min（数据容器）：数据容器最小值
t1 = (23,34,64,21,21)
print(min(t1))
# e.sum（数据容器）：数据容器求和，不适用于字符串
t1 = (23,34,64,21,21)
print(sum(t1))

# 实际开发中的元组，不一定是我们自己定义的，比如函数中的可变参数*args就是一个元组
def demo(*args):
    return sum(args)

result = demo(100,200,300)
print(result)

# 循环遍历
index = 0
while index <len(t1):
    print(t1[index])
    index+=1

for item in t1:
    print(item)