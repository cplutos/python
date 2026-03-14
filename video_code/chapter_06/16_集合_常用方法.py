# a.集合A.difference(集合B)：找出集合A中不同于集合B的元素（集合A和B都不变，返回的是一个新的集合）
s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23,88}
s3 = s1.difference(s2)
print(s1)
print(s2)
print(s3)


# b.集合A.difference_update(集合B)：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23,88}
s3 = s1.difference_update(s2)
print(s1)
print(s2)
print(s3)


# c.集合A.union(集合B)：合并两个集合，集合A和集合B都不变，返回的是一个新的集合
s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23,88}
s3 = s1.union(s2)
print(s1)
print(s2)
print(s3)

# d.集合A.issubset(集合B)：判断集合A是否为集合B的子集，返回布尔值

s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23}
s3 = s2.issubset(s1)
print(s1)
print(s2)
print(s3)


# e.集合A.issuperset(集合B)：判断集合A是否为集合B的超集，返回布尔值

s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23}
s3 = s1.issuperset(s2)
print(s1)
print(s2)
print(s3)

# 集合A.isdisjoint(集合B)：判断集合A与集合B是否没有交集，返回布尔值

s1 = {10,20,39,23,233,12,4,23}
s2 = {4,23,88,99}
s3 = s1.isdisjoint(s2)
print(s1)
print(s2)
print(s3)