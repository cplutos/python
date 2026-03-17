# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
# 鸭子类型是一种编程风格,他不检查对象的类型,只关注对象能否”作对某件事“

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

class Fish:
    def speak(self):
        print('咕噜噜')

class Computer:
    def speak(self):
        print('滋滋滋')

def make_sound(animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()
c2 = Computer()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)
make_sound(c2)


