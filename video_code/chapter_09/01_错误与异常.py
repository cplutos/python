# 错误：代码本身有语法错误，解释器无法执行代码。——无法通过异常处理机制解决
# age = 18
# if age>18
#     print('成年人')

# 异常：代码在语法上没有问题吗，但执行中出现了问题。——可以通过异常处理机制解决
# 1.ZeroDivisionError 除零异常
# res = 100/0

# 2.TypeError:当操作的数据类型不正确或不兼容时触发
# res = 100+'s'

# 3.AttributeError：当对象没有指定属性时触发
# class Person:
#     def __init__(self,name):
#         self.name = name
# p = Person('张三')
# p.age

# 4.IndexError:索引越界触发
# nums = [1,2]
# print(nums[3])

# 5.NameError：使用了不存在变量触发
# print(school)

# 6.KeyError:当访问字典中不存在的key触发
# person = {'name':'张三','age':11}
# print(person['gender'])

# 7.ValueError:当值不合法，但是类型正确时触发
# int('代发')

input()