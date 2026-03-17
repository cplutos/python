class Person:
    max_age= 120
    planet = '地球'

    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},我想说：{msg}')
# 定义一个Student类(子类,派生类),继承自Person类(父类,超类,基类)
class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类相同的方法，那么子类中的方法就会覆盖父类中的fangfa

    def speak(self,msg):
        super().speak(msg)
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},学号是：{self.stu_id},我想说:{msg}')

s1 = Student('李华',12,'男','202301','初二')
s1.speak('我是靓仔')
