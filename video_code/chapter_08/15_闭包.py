# 前置知识一：
# 1.每次调用函数时，Python都会为函数创建一个新的局部作用域
# 2.函数执行完毕后，这个局部作用域都会被销毁，其中的局部变量也会随之被释放

# def outer():
#     num = 10
#     num += 1
#     print(num)
# outer()
# outer()
# outer()

# 前置知识二：
# 1.在Python中，【内层函数】可以访问其【外层函数】作用域中的变量
# 2.访问外层函数变量无需使用nonlocal；但是修改外层变量时需要使用nonlocal
#
# def outer():
#     num = 10
#     num += 1
#     def inner():
#         nonlocal num
#         num = 99
#         print(1,num)
#     inner()
#     print(num)
# outer()
# outer()
# outer()

# 闭包 = 内层函数 + 被内层函数所引用的外层变量
# 闭包产生的条件
# 1.需要函数嵌套
# 2.在【内层函数】中，要访问【外层函数】变量
# 3.并且在【外层函数】要返回【内层函数】。--只有返回了内层函数，闭包才能活下来，才有意义
# def outer():
#     num = 10
#     print(hex(id(num)))
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return  inner
#
# f = outer()
# f()
# f()
# f()

# 结论
# 1.outer函数中，被inner所使用到的那些变量，会被封存到【闭包单元（cell）】中
# 2.这些cell会组成一个 __closure__ 元组，最终放在了 inner函数身上
# 打印 __closure__ 元组
# print(f.__closure__)
#
# # 打印 __closure__ 元组中的某一项
# print(f.__closure__[0])
#
# # 打印 __closure__ 元组中的某一项的具体值
# print(f.__closure__[0].cell_contents)

# 注意点
# 1.调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互补影响
def outer():
    num = 10
    print(hex(id(num)))
    def inner():
        nonlocal num
        num += 1
        print(num)

    return  inner

f = outer()
f()
f()
f()
print('**************')
f2 = outer()
f2()
# 内层函数中用到的外层变量是可变对象，过个闭包之间依然互不影响
def outer():
    nums = []

    def inner(value):
        nums.append(value)
        print(nums)
    return inner
f1 = outer()
f1(10)
f1(20)
f1(30)
f1(40)
print('********')
f2 = outer()
f2(777)

# 闭包的优点：
# 1.可以记住状态：不用全局变量，也不用写类，就能在多次调用之间保存数据
# 2.可以做配置过的函数：先传一部分参数，把环境固定住，得到一个定制版函数
# 3.可以实现简单的数据隐藏：外层变量对外不可见，只能通过内层函数访问
# 4.是装饰器（decoration）等高级用法的基础

def beauty(char,n):
    def show_msg(msg):
        print(char*n+msg+char*n)
    return show_msg
show1 = beauty('*',3)
show1('你好啊')
show1('靓仔')

# 闭包的缺点：
# 理解成本较高：对初学者不友好，滥用会让代码难读
# 如果闭包里应用了很大的对象，又长期不释放，可能会增加内存占用
# 很多场景下,其实用[类+实例属性]会更清晰,闭包不一定是最优解

class Beauty:
    def __init__(self,char,n):
        self.char = char
        self.n = n
    def show_msg(self,msg):
        print(self.char * self.n +msg +self.char * self.n)

b1 = Beauty('*',3)
b1.show_msg('你好啊')
b1.show_msg('靓仔')
