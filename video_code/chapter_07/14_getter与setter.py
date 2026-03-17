class Person:
    max_age = 120
    # 初始方法
    def __init__(self, name, age, idcard):
        self.name = name            # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age             # 受保护的属性：在当前类中。子类中，都可以方法
        self.__idcard = idcard        # 私有属性：仅能在当前类中方法
    # 注册属性age的getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age
    # 注册属性age的setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
    @age.setter
    def age(self,age):
        if age<self.max_age:
            self._age = age
        else:
            print('年龄不合法')

    @property
    def idcard(self):
        return self.__idcard[:6]+'********'+self.__idcard[-4:]

    @idcard.setter
    def idcard(self,idcard):
        print('身份证号不可修改')

p1 = Person('张三',122,'2131289312')

print(p1.name)
print(p1.age)
p1.age = 99
print(p1.age)
print(p1.idcard)
p1.idcard =2