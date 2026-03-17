# Python中所有类都继承了object类，即object类是所有类的顶级父类
class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 验证一下：Person类继承了object类
print(issubclass(Person,object))
print(issubclass(int,object))
print(issubclass(str,object))
print(issubclass(list,object))
print(issubclass(bool,object))
print(issubclass(tuple,object))


# 因为Object是所有类的父类，所以Python中的所有对象，都是间接是object类的实例
p1 = Person('张三',123,'男')
print(isinstance(p1,object))
print(isinstance('p1',object))

# 所有对象都继承了object类所提供的：各种属性和方法，从而保证了每个对象都具备统一的基本能力
for key in object.__dict__:
    print(key)

print(p1.__dict__) # 对象身上自己的东西
print(dir(p1))  # 对象可以访问到的东西（自己的、继承过来的）

print(p1.__str__())
print(p1)