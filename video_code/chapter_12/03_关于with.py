# 1. Python中的with主要用于管理程序中“需要成对出现的操作”，例如：
#   a. 上锁、解锁
#   b. 打开、关闭
#   c. 借用、归还
# 2. 最终目标：编码者只管做具体的事，“进入”和“离开”的事，让Python自动处理。
# 3. 语法格式如下：
# with 能得到一个上下文管理器的表达式 as 变量：
# 具体的事1
# 具体的事2
# 具体的事3
# 4. 上下文管理器协议：
#   a. __enter__方法：with 中的代码执行【之前】调用，其返回值会赋值给as后的变量
#   b. __exit__方法：with 中的代码执行【结束后】调用）（无论 with 中是否出现异常都会调用）

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print("你好，靓仔")
    def __enter__(self):
        print("进入逻辑")
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        """
        :param exc_type: 异常类型
        :param exc_value: 异常对象
        :param exc_tb: 异常追踪信息
        :return:
        """
        print(f'异常类型{exc_type}')
        print(f'异常对象{exc_value}')
        print(f'异常追踪信息{exc_tb}')


with Person('张三',13) as p1:
    p1.speak()
    p1.study()
    print(7787)