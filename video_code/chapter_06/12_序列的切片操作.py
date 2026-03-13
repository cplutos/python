# 对列表进行切片
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list1[0:7:3]
print(list2)
print(list1[0:10:1])
print(list1[::])
print(list1[-1::-1])
print(list1[::-1])
print(list1[::4])

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[7:2:-1])

# 对元组进行切片
tuple1 = (1,2,3,4,5,6,7,8,9,10)
print(tuple1[0:8:2])