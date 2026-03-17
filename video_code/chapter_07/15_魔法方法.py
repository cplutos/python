# 概念：以__xxx__命名的特俗方法（双下划线开头和结尾）
# 特点：不需要我们手动调用，我们只要准备好这些方法，Python会在特定场景下，去自动调用

class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 当执行print（Person的实例对象） 或str（Person的实例对象）时调用
    def __str__(self):
        return f'{self.name}={self.age}-{self.gender}'

    def __len__(self):
        return len(p1.__dict__)
    # 当执行Person实例对象1 < Person实例对象2 时调用
    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getattr__(self, item):
        return f'你访问的{item}属性不存在'

p1 = Person('张三',19,'男')
p2 = Person('张三',19,'男')
print(p1)
print(p2)
# res = str(p1)
# res2 = str(p2)
re = len(p1)
print(re)

print(p1 < p2)

print(p1 == p2)

print(p1.address)