# sorted函数：对一组数据进行排序，返回一组新数组
# 语法格式：sorted（可迭代对象，key=xxx，reverse = xxx）

# 数字排序
nums = [20,40,20,10]
result = sorted(nums,reverse=True)
print(result)

# 按照字符串的长度排序
# names = ['python','java','sql']
# result = sorted(names,key=lambda n: len(n),reverse=True)
# 等价
# result = sorted(names,key=len,reverse=True)
# print(result)

# 根据字典中的某个字段进行排序
persons = [
    {'name':'张三','age':13,'gender':'男'},
    {'name':'李四','age':18,'gender':'男'},
    {'name':'王五','age':16,'gender':'男'},
    {'name':'赵六','age':35,'gender':'男'}
]
result = sorted(persons,key=lambda p:p['age'],reverse=True)
print(result)

# 我们之前讲的max函数，min函数，也可以传递key参数，用于设置筛选数据
result1 = max(persons,key=lambda p: p['age'])
print(result1)
result2 = min(persons,key=lambda p: p['age'])
print(result2)