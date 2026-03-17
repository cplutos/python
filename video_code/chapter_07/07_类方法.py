from datetime import datetime

# 定义Person类
class Person:
    max_age= 120
    planet = '地球'

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

    # 使用@classmethod装饰过的方法，就叫类方法
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以直接访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息，一些工厂方法

    @classmethod
    def change_planet(cls,value):
        cls.planet = value

    @classmethod
    def create(cls,info_str):
        # 获取有效信息
        name,year,gender = info_str.split('-')
        print('我是test2')
        current_year = datetime.now().year
        age = current_year - int(year)
        # 创建并返回一个类方法
        return cls(name,age,gender)




print(Person.__dict__)

Person.change_planet('火星')
print(Person.__dict__)
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')

print(p1.planet)
print(p2.planet)

p3 = Person.create('李华-2004-女')
print(p3.__dict__)

# 注意点：类方法也能用过实例调用到，但是非常不推荐

p4 = p1.create('李华-2004-女')
print(p4.__dict__)