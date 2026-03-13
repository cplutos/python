# 定义有内容的【可变集合】
s1 = {10,20,39,23,233,12,12,4,23}
s2 = {'q','w','s','e','a','a'}
s3 = {1,True,'你好',12.45}

print(type(s1))
print(s2)
print(s3)
s2.add('z')

# 定义有内容的【不可变集合】
s1 = frozenset({10,20,39,23,233,12,12,4,23})
s2 = frozenset({'q','w','s','e','a','a'})
s3 = frozenset({1,True,'你好',12.45})

print(type(s1))
print(s2)
print(s3)
# s2.add('z')


# frozenset 接收的参数，可以是任意可迭代对象，但是最终返回的一定是不可变集合
s1 = frozenset([10,20,39,23,233,12,12,4,23])
s2 = frozenset(('q','w','s','e','a','a'))
s3 = frozenset('hello')

print(type(s1),s1)
print(type(s2),s2)
print(type(s3),s3)

# 定义空集合
s1 = set()
# 字典
s2 = {}
print(type(s1))
print(type(s2))
s3 = frozenset()
print(type(s3),s3)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】，只有不可变的东西，才能安全的放进集合里
s1 = frozenset([10,20,39,23,233,12,12,4,23])
s2 = {'q','w','s','e','a','a'}
s3 = frozenset('hello')
s4 = {1,2,3}

s5 = {2,s1}
# s5 = {2,s2}
print(s5)