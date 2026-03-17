# 多态的概念：同一个方法名，在不同对象上调用时的不同表现形式
# Python中支持：标准多态，鸭子多态
class Animal:
    def speak(self):
        print('动物正在发出叫声')
class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

class Pig:
    def speak(self):
        print('哼哼哼')

def make_sound(animal:Animal):
    animal.speak()

a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()

make_sound(a1)
make_sound(d1)
make_sound(c1)
make_sound(p1) # 此行代码在其他语言中必定报错，极其不推荐这种写法，违反规则