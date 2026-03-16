# 定义Person类
class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')

# 直接打印一个实例的话，我们是看不到实例身上的属性的
# print(p1)
# print(p2)
# 通过点语法可以访问实例身上的属性
print(p1.name)
print(p1.age)
print(p1.gender)
print(p2.name)
print(p2.age)
print(p2.gender)

# 通过 实例.__dict__ 可以查看实例身上的所有属性
print(p1.__dict__)
print(p2.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address = '东莞'
print(p1.__dict__)

# 通过type()函数，可以查看某个实例所属类
print(type(p1))
print(type(p2))



