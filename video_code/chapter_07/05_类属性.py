# 定义Person类
class Person:
    # max_age、planet都是类属性，类属性是保存在类身上
    # 通过类访问
    # 用于保存公共数据
    max_age = 124
    planet = '地球'
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        if age < Person.max_age:
            self.age = age
        else:
            print(f'超出最大年龄，设置为最大年龄{Person.max_age}')
            self.age = Person.max_age
        self.gender = gender
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')

#    # max_age、planet都是类属性，类属性是保存在类身上
print(p1.__dict__)
print(p2.__dict__)
# 通过类访问
print(Person.max_age)
print(p1.max_age)
print(p1.planet)

#
p3 = Person('王五',198,'女')
print(p3.__dict__)

p1.planet = '火星'
print(p1.__dict__)
print(p2.__dict__)


