class Person:
    # 初始方法
    def __init__(self, name, age, idcard):
        self.name = name            # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age             # 受保护的属性：在当前类中。子类中，都可以方法
        self.__idcard = idcard        # 私有属性：仅能在当前类中方法

    def speak(self):
        print(f'我叫{self.name},年龄是{self._age},性别是{self.__idcard}')
class Student(Person):
    def hello(self):
        print(f'我是学生({self.name}-{self._age})')

s1 = Student('张三',12,'121232')
p1 = Person('李四',12,'121232')

s1.hello()
print(s1.__dict__)
print(s1.name)

print(p1.name)
# 再类的外部，如果强制访问【受保护的属性】也能访问到，但十分不推荐
# print(p1._age)
# print(p1.__idcard)

# Python底层是通过重命名的方式，实现私有属性的
print(p1.__dict__)
# print(p1._Person__idcard)