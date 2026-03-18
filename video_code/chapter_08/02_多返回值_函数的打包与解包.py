# 一、函数的多返回值
# def calculate(x,y):
#     res1 = x+y
#     res2 = x-y
#     return res1,res2
# result = calculate(10,32)
# print(result)
#
# r1,r2 = calculate(32,21)
# print(r1,r2)

# 二、参数的打包与解包
# *args：打包所有的位置参数（会形成一个元组）
# **kwargs：打包所有的关键字参数（会形成一个字典）
# def show_info(*ddd,**eee):
#     print(ddd)
#     print(eee)
#
# show_info(10,323,32,name='a',age=12,gender='男')

# 2.解包传递参数
# *变量名：将元组拆解成一个一个的独立的位置参数
# **变量名：将字典拆解成一个一个 key-value 形式的关键字参数
def show_info(num1,num2,num3,name,age,gender):
    print(num1,num2,num3)
    print(name,age,gender)
a = (10,20,30)
person = {'name':'张三','age':'12','gender':'男'}
show_info(*a,**person)

# 3.打包接收参数 和 解包传递参数 一起使用
def show_info(*args,**kwargs):
    print(args)
    print(kwargs)

a = (10,20,30)
person = {'name':'张三','age':'12','gender':'男'}

show_info(*a,**person)