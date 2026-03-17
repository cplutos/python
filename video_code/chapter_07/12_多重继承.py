# 概念：多重继承指一个类同时继承多个父类，从而拥有多个父类的属性和方法
# 举例: 就像孩子能继承爸爸的长相,妈妈的性格

class Person:
    max_age= 120
    planet = '地球'

    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender}')

class Worker:
    def __init__(self,company):
        self.company = company
    def do_work(self):
        print(f'我要在{self.company}做兼职')

class Student(Person,Worker):
    def __init__(self,name,age,gender,company,stu_id,grade):
        Person.__init__(self,name,age,gender)
        Worker.__init__(self,company)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我在努力学习，争取考第一')

s1 = Student('张三',12,'男','麦当劳','12314','初二')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 类的__mro__属性：用于记录属性和方法的查找顺序
# 通过实例查找属性或方法时，会从实例本身开始查找
print(Student.__mro__)