from datetime import datetime


class Person:
    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 静态方法
    # 使用@staticmethod 装饰过得方法，就叫静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，他不会收到：self、cls参数，他收到的参数都是自定义参数
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前年龄
        current_year = datetime.now().year
        age = current_year - year
        return age>=18
    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6]+'********'+idcard[-4:]
#   验证静态方法在类身上
print(Person.__dict__)

# 静态方法要通过类调用
result = Person.is_adult(2012)
print(result)
res = Person.mask_idcard('192943199911021928')
print(res)

# 注意点：通过实例也能调用到静态方法，但非常不推荐
p1 = Person('张三',19,'男')
re = p1.mask_idcard('192943199911021928')
print(re)

