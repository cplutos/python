class Person:
    max_age= 120
    planet = '地球'

    # 初始方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

p1 = Person('张三',10,'男')
s1 = Student('李华',12,'男','202402','初二')

# 方法一：isinstance(instance,Class)，作用：判断某个对象是否是这个类或其子类的实例
print(isinstance(s1,Student))
print(isinstance(p1,Person))

print(isinstance(p1,Student))
print(isinstance(s1,Person))

# 方法二：issubclass(Class1，Class2)，作用：判断某个类是否是另一个类的子类
print(issubclass(Student,Person))
print(issubclass(Person,Student))