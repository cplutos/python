# 定义Person类
class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        # 通过【实例.属性 = 值】给实例添加的属性，就叫做实例属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己的【独一份的】实例属性，各个实例之间是互不干扰的
        self.name = name
        self.age = age
        self.gender = gender
# 创建实例
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')

print(p1.name)
# print(Person.name)