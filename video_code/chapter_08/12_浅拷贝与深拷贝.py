import copy
# 直接赋值：两个变量指向同一个对象，修改其中一个，就会影响另外一个（相互影响）
# num1 = [10,20,34,52]
# num2 = num1
# num2[3] =99
# print(num1)


# 浅拷贝：创建一个新的外层容器，但内部元素仍然引用原来的对象
# 存在的问题：嵌套数据仍然是共享的，修改嵌套数据会互相影响
num1 = [10,20,34,52]
num2 = copy.copy(num1)
num2[3] =99
print(num1[3])
print(num2[3])
print(id(num1))
print(id(num2))
# 嵌套
num1 = [10,20,34,[2,3,4]]
num2 = copy.copy(num1)
num2[3][2] =99
# 依旧影响 输出为99
print(num1[3][2])
print(num2[3][2])
print(id(num1))
print(id(num2))

# 深拷贝：创建一个新的外层容器并对其内部的所有科比那对象进行递归复制
# 备注：
# 1.深拷贝可以彻底消除数据之间的相互影响
# 2.深拷贝遇见不可变对象直接引用
num1 = [10,20,34,[2,3,4]]
num2 = copy.deepcopy(num1)
num2[3][2] =99
print(num1[3][2])
print(num2[3][2])
print(id(num1))
print(id(num2))
# 注意点：
# 1.深拷贝只复制可变对象，不可变对象直接应用
a = 666
b = copy.deepcopy(a)
print(id(a))
print(id(b))
# 2.元组中如果只包含不可变对象，则深拷贝没有效果