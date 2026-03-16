# 定义Person类
class Person:
    # 定义方法
    # __init__方法: 初始化方法，主要作用，给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实力对象(self),其他的自定义参数
    # 当我们以后编写代码去创建Person市里的时候，Python会自动调用__init__方法
    def __init__(self,name,age,gender):
        self.name =name
        self.age =age
        self.gender = gender
