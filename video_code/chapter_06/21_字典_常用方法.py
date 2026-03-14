# keys方法：用于获取字典中所有的键
d1 = {'张三': 1, '李四': 2, '王五': 3}

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
result = d1.keys()
print(type(result),result)

# dict_keys和列表类似，可以被遍历，但要注意的是：但不能通过下标访问元素
for item in result:
    print(item)

# 借助内置的类型转换，可以将dict_keys转换成list
l1 = list(result)
print(l1)
print(type(l1))

# values方法：获取字典中的所有值
d1 = {'张三': 1, '李四': 2, '王五': 3}
# values方法的返回类型是：dict_values，他的特点和dict_keys一样
result = d1.values()
print(type(result),result)

# items方法 ：获取字典中所有的键值对(每组键值对以元组的形式呈现)
d1 = {'张三': 1, '李四': 2, '王五': 3}
# items方法的返回类型是：dict_items，他的特点和dict_keys一样
result = d1.items()
print(result)
print(type(result))