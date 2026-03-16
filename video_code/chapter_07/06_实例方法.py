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

    def run(self,distance):
        print(f'{self.name}疯狂的跑了{distance}米')

p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')

print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

# 通过实例调用实例方法
p1.speak('你好')
p1.run(300)

# 通过类调用实例方法
# Person.run(100)
Person.run(p1,100)
Person.run(Person('1',1,1),100)

