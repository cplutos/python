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
        # 在子类中，有两种方式去调用父类的初始化方法，来实现继承属性：name，age，gender
        # 方式一 推荐
        # super().__init__(name,age,gender)
        # 方式二
        Person.__init__(self,name,age,gender)

        # 子类独有属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade
    def study(self,msg):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},我想说{msg}')


s1 = Student('张三',19,'男','2023091','初二')

print(s1.__dict__)
print(type(s1))


# 查找speak方法的过程：1，实例自身（s1） ==》2.Student ==》3.Person类
s1.speak('你好')
s1.study('嘿哈')