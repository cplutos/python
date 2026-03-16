# 定义Person类
class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法
    # speak方法收到的参数是：调用speak方法的实例对象：self、其他参数
    def speak(self,msg):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},我想说：{msg}')

print(Person.__dict__)

# 创建实例
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')
# 验证Person的实例队形身上是没有speak方法的
print(p1.__dict__)
print(p2.__dict__)

# 所有Person类的实力对象都可以调用speak方法：
# 当执行p1.speak()的时候，查找的speak方法的过程：1.实例对象自身  =》2.实例的缔造者身上
p1.speak('好好学习')
p2.speak('天天向上')

def speak():
    print("babble")

p1.speak = speak
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
p1.speak()