# filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据
# 语法格式：filter（过滤函数，可迭代对象）

# 筛选数值
nums = [10,20,30, 40,50]

# 筛选数值
res = filter(lambda n:n>30,nums)
print(list(res))
print(nums)

# 筛选成年人：
persons = [
    {'name':'张三','age':13,'gender':'男'},
    {'name':'李四','age':18,'gender':'男'},
    {'name':'王五','age':16,'gender':'男'},
    {'name':'赵六','age':35,'gender':'男'}
]

result = filter(lambda p: p['age']>=18,persons)
print(list(result))

# 过滤非法字符串
names = ['张三','','李四',None,'王五']
res = filter(lambda n : n,names)
print(list(res))

# 注意点：
# a.延迟执行：filter不会立刻计算，只有在‘需要结果’时才执行计算。
# b.返回值是迭代器对象，且一旦完成，就会被“耗尽”
# c.filter可能会影响元素数量

# filter函数的特殊用法：如果不传递过滤函数，那么会自动过滤掉"假值"
data = [0,1,'','hello',[],(),76]
res = filter(None,data)
print(list(res))